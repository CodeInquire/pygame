import pygame
from gamePkg.config import *
from gamePkg.keypress import *
from gamePkg.tilemap import TILEMAP
from gamePkg.entities import PLAYER, NPC, MECH
from gamePkg.colors import COLOR
from gamePkg.text_renderer import text_to_screen
from gamePkg.camera import CAM
from sys import exit
from math import sqrt
from random import randint

class Game:
	def __init__(self):
		pygame.init()
		self.cam = CAM
		self.fps = FPS
		self.tile_rects, self.background_rects = self.create_tile_rects()
		self.screen = SCREEN
		self.clock = pygame.time.Clock()
		self.delta_time = self.clock.tick(self.fps) / 1000 # Delta time in seconds
		self.text_display = text_to_screen(self.screen)
		self.dialogue_state = None
		self.gravity = GRAVITY	
		self.player = PLAYER
		self.player.image.fill(COLOR['blue'])
		self.npc = NPC
		self.npc.image.fill(COLOR['plum'])
		self.mech = MECH
		self.mech.image.fill(COLOR['ivory'])
		self.running = True

	def create_tile_rects(self):
		
		tile_rects = []
		background_rects = []

		for y, row in enumerate(TILEMAP):
			for x, tile in enumerate(row):
				if tile == 0:
					pass
				if tile == 1:
					tile_rects.append(pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE))
				if tile == 3:
					background_rects.append(pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)) 

		return tile_rects, background_rects

	def draw_tilemap(self, display_surface, color, tile_rects):
		for rect in tile_rects:
			pygame.draw.rect(display_surface, color, rect)

	def check_key_press(self):
		key_pressed = pygame.key.get_pressed()
		if key_pressed[pygame.K_LEFT]:
			self.player.move["left"] = True
			
		if key_pressed[pygame.K_RIGHT]:
			self.player.move["right"] = True

	def handle_events(self):

		fps = self.clock.get_fps()
		print(f"FPS: {fps}")

		self.handle_dialogue() # Handling the dialogue system for now?? (sorta nothing here yet)

		check_key_pressed(self)
		
		'''for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = not self.running
			
			if event.type == pygame.KEYDOWN:
				
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					self.player.move["up"] = True
				
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					self.player.move["down"] = True
				
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					self.player.move["left"] = True
				
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					self.player.move["right"] = True

				if event.key == pygame.K_SPACE:
					self.player.scan_body()

				if event.key == pygame.K_h:
					self.player.body['head'] -= 5
					print(self.player.body['head'])

			if event.type == pygame.KEYUP:
				
				if event.key == pygame.K_ESCAPE:
					self.running = not self.running
				
				if event.key == pygame.K_UP or event.key == pygame.K_w:
					self.player.move["up"] = False
				
				if event.key == pygame.K_DOWN or event.key == pygame.K_s:
					self.player.move["down"] = False
				
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					self.player.move["left"] = False
				
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					self.player.move["right"] = False
				
				if event.key == pygame.K_SPACE:
					pass'''

 
	def handle_dialogue(self):
		match self.dialogue_state==True:
			case 'NPC1':
				self.text_display.render("hello",(100, 100), COLOR['white'])
			case _:
				self.dialogue_state = None

	def draw(self):
			self.screen.fill(COLOR['black'])
			self.draw_tilemap(self.screen, COLOR['forest green'], self.tile_rects)
			self.draw_tilemap(self.screen, COLOR['chocolate'], self.background_rects)
			#self.cam.focus_on(self.screen, self.player)

	def update(self):
		self.mech.update(self.delta_time, self.tile_rects, self.gravity)
		self.npc.update(self.delta_time, self.tile_rects, self.gravity)
		self.player.update(self.delta_time, self.tile_rects, self.gravity)

		pygame.display.update()

	def run(self):
		while self.running:
			self.delta_time = self.clock.tick(self.fps) / 1000
			self.handle_events()
			self.update()
			self.draw()

	def quit(self):
		pygame.quit()
		exit()

if __name__ == "__main__":		
		game = Game() # instantiates Game class as variable "game"
		game.run()    # runs all methods to progress game flow
		game.quit()   # quits pygame and exits program completely
else:
	print("NOT THE MAIN FILE")
