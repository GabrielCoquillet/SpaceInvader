import pyxel, random
from pyxel.pyxel_wrapper import KEY_ESCAPE


class Ennemi:
    def __init__(self):
        self.ennemi_li = []


class Ship:
    def __init__(self):
        self.x, self.y = 50, 50

    def move(self):
        if pyxel.btn(KEY_ESCAPE):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_Z) and self.y>0:
            self.y-=2
        elif pyxel.btn(pyxel.KEY_S) and self.y<App.HEIGHT:
            self.y+=2
        elif pyxel.btn(pyxel.KEY_Q) and self.x>0:
            self.x-=2
        elif pyxel.btn(pyxel.KEY_D) and self.x<App.WIDTH:
            self.x+=2

    def getx(self):
        return self.x

    def gety(self):
        return self.y

class Shot:
    def __init__(self):
        self.shot_li = []

    def add_shot(self, x, y):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.shot_li.append([x, y])

    def shot_move(self):
        for shot in self.shot_li:
            shot[1]-=2

    def get_shot(self):
        return self.shot_li

class App:
    TITLE = "Space Invaders"
    WIDTH = 300
    HEIGHT = 400
    def __init__(self):
        pyxel.init(self.WIDTH, self.HEIGHT, title=self.TITLE)
        pyxel.load("res.pyxres")
        self.ship = Ship()
        self.shots = Shot()
        pyxel.run(self.update,self.draw)

    def update(self):
        self.ship.move()
        self.shots.add_shot(self.ship.getx(), self.ship.gety())
        self.shots.shot_move()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.ship.getx(), self.ship.gety(),0,0,0, 8, 8, 0)
        for shot in self.shots.get_shot():
            pyxel.rect(shot[0], shot[1], 5, 5, 7)

app = App()