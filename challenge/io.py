import json
import os
from contextlib import ExitStack
from typing import Tuple, Generator

import cv2
import numpy as np


class Mp4Reader:
    def __init__(self, path: str):
        self.path = path

        # check if the path exists because OpenCV won't
        if not os.path.exists(self.path):
            raise FileNotFoundError

        self._cam = cv2.VideoCapture(path)
        self._total_frames = None

    @property
    def frame_rate(self) -> int:
        return int(self._cam.get(cv2.CAP_PROP_FPS))

    @property
    def frame_shape(self):
        width = self._cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self._cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        return [int(height), int(width)]

    def read(self) -> Tuple[bool, np.ndarray]:
        return self._cam.read()

    def read_iter(self) -> Generator[np.ndarray, None, None]:
        ret = True
        while ret:
            ret, frame = self.read()
            if ret:
                yield frame

    def set_pos(self, pos):
        """ set reader position """
        self._cam.set(cv2.CAP_PROP_POS_FRAMES, pos)

    def total_frames(self) -> int:
        """ number of frames in the video """
        if self._total_frames is None:
            self._total_frames = int(self._cam.get(cv2.CAP_PROP_FRAME_COUNT))
        return self._total_frames

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cam.release()


class JSONLinesReader(ExitStack):
    def __init__(self, path: str):
        super().__init__()
        self.path = path

    def __enter__(self):
        self._file = self.enter_context(open(self.path, "r"))
        return self

    def read_iter(self):
        for line in self._file.readlines():
            yield json.loads(line)


