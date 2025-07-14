
# Image from Conversation - Proper Workflow

## The Issue
Claude Code cannot extract binary image data from conversation messages.
The Write tool only handles text content, creating placeholder files instead of actual images.

## The Solution
1. Save the image manually:
   - Right-click on the image in the conversation
   - Select "Save image as..." or similar
   - Save to this directory with a descriptive name (e.g., 'screenshot.png')

2. Process the saved image:
   ```bash
   python3 scripts/resize_single.py screenshot.png
   ```

## Why This Happens
- Images in conversation are visual data embedded in the message
- Claude Code's tools cannot extract this binary data
- The Write tool creates text placeholders instead of actual image files
- This is a fundamental limitation of the current toolset

## Best Practice
Always save image files directly to the working directory, then use the reusable scripts.
