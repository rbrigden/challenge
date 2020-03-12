# A challenge from Inokyo

## Overview

Given a video from a stationary camera overlooking a pedestrian walkway, identify the number of distinct individuals
who have both entered *and* exited the scene. You must also estimate the time (represented as the number of frames from the start of the video)
at which each individual entered and exited within a margin of 0.5 seconds. Given that the provided video is 
recorded at 24 FPS, this is a margin of 12 frames.

To get started, you are provided a set of (noisy) person bounding box detections of format `[x0, y0, x1, y1]` for each frame in the video. 
These are in standard image coordinates

To view the test video with annotated detections, run

```shell script
python challenge/main.py visualize-detections --video data/pedestrians.mp4 --detections data/pedestrians.jsonl
```

Refer to the `visualize_detections` function to see how to easily read the video and detections.

## Solution format

The solution is a `List` of `Tuple`s of `int`s, with each tuple corresponding to the 
approximate frames (within a 0.5 second margin) at which an individual entered and exited the scene.

For example, if 3 individuals walk through the scene in a video, a solution could look like

```python
[(10, 90), (55, 140), (85, 200)]
```

Your goal is to maximize the F1-score of your solution. You can test the performance of your solution using 
the `test` function provided in `test.py`. The `REFERENCE` list in `test.py` is the ground truth solution for the
provided video.

Once you are satisfied with the performance of your solution, ensure that the following command successfully 
displays the output of the `test` function when provided your solution.

```shell script
python challenge/main.py run --video data/pedestrians.mp4 --detections data/pedestrians.jsonl
```

Then, briefly discuss your approach in a file called `DISCUSSION.md`. Please detail 
the pros and cons of your approach, and specifically what the failure cases are.

## Provided materials
- Test video `data/pedestrians.mp4`
- Detections (JSON lines format) `data/pedestrians.jsonl`

## Environment

This requires a python3.7 environment with the dependencies listed in `requirements.txt`

### Easy setup with virtualenv

Create a virtualenv 

```shell script
virtualenv --python=python3.7 venv
source venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$PWD:$PYTHONPATH
```


## Details
- The solution must run in real time (24 FPS)
- You may import any other open-source python package. If you do, you must add it to `requirements.txt` 
  with a version specified.
- You may use snippets of open-source code as long as it is clear that you are using it in a 
  principled way. For example, you don't need to implement a Kalman filter from scratch if you would find one useful,
  but setting the parameters for the filter should reflect your understanding of the algorithm in practice.
 


## What we are looking for
- Clear, concise code
- Robust solutions over clever tricks (we like clever, but not if it might only work on this single test case)
- An insightful discussion in `DISCUSSION.md`, especially if your solutions performance is l
- [OPTIONAL] a visualization of your solution. we have provided a function template called `visualize_solution`

## Tips
- Each pedestrian walks at a near constant velocity and only move a short distance frame over frame, so trying to associate
  detections at `t+1` to a set of hypotheses at `t` could be a good idea
- For bipartite matching: [linear_sum_assignment](https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linear_sum_assignment.html)
- For localizing motion: [optical flow](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html)
- For an elegant distance function: [gIoU](https://arxiv.org/abs/1902.09630)
- For easy kalman filtering: [pykalman](https://pykalman.github.io/) or [filterpy](https://filterpy.readthedocs.io/en/latest/)

These tips are just tips, and none of the aforementioned techniques are required to produce a working solution.

## Feedback

If there appears to be an error in this writeup or in the provided starter code, please send an email to `ryan@inokyo.com`.
