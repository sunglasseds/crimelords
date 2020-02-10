import pygame
import math
import random

class GameObject():
    #Type:Base, Building,
    #Location: (x,y)
    #Team: "R", "B", or None
    def __init__(self, t, loc, color, i):
        self.id = id(self)
        self.type = t
        self.location = loc
        self.team = color
        self.icon = i

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_location(self):
        return self.location

    def get_team(self):
        return self.team

    def get_icon(self):
        return self.icon

    def set_icon(self, i):
        self.icon = i

    def get_location_string(self):
        return "(" + str(self.location[0]) + "," + str(self.location[1]) + ")"

class Unit(GameObject):
    def __init__(self, t, loc, color, i):
        super(Unit, self).__init__(t, loc, color, i)

class Mafioso(Unit):
    def __init__(self, t, loc, color, i):
        self.hp=100
        self.move_max=5
        self.ap=25
        self.alive=True
        super(Mafioso, self).__init__(t, loc, color, i)

    def strike(self, loc, objects):
        #Checks for valid location
        validLoc = False
        if (0 <= loc[0] < 20) and (0 <= loc[1] < 20):
            if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
                if (abs(loc[0] - self.location[0]) <= self.attack_max) and (abs(loc[1] - self.location[1]) <= self.attack_max):
                    validLoc = True

        #Checks if object can be attacked
        canStrike = False
        if validLoc:
            for o in objects:
                if o.get_location() == loc:
                    if o.get_type() in ["Demo", "Mafioso", "Assassin"]:
                        o.modify_hp(-self.ap)
                        canStrike = True
        return canStrike

    def take_action(self, list, objects, color, player):
        if self.alive:
            if 'move' in list[0]:
                self.move(list[0]['move'], objects)
            elif 'strike' in list[0]:
                self.strike(list[0]['strike'], objects)

class Demo(Unit):
    def __init__(self, t, loc, color, i):
        self.hp=750
        self.charge=1
        self.move_max=3
        self.ap=0
        self.alive=True
        super(Demo, self).__init__(t, loc, color, i)

    def move(self, loc, objects):
    #Checks if various conditions are met
    #Returns True if the move was successful, otherwise returns False
        canMove = True
        for o in objects:
            if o.get_location() == loc:
                canMove = False

        if canMove:
            if (0 <= loc[0] < 20) and (0 <= loc[1] < 20):
                if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
                    if (abs(loc[0] - self.location[0]) <= self.move_max) and (abs(loc[1] - self.location[1]) <= self.move_max):
                        self.location = loc
                        return True
        return False

    def take_action(self, list, objects, color, player):
        if self.alive:
            if 'move' in list[0]:
                self.move(list[0]['move'], objects)
            elif 'strike' in list[0]:
                self.strike(list[0]['strike'], objects)

class Assassin(Unit):
    def __init__(self, t, loc, color, i):
        self.hp=50
        self.move_max=10
        self.ap=50
        self.attack_max=5
        self.alive=True
        super(Assassin, self).__init__(t, loc, color, i)

    def strike(self, loc, objects):
        #Checks for valid location
        validLoc = False
        if (0 <= loc[0] < self.attack_max) and (0 <= loc[1] < self.attack_max):
            if (int(loc[0]) == loc[0]) and (int(loc[1]) == loc[1]):
                if (abs(loc[0] - self.location[0]) <= self.attack_max) and (abs(loc[1] - self.location[1]) <= self.attack_max):
                    validLoc = True

        #Checks if object can be attacked
        canStrike = False
        if validLoc:
            for o in objects:
                if o.get_location() == loc:
                    if o.get_type() in ["Demo", "Mafioso", "Assassin"]:
                        o.modify_hp(-self.ap)
                        canStrike = True
        return canStrike

    def take_action(self, list, objects, color, player):
        if self.alive:
            if 'move' in list[0]:
                self.move(list[0]['move'], objects)
            elif 'strike' in list[0]:
                self.strike(list[0]['strike'], objects)


class Base(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 2
        self.ap = 0
        self.mp = 0
        self.move_max = 0
        self.build_max = 1
        self.alive = True
        self.destructable = False
        super(Base, self).__init__(t, loc, color, i)

class restaurant(Unit):
    def __init__(self, t, loc, color, i):
        self.hp = 2
        self.ap = 0
        self.mp = 0
        self.move_max = 0
        self.alive = True
        self.destructable = True
        super(Base, self).__init__(t, loc, color, i)

'''class Base(Unit):
    def __init__(self, hp, move_max, melee_dmg, melee_rng, cost, drop, alive_state):
        self.hp = 100
        self.move_max = 5
        self.melee_dmg = 25
        self.melee_rng = 1
        self.cost = 10 
        self.drop = 5 
        self.color = ""
        self.alive_state= True
        super(Base, self).__init__( hp, move_max, melee_dmg, melee_rng, cost, drop, alive_state)
'''