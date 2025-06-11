
# 🎥 Video Captioning with BLIP 🧠

This project uses a Vision-Language Model (VLM) to automatically generate natural language descriptions from videos. It extracts key frames from `.mp4` videos and uses Salesforce's BLIP model to generate accurate and concise captions.

🔗 **GitHub Repository**: [video-captioning-with-blip](https://github.com/rjvibez/video-captioning-with-blip)

---

## 🧠 Model Used

- **Model**: [`Salesforce/blip-image-captioning-base`](https://huggingface.co/Salesforce/blip-image-captioning-base)
- **Framework**: Hugging Face Transformers


---

## 📂 Project Structure

```
video-captioning-with-blip/
├── blip_video_captioning.py     # Main captioning script
├── requirements.txt             # Dependency list
├── *.mp4                        # Your input videos
├── *_frame*.jpg                 # Extracted video frames
└── README.md                    # Project documentation
```

---

## 🚀 How It Works

1. Loads BLIP image captioning model from Hugging Face.
2. For each video in the list:
   - Captures 3 frames from the video (at 10%, 50%, 90% of duration).
   - Saves and loads those frames using OpenCV + PIL.
   - Feeds the frames to the BLIP model for captioning.
   - Combines all 3 frame captions into a final description.

---

## 🧪 Example Output

**Video**: `cutting_onion.mp4`  
```
🖼️ Frame 1 Caption: a person chopping vegetables on a cutting board  
🖼️ Frame 2 Caption: a close up of onions being chopped  
🖼️ Frame 3 Caption: a wooden cutting board with onions  
✅ Final Caption: a person chopping vegetables on a cutting board | a close up of onions being chopped | a wooden cutting board with onions
```

**Video**: `eye_makeup.mp4`  
```
🖼️ Frame 1 Caption: a woman applying her makeup with a brush  
🖼️ Frame 2 Caption: a person looking in the mirror  
🖼️ Frame 3 Caption: a closeup of the eye  
✅ Final Caption: a woman applying her makeup with a brush | a person looking in the mirror | a closeup of the eye
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/rjvibez/video-captioning-with-blip.git
cd video-captioning-with-blip
```

### 2. (Optional) Create Virtual Environment
```bash
python -m venv caption_env
caption_env\Scripts\activate   # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Script
Ensure your `.mp4` files are in the root folder and then run:

```bash
python blip_video_captioning.py
```

---

## 📦 Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, here are the key packages:

```txt
transformers
torch
opencv-python
Pillow
```

---

## 🤖 Approach Overview

The script processes each video by:
- Extracting three key frames (start, middle, end)
- Captioning each frame using BLIP
- Combining captions for a more complete summary

This improves accuracy and relevance by leveraging multiple temporal perspectives.

---

## 🧠 Reflection

In some cases (e.g., `cutting_onion.mp4`), the model generated highly relevant captions. However, in others (like `eye_makeup.mp4`), the captions were vague. Manual labeling often outperformed the model in creativity and specificity, especially when the video context required deeper reasoning.

---

## 📜 License

This project is open-source and for educational purposes.

---

## 👤 Author

Developed by [@rjvibez](https://github.com/rjvibez)
