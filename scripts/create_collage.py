#!/usr/bin/env python3
"""
Create horizontal collage from multiple images
Usage: python3 scripts/create_collage.py <image1> <image2> [image3] ...
"""

import sys
import os
import shutil
import uuid
from PIL import Image

def create_collage(image_paths):
    """
    Create a horizontal collage from multiple images
    
    Args:
        image_paths: List of paths to input image files
        
    Returns:
        str: Path to the output file if successful, None if failed
    """
    
    # Validate input files exist
    for path in image_paths:
        if not os.path.exists(path):
            print(f"Error: Input file '{path}' does not exist")
            return None
    
    # Create necessary directories
    os.makedirs('tmp', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    try:
        # Load all images
        images = []
        print(f"Loading {len(image_paths)} images...")
        
        for i, path in enumerate(image_paths, 1):
            img = Image.open(path)
            images.append(img)
            print(f"Image {i} dimensions: {img.size}")
        
        # Find the maximum height to resize all images to same height
        max_height = max(img.size[1] for img in images)
        print(f"Target height: {max_height}")
        
        # Resize images to same height while maintaining aspect ratio
        def resize_to_height(img, target_height):
            aspect_ratio = img.size[0] / img.size[1]
            new_width = int(target_height * aspect_ratio)
            return img.resize((new_width, target_height), Image.LANCZOS)
        
        resized_images = []
        for i, img in enumerate(images, 1):
            resized = resize_to_height(img, max_height)
            resized_images.append(resized)
            print(f"Resized image {i}: {resized.size}")
        
        # Calculate total width including gaps
        gap_width = 10  # 10px gaps as specified
        total_width = sum(img.size[0] for img in resized_images) + (gap_width * (len(resized_images) - 1))
        print(f"Total collage width: {total_width}")
        
        # Create collage canvas with light gray background
        collage = Image.new('RGB', (total_width, max_height), color='#D3D3D3')
        
        # Paste images with gaps (top-aligned)
        x_offset = 0
        for i, img in enumerate(resized_images):
            collage.paste(img, (x_offset, 0))  # Top-aligned (y=0)
            x_offset += img.size[0]
            
            # Add gap (except after last image)
            if i < len(resized_images) - 1:
                x_offset += gap_width
        
        # Resize collage to 30% for web-friendly size
        collage_scale = 0.3
        final_width = int(collage.size[0] * collage_scale)
        final_height = int(collage.size[1] * collage_scale)
        final_collage = collage.resize((final_width, final_height), Image.LANCZOS)
        
        print(f"Original collage dimensions: {collage.size}")
        print(f"Final collage dimensions (30% scale): {final_collage.size}")
        
        # Generate UUID and create output filename
        uuid_str = str(uuid.uuid4())
        output_filename = f"collage_{uuid_str}.png"
        output_path = os.path.join('output', output_filename)
        
        # Save the resized collage as PNG
        final_collage.save(output_path)
        
        print(f"SUCCESS: Collage saved to {output_path}")
        print(f"Final dimensions: {final_collage.size}")
        print(f"UUID: {uuid_str}")
        
        return output_path
        
    except Exception as e:
        print(f"Error creating collage: {e}")
        return None
        
    finally:
        # Clean up tmp folder
        if os.path.exists('tmp'):
            shutil.rmtree('tmp', ignore_errors=True)

def main():
    """Main function to handle command line arguments"""
    
    if len(sys.argv) < 3:
        print("Usage: python3 scripts/create_collage.py <image1> <image2> [image3] ...")
        print("Example: python3 scripts/create_collage.py img1.png img2.png img3.png")
        print("Note: At least 2 images required for collage")
        sys.exit(1)
    
    image_paths = sys.argv[1:]
    print(f"Creating collage from {len(image_paths)} images...")
    
    result = create_collage(image_paths)
    
    if result:
        print(f"\n✅ Collage creation completed successfully!")
        print(f"Output: {result}")
    else:
        print(f"\n❌ Collage creation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()