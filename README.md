# Claude Image Processor

An automated image processing tool that handles screenshot resizing and collage creation using Claude AI.

## Features

- **Single Image Processing**: Automatically resizes images to 70% of original size
- **Multiple Image Processing**: Creates horizontal collages with proper spacing
- **Smart File Naming**: Uses UUIDs for unique output filenames
- **Format Preservation**: Maintains original image formats for single images, outputs PNG for collages

## Setup

### Prerequisites

- Python 3.x
- Pillow (PIL) library

### Installation

1. Clone this repository:
   ```bash
   git clone git@github.com:DRadmir/Claude_image_processor.git
   cd Claude_image_processor
   ```

2. Install dependencies:
   ```bash
   pip3 install --break-system-packages Pillow
   ```

## Usage

### Processing Single Image

Provide a single image file path to Claude:

```
/path/to/your/image.png
```

**Result**: Creates `resized_<UUID>.<original_extension>` with image resized to 70% of original size.

### Processing Multiple Images

Provide multiple image file paths to Claude:

```
/path/to/image1.png /path/to/image2.png /path/to/image3.png
```

**Result**: Creates `collage_<UUID>.png` with images arranged horizontally with 10px light gray (#D3D3D3) gaps between them.

## Processing Rules

### Single Image Processing
- ✅ Resize to 70% of original dimensions
- ✅ Keep same image format
- ✅ No compression or filters applied
- ✅ Save as: `resized_<UUID>.<original_extension>`

### Multiple Image Processing
- ✅ Create horizontal collage
- ✅ 10px gaps with light gray color (#D3D3D3)
- ✅ Images aligned to top edge
- ✅ Auto-resize to consistent height if needed
- ✅ Save as: `collage_<UUID>.png`

## File Structure

```
Claude_image_processor/
├── README.md           # This file
├── Claude.md          # Detailed processing instructions for Claude
├── .gitignore         # Excludes all image files from version control
└── [output images]    # Generated resized images and collages
```

## Technical Details

- **Image Processing**: Uses Python Pillow (PIL) library
- **UUID Generation**: Uses system `uuidgen` command
- **Supported Formats**: PNG, JPG, JPEG, GIF, BMP, SVG, WebP, ICO, TIFF
- **Gap Color**: #D3D3D3 (light gray)
- **Alignment**: Top-aligned for collages

## Examples

### Example 1: Single Image
```bash
# Input: screenshot.png (1200x800)
# Output: resized_A1B2C3D4-E5F6-7890-ABCD-EF1234567890.png (840x560)
```

### Example 2: Multiple Images
```bash
# Input: img1.png, img2.png, img3.png (each 1206x2622)
# Output: collage_A1B2C3D4-E5F6-7890-ABCD-EF1234567890.png (3638x2622)
```

## Notes

- Original images are not copied to the working directory
- Only processed results are saved in the working directory
- All image files are excluded from git tracking via `.gitignore`
- Generated files use UUID for uniqueness and avoid conflicts