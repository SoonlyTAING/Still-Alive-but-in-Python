import sys
from time import sleep
import os
from playsound import playsound
from threading import Thread

def song():
    dir="D:/git/Still Alive Lyrics (py)/song.mp3" #change the directory of the song to whatever is on your pc
    playsound(dir)
    
def lyrics():
    l1="This was a triumph."
    for char in l1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (2.1)
    l1="\nI'm making a note here:"
    for char in l1:
        sleep(0.085)
        print(char, end='', flush=True)
    sleep (0.5)
    l1=" HUGE SUCCESS!"
    for char in l1:
        sleep(0.085)
        print(char, end='', flush=True)
    sleep (1.6)
    l1="\nIt's hard to over"
    for char in l1:
        sleep(0.09)
        print(char, end='', flush=True)
    l1="state my satisfaction"
    for char in l1:
        sleep(0.15)
        print(char, end='', flush=True)
    sleep (2)
    l1="\nAperture Science"
    for char in l1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (2.5)
    l1="\nWe do what we must because we can"
    for char in l1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (2.3)
    l1="\nFor the good of all of us,"
    for char in l1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep(0.5)
    l1=" except the ones who are dead"
    for char in l1:
        sleep(0.06)
        print(char, end='', flush=True)
    sleep(0.9)
    print("\n")
    p1="\nBut there's no sense crying over every mistake"
    for char in p1:
        sleep(0.07)
        print(char, end='', flush=True)
    sleep(0.4)
    p1="\nYou just keep on trying until you run out of cake"
    for char in p1:
        sleep(0.07)
        print(char, end='', flush=True)
    sleep(0.4)
    p1="\nAnd the science gets done"
    for char in p1:
        sleep(0.07)
        print(char, end='', flush=True)
    p1="\nAnd you make a neat gun"
    for char in p1:
        sleep(0.07)
        print(char, end='', flush=True)
    p1="\nFor the people who are"
    for char in p1:
        sleep(0.09)
        print(char, end='', flush=True)
    p1="\nStill alive"
    for char in p1:
        sleep(0.09)
        print(char, end='', flush=True)
    print("\n")
    print("\n[🎵Instrumental🎵]")
    print("\n")
    sleep(6.6)
    l2="I'm not even angry"
    for char in l2:
        sleep(0.08)
        print(char, end='', flush=True)
    sleep (2.6)
    l2="\nI'm being so sincere right now"
    for char in l2:
        sleep(0.085)
        print(char, end='', flush=True)
    sleep (0.5)
    sleep (1.6)
    l2="\nEven though you broke my heart"
    for char in l2:
        sleep(0.1)
        print(char, end='', flush=True)
    l2=" and killed me"
    for char in l2:
        sleep(0.125)
        print(char, end='', flush=True)
    sleep (1.8)
    l2="\nAnd tore me to pieces"
    for char in l2:
        sleep(0.08)
        print(char, end='', flush=True)
    sleep (2.5)
    l2="\nAnd threw every pieces into a fire"
    for char in l2:
        sleep(0.08)
        print(char, end='', flush=True)
    sleep (2.3)
    l2="\nAs they burned it hurt because"
    for char in l2:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep(0.5)
    l2="\nI was so happy for you"
    for char in l2:
        sleep(0.065)
        print(char, end='', flush=True)
    sleep(0.9)
    print("\n")
    p1="\nNow, these points of data make a beautiful line"
    for char in p1:
        sleep(0.075)
        print(char, end='', flush=True)
    sleep(0.45)
    p1="\nAnd we're out of beta, we're releasing on time"
    for char in p1:
        sleep(0.075)
        print(char, end='', flush=True)
    sleep(0.45)
    p1="\nSo I'm GLaD I got burned"
    for char in p1:
        sleep(0.065)
        print(char, end='', flush=True)
    p1="\nThink of all the things we learned-"
    for char in p1:
        sleep(0.065)
        print(char, end='', flush=True)
    p1="\nFor the people who are"
    for char in p1:
        sleep(0.07)
        print(char, end='', flush=True)
    p1="\nStill alive"
    for char in p1:
        sleep(0.09)
        print(char, end='', flush=True)
    print("\n")
    print("\n[🎵Instrumental🎵]")
    print("\n")
    sleep(6.6)
    l1="Go ahead and leave me"
    for char in l1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (2.1)
    l1="\nI think I'd prefer to stay inside"
    for char in l1:
        sleep(0.085)
        print(char, end='', flush=True)
    sleep (0.5)
    sleep (1.6)
    l1="\nMaybe you'll find someone else"
    for char in l1:
        sleep(0.09)
        print(char, end='', flush=True)
    l1="\nTo help you?"
    for char in l1:
        sleep(0.15)
        print(char, end='', flush=True)
    sleep (2)
    l1="\nMaybe Black Mesa?"
    for char in l1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (2.5)
    l1="\nThat was a joke - haha, fat chance!"
    for char in l1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (2.3)
    l1="\nAnyway this cake is great"
    for char in l1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep(0.5)
    l1="\nIt's so delicious and moist"
    for char in l1:
        sleep(0.06)
        print(char, end='', flush=True)
    sleep(0.7)
    print("\n")
    p1="\nLook at me: still talking when there's science to do"
    for char in p1:
        sleep(0.065)
        print(char, end='', flush=True)
    sleep(0.3)
    p1="\nWhen I look out there, it makes me GLaD I'm not you"
    for char in p1:
        sleep(0.065)
        print(char, end='', flush=True)
    sleep(0.3)
    p1="\nI've experiments to run"
    for char in p1:
        sleep(0.075)
        print(char, end='', flush=True)
    p1="\nThere is research to be done"
    for char in p1:
        sleep(0.07)
        print(char, end='', flush=True)
    p1="\nOn the people who are"
    for char in p1:
        sleep(0.075)
        print(char, end='', flush=True)
    p1="\nStill alive"

    for char in p1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (1)
    print("\n")

    o1="\nAnd believe me I am"
    for char in o1:
        sleep(0.075)
        print(char, end='', flush=True)
    o1="\nStill alive"
    for char in o1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (1.1)
    o1="\nI'm doing science and I'm"
    for char in o1:
        sleep(0.075)
        print(char, end='', flush=True)
    o1="\nStill alive"
    for char in o1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (1.1)
    o1="\nI feel fantastic and I'm"
    for char in o1:
        sleep(0.075)
        print(char, end='', flush=True)
    o1="\nStill alive"
    for char in o1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (1.0)
    o1="\nWhile you're dying I'll be"
    for char in o1:
        sleep(0.075)
        print(char, end='', flush=True)
    o1="\nStill alive"
    for char in o1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (1.0)
    o1="\nAnd when you're dead I will be"
    for char in o1:
        sleep(0.075)
        print(char, end='', flush=True)
    o1="\nStill alive"
    for char in o1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (0.9)
    print("\n")
    o1="\nStill alive"
    for char in o1:
        sleep(0.09)
        print(char, end='', flush=True)
    sleep (0.9)
    print("\n")
    o1="\nStill alive"
    for char in o1:
        sleep(0.09)
        print(char, end='', flush=True)
print ("Hello World")
x=input("Start")
os.system("cls")



Thread(target = song).start()
Thread(target = lyrics).start()