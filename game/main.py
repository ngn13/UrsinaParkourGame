from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

jblock = load_texture('assets/jblock.png')
last = load_texture('assets/last.png')
checkb = load_texture('assets/checkb.png')
back = load_texture('assets/back.png')
music = Audio('assets/Else - Paris.mp4', loop=True, autoplay=True)	

window.exit_button.visible = False
window.title = 'UrsinaParkourGame/Github-ngn13'


gameover = False
checkpoint = (0,0,0)

lvl = 1
lvbef = 1

isMusic = True

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
			color = color.color(0,0,10))

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
			color = color.color(0,0,10))

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
			color = color.color(0,0,10))

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
			color = color.color(0,0,10))

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
			color = color.color(0,0,10),
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
			color = color.color(0,0,10),
			rotation = Vec3(150,-10,0),
			scale = 0.5)
	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				global gameover		
				global lvl
				lvl += 1
				if lvl == 1000:
					gameover = True
				createLvl()			
				destroy(self)


player = FirstPersonController(gravity=1,height=25,speed=20,jump_height=5,jump_duration=.45,mouse_sensitivity = Vec2(60, 60) 
,cursor = Entity(parent=camera.ui, model='quad', color=color.red, scale=.001, rotation_z=45))

sky = Sky()

voxel = Voxel(position = (0,0,0))
voxel.rotation_y = 0
voxel.rotation_x = 0

r = random.randint(0,1000)%5

a = 3
b = 15
c = []
j = []
j2 = []
j3 = []
k = []
lastL = []
z = 0

test = Text(text='Level: ' + str(lvl), origin=(0,-15), background=True)


def createLvl():
	global a
	global b
	global c
	global j
	global j2
	global j3
	global k
	global z
	global last
	for i in range(20):
		p = random.randint(1,5)
		p2 = random.randint(1,4)

		if p == 1:
			c.append(CheckB(random.randint(0,7),a+1,b))
		if i == 19:
			lastL.append(Last(random.randint(0,7),a+1,b))
	
		if p == 1:
			j.append(Voxel(position = (random.randint(0,7),a,b)))
	
		elif p == 2:
			j2.append(Voxel2(position = (random.randint(0,7),a,b)))

		elif p == 3:
			j3.append(Voxel3(position = (random.randint(0,7),a,b)))

		elif p == 4 and p2 == 4:
			k.append(Voxel3(position = (random.randint(0,7),a,b)))
	
		else:
			j2.append(Voxel2(position = (random.randint(0,7),a,b)))
		
	
		a += 3
		b += 15
		z += 1


def update():
	global a
	global b
	global c
	global j
	global j2
	global j3
	global k
	global z
	global last
	global lvl
	global lvbef
	if not lvbef == lvl:
		lvbef = lvl
		test.text = "Level " + str(lvl)
	for i in c:
		if i:		
			i.rotation_y += 40 * time.dt
			i.rotation_x += 40 * time.dt
	for i in k:
		if i:		
			i.rotation_y += 30 * time.dt
			i.rotation_x += 30 * time.dt

	for i in lastL:
		if i:
			i.rotation_x += 40 * time.dt
			i.rotation_y += 40 * time.dt
	

	if player.y < -2:
		player.position = checkpoint

	if gameover:
		Text.default_resolution = 1080 * Text.size
		Text.size = .050
		Text(text='You won!', origin=(0,0), background=True)
		application.pause()
	if held_keys['m']:
		global isMusic
		if isMusic:
			music.stop()
			isMusic = False
		else:
			music.play()
			isMusic = True
	if held_keys['q']:
		exit(0);
	if held_keys['shift']:
		if player.speed == 20:
			player.speed = 10
		else:
			player.speed = 20
		
	
		

createLvl()
music.play()
app.run()