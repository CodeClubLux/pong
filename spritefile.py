#!#/usr/bin/env python
import pygame
from pygame import *
from random import randint
class ball(pygame.sprite.Sprite):
	def __init__(self, w, h):
		super().__init__()
		self.width=21
		self.height=21
		self.x=randint(0, w-self.width)
		self.y=randint(0, h-self.height)
		self.vx=1
		self.vy=1
		self.x_max = w-self.width
		self.y_max = h-self.height
		color = white
		self.image = pygame.Surface([self.width, self.height])
		#self.image = pygame.draw.circle(Surface, (255, 255, 255), (400, 300), 15, 0)
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.move_right = True
		self.move_down = True
		self.rect.x = self.x
		self.rect.y = self.y

	def update(self):
		self.y += self.vy
		self.x += self.vx
		if self.x>=self.x_max:
			self.vx=-self.vx
		if self.y>=self.y_max: 
			self.vy=-self.vy
		if self.x<=0:
			self.vx=-self.vx
		if self.y<=0:
			self.vy=-self.vy
		#print (self.x,self.y,self.vx,self.vy) 
		self.rect.x = self.x
		self.rect.y = self.y
		self.vx *=0.9999
		self.vy *=0.9999

	def bounce(self, rvx, rvy):
		self.vx = - self.vx - rvx/100
		self.vy = self.vy - rvy/100 
		if abs(self.vx) > 4 :
			self.vx = 4
		if abs(self.vy) > 4	:
			self.vy = 4
		print('%.2f\t%.2f'%(self.vx, self.vy))
		
class racket(pygame.sprite.Sprite):
	def __init__(self, x, y, color):
		super().__init__()
		pygame.mouse.set_visible(0)
		self.x=x
		self.y=y
		self.width=20
		self.height=220
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.mouse_xy = pygame.mouse.get_pos()
		self.rect.x = self.mouse_xy[0]
		self.rect.y = self.mouse_xy[1]
		
	def update(self):
		self.mouse_xy = pygame.mouse.get_pos() 
		self.vx = -self.x + self.mouse_xy[0]
		self.vy = -self.y + self.mouse_xy[1]
		self.x += self.vx/100
		self.y += self.vy/100
		#if self.x>=self.x_max:
		#	self.vx=-self.vx
		#if self.y>=self.y_max: 
		#	self.vy=-self.vy
		#if self.x<=0:
		#	self.vx=-self.vx
		#if self.y<=0:
		#	self.vy=-self.vy
		#print (self.x,self.y,self.vx,self.vy)
		self.rect.x = self.x
		self.rect.y = self.y
		#if self.vx != 0 or self.vy != 0:
		#print(self.vx, self.vy)
		
class target(pygame.sprite.Sprite):
	def __init__(self, x, y, color=(255,0,0)):
		super().__init__()
		#self.x=x
		#self.y=y
		self.width=30
		self.height=30
		self.x=randint(0, x-self.width)
		self.y=randint(0, y-self.height)
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
		self.hit = False
		#print(self.x)
		#print(self.y)
		
	def update(self):
		if self.hit is True:
			self.x = randint(0, 800-self.width)
			self.y = randint(0, 600-self.height)
			self.image = pygame.Surface([self.width, self.height])
			self.image.fill((randint(0, 255),randint(0, 255),randint(0, 255)))
			self.rect = self.image.get_rect()
			self.rect.x = self.x
			self.rect.y = self.y
			self.hit = False
		#if all_sprites.remove(target) = True:
		#def create(self, x, y, color= (255, 0, 0)

if __name__=="__main__":
	import pygame

	pygame.init()
	white = (255,255,255)
	black = (0,0,0)
	window = pygame.display.set_mode((800,600))
	clock = pygame.time.Clock()
	ball = ball(800,600)
	racket = racket(400,300,(50,150,255))
	target = target(400,300)
	bounced = 0
	score = 0
	time = 0
	all_sprites = pygame.sprite.Group()
	all_sprites.add(ball)
	all_sprites.add(racket)
	all_sprites.add(target)
	background = pygame.Surface(window.get_size())
	window.fill(black)
	while True:
		time += 1
		for i in pygame.event.get():
			if i.type == QUIT:
				exit()
		
		all_sprites.update()
		#if bounced > 0:
		#	bounced -= 1
		if pygame.sprite.collide_rect(ball, racket): 
		#pygame.sprite.spritecollide(ball, all_sprites, False) and (bounced <= 0):
			#spritecollide(sprite, group, dokill, collided = None)
			ball.bounce(racket.vx, racket.vy)
			#bounced = 5
			#print('%.2f\t%.2f\t%d\t%d' % (ball.x, ball.y, racket.x, racket.y))
		if pygame.sprite.collide_rect(ball, target):  
		#pygame.sprite.spritecollide(target, all_sprites, False):
		    #all_sprites.remove(target)
		    target.hit = True
		    #print("I have been hit!")
		    score += 1
		    print(score)

			
		    

		if time == 10:
			window.fill(black)
			all_sprites.draw(window)
			time = 0
		clock.tick(300)
		pygame.display.flip()
