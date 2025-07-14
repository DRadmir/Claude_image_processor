
# Claude.md

## 🖼 Image Processing Instruction for Terminal Worker (Claude)

Claude operates **inside a single working directory**. You will provide file paths to screenshots (input images), and Claude must process them according to the rules below and save only the results **in the working directory** without copying the original images.

---

### ✅ Rules for Processing Images

#### 1. **If there is only ONE image:**
- Resize it to **70% of its original dimensions** (reduce by 30%).
- Keep the same image format.
- Do not apply filters, compression, or any visual changes.
- Save the result in the same folder using the filename format:
  ```
  resized_<UUID>.<original_extension>
  ```

#### 2. **If there are MULTIPLE images:**
- Combine them into a **horizontal collage**.
- Place the images **side by side** with a clearly visible gap between them.
- The gap must:
  - Be at least **10 pixels wide**
  - Have a **non-vivid, neutral color**: `#D3D3D3` (light gray)
- Save the result as a **PNG** using the filename format:
  ```
  collage_<UUID>.png
  ```

---

### 🧾 General Notes
- Always generate a **new UUID** for each result.
- Do **not** compress images or apply filters.
- For collages:
  - Resize all images to the same height (if needed), keeping aspect ratio.
  - Align images to the **top edge**.

---

### 🛠️ Suggested Tools (optional)
You may use CLI tools such as:
- `convert` (from ImageMagick)
- `uuidgen` for generating UUIDs
- `identify` for image dimensions

### 📦 Dependencies
For Python-based image processing:
- **Pillow** (PIL): Install with `pip3 install --break-system-packages Pillow`
- Provides `PIL.Image` module for loading, manipulating, and saving images

---

### 🔄 Examples

#### Resize one image:
```bash
convert input.jpg -resize 70% resized_$(uuidgen).jpg
```

#### Create collage:
```bash
convert \( img1.jpg \) \
  \( -size 10xHEIGHT xc:"#D3D3D3" \) \
  \( img2.jpg \) \
  +append collage_$(uuidgen).png
```
*Note: replace `HEIGHT` with the target height (e.g., the tallest image’s height).*
