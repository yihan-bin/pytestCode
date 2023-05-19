import numpy as np

from manim import *
from manim import config as global_config
config = global_config.copy()
from fourier_series import *

class abc(FourierCirclesScene):
    config = {

        "center_point": ORIGIN,
        "start_drawn": False,
        "n_cycles" : 1,
        'tex' : '\\pi',
        "n_vectors" : 101,
        "max_circle_stroke_width" : 1,
        "slow_factor" : 0.1,
    }



    def construct(self):

        self.center_point = ORIGIN
        self.start_drawn = False
        self.n_cycles = 1
        self.tex = '\\pi'


        self.n_vectors = 101
        self.max_circle_stroke_width = 1
        self.slow_factor = 0.1


        self.add_vectors_circles_path()
        for n in range(self.n_cycles):
            self.run_one_cycle()

    def add_vectors_circles_path(self):
        path = self.get_path()
        coefs = self.get_coefficients_of_path(path)

        for freq, coef in zip(self.get_freqs(), coefs):
            print(freq, "\t", coef)

        vectors = self.get_rotating_vectors(coefficients=coefs)
        circles = self.get_circles(vectors)
        self.set_decreasing_stroke_widths(circles)
        # approx_path = self.get_vector_sum_path(circles)
        drawn_path = self.get_drawn_path(vectors)
        if self.start_drawn:
            self.vector_clock.increment_value(1)

        self.add(path)
        self.add(vectors)
        self.add(circles)
        self.add(drawn_path)

        self.vectors = vectors
        self.circles = circles
        self.path = path
        self.drawn_path = drawn_path

    def run_one_cycle(self):
        time = 1 / self.slow_factor
        self.wait(time)

    def set_decreasing_stroke_widths(self, circles):
        mcsw = self.max_circle_stroke_width
        for k, circle in zip(it.count(1), circles):
            circle.set_stroke(width=max(
                # mcsw / np.sqrt(k),
                mcsw / k,
                mcsw,
            ))
        return circles

    def get_path(self):
        tex_mob = Tex(self.tex)
        tex_mob.set_height(6)
        path = tex_mob.family_members_with_points()[0]
        path.set_fill(opacity=0)
        path.set_stroke(WHITE, 1)
        return path
if __name__=='__main__':
    x = abc()
    x.construct()

