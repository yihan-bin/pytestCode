from manim import *
class abc(Scene):
    def Mover_rotate(mob, dt):
        pass

    def construct(self):
        stator= '1.png'
        Mover= '2.png'
        coil= '3.png'
        self.doctor=Text('directed by z').shift([-4,3,0])
        self.stator=ImageMobject(stator).shift([0,0,0])
        self.stator.set_height(5.0)
        self.Mover = ImageMobject(Mover).shift([0,0,0])
        self.Mover.set_height(5.0)
        self.coil1 = ImageMobject(coil).set_height(5.0).shift([0,0,0])
        self.coil2 = ImageMobject(coil).set_height(5.0).rotate(PI).shift([0,0,0])

        #self.coil = VGroup(self.coil1,self.coil2)
        # #stator.shift()
        # #Mover.next_to(stator,LEFT)
        # #coil.next_to(stator,RIGHT)
        self.play(Write(self.doctor),colour=BLUE_A)
        self.play(FadeIn(self.stator),run_time=1)
        self.play(FadeIn(self.Mover), run_time=1)
        self.play(FadeIn(self.coil1), run_time=1)
        self.play(FadeIn(self.coil2), run_time=1)
        #self.coil=VGroup(self.coil1,self.coil2)
        for i in range(12):
            self.play(
                    ApplyMethod(self.coil1.rotate, {"angle":PI  / 3,
                        "about_point":ORIGIN}),
                    ApplyMethod(self.coil2.rotate, {"angle": PI / 3,
                         "about_point": ORIGIN})
                      )
            #self.play()
            self.wait(1)
            self.play(ApplyMethod(self.Mover.rotate, {"angle":-PI / 6,
                "about_point":ORIGIN}))
            self.wait(1)


if __name__=='__main__':
    x = abc()
    x.construct()
