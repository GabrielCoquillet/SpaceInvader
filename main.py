import pyxel, random
from pyxel.pyxel_wrapper import KEY_ESCAPE


class Ennemi:
    def __init__(self):
        self.ennemi_li = []

    def ennemi_spawn(self):
        if pyxel.frame_count % 30 == 0:
            self.ennemi_li.append([random.randint(0,App.WIDTH-8),0])

    def ennemi_move(self):
        for ennemi in self.ennemi_li:
            ennemi[1]+=1

    def get_ennemi(self):
        return self.ennemi_li

    def delete_ennemi(self, ennemi):
        self.ennemi_li.remove(ennemi)

class Ship:
    def __init__(self):
        self.x, self.y = 50, 50

    def move(self):
        if pyxel.btn(KEY_ESCAPE):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_Z) and self.y>1:
            self.y-=2
        elif pyxel.btn(pyxel.KEY_S) and self.y<App.HEIGHT-7:
            self.y+=2
        elif pyxel.btn(pyxel.KEY_Q) and self.x>1:
            self.x-=2
        elif pyxel.btn(pyxel.KEY_D) and self.x<App.WIDTH-7:
            self.x+=2

    def getx(self):
        return self.x

    def gety(self):
        return self.y

class Shot:
    def __init__(self):
        self.shot_li = []

    def add_shot(self, x, y):
        if pyxel.btnp(pyxel.KEY_SPACE) and not [x,y] in self.shot_li:
            self.shot_li.append([x, y])

    def shot_move(self):
        for shot in self.shot_li:
            shot[1]-=2

    def get_shot(self):
        return self.shot_li

    def delete_shot(self, shot):
        self.shot_li.remove(shot)

class App:
    TITLE = "Space Invaders"
    WIDTH = 150
    HEIGHT = 200

    def __init__(self):
        pyxel.init(self.WIDTH, self.HEIGHT, title=self.TITLE)
        pyxel.load("res.pyxres")
        self.score = 0
        self.ship = Ship()
        self.shots = Shot()
        self.ennemi1 = Ennemi()
        pyxel.run(self.update,self.draw)

    def score_modify(self):
        for tir in self.shots.get_shot():
            for ennemi in self.ennemi1.get_ennemi():
                pass

    def update(self):
        self.ship.move()
        self.shots.add_shot(self.ship.getx(), self.ship.gety())
        self.shots.shot_move()
        self.ennemi1.ennemi_move()
        self.ennemi1.ennemi_spawn()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.ship.getx(), self.ship.gety(),0,0,0, 8, 8, 0)
        for shot in self.shots.get_shot():
            pyxel.blt(shot[0], shot[1]-3, 0, 0, 8,8,8,0)
        for ennemi in self.ennemi1.get_ennemi():
            pyxel.blt(ennemi[0], ennemi[1], 0, 8, 0,8,8,0)
        pyxel.text(5,5,f"SCORE : {self.score}", 7, None)
app = App()