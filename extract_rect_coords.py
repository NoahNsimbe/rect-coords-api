import cv2
from flask import Blueprint, request, jsonify
import numpy as np
from werkzeug.exceptions import BadRequest

extract_rect_coords_bp = Blueprint("extract_rect_coords", __name__)
ALLOWED_EXTENSIONS = {"png"}


def get_rects_and_vertices(grayscale_image) -> list[tuple[int, list[list[int]]]]:
    edges = cv2.Canny(grayscale_image, 30, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    rectangles = []

    for index, contour in enumerate(contours[::-1]):
        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        vertices = approx.reshape(-1, 2)
        vertices = [[int(coordinate[0]), int(coordinate[1])] for coordinate in vertices]
        rectangles.append((index, vertices))

    return rectangles


@extract_rect_coords_bp.route("/extract-rect-coords", methods=["POST"])
def extract_rect_coords():
    if "file" not in request.files:
        raise BadRequest("No image in form data")

    image = request.files["file"]

    if (
        image.filename == ""
        or image.filename.rsplit(".", 1)[1].lower() not in ALLOWED_EXTENSIONS
    ):
        raise BadRequest("No selected png file")

    image_data = image.read()

    np_array = np.frombuffer(image_data, np.uint8)
    image_decode = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    grayscale_image = cv2.cvtColor(image_decode, cv2.COLOR_BGR2GRAY)

    rectangles = get_rects_and_vertices(grayscale_image)
    rectangles = [
        {"id": rectangle[0], "coordinates": rectangle[1]} for rectangle in rectangles
    ]

    return jsonify(rectangles), 200
