#!/usr/bin/env python

import spytank
from gtts import gTTS
import os

spytank.init()

texte1= "Utiliser les touches ZQSD pour le manipuler"
texte2 = "Taper X pour arreter le robot"

tts = gTTS("texte1",lang="fr")
tts.save("text1.mp3")
tts = gTTS(texte2,lang="fr")
tts.save("text2.mp3")

os.system("mpg321 text1.mp3")
os.system("mpg321 text2.mp3")

os.system("rm text1.mp3 text2.mp3")

print(texte1)
print(texte2)


while True:
    lettre = input(">> ")
    if lettre == "z":
        spytank.avance(100)
    elif lettre == "s":
        spytank.recule(100)
    elif lettre == "q":
        spytank.gauche(100)
    elif lettre == "d":
        spytank.droite(100)
    elif lettre == "x":
        spytank.stop()