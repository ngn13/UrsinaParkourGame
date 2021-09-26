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

bottom = -2

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
			scale = (20,0.5,10),
			rotation_x = random.randint(-15,15),
			rotation_y = random.randint(-15,15),
			color = color.color(0,0,random.uniform(0.9,1)))

class MVoxel(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = jblock,
			scale = (3,0.5,5),
			rotation_y = random.randint(-15,15),
			rotation_x = random.randint(-15,15),
			color = color.color(0,0,random.uniform(0.9,1)))

class Voxel2(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = jblock,
			scale = (5,0.5,10),
			rotation_y = random.randint(-15,15),
			rotation_x = random.randint(-15,15),
			color = color.color(0,0,random.uniform(0.9,1)))

class Voxel3(Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = 0.5,
			texture = jblock,
			scale = (3,0.5,5),
			rotation_y = random.randint(-15,15),
			rotation_x = random.randint(-15,15),
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


player = FirstPersonController(gravity=1,height=15,speed=17,jump_height=3,jump_duration=.42,mouse_sensitivity = Vec2(60, 60) 
,cursor = Entity(parent=camera.ui, model='quad', color=color.red, scale=.001, rotation_z=45))

sky = Sky()

voxel = Voxel(position = (0,0,0))

r = random.randint(0,1000)%5

a = 2
b = 12
c = []
j = []
k = []
z = 0

for i in range(200):
	p = random.randint(1,5)
	p2 = random.randint(1,4)

	if p == 1:
		c.append(CheckB(random.randint(0,7),a+1,b))
	if i == 199:
		last = Last(random.randint(0,7),a+1,b)

	if p == 1:
		j.append(Voxel(position = (random.randint(0,7),a,b)))

	elif p == 2:
		j.append(Voxel2(position = (random.randint(0,7),a,b)))

	elif p == 3:
		j.append(Voxel3(position = (random.randint(0,7),a,b)))

	elif p == 4 and p2 == 4:
		k.append(Voxel3(position = (random.randint(0,7),a,b)))

	else:
		j.append(Voxel2(position = (random.randint(0,7),a,b)))
		

	a += 2
	b += 12
	z += 1

def update():
	for i in c:
		if i:		
			i.rotation_y += 40 * time.dt
			i.rotation_x += 40 * time.dt
	for i in k:
		if i:		
			i.rotation_y += 30 * time.dt
			i.rotation_x += 30 * time.dt

	if last:
		last.rotation_x += 40 * time.dt
		last.rotation_y += 40 * time.dt
	

	if player.y < -2:
		player.position = checkpoint
	if gameover:
		Text.default_resolution = 1080 * Text.size
		Text.size = .050
		Text(text='You won!', origin=(0,0), background=True)
	if held_keys['m']:
		music.stop()
	if held_keys['q']:
		exit(0);
	
		
		

music.play()
app.run()