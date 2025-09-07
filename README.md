# Image Processing - Project 1: Color Detection

This repository contains a project that detects and outlines yellow colored objects in a video using OpenCV. The script processes frames, applies color masking, and uses connected components to draw separate bounding boxes around each object.

## Files
- `yellow_flower.mp4`: Demonstration video showing the detection in action.
- `main_saved_video_test.py`: Main Python script with the image processing logic.

## How to Run
1. Install dependencies: `pip install opencv-python numpy pillow`
2. Place `yellow_flower.mp4` in the repo folder.
3. Run: `python main_saved_video_test.py`

## Demo
<video width="640" height="480" controls>
  <source src="https://github.com/aminemoussi/Image-Processing-Projects/color_detection_demo.mp4" type="video/mp4">
  Your browser doesn't support video. Download it [here](https://github.com/aminemoussi/Image-Processing-Projects/color_detection_demo.mp4).
</video>

## Notes
- Adjust the yellow color bounds or kernel size in the script for better results.
- Feel free to contribute or suggest improvements!

-------
