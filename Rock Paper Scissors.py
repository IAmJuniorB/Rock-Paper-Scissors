from random import randint
import pygame
import sys
from random import choice

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Rock, Paper, Scissors")

rock_img = pygame.image.load("rock.png").convert()
paper_img = pygame.image.load("paper.png").convert()
scissors_img = pygame.image.load("scissors.png").convert()

rock_pos = (150, 300)
paper_pos = (300, 300)
scissors_pos = (450, 300)

font = pygame.font.Font(None, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Check if the player clicked on one of the buttons
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            # Check if the mouse position is within the rock button
            if rock_pos[0] <= pos[0] <= rock_pos[0] + rock_img.get_width() and rock_pos[1] <= pos[1] <= rock_pos[1] + rock_img.get_height():
                computer_choice = choice(["rock", "paper", "scissors"])
                if computer_choice == "rock":
                    result = "Tie"

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

scissors ="""
_   _
\   /
 \ /
  /
 / \
/   \

"""

paper = """

    _____
   |     |
   |     |
   |     |
   |_____|

"""

rock = """

     _____ 
   .*     *.
  /  `   '  \
 |  p      / |
  \     *   /
   *._____.*
  
"""

while player == False:
    player = input("Rock, Paper, Scissors?\n").lower()
    if player == computer:
        print("Tie!")
    elif player == "rock" or player == "r":
        if computer == "paper":
            print("You lose!", computer, "covers rock")
        else:
            print("You win! Rock smashes", computer, "\n" f"{rock}")
    elif player == "paper" or player == "p":
        if computer == "scissors":
            print("You lose!", computer, "cut paper")
        else:
            print("You win! Paper covers", computer, "\n" f"{paper}")
    elif player == "scissors" or player == "s":
        if computer == "rock":
            print("You lose...", computer, "smashes scissors")
        else:
            print("You win! Scissors cut", computer, "\n" f"{scissors}")
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[randint(0,2)]



