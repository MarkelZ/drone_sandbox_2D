
import math


class Background:
    def __init__(self, col_back1, col_back2, col_grnd1, col_grnd2, square_len):
        self.col_back_list = [col_back1, col_back2]
        self.col_grnd_list = [col_grnd1, col_grnd2]
        self.square_len = square_len

    def draw(self, camera):
        x, y = camera.x, camera.y
        width, height = camera.width, camera.height
        l = self.square_len

        i0 = int(x / l) - 1
        j0 = int(y / l) - 1
        N_i = int((x + width) / l) + 1
        N_j = int((y + height) / l) + 1

        for i in range(i0, N_i):
            for j in range(j0, N_j):
                x = i * l
                y = j * l
                if y >= camera.height:
                    color = self.col_grnd_list[(i + j) % 2]
                else:
                    color = self.col_back_list[(i + j) % 2]
                camera.render_axis_aligned_rect(
                    color, i * l, j * l, l, l)
