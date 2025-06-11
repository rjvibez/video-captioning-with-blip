from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import cv2
import os

# --------- Load Smaller, Faster BLIP Model ----------
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# --------- List of Videos ----------
video_files = ["eye_makeup.mp4", "cutting_onion.mp4", "handstand_pushupAi.mp4", "Dough_Tossing.mp4", "teacher_teaching-AI.mp4", "yoyo.mp4"]

# --------- Frame Capture Positions ----------
frame_ratios = [0.1, 0.5, 0.9]  # 10%, 50%, 90%

# --------- Process Each Video ----------
for video_path in video_files:
    print(f"\n🎥 Processing: {video_path}")
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if frame_count == 0:
        print(f"❌ Unable to read frames from {video_path}")
        continue

    captions = []

    for idx, ratio in enumerate(frame_ratios):
        frame_num = int(frame_count * ratio)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        success, frame = cap.read()

        if not success:
            print(f"⚠️ Failed to capture frame at {ratio*100}% for {video_path}")
            continue

        # Save and load frame
        frame_name = f"{os.path.splitext(video_path)[0]}_frame{idx+1}.jpg"
        cv2.imwrite(frame_name, frame)
        image = Image.open(frame_name).convert("RGB")

        # Generate caption
        inputs = processor(images=image, return_tensors="pt").to(device)
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        captions.append(caption)

        print(f"🖼️ Frame {idx+1} Caption: {caption}")

    cap.release()

    # --------- Combine Captions ----------
    combined_caption = " | ".join(captions)
    print(f"✅ Final Caption for {video_path}: {combined_caption}")
