import cv2
import pytest

from extract_rect_coords import get_rects_and_vertices


@pytest.fixture
def grayscale_images():
    rotated_image = cv2.imread("rotated.png")
    rotated_gray = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2GRAY)

    simple_image = cv2.imread("simple.png")
    simple_gray = cv2.cvtColor(simple_image, cv2.COLOR_BGR2GRAY)

    return rotated_gray, simple_gray


def test_get_rotated_rects_and_vertices(grayscale_images):
    rotated_rectangles = get_rects_and_vertices(grayscale_images[0])
    assert len(rotated_rectangles) == 3

    assert rotated_rectangles[0][0] == 0
    assert rotated_rectangles[0][1] == [[112, 52], [47, 393], [93, 405], [157, 62]]

    assert rotated_rectangles[1][0] == 1
    assert rotated_rectangles[1][1] == [[265, 79], [201, 418], [246, 432], [310, 93]]

    assert rotated_rectangles[2][0] == 2
    assert rotated_rectangles[2][1] == [[418, 106], [354, 449], [399, 459], [464, 118]]


def test_get_simple_rects_and_vertices(grayscale_images):
    simple_rectangles = get_rects_and_vertices(grayscale_images[1])
    assert len(simple_rectangles) == 3

    assert simple_rectangles[0][0] == 0
    assert simple_rectangles[0][1] == [[76, 55], [74, 454], [124, 455], [124, 56]]

    assert simple_rectangles[1][0] == 1
    assert simple_rectangles[1][1] == [[232, 55], [230, 454], [280, 455], [280, 56]]

    assert simple_rectangles[2][0] == 2
    assert simple_rectangles[2][1] == [[388, 55], [386, 454], [436, 455], [436, 56]]
