#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
 
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

sanitynum = 18
cthulu = 0

def main_menu():
	global sanitynum
	global cthulu

	while True:
 
		screen.fill((0,0,0))

		# draw_text('main menu', font, (255, 255, 255), screen, 20, 20)
		mx, my = pygame.mouse.get_pos()

		draw_text("SANITY: " + str(sanitynum).encode("utf-8").decode("utf-8") + " CTHULU: " + str(cthulu).encode("utf-8").decode("utf-8")  , font,(255, 255, 255), screen, 20, 20)

		button_1 = pygame.Rect(50, 100, 200, 50)
		button_2 = pygame.Rect(50, 200, 200, 50)
		button_3 = pygame.Rect(50, 300, 200, 50)

		if button_1.collidepoint((mx, my)):
			if click:
				game()
		if button_2.collidepoint((mx, my)):
			if click:
				options()
		if button_3.collidepoint((mx, my)):
			if click:
				sanitynum -= 1
				print(sanitynum)
				cthulu += 1


		pygame.draw.rect(screen, (255, 0, 0), button_1)
		pygame.draw.rect(screen, (255, 0, 0), button_2)
		pygame.draw.rect(screen, (255, 0, 0), button_3)
 
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