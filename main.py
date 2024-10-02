from math import sin, cos
from matplotlib import pyplot as plt
import random

## Represent a cannonball, tracking its position and velocity.
#
class Cannonball:
    ## Create a new cannonball at the provided x position.
    #  @param x the x position of the ball
    #

    class  Print_Iface:
        def print(self, x, y):
            print("The ball is at (%.1f, %.1f)" % (x, y))
            plt.scatter(x, y)
            plt.pause(.01)

    def __init__(self, x):
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0
        self.Print_Iface = self.Print_Iface()
    #testing 123
    ## Move the cannon ball, using its current velocities.
    #  @param sec the amount of time that has elapsed.
    #
    
    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec

        self._vy = self._vy - grav * sec

        self._x = self._x + dx
        self._y = self._y + dy

    ## Get the current x position of the ball.
    #  @return the x position of the ball
    #
    def getX(self):
        return self._x

    ## Get the current y position of the ball.
    #  @return the y position of the ball
    #
    def getY(self):
        return self._y

    ## Shoot the canon ball.
    #  @param angle the angle of the cannon
    #  @param velocity the initial velocity of the ball
    #
    def shoot(self, angle, velocity, user_grav):
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)

        while self.getY() > 1e-14:
            self.Print_Iface.print(self.getX(), self.getY())
            self.move(0.1, user_grav)

class Crazyball(Cannonball):
    def move(self):
        self.rand_q = random.randrange(0,10)
        if self.getX() < 400:
            self._x = self._x + self.rand_q
        if self.getX() >= 400:
            self._x = self._x - self.rand_q

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ##
    #  Demonstrate the cannonball class.
    #
    #from cannonball import Cannonball

    angle = float(input("Enter starting angle: "))
    v = float(input("Enter initial velocity: "))
    c = Cannonball(0)
    c.shoot(angle, v, 9.81)

class Crazyball(Cannonball):
    def move(self):
        self.rand_q = random.randrange(0,10)
        if self.getX() < 400:
            self._x = self._x + self.rand_q
        if self.getY() >= 400:
            self._y = self._y - self.rand_q

def main():
    testCannnonball = Cannonball
    testCrazyball = Crazyball
    angle = input("Input angle: ")
    velocity = input("Input velocity: ")
    gravity = input("Enter 1-4 to select from the following: \n 1.Earth Gravity \n 2.Moon Gravity \n 3.Crazy trajectory \n 4.Quit \n")
    match gravity: 
        case "1":
            testCannnonball.shoot(angle, velocity, 9.81)
        case "2":
            testCannnonball.shoot(angle, velocity, 1.62)
        case "3":
            testCrazyball.shoot(angle, velocity, gravity)
        case "4":
            exit()
        case _:
            print("Invalid input. Please try again.")
            main()
