#!/usr/bin/python

from gpiozero import LED, Button
from time import sleep
from random import randint

button = Button(14)
led = LED(4)

def change():
  print("pressed")


while True:
  cycle = randint(2,4)
  sleepTime = randint(1,6)*0.5
  for x in range(0,cycle):
      led.on()
      sleep(sleepTime)
      led.off()
      sleep(sleepTime)
      button.when_pressed = change


