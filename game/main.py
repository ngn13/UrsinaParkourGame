from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

jblock = load_texture('assets/jblock.png')
last = load_texture('assets/last.png')
checkb = load_texture('assets/checkb.png')
back = load_texture('assets/back.png')
music = Audio('music.mpeg', loop=True, autoplay=True)

window.exit_button.visible = False
window.title = 'Bl4ck'

gameover = False
checkpoint = (0,0,0)

class Voxel(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = jblock,
			scale = (20,1,10),
			color = color.color(0,0,random.uniform(0.9,1)))

class Voxel2(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = jblock,
			scale = (5,1,10),
			color = color.color(0,0,random.uniform(0.9,1)))

class Voxel3(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = jblock,
			scale = (3,1,5),
			color = color.color(0,0,random.uniform(0.9,1)))

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = back,
			scale = 15000,
			double_sided = True)

class CheckB(Button):
	def __init__(self, x,y,z):
		super().__init__(
			parent = scene,
			position = (x,y,z),
			model = 'cube',
			origin_y = 0.5,
			texture = checkb,
			color = color.color(0,0,random.uniform(0.9,1)),
			rotation = Vec3(150,-10,0),
			scale = 0.5)
	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				global checkpoint
				checkpoint = (self.x, self.y, self.z)				
				destroy(self)

class Last(Button):
	def __init__(self, x,y,z):
		super().__init__(
			parent = scene,
			position = (x,y,z),
			model = 'cube',
			origin_y = 0.5,
			texture = last,
			color = color.color(0,0,random.uniform(0.9,1)),
			rotation = Vec3(150,-10,0),
			scale = 0.5)
	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				global gameover
				global checkpoint
				checkpoint = (self.x, self.y, self.z)				
				gameover = True				
				destroy(self)


player = FirstPersonController(height=10,speed=17,jump_height=3,jump_duration=.42,mouse_sensitivity = Vec2(60, 60) 
,cursor = Entity(parent=camera.ui, model='quad', color=color.red, scale=.001, rotation_z=45))

sky = Sky()

voxel = Voxel(position = (0,0,0))

r = random.randint(0,1000)%5

a = 2
b = 12
c = []
z = 0

for i in range(200):
	p = random.randint(1,3)

	if p == 1:
		c.append(CheckB(random.randint(0,7),a+1,b))
	if i == 199:
		last = Last(random.randint(0,7),a+1,b)

	if p == 1:
		i = Voxel(position = (random.randint(0,7),a,b))
		i.rotation_x = random.randint(-15,15)
		i.rotation_y = random.randint(-15,15)

	elif p == 2:
		i = Voxel2(position = (random.randint(0,7),a,b))
		i.rotation_x = random.randint(-15,15)
		i.rotation_y = random.randint(-15,15)
	
	elif p == 3:
		i = Voxel3(position = (random.randint(0,7),a,b))
		i.rotation_x = random.randint(-15,15)
		i.rotation_y = random.randint(-15,15)
	
	a += 2
	b += 12
	z += 1

def update():
	if player.y < -3:
		player.position = checkpoint
	if gameover:
		Text.default_resolution = 1080 * Text.size
		Text.size = .050
		Text(text='You won!', origin=(0,0), background=True)
		application.pause()
	if held_keys['m']:
		music.stop()
	if held_keys['q']:
		exit(0);
		
		

music.play()
app.run()