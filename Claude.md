
# Claude.md

## 🖼 Image Processing Instruction for Terminal Worker (Claude)

Claude operates **inside a single working directory**. You will provide file paths to screenshots (input images), and Claude must process them according to the rules below and save only the results **in the `output/` folder** without copying the original images.

**Important Limitation:** Claude Code cannot extract binary image data from conversation messages. The Write tool only handles text content, creating placeholder files instead of actual images. 

**Solution:** Save images manually to the working directory, then use the reusable scripts for processing.

---

### ✅ Rules for Processing Images

#### 1. **If there is only ONE image:**
- Resize it to **70% of its original dimensions** (reduce by 30%).
- Keep the same image format.
- Do not apply filters, compression, or any visual changes.
- Save the result in the `output/` folder using the filename format:
  ```
  output/resized_<UUID>.<original_extension>
  ```

#### 2. **If there are MULTIPLE images:**
- Combine them into a **horizontal collage**.
- Place the images **side by side** with a clearly visible gap between them.
- The gap must:
  - Be at least **10 pixels wide**
  - Have a **non-vivid, neutral color**: `#D3D3D3` (light gray)
- **Resize the final collage to 30% of its original size** for web-friendly dimensions
- Save the result as a **PNG** in the `output/` folder using the filename format:
  ```
  output/collage_<UUID>.png
  ```

---

### 🧾 General Notes
- Always generate a **new UUID** for each result.
- Do **not** compress images or apply filters.
- For collages:
  - Resize all images to the same height (if needed), keeping aspect ratio.
  - Align images to the **top edge**.
  - **Final collage is resized to 30% of original size** for web-friendly dimensions.

### 📁 Working with Images from Conversation
- **Limitation**: Claude Code cannot extract binary image data from conversation messages
- **Issue**: Write tool creates placeholder text files instead of actual images
- **Solution**: Save images manually to working directory first
- **Workflow**: Save image → Use reusable scripts → Check output folder
- **Best Practice**: Always save image files directly to the working directory

---

### 🛠️ Convenient Aliases (Recommended)
Quick and easy commands for image processing:
- `./resize <image>` - Resize single image to 70% of original dimensions
- `./collage <img1> <img2> [img3]...` - Create horizontal collage from multiple images
- `./process <img1> [img2]...` - Auto-detect single vs multiple and process accordingly

### 🛠️ Reusable Scripts (Alternative)
The `scripts/` folder contains ready-to-use Python scripts:
- `scripts/resize_single.py` - Resize single image to 70% of original dimensions
- `scripts/create_collage.py` - Create horizontal collage from multiple images
- `scripts/process_images.py` - Auto-detect single vs multiple and process accordingly

### 🛠️ Optional CLI Tools
You may also use CLI tools such as:
- `convert` (from ImageMagick)
- `uuidgen` for generating UUIDs
- `identify` for image dimensions

### 📦 Dependencies
For Python-based image processing:
- **Pillow** (PIL): Install safely using virtual environment (`python3 -m venv venv && source venv/bin/activate && pip install Pillow`) or user installation (`pip3 install --user Pillow`)
- Provides `PIL.Image` module for loading, manipulating, and saving images

---

### 🔄 Examples

#### **Recommended: Using Convenient Aliases**

**Single image processing:**
```bash
./resize "/path/to/image.png"
```

**Multiple image processing (collage):**
```bash
./collage "/path/to/img1.png" "/path/to/img2.png" "/path/to/img3.png"
```

**Auto-detect single vs multiple:**
```bash
./process "/path/to/image1.png" "/path/to/image2.png"
```

#### **Alternative: Using Full Script Paths**

**Single image processing:**
```bash
python3 scripts/resize_single.py "/path/to/image.png"
```

**Multiple image processing (collage):**
```bash
python3 scripts/create_collage.py "/path/to/img1.png" "/path/to/img2.png" "/path/to/img3.png"
```

**Auto-detect single vs multiple:**
```bash
python3 scripts/process_images.py "/path/to/image1.png" "/path/to/image2.png"
```

#### **Alternative: Manual Processing**

**Resize one image (ImageMagick):**
```bash
mkdir -p output && convert input.jpg -resize 70% output/resized_$(uuidgen).jpg
```

**Create collage (ImageMagick):**
```bash
convert \( img1.jpg \) \
  \( -size 10xHEIGHT xc:"#D3D3D3" \) \
  \( img2.jpg \) \
  +append output/collage_$(uuidgen).png
```
*Note: replace `HEIGHT` with the target height (e.g., the tallest image's height).*

**Manual Python processing:**
```bash
python3 -c "
from PIL import Image
import uuid
img = Image.open('input.png')
width, height = img.size
new_width = int(width * 0.7)
new_height = int(height * 0.7)
resized = img.resize((new_width, new_height), Image.LANCZOS)
resized.save(f'output/resized_{uuid.uuid4()}.png')
"
```
