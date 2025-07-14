#!/usr/bin/env python3
"""
Main image processing script - automatically detects single vs multiple images
Usage: python3 scripts/process_images.py <image1> [image2] [image3] ...
"""

import sys
import os
from resize_single import resize_single_image
from create_collage import create_collage

def main():
    """Main function to process images based on count"""
    
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/process_images.py <image1> [image2] [image3] ...")
        print("Examples:")
        print("  Single image: python3 scripts/process_images.py /path/to/image.png")
        print("  Multiple images: python3 scripts/process_images.py img1.png img2.png img3.png")
        sys.exit(1)
    
    image_paths = sys.argv[1:]
    
    # Validate all input files exist
    for path in image_paths:
        if not os.path.exists(path):
            print(f"Error: Input file '{path}' does not exist")
            sys.exit(1)
    
    print(f"Processing {len(image_paths)} image(s)...")
    
    if len(image_paths) == 1:
        # Single image processing
        print("Single image detected - resizing to 70% of original dimensions")
        result = resize_single_image(image_paths[0])
        
        if result:
            print(f"\n✅ Single image processing completed successfully!")
            print(f"Output: {result}")
        else:
            print(f"\n❌ Single image processing failed!")
            sys.exit(1)
    
    else:
        # Multiple images - create collage
        print("Multiple images detected - creating horizontal collage")
        result = create_collage(image_paths)
        
        if result:
            print(f"\n✅ Collage creation completed successfully!")
            print(f"Output: {result}")
        else:
            print(f"\n❌ Collage creation failed!")
            sys.exit(1)

if __name__ == "__main__":
    main()