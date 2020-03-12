from copy import copy
from typing import List, Tuple, Optional

# 0.5 second margin (assume 24 FPS)
MARGIN = 12

# Reference solution
REFERENCE = [(135, 165), (152, 342), (225, 423), (228, 490), (295, 545), (383, 571)]


def component_l1_dist(a: Tuple, b: Tuple):
    d0 = abs(a[0] - b[0])
    d1 = abs(a[1] - b[1])
    return d0, d1


def f1_score(precision: float, recall: float) -> float:
    return 2 * (precision * recall) / (precision + recall)


def find_match(
    query: Tuple[int, int], gallery: List[Tuple[int, int]], margin: int
) -> Optional[Tuple[int, int]]:
    dists = [
        (z, d0 + d1)
        for z, (d0, d1) in zip(
            gallery, map(lambda x: component_l1_dist(x, query), gallery)
        )
        if d0 <= margin and d1 <= margin
    ]
    if len(dists) > 0:
        return min(dists, key=lambda x: x[1])[0]
    return None


def test(solution: List[Tuple[int, int]]) -> Tuple[float, float]:
    """ Test your solution with this function """
    tp = 0
    candidates = copy(solution)
    for y in REFERENCE:
        match = find_match(y, candidates, MARGIN)
        if match:
            tp += 1
            candidates.pop(candidates.index(match))

    fp = len(solution) - tp
    precision = tp / float(tp + fp)
    fn = len(REFERENCE) - tp
    recall = tp / float(tp + fn)
    print(
        f"Precision: {precision:.3f}, Recall: {recall:.3f}, F1-score: {f1_score(precision, recall):.3f}"
    )
    return precision, recall


if __name__ == "__main__":
    # sanity check
    assert test(REFERENCE) == (1.0, 1.0)
