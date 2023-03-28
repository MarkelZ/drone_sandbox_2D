
import math


class Background:
    def __init__(self, col_back1, col_back2, col_grnd1, col_grnd2, square_len):
        self.col_back1 = col_back1
        self.col_back2 = col_back2
        self.col_grnd1 = col_grnd1
        self.col_grnd2 = col_grnd2
        self.square_len = square_len

    def draw(self, camera):
        x, y = camera.x, camera.y
        width, height = camera.width, camera.height
        l = self.square_len

        i0 = int(x / l)
        j0 = int(y / l)
        N_i = int((x + width) / l) + 1
        N_j = int((y + height) / l) + 1

        for i in range(i0, N_i):
            for j in range(j0, N_j):
                col_back = self.col_back1 if (
                    i + j) % 2 == 0 else self.col_back2
                camera.render_axis_aligned_rect(
                    col_back, i * l, j * l, (i + 1) * l, (j + 1) * l)
