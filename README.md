# finger-counting
Real-time hand tracking using MediaPipe and OpenCV with landmark detection and finger counting

This project detects and tracks a single hand in real-time using MediaPipe's Hand Landmark model combined with OpenCV for video capture. It identifies key landmarks on the hand, determines which fingers are extended, and displays the total number of extended fingers on the video feed.

## Reference Image

The file `MediaPipe Hands - Hand Landmark Model.png` is included in the repository for reference purposes only. It illustrates the landmark index IDs and their corresponding anatomical positions as defined by the MediaPipe Hands model. While it is not required for the functionality of the program, the image serves as a helpful visual guide for understanding which ID corresponds to which part of the hand, such as `WRIST`, `THUMB_TIP`, `INDEX_FINGER_MCP`, and so on.

## Dependencies

This project requires the following Python packages. It is recommended to install them in a virtual environment using the `requirements.txt` file included in the repository.
