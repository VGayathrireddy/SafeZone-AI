# SafeZone AI — AI-Powered Workplace Hazard Detection

SafeZone AI is a computer vision project designed to improve workplace safety by analyzing video footage from warehouses, factories, and construction sites. It uses object detection to identify people in workplace environments and aims to detect safety violations such as missing protective equipment and restricted-area entry.

The system is being developed to combine object detection, object tracking, and temporal event verification to identify potential hazards and generate timestamped alerts.

## 🎯 Project Objectives

* Detect people in workplace video footage.
* Identify missing personal protective equipment (PPE), such as helmets and safety vests.
* Detect entry into restricted or hazardous zones.
* Track people across video frames.
* Generate alerts for potential safety violations.
* Build a dashboard to review detected hazards and incidents.

## ✨ Key Features

### Implemented

* Video input and frame-by-frame processing.
* Person detection using the YOLO object detection model.
* GPU-accelerated inference using an NVIDIA GPU.
* Annotated video output showing detection results.
* Basic detection statistics, including processed frames and detection counts.

### Planned

* Helmet and safety-vest detection.
* Person tracking across consecutive frames.
* Restricted-area intrusion detection.
* Temporal verification to reduce false alerts.
* Timestamped hazard event logging.
* FastAPI backend and React dashboard.
* PostgreSQL database for storing incidents and alert history.

## 🛠️ Tech Stack

* **Language:** Python
* **Computer Vision:** OpenCV
* **Object Detection:** Ultralytics YOLO
* **Deep Learning:** PyTorch
* **Backend (planned):** FastAPI
* **Frontend (planned):** React.js
* **Database (planned):** PostgreSQL
* **Version Control:** Git and GitHub

## 🖥️ System Requirements

* Python 3.10 or a compatible version supported by the installed dependencies
* OpenCV
* Ultralytics
* PyTorch
* An NVIDIA GPU with compatible drivers and CUDA-enabled PyTorch is recommended for faster inference
* A workplace video file for testing

CPU inference may also be possible, but processing speed can be lower.

## 📁 Project Structure

```text
SafeZone-AI/
├── ai-engine/
│   └── detector.py
├── videos/
│   └── input_video.mp4
├── outputs/
│   └── detected_workplace.mp4
├── requirements.txt
└── README.md
```

*The structure above is a suggested layout. Adjust it to match the actual files in your repository.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/VGayathrireddy/SafeZone-AI.git
cd SafeZone-AI
```

### 2. Create a virtual environment

```bash
python -m venv safezone-ai
```

Activate it on Windows PowerShell:

```powershell
.\safezone-ai\Scripts\Activate.ps1
```

### 3. Install dependencies

If the project includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the core packages:

```bash
pip install ultralytics opencv-python
```

Install a PyTorch build appropriate for your hardware from the official [PyTorch installation guide](https://pytorch.org/get-started/locally/).

### 4. Add a test video

Place your workplace video in the location expected by `ai-engine/detector.py`. Update the input video path in the script if necessary.

### 5. Run SafeZone AI

```bash
python ai-engine/detector.py
```

The script processes the video, runs person detection, and saves the annotated output to the configured output path.

## 📊 Initial Detection Results

In an initial test using a 766-frame workplace video:

| Metric                          |    Result |
| ------------------------------- | --------: |
| Frames processed                |       766 |
| Person detections across frames |     2,671 |
| Average detections per frame    |      3.49 |
| Average processing speed        | 13.15 FPS |

**Note:** These are initial person-detection results from one test video. They do not represent unique people, PPE detection accuracy, or validated hazard-detection performance.

## 🔮 Future Enhancements

* Train or fine-tune a model to recognize helmets, safety vests, and missing PPE.
* Integrate multi-object tracking to maintain person identities across frames.
* Define configurable restricted zones and detect intrusion events.
* Verify incidents across multiple frames before raising alerts.
* Build a React dashboard with video playback and incident summaries.
* Add a FastAPI service and PostgreSQL-based incident storage.
* Evaluate precision, recall, and false-positive rates on a labeled test set.

## 🌍 Potential Applications

* Construction sites
* Manufacturing facilities
* Warehouses and logistics centers
* Industrial plants
* Other workplaces requiring PPE compliance monitoring

## ⚠️ Disclaimer

SafeZone AI is a developing prototype intended for experimentation and demonstration. Its detections may be inaccurate, and it should not be used as the sole method for workplace safety monitoring or emergency decisions.

## 👩‍💻 Author

**Gayathri Reddy**

* GitHub: [VGayathrireddy](https://github.com/VGayathrireddy)
