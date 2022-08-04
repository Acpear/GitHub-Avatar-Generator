import cv2
import numpy as np
import random
import uuid

SIZE = 256       # Image width and height (square, not rectangle)
RADIUS = 96      # The max radius
RSPLIT = 8       # Number of segments along the radius
PIECES = 12      # Divide 360 degrees into how many parts
THICKNESS = 0.5  # The probability to color a sector ring, 0(full white) to 1(pure color)
FORMAT = "png"   # Output format


def main():
    CENTER = (SIZE // 2, SIZE // 2)
    COLOR = (
        random.randrange(0, 255),
        random.randrange(0, 255),
        random.randrange(0, 255),
    )
    WHITE = (255, 255, 255)

    img = np.ones((SIZE, SIZE, 3), np.uint8) * 255
    for angle in np.linspace(0, 360, PIECES, endpoint=False):
        for radius in np.linspace(RADIUS, 0, RSPLIT, endpoint=False):
            cv2.ellipse(
                img,
                CENTER,
                (int(radius), int(radius)),
                0,
                angle,
                angle + 360 / PIECES,
                COLOR if random.random() < THICKNESS else WHITE,
                -1,
            )

    NAME = str(uuid.uuid4()) + "." + FORMAT
    cv2.imwrite(NAME, img)


if __name__ == "__main__":
    main()
