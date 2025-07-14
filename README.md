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

2. Install dependencies (choose one method):

   **Option A: Using virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install Pillow
   ```

   **Option B: Using pipx**
   ```bash
   brew install pipx  # On macOS
   pipx install Pillow
   ```

   **Option C: Using Homebrew (macOS)**
   ```bash
   brew install pillow
   ```

   **Option D: User installation**
   ```bash
   pip3 install --user Pillow
   ```

## Usage

### **Recommended: Using Reusable Scripts**

The `scripts/` folder contains ready-to-use Python scripts that handle all image processing tasks:

**Single Image Processing:**
```bash
python3 scripts/resize_single.py "/path/to/image.png"
```

**Multiple Image Processing (Collage):**
```bash
python3 scripts/create_collage.py "/path/to/img1.png" "/path/to/img2.png" "/path/to/img3.png"
```

**Auto-detect Single vs Multiple:**
```bash
python3 scripts/process_images.py "/path/to/image1.png" "/path/to/image2.png"
```

### **Alternative: Using Claude AI**

**Option A: Using file paths**
Provide image file paths to Claude:

```
Single image: /path/to/your/image.png
Multiple images: /path/to/image1.png /path/to/image2.png /path/to/image3.png
```

**Option B: Using images from conversation**
⚠️ **Important Limitation**: Claude Code cannot extract binary image data from conversation messages.

**Solution**: Save images manually first:
1. Right-click on image in conversation
2. Save image to this directory (e.g., 'screenshot.png')
3. Use scripts to process the saved image:
   ```bash
   python3 scripts/resize_single.py screenshot.png
   ```

**Results:**
- **Single image**: Creates `output/resized_<UUID>.<original_extension>` with image resized to 70% of original size
- **Multiple images**: Creates `output/collage_<UUID>.png` with images arranged horizontally with 10px light gray (#D3D3D3) gaps, final collage resized to 30% for web-friendly dimensions

## Processing Rules

### Single Image Processing
- ✅ Resize to 70% of original dimensions
- ✅ Keep same image format
- ✅ No compression or filters applied
- ✅ Save as: `output/resized_<UUID>.<original_extension>`

### Multiple Image Processing
- ✅ Create horizontal collage
- ✅ 10px gaps with light gray color (#D3D3D3)
- ✅ Images aligned to top edge
- ✅ Auto-resize to consistent height if needed
- ✅ **Final collage resized to 30% for web-friendly dimensions**
- ✅ Save as: `output/collage_<UUID>.png`

## File Structure

```
Claude_image_processor/
├── README.md           # This file
├── Claude.md          # Detailed processing instructions for Claude
├── .gitignore         # Excludes output folder from version control
├── scripts/           # Reusable Python scripts for image processing
│   ├── resize_single.py    # Single image resizing script
│   ├── create_collage.py   # Multiple image collage creation script
│   └── process_images.py   # Auto-detect single vs multiple processor
├── tmp/               # Temporary folder (created/deleted during processing)
└── output/            # Generated resized images and collages
    ├── resized_*.png
    ├── resized_*.jpg
    └── collage_*.png
```

## Technical Details

- **Image Processing**: Uses Python Pillow (PIL) library
- **UUID Generation**: Uses system `uuidgen` command
- **Supported Formats**: PNG, JPG, JPEG, GIF, BMP, SVG, WebP, ICO, TIFF
- **Gap Color**: #D3D3D3 (light gray)
- **Alignment**: Top-aligned for collages

## Examples

### Example 1: Single Image Using Script
```bash
python3 scripts/resize_single.py "/path/to/screenshot.png"
# Processing: /path/to/screenshot.png
# Original dimensions: 1200x800
# New dimensions: 840x560
# SUCCESS: Resized image saved to output/resized_A1B2C3D4-E5F6-7890-ABCD-EF1234567890.png
```

### Example 2: Multiple Images Using Script
```bash
python3 scripts/create_collage.py "/path/to/img1.png" "/path/to/img2.png" "/path/to/img3.png"
# Loading 3 images...
# Image 1 dimensions: (1206, 2622)
# Image 2 dimensions: (1206, 2622)
# Image 3 dimensions: (1206, 2622)
# Total collage width: 3638
# Original collage dimensions: (3638, 2622)
# Final collage dimensions (30% scale): (1091, 786)
# SUCCESS: Collage saved to output/collage_A1B2C3D4-E5F6-7890-ABCD-EF1234567890.png
```

### Example 3: Auto-detect Processing
```bash
python3 scripts/process_images.py "/path/to/single_image.png"
# Processing 1 image(s)...
# Single image detected - resizing to 70% of original dimensions

python3 scripts/process_images.py "/path/to/img1.png" "/path/to/img2.png"
# Processing 2 image(s)...
# Multiple images detected - creating horizontal collage
```

## Notes

- **Recommended**: Use the reusable scripts in `scripts/` folder for reliable processing
- The scripts handle all edge cases and provide better error handling than manual processing
- Original images are not copied to the working directory
- Only processed results are saved in the `output/` folder
- The entire `output/` folder is excluded from git tracking via `.gitignore`
- Generated files use UUID for uniqueness and avoid conflicts
- **Important**: Claude Code cannot extract binary image data from conversation messages
- **Solution**: Save images manually to working directory first, then use scripts
- **Limitation**: Write tool creates placeholder text files instead of actual images
- The `tmp/` folder is automatically created and cleaned up during processing
- All scripts are executable and handle cleanup automatically
- See `IMAGE_WORKFLOW_INSTRUCTIONS.md` for detailed workflow guidance