#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
from operator import truediv
import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

click = False

global sanitynum 

defaultsanitynum = 3
defaultcthulunum = 0

rollMin = 1
rollMax = 5
tempnum = 0

player1sanitynum = defaultsanitynum
cthulu = defaultcthulunum
player2sanitynum = defaultsanitynum
playerturn = 0
pickchoice = False

def rollDice():
	global rollMin
	global rollMax
	cheese = random.randint(rollMin, rollMax)
	return cheese

def compress():
	global player1sanitynum
	global player2sanitynum
	global cthulu
	global click
	global playerturn
	global pickchoice
	global tempnum
	if playerturn == 0:
		if pickchoice != True:
			tempnum = rollDice()
		if pickchoice == True:
			pickchoice = False
			print("player 1")
		match tempnum:
			case 1:
				player2sanitynum -= 1
				cthulu += 1
			case 2:
				player1sanitynum += 1
				player2sanitynum -= 1
			case 3:
				if cthulu > 0:
					player1sanitynum += 1
					cthulu -= 1
			case 4:
				player1sanitynum -= 1
				player2sanitynum -= 1
				cthulu += 2
			case 5:
				pickchoice = True
		if pickchoice != True:
			playerturn = 1

	elif playerturn == 1:
		if pickchoice != True:
			tempnum = rollDice()
		if pickchoice == True:
			pickchoice = False
		print("player 2")
		match tempnum:
			case 1:
				player1sanitynum -= 1
				cthulu += 1
			case 2:
				player2sanitynum += 1
				player1sanitynum -= 1
			case 3:
				if cthulu > 0:
					player2sanitynum += 1
					cthulu -= 1
			case 4:
				player2sanitynum -= 1
				player1sanitynum -= 1
				cthulu += 2
			case 5:
				pickchoice = True
		if pickchoice != True:
			playerturn = 0

def main_menu():
	global player1sanitynum
	global player2sanitynum
	global cthulu
	global click
	global playerturn
	global pickchoice
	global tempnum
	
	while True:
	
		screen.fill((0,0,0))

		if player1sanitynum <= 0 and player2sanitynum <= 0:
			print("tie!")
		elif player1sanitynum <= 0:
			print("player 1 loses!")
		elif player2sanitynum <= 0:
			print("player 2 loses!")


		# draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
		mx, my = pygame.mouse.get_pos()

		draw_text("PLAYER 1 - SANITY: " + str(player1sanitynum).encode("utf-8").decode("utf-8") + " " + str(playerturn).encode("utf-8").decode("utf-8"), font,(255, 255, 255), screen, 20, 20)
		draw_text("PLAYER 2 - SANITY: " + str(player2sanitynum).encode("utf-8").decode("utf-8") , font,(255, 255, 255), screen, 300, 20)
		draw_text("CTHULU: " + str(cthulu).encode("utf-8").decode("utf-8"), font,(255, 255, 255), screen, 200, 20)

		button_1 = pygame.Rect(100, 100, 50, 50)
		button_2 = pygame.Rect(50, 200, 50, 50)

		button_3 = pygame.Rect(50, 300, 200, 50)

		button_4 = pygame.Rect(120, 200, 50, 50)
		button_5 = pygame.Rect(200, 200, 50, 50)
		
		if pickchoice == True:
			pygame.draw.rect(screen, (255, 0, 0), button_1)
			pygame.draw.rect(screen, (255, 0, 0), button_2)
			pygame.draw.rect(screen, (255, 0, 0), button_4)
			pygame.draw.rect(screen, (255, 0, 0), button_5)
			if button_1.collidepoint((mx, my)):
				if click: 
					tempnum = 1
					compress()
			if button_2.collidepoint((mx,my)):
				if click: 
					tempnum = 2
					compress()
			if button_4.collidepoint((mx,my)):
				if click: 
					tempnum = 3
					compress()
			if button_5.collidepoint((mx,my)):
				if click: 
					tempnum = 4
					compress()

		if button_3.collidepoint((mx, my)):
			if click:
				print("leak")
				if pickchoice != True:
					print("bullshit")
					compress()



		pygame.draw.rect(screen, (255, 0, 0), button_3)
		draw_text("ROLL DICE", font, (255, 255, 255), screen, 100, 320)

		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		mainClock.tick(60)

def game():
	running = True
	while running:
		screen.fill((0,0,0))
		
		draw_text('game', font, (255, 255, 255), screen, 20, 20)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
		
		pygame.display.update()
		mainClock.tick(60)

def options():
	running = True
	while running:
		screen.fill((0,0,0))

		draw_text('options', font, (255, 255, 255), screen, 20, 20)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
		
		pygame.display.update()
		mainClock.tick(60)

main_menu()