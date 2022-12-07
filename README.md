# oss-opencv-termproject

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white) ![Numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)

> Gachon OpenSourceSW term project with OpenCV

## Introduce

- Check person and background
- Remove original background and Change to other background.
- And Add watermark(or some text).

## Demo

## Getting Started

- Require Python3 (This project was test on Python3.10)
- Require OpenCV, Numpy and Pillow for dependencies

```shell
pip install opencv-python numpy pillow
```

## How to run

First, Run main source code.

```shell
py main.py
```

And, Enter a text that you want to put as a watermark.

```shell
Enter the background country name : <Your Input>
```

Finally, Show a result image and save.

## References

- Facial Recognition
  - https://suy379.tistory.com/91
- Detect a background
  - WIP
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
