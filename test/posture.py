# -*- encoding: UTF-8 -*-

import sys                   
from naoqi import ALProxy     

def main(robotIP):
    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    postureProxy.goToPosture("StandInit", 1.0)
    postureProxy.goToPosture("Crouch", 1.0)
    postureProxy.goToPosture("StandInit", 1.0)
    postureProxy.goToPosture("Crouch", 1.0)
    postureProxy.goToPosture("StandInit", 1.0)
    postureProxy.goToPosture("StandInit", 1.0)


    print postureProxy.getPostureFamily()

if __name__ == "__main__":
    robotIp = "192.168.0.106"

    if len(sys.argv) <= 1:
        print "Usage python ALRobotPosture, robotIP (optional default: 127.0.0.1), port"
    else:
        robotIp = sys.argv[1]

    main(robotIp)
