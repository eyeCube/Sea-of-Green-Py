'''
    entities.py
    Sea of Green
'''

import esper
import random

from colors import COLORS as COL
from const import *
import components as cmp
import rogue as rog
import ai
import game


def create_bubbles(x,y):
    world=rog.world()
    ent = world.create_entity(
        cmp.Name("bubbles"),
        cmp.Image(random.choice((19,20,)), COL['accent'], COL['black']),
        cmp.Actor(),
        cmp.AI(ai.ai_bubbles),
        cmp.Position(x,y),
        cmp.Opaque(),
        cmp.Flags()
        )
    return ent

def create_chest(x,y,gold):
    ent = rog.world().create_entity(
        cmp.Name("chest"),
        cmp.Image(18, COL['gold'], COL['black']),
        cmp.Position(x,y),
        cmp.Opaque(),
        cmp.Reward(gold),
        cmp.Flags()
        )
    return ent


def create_npc(x,y):
    world=rog.world()
    ent = world.create_entity(
        cmp.Creature(),
        cmp.Actor(),
        cmp.Position(x,y),
        cmp.SenseSight(),
        cmp.SenseHearing(),
        cmp.Flags()
        )
    return ent

def create_angelfish(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("angelfish"))
    world.add_component(ent, cmp.Image(5, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(20))
    world.add_component(ent, cmp.AI(ai.ai_curious))
    world.add_component(ent, cmp.Value(10))
    world.add_component(ent, cmp.Mobility([0,1,0,
                                           1,1,1,
                                           0,1,0]))
    world.add_component(ent, cmp.HP(1))
    world.add_component(ent, cmp.Damage(1))
    return ent

def create_angler(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("angler"))
    world.add_component(ent, cmp.Image(6, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(50))
    world.add_component(ent, cmp.AI(ai.ai_hunter))
    world.add_component(ent, cmp.Value(75))
    world.add_component(ent, cmp.Mobility([1,0,1,
                                           1,1,1,
                                           1,0,1]))
    world.add_component(ent, cmp.HP(2))
    world.add_component(ent, cmp.Damage(2))
    return ent

def create_barracudas(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("barracudas"))
    world.add_component(ent, cmp.Image(7, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(30))
    world.add_component(ent, cmp.AI(ai.ai_swarm))
    world.add_component(ent, cmp.Value(20))
    world.add_component(ent, cmp.Mobility([1,0,1,
                                           0,1,0,
                                           1,0,1]))
    world.add_component(ent, cmp.HP(2))
    world.add_component(ent, cmp.Damage(1))
    return ent

def create_seadragon(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("seadragon"))
    world.add_component(ent, cmp.Image(8, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(200))
    world.add_component(ent, cmp.AI(ai.ai_hunter))
    world.add_component(ent, cmp.Value(150))
    world.add_component(ent, cmp.Mobility([1,1,1,
                                           1,1,1,
                                           1,1,1]))
    world.add_component(ent, cmp.HP(3))
    world.add_component(ent, cmp.Damage(2))
    return ent

def create_crocodile(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("crocodile"))
    world.add_component(ent, cmp.Image(9, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(150))
    world.add_component(ent, cmp.AI(ai.ai_hunter))
    world.add_component(ent, cmp.Value(60))
    world.add_component(ent, cmp.Mobility([0,1,0,
                                           2,1,2,
                                           0,1,0]))
    world.add_component(ent, cmp.HP(2))
    world.add_component(ent, cmp.Damage(2))
    return ent

def create_shark(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("shark"))
    world.add_component(ent, cmp.Image(16, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(300))
    world.add_component(ent, cmp.AI(ai.ai_hunter))
    world.add_component(ent, cmp.Value(200))
    world.add_component(ent, cmp.Mobility([1,0,1,
                                           2,1,2,
                                           1,0,1]))
    world.add_component(ent, cmp.HP(3))
    world.add_component(ent, cmp.Damage(2))
    return ent

def create_ray(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("ray"))
    world.add_component(ent, cmp.Image(17, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(150))
    world.add_component(ent, cmp.AI(ai.ai_curious))
    world.add_component(ent, cmp.Value(20))
    world.add_component(ent, cmp.Mobility([1,0,1,
                                           1,1,1,
                                           1,0,1]))
    world.add_component(ent, cmp.HP(1))
    world.add_component(ent, cmp.Damage(1))
    return ent

def create_bonefish(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("bonefish"))
    world.add_component(ent, cmp.Image(140, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(10))
    world.add_component(ent, cmp.AI(ai.ai_support)) # hang back, attack occasionally
    world.add_component(ent, cmp.Value(25))
    world.add_component(ent, cmp.Mobility([0,1,0,
                                           1,1,1,
                                           0,1,0]))
    world.add_component(ent, cmp.HP(1))
    world.add_component(ent, cmp.Damage(1))
    return ent

def create_turtle(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("turtle"))
    world.add_component(ent, cmp.Image(141, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(300))
    world.add_component(ent, cmp.AI(ai.ai_docile))
    world.add_component(ent, cmp.Value(100))
    world.add_component(ent, cmp.Mobility([1,0,1,
                                           1,1,1,
                                           1,0,1]))
    world.add_component(ent, cmp.HP(3))
    world.add_component(ent, cmp.Damage(1))
    return ent

def create_pufferfish(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("pufferfish"))
    world.add_component(ent, cmp.Image(142, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(25))
    world.add_component(ent, cmp.AI(ai.ai_puff)) # changes to chr 143 
    world.add_component(ent, cmp.Value(70))
    world.add_component(ent, cmp.Mobility([0,1,0,
                                           1,1,1,
                                           0,1,0]))
    world.add_component(ent, cmp.HP(1))
    world.add_component(ent, cmp.Damage(2))
    return ent

def create_eel(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("eel"))
    world.add_component(ent, cmp.Image(144, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(40))
    world.add_component(ent, cmp.AI(ai.ai_electrify))
    world.add_component(ent, cmp.Value(150))
    world.add_component(ent, cmp.Mobility([1,1,1,
                                           0,1,0,
                                           1,1,1]))
    world.add_component(ent, cmp.HP(1))
    world.add_component(ent, cmp.Damage(2))
    return ent

def create_goldfish(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("goldfish"))
    world.add_component(ent, cmp.Image(224, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(30))
    world.add_component(ent, cmp.AI(ai.ai_curious))
    world.add_component(ent, cmp.Value(5))
    world.add_component(ent, cmp.Mobility([0,1,0,
                                           1,1,1,
                                           0,1,0]))
    world.add_component(ent, cmp.HP(1))
    world.add_component(ent, cmp.Damage(1))
    return ent

def create_seahorse(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("seahorse"))
    world.add_component(ent, cmp.Image(225, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(20))
    world.add_component(ent, cmp.AI(ai.ai_fearful))
    world.add_component(ent, cmp.Value(80))
    world.add_component(ent, cmp.Mobility([1,0,1,
                                           0,1,0,
                                           1,0,1]))
    world.add_component(ent, cmp.HP(1))
    world.add_component(ent, cmp.Damage(1))
    return ent

def create_octopus(x,y):
    world=rog.world()
    ent = create_npc(x,y)
    world.add_component(ent, cmp.Name("octopus"))
    world.add_component(ent, cmp.Image(234, COL['accent'], COL['black']))
    world.add_component(ent, cmp.Mass(150))
    world.add_component(ent, cmp.AI(ai.ai_curious))
    world.add_component(ent, cmp.Value(300))
    world.add_component(ent, cmp.Mobility([1,1,1,
                                           1,1,1,
                                           1,1,1]))
    world.add_component(ent, cmp.HP(4))
    world.add_component(ent, cmp.Damage(2))
    return ent

CREATURES={
    #chr:(L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,create script
    5   :(4, 2, 0, 0, 0, 0, 0, 0, 0, 0, create_angelfish),
    6   :(0, 0, 0, 0, 0, 0, 2, 3, 4, 4, create_angler),
    7   :(0, 6, 1, 0, 0, 0, 0, 0, 0, 0, create_barracudas),
    8   :(0, 0, 0, 0, 2, 6, 4, 0, 1, 4, create_seadragon),
    9   :(0, 0, 6, 4, 0, 0, 0, 0, 0, 0, create_crocodile),
    16  :(0, 0, 0, 0, 0, 2, 4, 6, 2, 0, create_shark),
    17  :(1, 2, 4, 3, 1, 0, 0, 0, 0, 0, create_ray),
    140 :(0, 0, 0, 0, 0, 0, 2, 4, 6, 0, create_bonefish),
    141 :(0, 1, 2, 8, 4, 2, 0, 0, 0, 0, create_turtle),
    142 :(0, 0, 0, 4, 6, 2, 0, 0, 0, 0, create_pufferfish),
    144 :(0, 0, 2, 4, 2, 0, 0, 0, 0, 0, create_eel),
    224 :(4, 3, 2, 1, 0, 0, 0, 0, 0, 0, create_goldfish),
    225 :(0, 0, 0, 1, 1, 2, 3, 4, 2, 0, create_seahorse),
    234 :(0, 0, 0, 0, 0, 1, 2, 4, 5, 6, create_octopus),
}



# Gear / Modules / Modularity

def add_module(ent:int, slot:int, module):
    world=rog.world()
    compo = world.component_for_entity(ent, cmp.Modularity)
    if slot <= compo.num_slots and slot > 0:
        if compo.modules.get(slot, None):
            pass
        # NOTE: error when running msg before full game initialization!!!
##            rog.msg("Cannot add module; slot is occupied.")
        else:
##            rog.msg("Added module {}.".format(module.NAME))
            compo.modules.update({slot : module})
    else:
        print("FAILED TO ADD MODULE")
##        rog.msg("Cannot add module; slot limit exceeded.")
def remove_module(ent:int, slot:int):
    world=rog.world()
    compo = world.component_for_entity(ent, cmp.Modularity)
    if compo.modules.get(slot, None):
        rog.msg("Removed {}.".format(compo.modules[slot].NAME))
        del compo.modules[slot]
    else:
        print("FAILED TO REMOVE MODULE")
        rog.msg("Cannot remove module; slot is empty.")

def module_level_up(module):
    if module.level < 3:
        module.level += 1
        return True
    return False


class Gear:
    MOVE_DIRECTIONS = [] # for regular movement (not counting harpoon, ink jets, etc.)
    def __init__(self):
        self.quantity = -1
        self.level = 0
        self.active = False
    def toggle(self):
        self.active = not self.active
    def get_cost(self):
        return self.COST
    def get_energy(self):
        return self.ENERGY[self.level]
    def get_volume(self):
        return self.VOLUME[self.level]
    def get_damage(self):
        return self.DAMAGE[self.level]
    def get_damage_type(self):
        return self.DAMAGETYPE
    def get_duration(self):
        return self.DURATION[self.level]
    def get_uses(self):
        return self.USES[self.level]
    def get_timer(self):
        return self.TIMER[self.level]
    def get_move(self):
        return self.MOVE[self.level]
    def get_stun(self):
        return self.STUN[self.level]
    def get_range(self):
        return self.RANGE[self.level]
    def decrement_uses(self):
        self.quantity = max(self.quantity - 1, 0)
    def refill_uses(self):
        self.quantity = self.get_uses()

class Gear_Screw(Gear):
    NAME = "Screw"
    DESCRIPTION = "Permits horizontal movement and rapid dashing, but is loud."
    # dash moves 2 spaces, doubles the volume, and uses triple amount of energy.
    ID = GEAR_SCREW
    COST = 50
    CHAR = 160
    ENERGY = [8, 7, 6, 6] # Level 0, 1, 2, 3
    USES = None
    VOLUME = [32, 28, 24, 20]
    MOVE_DIRECTIONS = [(-1,0),(1,0)]
    def __init__(self):
        super(Gear_Screw, self).__init__()
        self.level = 0
        
class Gear_BallastTank(Gear): 
    NAME = "Ballast Tanks"
    DESCRIPTION = "Permits silent vertical movement."
    ID = GEAR_BALLASTTANK
    COST = 50
    CHAR = 161
    ENERGY = [6, 5, 4, 3]
    USES = None
    VOLUME = [6, 4, 2, 0]
    MOVE_DIRECTIONS = [(0,-1),(0,1)]
    def __init__(self):
        super(Gear_BallastTank, self).__init__()
        self.level = 0
        
class Gear_PumpJet(Gear):
    NAME = "Pump-Jets"
    DESCRIPTION = "Permits quiet cardinal movement."
    ID = GEAR_PUMPJET
    COST = 200
    CHAR = 162
    ENERGY = [10, 9, 8, 7] # Level 0, 1, 2, 3
    USES = None
    VOLUME = [12, 10, 8, 6]
    MOVE_DIRECTIONS = [(-1,0),(1,0),(0,1),(0,-1)]
    def __init__(self):
        super(Gear_PumpJet, self).__init__()
        self.level = 0
        
class Gear_ControlSurfaces(Gear):
    NAME = "Control Surfaces"
    DESCRIPTION = "Permits diagonal movement."
    ID = GEAR_CONTROLSURFACE
    COST = 150
    CHAR = 163
    ENERGY = [9, 8, 7, 6] # Level 0, 1, 2, 3
    USES = None
    VOLUME = [24, 20, 16, 12]
    MOVE_DIRECTIONS = [(-1,-1),(1,1),(-1,1),(1,-1)]
    def __init__(self):
        super(Gear_ControlSurfaces, self).__init__()
        self.level = 0
        
class Gear_SonarPulse(Gear):  # AOE damage around player;
        # Status Hell for target:
        # stuns some enemies; scares some enemies;
        # makes enemies permanently deaf;
        # makes target weak to physical damage for duration.
        # Also reveals locations of hidden passageways in radius.
    NAME = "Sonar Pulse"
    DESCRIPTION = "AoE damage around sub; induces various status effects."
    ID = GEAR_SONARPULSE
    COST = 100
    CHAR = 164
    ENERGY = [80, 90, 100, 110]
    USES = None
    DAMAGE = [1, 1, 1, 1]
    RANGE = [3, 4, 5, 6] # radius
    VOLUME = [64, 80, 96, 108]
    DURATION = [2, 3, 4, 5] # duration of all status effects
    DAMAGETYPE = DMG_SOUND
    def __init__(self):
        super(Gear_SonarPulse, self).__init__()
        self.level = 0
        
class Gear_InkJet(Gear):  # move in cardinal direction, and Shoot ink in opposite direction, 
                    # Ink coats target, blinding them. Also obscures vision
    NAME = "Ink Jets"
    DESCRIPTION = "Launch self in cardinal direction; shoot blinding ink behind."
    ID = GEAR_INKCLOUD
    COST = 150
    CHAR = 165
    ENERGY = [12, 11, 10, 9]
    USES = [4, 8, 16, 32]
    DAMAGE = [1, 1, 1, 1]
    MOVE = [1, 2, 3, 4] # maximum amount of tiles you can move
    DURATION = [5, 10, 15, 20] # duration of ink cloud AND ink status
    VOLUME = [32, 24, 20, 18]
    def __init__(self):
        super(Gear_InkJet, self).__init__()
        self.level = 0
        
class Gear_Torpedo(Gear): # create bubbles behind player; fire missile forward cardinal direction
    NAME = "Torpedos"
    DESCRIPTION = "Launch missile in horizontal direction & create bubbles behind."
    ID = GEAR_TORPEDO
    COST = 100
    CHAR = 166
    ENERGY = [1, 1, 1, 1]
    USES = [4, 8, 12, 16]
    DAMAGE = [2, 2, 2, 2]
    MOVE = [1, 1, 2, 2] # push amount
    VOLUME = [120, 120, 120, 120]
    DAMAGETYPE = DMG_PHYSICAL
    def __init__(self):
        super(Gear_Torpedo, self).__init__()
        self.level = 0
        self.quantity = self.USES[0]
        
class Gear_SuperTorpedo(Gear): # fire missile forward cardinal direction
                         # destroys walls on contact
    NAME = "Super Torpedos"
    DESCRIPTION = "Launch highly destructive AoE missile in horizontal direction."
    ID = GEAR_SUPERTORPEDO
    COST = 500
    CHAR = 167
    ENERGY = [2, 2, 2, 2]
    USES = [2, 3, 4, 5]
    DAMAGE = [4, 5, 6, 7]
    SPEED = [10, 10, 10, 10]
    RANGE = [2, 2, 3, 3] #explosion radius
    VOLUME = [150, 150, 150, 150]
    DAMAGETYPE = DMG_PIERCING
    def __init__(self):
        super(Gear_SuperTorpedo, self).__init__()
        self.level = 0
        self.quantity = self.USES[0]
        
class Gear_Mine(Gear): # create bubbles;
                        # drop single-target mine downward. Stuns on contact.
    NAME = "Mines"
    DESCRIPTION = "Deploy stunning mine downward & create bubbles."
    ID = GEAR_MINE
    COST = 150
    CHAR = 168
    ENERGY = [0, 0, 0, 0]
    USES = [10, 15, 20, 30]
    DAMAGE = [1, 1, 1, 1]
    VOLUME = [80, 80, 80, 80]
    STUN = [1, 2, 3, 4]
    DAMAGETYPE = DMG_PHYSICAL
    def __init__(self):
        super(Gear_Mine, self).__init__()
        self.level = 0
        self.quantity = self.USES[0]
        
class Gear_DepthCharge(Gear): # drop powerful time bomb that detonates within a small blast radius
                              # destroys walls in blast radius
                              # also move submarine up one tile
    NAME = "Depth Charges"
    DESCRIPTION = "Move up 1 tile & deploy deadly time bomb with a compact blast radius."
    ID = GEAR_DEPTHCHARGE
    COST = 300
    CHAR = 169
    ENERGY = [0, 0, 0, 0]
    USES = [2, 4, 6, 8]
    DAMAGE = [2, 2, 3, 3]
    RANGE = [2, 2, 3, 3] # blast radius size
    TIMER = [5, 5, 5, 5]
    VOLUME = [150, 150, 150, 150]
    DAMAGETYPE = DMG_PHYSICAL
    def __init__(self):
        super(Gear_DepthCharge, self).__init__()
        self.level = 0
        self.quantity = self.USES[0]
        
class Gear_Harpoon(Gear): # shoot missile forward cardinal direction
                    # pull target to player, or player to target based on mass
                    # moves up to X squares based on level
    NAME = "Harpoon"
    DESCRIPTION = "Fire harpoon in horizontal dir. to pull things (or self) closer."
    ID = GEAR_HARPOON
    COST = 500
    CHAR = 170
    ENERGY = [28, 26, 24, 22]
    USES = None
    DAMAGE = [1, 1, 1, 1]
    RANGE = [5, 10, 15, 20]
    MOVE = [2, 4, 6, 10] # max amount of tiles you can pull / be pulled
    VOLUME = [60, 55, 50, 45]
    DAMAGETYPE = DMG_PHYSICAL
    def __init__(self):
        super(Gear_Harpoon, self).__init__()
        self.level = 0
        
class Gear_Electrifier(Gear): # shock adjacent target to left or right
    NAME = "Electrifier"
    DESCRIPTION = "Shocks and stuns adjacent target in horizontal direction."
    ID = GEAR_ELECTRIFIER
    COST = 200
    CHAR = 171
    ENERGY = [50, 55, 60, 65]
    USES = None
    DAMAGE = [2, 2, 3, 4]
    STUN = [3, 4, 5, 6]
    VOLUME = [48, 54, 60, 66]
    DAMAGETYPE = DMG_ELECTRIC
    def __init__(self):
        super(Gear_Electrifier, self).__init__()
        self.level = 0
        
class Gear_(Gear):
    NAME = ""
    ID = 0
    COST = 2
    ENERGY = [0, 0, 0, 0]
    def __init__(self):
        self.level = 1



# animation

def animate(ent):
    world = rog.world()
    animation = world.component_for_entity(ent, cmp.Animation)
    image = world.component_for_entity(ent, cmp.Image)
    animation.index += 1
    image.char = animation.charList[int(animation.index)]
    listLen = len(animation.charList)
    if animation.looping:
        animation.index = animation.index % listLen
    elif animation.index >= listLen - 1:
        rog.release_entity(ent)
##        print("RELEASE")
##        animation.index = listLen - 1
##    image.char = animation.charList[int(animation.index)]






