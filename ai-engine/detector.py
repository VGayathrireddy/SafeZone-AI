
import cv2
import torch
from pathlib import Path
from ultralytics import YOLO
import time

# 1. Select GPU when available
device = 0 if torch.cuda.is_available() else "cpu"

if device == 0:
    print("Running on:", torch.cuda.get_device_name(0))
else:
    print("Running on: CPU")

# 2. Load the pretrained YOLO model
model = YOLO("yolo11n.pt")

# 3. Set input and output paths
video_path = "videos/workplace.mp4"
output_path = "outputs/detected_workplace.mp4"

Path("outputs").mkdir(exist_ok=True)

# 4. Open the input video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise FileNotFoundError(
        f"Could not open {video_path}. Check the file path."
    )

# 5. Read video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0 or width <= 0 or height <= 0:
    cap.release()
    raise ValueError("Could not read video properties.")

# 6. Create output video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (width, height)
)

if not writer.isOpened():
    cap.release()
    raise RuntimeError("Could not create the output video.")

# 7. Initialize statistics
total_frames = 0
total_detections = 0
start_time = time.perf_counter()

print("\nProcessing video... Press Q to stop early.\n")

# 8. Process each frame
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect people (COCO class 0)
    results = model.predict(
        source=frame,
        device=device,
        imgsz=640,
        conf=0.25,
        classes=[0],
        verbose=False
    )

    # Count detections in this frame
    person_count = len(results[0].boxes)

    total_frames += 1
    total_detections += person_count

    # Draw boxes and labels
    annotated_frame = results[0].plot()

    # Save the annotated frame
    writer.write(annotated_frame)

    # Display the processed frame
    cv2.imshow(
        "SafeZone AI - Person Detection",
        annotated_frame
    )

    # Press Q to exit early
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 9. Release resources
cap.release()
writer.release()
cv2.destroyAllWindows()

# 10. Calculate and display statistics
elapsed_time = time.perf_counter() - start_time

print("\n========== SafeZone AI Results ==========")
print("Total frames processed:", total_frames)
print("Total person detections across frames:", total_detections)

if total_frames > 0:
    avg_detections = total_detections / total_frames
    print("Average detections per frame:", round(avg_detections, 2))

if elapsed_time > 0:
    processing_fps = total_frames / elapsed_time
    print("Processing speed:", round(processing_fps, 2), "FPS")

print("Output video:", output_path)
print("=========================================")