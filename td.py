import pyxel, random
from pyxel.pyxel_wrapper import circb


class Jeu():
    TITLE = "The Last Space"
    WIDTH = 128
    HEIGHT = 128
    def __init__(self):
        pyxel.init(self.WIDTH, self.HEIGHT, title=self.TITLE)
        self.vaisseaux=60
        self.vaisseauy = 60
        self.tirs_li = []
        self.ennemi_li = []
        self.score=0
        self.vies = 3
        self.explosionli = []
        pyxel.run(self.draw, self.update)
    def tirs_creation(self):
        if pyxel.btnr(pyxel.KEY_SPACE):
            self.tirs_li.append([self.vaisseaux+3, self.vaisseauy-4])
    def tirs_deplacement(self):
        for tir in self.tirs_li:
            tir[1]-=1
            if tir[1]<-5:
                self.tirs_li.remove(tir)
    def vaisseaudeplacement(self):
        if pyxel.btn(pyxel.KEY_ESCAPE):
            pyxel.quit
        #if pyxel.btn(pyxel.KEY_SPACE):
            #self.vaisseaux, self.vaisseauy = 60, 60
        if pyxel.btn(pyxel.KEY_UP) and self.vaisseauy>0:
            self.vaisseauy-=1
        if pyxel.btn(pyxel.KEY_DOWN) and self.vaisseauy<120:
            self.vaisseauy+=1
        if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseaux>0:
            self.vaisseaux-=1
        if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseaux<120:
            self.vaisseaux+=1
    def vaisseausuppression(self):
        for ennemi in self.ennemi_li:
            if (self.vaisseaux <= ennemi[0] and self.vaisseaux+8>=ennemi[0] and self.vaisseauy+8 >= ennemi[1] and self.vaisseauy <= ennemi[1]) or (ennemi[0]+8>= self.vaisseaux and ennemi[0]<= self.vaisseaux and ennemi[1]+8 >= self.vaisseauy and ennemi[1]<=self.vaisseauy):
                self.vies-=1
                self.ennemi_li.remove(ennemi)
                self.explosioncreation(self.vaisseaux,self.vaisseauy)
    def ennemicreation(self):
        if pyxel.frame_count%30 == 0:
            co = [random.randint(0,120), 0]
            if co not in self.ennemi_li:
                self.ennemi_li.append([random.randint(0,120), 0])
    def ennemideplacement(self):
        for ennemi in self.ennemi_li:
            ennemi[1]+=1
            if ennemi[1]>128:
                self.ennemi_li.remove(ennemi)
    def ennemissuppressions(self):
        for ennemi in self.ennemi_li:
            for tir in self.tirs_li:
                if ennemi[1]+8 >= tir[1] and ennemi[1] <= tir[1] and ennemi[0]+8>=tir[0]+2 and ennemi[0]<=tir[0]+2:
                    self.score+=1
                    self.tirs_li.remove(tir)
                    self.ennemi_li.remove(ennemi)
                    self.explosioncreation(ennemi[0], ennemi[1])
    def explosioncreation(self,x,y):
        self.explosionli.append([x,y,0])
    def explosionannimation(self):
        for explosion in self.explosionli:
            explosion[2]+=1
            if explosion[2]==12:
                self.explosionli.remove(explosion)
    def update(self):
        self.vaisseaudeplacement()
        self.tirs_creation()
        self.tirs_deplacement()
        self.ennemicreation()
        self.ennemideplacement()
        self.vaisseausuppression()
        self.ennemissuppressions()
        self.explosionannimation()

    def draw(self):
        pyxel.cls(0)
        if self.vies>0:
            pyxel.rect(self.vaisseaux, self.vaisseauy, 8, 8, 5)
            for tir in self.tirs_li:
                pyxel.rect(tir[0], tir[1], 1,4,10)
            for ennemi in self.ennemi_li:
                pyxel.rect(ennemi[0], ennemi[1],8,8,3)
            for explosion in self.explosionli:
                circb(explosion[0]+4, explosion[1]+4, explosion[2],8+explosion[2]%3)
            pyxel.text(5,5, f"SCORE : {self.score}",7)
            pyxel.text(90,5, f"VIES : {self.vies}",7)
        else:
            pyxel.text(60,60,"GAME OVER",7)

jeu = Jeu()