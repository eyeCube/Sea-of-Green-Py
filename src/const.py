'''
    const.py
'''

class Symbol:
    nextID = 1
    def __init__(self):
        self.ID = Symbol.nextID
        Symbol.nextID += 1
        
    def __key(self):
        return self.ID

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, A):
            return self.__key() == other.__key()
        return NotImplemented
#end def



# fractions (_1_8 == 1/8)
_1_8    = 0.125
_1_16   = 0.0625
_1_32   = 0.03125
_1_64   = 0.015625
_1_128  = 0.0078125
_1_256  = 0.00390625
_1_512  = 0.001953125
_1_1024 = 0.0009765625


#
# Engine Constants
#


# special character key inputs
K_ESCAPE    = 19
K_UP        = 24
K_DOWN      = 25
K_RIGHT     = 26
K_LEFT      = 27
K_ENTER     = 28
K_PAGEUP    = 30
K_PAGEDOWN  = 31
K_HOME      = 127
K_END       = 144
K_BACKSPACE = 174
K_DELETE    = 175
K_INSERT    = 254


#direction
DIRECTIONS={
    (-1,-1) : 'northwest',
    (1,-1)  : 'northeast',
    (0,-1)  : 'north',
    (-1,0)  : 'west',
    (0,0)   : 'self',
    (1,0)   : 'east',
    (-1,1)  : 'southwest',
    (0,1)   : 'south',
    (1,1)   : 'southeast',
}
DIRECTIONS_TERSE={
    (-1,-1) : 'NW',
    (1,-1)  : 'NE',
    (0,-1)  : 'N',
    (-1,0)  : 'W',
    (0,0)   : 'self',
    (1,0)   : 'E',
    (-1,1)  : 'SW',
    (0,1)   : 'S',
    (1,1)   : 'SE',
}
DIRECTION_FROM_INT={
    0   : (1,0,),
    1   : (1,-1,),
    2   : (0,-1,),
    3   : (-1,-1,),
    4   : (-1,0,),
    5   : (-1,1,),
    6   : (0,1,),
    7   : (1,1,),
}


WINDOW_WIDTH = 80
WINDOW_HEIGHT = 50



# special chars #

# border 0
# single-line on all sides
CH_VW       = [179, 179, 186] # vertical wall
CH_HW       = [196, 205, 205] # horizontal wall
CH_TLC      = [218, 213, 201] # top-left corner
CH_BLC      = [192, 212, 200] # bottom-left corner
CH_BRC      = [217, 190, 188] # bottom-right corner
CH_TRC      = [191, 184, 187] # top-right corner



    #------------------------#
    #     Game Constants     #
    #------------------------#

MASS_PLAYER = 100


TILES_PER_ROW = 16
TILES_PER_COL = 16
GAME_TITLE = "Sea of Green"

ROOMW       = 80        # max dungeon level size, width
ROOMH       = 50        # ", height
MAXLEVEL    = 10        # deepest dungeon level


#
# Tiles
#

TILE_OCEAN      =   249     # centered dot
TILE_AIR        =   32     # space
TILE_WALL       = ord('#')



# flags

DEAD = Symbol()
BLIND = Symbol()
DEAF = Symbol()
NVISION = Symbol()



# damage types

DMG_PHYSICAL = Symbol()
DMG_SOUND = Symbol()
DMG_ELECTRIC = Symbol()



# gear

GEAR_SCREW = Symbol()
GEAR_PUMPJET = Symbol()
GEAR_BALLASTTANK = Symbol()
GEAR_CONTROLSURFACE = Symbol()
GEAR_SONARPULSE = Symbol()
GEAR_TORPEDO = Symbol()
GEAR_MINE = Symbol()
GEAR_DEPTHCHARGE = Symbol()
GEAR_HARPOON = Symbol()
GEAR_INKCLOUD = Symbol()
GEAR_ELECTRIFIER = Symbol()


OXYGEN_TIERS={
    # tier  : cost, oxygen max
    0       : (5,   80,),
    1       : (25,  160,),
    2       : (125, 320,),
    3       : (500, 640,),
    4       : (1500,1280,),
    5       : (3500,2560,),
}
BATTERY_TIERS={
    # tier  : cost, energy max
    0       : (5,   400,),
    1       : (20,  800,),
    2       : (100, 1600,),
    3       : (600, 3200,),
    4       : (3000,6400,),
    5       : (9500,12800,),
}
ENGINE_TIERS={
    # tier  : cost, +energy/turn
    0       : (10,  1,),
    1       : (40,  2,),
    2       : (360, 3,),
    3       : (960, 4,),
    4       : (3600,6,),
    5       : (8000,8,),
}
HULL_TIERS={
    # tier  : cost, max Hull integrity Points (HP)
    0       : (40,  2,),
    1       : (100, 4,),
    2       : (400, 6,),
    3       : (1200,8,),
    4       : (2600,10,),
    5       : (6000,12,),
}
TREASURE={
    # depth : (%spawnRate, minGold, maxGold,),
    1       : (3,   1,  10,),
    2       : (4,   2,  20,),
    3       : (5,   4,  30,),
    4       : (6,   6,  40,),
    5       : (7,   8,  50,),
    6       : (8,   10, 60,),
    7       : (9,   12, 70,),
    8       : (10,  14, 80,),
    9       : (11,  16, 90,),
    10      : (12,  18, 100,),
}


# maybe we don't even need this at all
# move to different file
##GEAR={
##    # const             :( name, GearComponent, create script, equip script, use script
##    GEAR_PROPELLER      :("Propeller", Gear_Propeller, create_gear_propeller, equip_propeller, None,),
##    GEAR_BALLASTTANK    :("Ballast Tank", Gear_BallastTank, create_gear_ballast_tank, equip_ballast_tank, None,),
##    GEAR_SONARPULSE     :("Sonar Pulse", Gear_SonarPulse, create_gear_sonar_pulse, None, use_sonar_pulse,),
##    GEAR_TORPEDO        :("Torpedos", Gear_Torpedo, create_gear_torpedo, None, use_torpedo,),
##    GEAR_MINE           :("Mines", Gear_Mine, create_gear_mine, None, use_mine,),
##    GEAR_DEPTHCHARGE    :("Depth Charge", Gear_DepthCharge, create_gear_depth_charge, None, use_depth_charge,),
##    GEAR_GRAPPLINGHOOK  :("Grappling Hook", Gear_GrapplingHook, create_gear_grappling_hook, None, use_grappling_hook,),
##}
##ENGINES={
##    ENGINE_NUCLEAR      :("Thermonuclear Engine", 40, 2,),
##}


