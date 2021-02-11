# -*- encoding: UTF-8 -*-

import time         
from naoqi import ALProxy 

def main(robotIP, PORT=9559):
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    motionProxy.wakeUp()  
    postureProxy.goToPosture("StandInit", 0.5) 

    x = 1.0 
    y  = 0.0
    theta = 0.0
    frequency = 1.0
    motionProxy.moveToward(x, y, theta, [["Frequency", frequency]])

    time.sleep(3)
    x = 0.5
    frequency = 0.5
    motionProxy.moveToward(x, y, theta, [["Frequency", frequency]])

    time.sleep(3)
    frequency = 0.3
    motionProxy.moveToward(x, y, theta, [["Frequency", frequency]])

    time.sleep(3)
    motionProxy.stopMove()
    motionProxy.rest()

if __name__ == "__main__":
    robotIP = "192.168.0.106"
    main(robotIP)
