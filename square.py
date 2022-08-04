import cv2
import numpy as np
import random
import uuid

BLOCK_SIDE_LENGTH = 32  # How many pixels a little square take
MARGIN = 32             # How many pixels between contents and border
SEGMENT = 7             # How many rows and columns the content would display
SYMMETRY = True         # Is it symmetry about vertical direction
THICKNESS = 0.5         # The probability to color a block, 0(full white) to 1(pure color)
FORMAT = "png"          # Output format


def main():
    # Create a new white canvas
    SIDE_LENGTH = 2 * MARGIN + SEGMENT * BLOCK_SIDE_LENGTH
    img = np.ones((SIDE_LENGTH, SIDE_LENGTH, 3), np.uint8)
    img *= 255

    # Color the map
    random.seed(str(uuid.uuid4()))
    COLOR = (
        random.randrange(0, 255),
        random.randrange(0, 255),
        random.randrange(0, 255),
    )
    if SYMMETRY:
        for row in range(SEGMENT):
            for col in range(SEGMENT // 2):
                if random.random() < THICKNESS:
                    # Left part
                    cv2.rectangle(
                        img,
                        (
                            MARGIN + col * BLOCK_SIDE_LENGTH,
                            MARGIN + row * BLOCK_SIDE_LENGTH,
                        ),
                        (
                            MARGIN + (col + 1) * BLOCK_SIDE_LENGTH,
                            MARGIN + (row + 1) * BLOCK_SIDE_LENGTH,
                        ),
                        COLOR,
                        -1,
                    )
                    # Symmetry to right part
                    cv2.rectangle(
                        img,
                        (
                            MARGIN + (SEGMENT - col) * BLOCK_SIDE_LENGTH,
                            MARGIN + row * BLOCK_SIDE_LENGTH,
                        ),
                        (
                            MARGIN + (SEGMENT - (col + 1)) * BLOCK_SIDE_LENGTH,
                            MARGIN + (row + 1) * BLOCK_SIDE_LENGTH,
                        ),
                        COLOR,
                        -1,
                    )
        if SEGMENT % 2:  # Middle line
            for row in range(SEGMENT):
                if random.random() < THICKNESS:
                    cv2.rectangle(
                        img,
                        (
                            MARGIN + (SEGMENT // 2) * BLOCK_SIDE_LENGTH,
                            MARGIN + row * BLOCK_SIDE_LENGTH,
                        ),
                        (
                            MARGIN + (SEGMENT // 2 + 1) * BLOCK_SIDE_LENGTH,
                            MARGIN + (row + 1) * BLOCK_SIDE_LENGTH,
                        ),
                        COLOR,
                        -1,
                    )
    else:  # No symmetry
        for row in range(SEGMENT):
            for col in range(SEGMENT):
                if random.random() < THICKNESS:
                    cv2.rectangle(
                        img,
                        (
                            MARGIN + col * BLOCK_SIDE_LENGTH,
                            MARGIN + row * BLOCK_SIDE_LENGTH,
                        ),
                        (
                            MARGIN + (col + 1) * BLOCK_SIDE_LENGTH,
                            MARGIN + (row + 1) * BLOCK_SIDE_LENGTH,
                        ),
                        COLOR,
                        -1,
                    )

    # Save
    NAME = str(uuid.uuid4()) + "." + FORMAT
    cv2.imwrite(NAME, img)


if __name__ == "__main__":
    main()
    # To generate hundreds of pictures by once, you can add a loop for main()
    # for i in range(100):
    #     main()
