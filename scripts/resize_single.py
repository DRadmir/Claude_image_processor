#!/usr/bin/env python3
"""
Resize single image to 70% of original dimensions
Usage: python3 scripts/resize_single.py <image_path>
"""

import sys
import os
import shutil
import uuid
from PIL import Image

def resize_single_image(input_path):
    """
    Resize a single image to 70% of original dimensions
    
    Args:
        input_path: Path to the input image file
        
    Returns:
        str: Path to the output file if successful, None if failed
    """
    
    # Validate input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist")
        return None
    
    # Create necessary directories
    os.makedirs('tmp', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    
    try:
        # Load the image
        print(f"Processing: {input_path}")
        img = Image.open(input_path)
        
        # Get original dimensions
        original_width, original_height = img.size
        print(f"Original dimensions: {original_width}x{original_height}")
        
        # Calculate new dimensions (70% of original)
        new_width = int(original_width * 0.7)
        new_height = int(original_height * 0.7)
        print(f"New dimensions: {new_width}x{new_height}")
        
        # Resize the image using high-quality resampling
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Get original file extension
        _, ext = os.path.splitext(input_path)
        if not ext:
            ext = '.png'  # Default to PNG if no extension
        
        # Generate UUID and create output filename
        uuid_str = str(uuid.uuid4())
        output_filename = f"resized_{uuid_str}{ext}"
        output_path = os.path.join('output', output_filename)
        
        # Save the resized image
        resized_img.save(output_path)
        
        print(f"SUCCESS: Resized image saved to {output_path}")
        print(f"UUID: {uuid_str}")
        
        return output_path
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return None
        
    finally:
        # Clean up tmp folder
        if os.path.exists('tmp'):
            shutil.rmtree('tmp', ignore_errors=True)

def main():
    """Main function to handle command line arguments"""
    
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/resize_single.py <image_path>")
        print("Example: python3 scripts/resize_single.py /path/to/image.png")
        sys.exit(1)
    
    input_path = sys.argv[1]
    result = resize_single_image(input_path)
    
    if result:
        print(f"\n✅ Single image processing completed successfully!")
        print(f"Output: {result}")
    else:
        print(f"\n❌ Single image processing failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()