import crimelords
import random

built = False
def turn(me, unit, objects):
	print(me.money)
	dirs = random.choice([(0, 1), (1, 0), (-1, 0), (0, -1)])
	if unit.type == "Mafioso" and unit.color == me.color and not built:
		built == True
		unit.move(dirs[0], dirs[1], objects)
	elif unit.type == "Base":
		if not built:
			unit.build("Mafioso", [unit.location[0]+dirs[0], unit.location[0]+dirs[1]], objects, me)
	return unit
