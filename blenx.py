import autopy as ap
from autopy.mouse import LEFT_BUTTON, RIGHT_BUTTON
from autopy.key import *
from autopy import *
import time
import random

name = 'Will'

def hpget():
    ap.mouse.move(900, 600)
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(.1)
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(.1)
    ap.mouse.smooth_move(1000, 600)
    time.sleep(.1)
    ap.mouse.smooth_move(800, 600)
    time.sleep(.1)
    ap.mouse.smooth_move(900, 600)
    ap.mouse.toggle(False, LEFT_BUTTON)
    time.sleep(.1)
    
def artct():
    ap.mouse.move(550, 300)
    time.sleep(.1)
    
    
    
def movtop():
    ap.mouse.move(200, 300)
    print "mouse moved"
    time.sleep(1)
    ap.mouse.click(LEFT_BUTTON)
    print "mouse clicked - left"
    time.sleep(1)
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(1)
    ap.mouse.toggle(False, LEFT_BUTTON)
    time.sleep(.1)
    
def satk():
    ap.mouse.RIGHT_BUTTON
    time.sleep(.2)
    ap.mouse.toggle(True, RIGHT_BUTTON)
    time.sleep(.2)
    ap.mouse.toggle(False, LEFT_BUTTON)
    time.sleep(.2)
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(.2)
    ap.mouse.toggle(False, LEFT_BUTTON)
    
    
    
def cliklef():
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(1)
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(1)
    ap.mouse.toggle(False, LEFT_BUTTON)
    time.sleep(1)
##Clicks the left button


def topc():
    ap.mouse.smooth_move(400, 250)
    print "mouse top"
    time.sleep(5)

def topr():
    ap.mouse.smooth_move(450,250)
    print "mouse top right"
    time.sleep(5)
    
    
def sidr():
    ap.mouse.smooth_move(450,300)
    print "mouse right side"
    time.sleep(5)
    
    
def botr():
    ap.mouse.smooth_move(450, 350)
    print "mouse side right"
    time.sleep(5)
    
    
def botc():
    ap.mouse.smooth_move(400, 350)
    print "mouse bottom center"
    time.sleep(5)
    
def botl():
    ap.mouse.smooth_move(350, 350)
    print "mouse bottom left"
    time.sleep(5
               )
def sidl():
    ap.mouse.smooth_move(350, 300)
    print "mouse side left"

def topl():
    ap.mouse.smooth_move(350, 250)
    print "mouse top left"
    time.sleep(5)


def pokemon():
    ap.mouse.move(1200,50)
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(1)
    ap.mouse.move(1200,800)
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(1)

def drag():
    ap.mouse.move(1200,30)
    ap.mouse.toggle(True, LEFT_BUTTON)
    ap.mouse.smooth_move(1200, 500)
    time.sleep(.1)
    ap.mouse.smooth_move(200, 500)
    time.sleep(.1)
    ap.mouse.smooth_move(200, 1000)
    time.sleep(.1)
    ap.mouse.smooth_move(1200, 1000)
    time.sleep(.1)
    ap.mouse.smooth_move(1200, 500)
    time.sleep(.1)
    ap.mouse.smooth_move(1200, 30)
    time.sleep(.1)
    ap.mouse.smooth_move(200, 500)
    time.sleep(.1)
    ap.mouse.smooth_move(1200,50)
    ap.mouse.toggle(False, LEFT_BUTTON)

