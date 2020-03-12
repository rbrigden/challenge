from typing import List, Tuple

# 0.5 second margin (assume 24 FPS)
MARGIN = 12

# Reference solution
REFERENCE = [(135, 165), (152, 342), (225, 423), (228, 490), (295, 545), (383, 571)]


def bounds_close(a: Tuple, b: Tuple, m=5) -> bool:
    d0 = abs(a[0] - b[0])
    d1 = abs(a[1] - b[1])
    return d0 <= m and d1 <= m


def f1_score(precision: float, recall: float) -> float:
    return 2 * (precision * recall) / (precision + recall)


def test(solution: List[Tuple[int, int]]) -> Tuple[float, float]:
    """ Test your solution with this function """
    tp = 0
    for y in REFERENCE:
        compares = sum([bounds_close(x, y, m=MARGIN) for x in solution])
        tp += int(compares > 0)
    fp = max(len(solution) - len(REFERENCE), 0)
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
