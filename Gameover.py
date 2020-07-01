import pygame
from pygame_functions import *
import random
from config import *

screenSize(720,400)


name = makeLabel("Please enter 3 letters:",40,10,10,"white","Arial","black")
showLabel(name)

wordBox = makeTextBox(10,80,100,2,"Enter text here",3,40)
showTextBox(wordBox)
entry = textBoxInput(wordBox)