def torch():
    ap.mouse.smooth_move(400,200)
    print "mid pos"
    time.sleep(.1)
    ap.mouse.smooth_move(500,480)
    print "moving to first item"
    ap.mouse.toggle(True, LEFT_BUTTON)
    print "left pressed"
    time.sleep(.1)
    ap.mouse.smooth_move(20,480)
    print "moving to drop item"
    time.sleep(.1)
    ap.mouse.toggle(False, LEFT_BUTTON)
    print "droping item"
    time.sleep(1)
    
    ap.mouse.smooth_move(540,480)
    print "moving to first item"
    ap.mouse.toggle(True, LEFT_BUTTON)
    print "left pressed"
    time.sleep(.1)
    ap.mouse.smooth_move(60,480)
    print "moving to drop item"
    time.sleep(.1)
    ap.mouse.toggle(False, LEFT_BUTTON)
    print "droping item"
    time.sleep(.1)
    
    ap.mouse.smooth_move(580,480)
    print "moving to first item"
    ap.mouse.toggle(True, LEFT_BUTTON)
    print "left pressed"
    time.sleep(.1)
    ap.mouse.smooth_move(100,480)
    print "moving to drop item"
    time.sleep(.1)
    ap.mouse.toggle(False, LEFT_BUTTON)
    print "droping item"
    time.sleep(.1)
    
    ap.mouse.smooth_move(620, 480)
    print "moving to third item"
    time.sleep(.1)
    ap.mouse.toggle(True, LEFT_BUTTON)
    print "left pressed"
    time.sleep(.1)
    ap.mouse.smooth_move(140,480)
    print "moving to drop item"
    time.sleep(.1)
    ap.mouse.toggle(False, LEFT_BUTTON)
    print "dropping the item"
    time.sleep(.1)
    
    ap.mouse.smooth_move(660, 480)
    print "moving to third item"
    time.sleep(.1)
    ap.mouse.toggle(True, LEFT_BUTTON)
    print "left pressed"
    time.sleep(.1)
    ap.mouse.smooth_move(180,480)
    print "moving to drop item"
    time.sleep(.1)
    ap.mouse.toggle(False, LEFT_BUTTON)
    print "dropping the item"
    time.sleep(.1)
    
    ap.mouse.smooth_move(700, 480)
    print "moving to third item"
    time.sleep(.1)
    ap.mouse.toggle(True, LEFT_BUTTON)
    print "left pressed"
    time.sleep(.1)
    ap.mouse.smooth_move(220,480)
    print "moving to drop item"
    time.sleep(.1)
    ap.mouse.toggle(False, LEFT_BUTTON)
    print "dropping the item"
    time.sleep(.1)
    
    ap.mouse.smooth_move(740,480)
    print "moving to third item"
    time.sleep(.1)
    ap.mouse.toggle(True, LEFT_BUTTON)
    print "left pressed"
    time.sleep(.1)
    ap.mouse.smooth_move(260,480)
    print "moving to drop item"
    time.sleep(.1)
    ap.mouse.toggle(False, LEFT_BUTTON)
    print "dropping the item"
    time.sleep(.1)
    
    ap.mouse.smooth_move(780,480)
    print "moving to third item"
    time.sleep(.1)
    ap.mouse.toggle(True, LEFT_BUTTON)
    print "left pressed"
    time.sleep(.1)
    ap.mouse.smooth_move(300,480)
    print "moving to drop item"
    time.sleep(.1)
    ap.mouse.toggle(False, LEFT_BUTTON)
    print "dropping the item"
    time.sleep(.1)
    
def starg():
    ap.mouse.move(400,590)
    time.sleep(.2)
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(.2)
    ap.mouse.toggle(False, LEFT_BUTTON)
    time.sleep(.2)
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(.2)
    ap.mouse.toggle(False, LEFT_BUTTON)
    
    
    ap.mouse.move(400,300)
    time.sleep(.2)
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(.2)
    ap.mouse.toggle(False, LEFT_BUTTON)
    ap.mouse.toggle(True, LEFT_BUTTON)
    time.sleep(.2)
    ap.mouse.toggle(False, LEFT_BUTTON)
    
def webadres():
    ap.mouse.move(300, 50)
    ap.mouse.toggle(True, LEFT_BUTTON)
    ap.mouse.toggle(False, LEFT_BUTTON)
    time.sleep(.1)
    ap.key.type_string('www.gmail.com',0)
    ap.key.tap(K_RETURN,)
    
def webcap():
    ap.bitmap.capture_screen(rect=None)
    
    
    ap.mouse.move(300,550)
    time.sleep(10)
    print 'sleep is over'
    ap.mouse.click(button=LEFT_BUTTON)

def movclik():
    ap.mouse.move(1500,300)
    ap.mouse.click(LEFT_BUTTON)

def say_hi():
    ap.key.type_string('Hello', 50)

def say_talk():
    ap.key.type_string('omomomo', 50)
def say_bye():
    ap.key.type_string('Goodbye', 50)
    
def typetwo():
    ap.key
    
def rannum():
    num = random.randint(1,5)
    if num == 1:
        print  "The figet"
    elif num == 2:
        print "The William"
    elif num == 3:
        print "The Mummy"
    elif num == 4:
        print "The Flow Mummy"
    elif num == 5:
        print "The Luke"
    return num()
    print num()


def talkran():
    ap.autopy.key('k')
    


##torch()
#drag()
#movclik()
#for x in range(0,10):
#    say_hi()
 #   time.sleep(1)
  #  say_talk()
   # time.sleep(.5)
    #say_bye()
    

    
#movclik()
#for x in range(0, 3):
 #       say_hi()
  #      print rannum()