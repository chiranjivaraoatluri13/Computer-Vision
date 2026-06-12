# Computer Vision: YOLOv8 Object Detection

Foundational object detection experiments using **YOLOv8** (Ultralytics) and **OpenCV**. Run detection on a static image or a live webcam feed.

Originally built as part of assistive technology and robotics coursework at Arizona State University.

## Features

- Real time object detection from a webcam (`detect_webcam.py`)
- Single image detection with saved output (`detect_sample.py`)
- Uses the pretrained `yolov8s.pt` model (downloads automatically on first run)

## Requirements

- Python 3.8+
- Webcam (for live detection)

## Installation

```bash
git clone https://github.com/chiranjivaraoatluri13/Computer-Vision.git
cd Computer-Vision
pip install ultralytics opencv-python
```

## Usage

### Live webcam detection

```bash
python detect_webcam.py
```

Press **q** to quit.

### Detect objects in an image

1. Place your image in the project folder.
2. Update the filename in `detect_sample.py` (default: `your_image.jpg`).
3. Run:

```bash
python detect_sample.py
```

Annotated results are saved to the `output/` folder.

## Project structure

```
Computer-Vision/
├── detect_webcam.py    # Live YOLOv8 webcam inference
├── detect_sample.py    # Single image detection
└── README.md
```

## Model

This project uses [YOLOv8s](https://docs.ultralytics.com/models/yolov8/) from Ultralytics. The weights file is downloaded automatically the first time you run either script.

## License

MIT
