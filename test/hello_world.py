# -*- encoding: UTF-8 -*-

import naoqi                 
from naoqi import ALProxy    
from time import sleep

robotIP = "172.17.92.17"    
port = 9559                  

tts = ALProxy("ALTextToSpeech", robotIP, port)  
tts.setLanguage("Spanish")

tts.say("Hola, soy NAO. Peretenezco al programa de ingeniería Electrónica de esta Universidad.")
sleep(0.5)
tts.say("Para mi, es un verdadero placer darles la bienvenida a estas instalaciones, en donde paso la mayor parte de mi tiempo, colaborando en las areas de aprendizaje, e investigación.")
sleep(2)
