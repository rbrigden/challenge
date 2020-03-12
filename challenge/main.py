import click
from challenge.io import Mp4Reader, JSONLinesReader
import cv2
import os
from challenge.test import test


def draw_box(img, box, color=(0, 255, 0), thickness=1, **kwargs):
    """ wrapper with sensible defaults """

    x0, y0, x1, y1 = box
    pt0 = (int(x0), int(y0))
    pt1 = (int(x1), int(y1))
    return cv2.rectangle(img, pt0, pt1, color=color, thickness=thickness, **kwargs)


def draw_text(img, text, offset, color=(0, 0, 0), font_scale=1, thickness=2):
    return cv2.putText(
        img,
        text,
        offset,
        cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=font_scale,
        color=color,
        thickness=thickness,
    )


@click.group()
def main():
    pass


@main.command()
@click.option("--video", type=str, required=True, help="path to mp4 video")
@click.option(
    "--detections",
    type=str,
    required=True,
    help="path to JSON lines file with synced detections",
)
def run(video: str, detections: str):
    """ REQUIRED to implement"""
    # YOUR CODE HERE
    solution = None
    test(solution)


@main.command()
@click.option("--video", type=str, required=True, help="path to mp4 video")
@click.option(
    "--detections",
    type=str,
    required=True,
    help="path to JSON lines file with synced detections",
)
def visualize_solution(video: str, detections: str):
    """ This could be helpful to implement! """
    # YOUR CODE HERE
    raise NotImplementedError


@main.command()
@click.option("--video", type=str, required=True, help="path to mp4 video")
@click.option(
    "--detections",
    type=str,
    required=True,
    help="path to JSON lines file with synced detections",
)
def visualize_detections(video: str, detections: str):
    window_name = os.path.basename(video)
    with Mp4Reader(video) as video_reader, JSONLinesReader(
        detections
    ) as detections_reader:
        fps = video_reader.frame_rate
        frame_shape = video_reader.frame_shape
        for t, (bgr_frame, detections) in enumerate(
            zip(video_reader.read_iter(), detections_reader.read_iter())
        ):
            for d in detections:
                bgr_frame = draw_box(bgr_frame, d, thickness=2)

            draw_text(bgr_frame, f"{frame_shape[0]}x{frame_shape[1]}, {fps}fps, t={t:04}", (20, 50))
            cv2.imshow(window_name, bgr_frame)
            wait_ms = int(1000.0 / fps)
            cv2.waitKey(wait_ms)


if __name__ == "__main__":
    main()
