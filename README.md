# oss-opencv-termproject

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![Numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)

## Introduce

> Detect a person, Change only background image and Add a watermark.

- Detect a person (Han Seunggyu)
- Detect and Remove a background (Hwang Sungwook)
- Change to other background. (Ha Daegyeom)
- Add a watermark. (Cho Hyunjun)

## Demo

## Getting Started

- Require Python3 (This project was test on Python3.10)
- Require OpenCV, Numpy and Pillow for dependencies

```shell
pip install opencv-python numpy pillow
```

## How to run

First, Add two images: an Input image and A background image of what you want to change.

- The Default filenames are input.png and background.png

Second, Run main source code.

```shell
py main.py
```

And, Enter a text that you want to put as a watermark.

```shell
Enter the background country name : <Your Input>
```

Finally, Show a result image and save(result.jpg).

## References

- Facial Recognition
  - https://suy379.tistory.com/91
- Detect and Remove a background
  - https://stackoverflow.com/questions/62648862/how-can-i-change-the-hue-of-a-certain-area-with-opencv-python
  - https://stackoverflow.com/questions/64491530/how-to-remove-the-background-from-a-picture-in-opencv-python
- Change a background
  - Resize image (because copyTo() can use when the image size is the same.)
    - https://www.tutorialkart.com/opencv/python/opencv-python-get-image-size/
    - https://076923.github.io/posts/Python-opencv-8/
  - copyTo() function
    - https://deep-learning-study.tistory.com/104?category=946336
- Draw a watermark
  - https://appia.tistory.com/374
- Convert to PIL image from OpenCV image
  - https://www.zinnunkebi.com/python-opencv-pil-convert/
