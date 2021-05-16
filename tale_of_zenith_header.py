import pygame


def load_texture(file_name, subdir=""):
    return pygame.image.load(f"{ASSETS_PATH}\\{TEXTURE_PATH}\\{subdir}\\{file_name}.{TEXTURE_FILE_EXT}")


WIDTH = "w"  # Yes I'm funny
HEIGHT = "h"

# SCREEN_SIZE = {WIDTH: 1609, HEIGHT: 909}
SCREEN_SIZE = {WIDTH: 1366, HEIGHT: 704}
GAME_CAPTION = "Tale of Zenith"

DIRECTION_NORTH = "n"
DIRECTION_NORTHWEST = "nw"
DIRECTION_NORTHEAST = "ne"
DIRECTION_EAST = "e"
DIRECTION_SOUTH = "s"
DIRECTION_SOUTHWEST = "sw"
DIRECTION_SOUTHEAST = "se"
DIRECTION_WEST = "w"

DIRECTION_ORDER = (DIRECTION_NORTH, DIRECTION_NORTHEAST, DIRECTION_EAST, DIRECTION_SOUTHEAST,
                   DIRECTION_SOUTH, DIRECTION_SOUTHWEST, DIRECTION_WEST, DIRECTION_NORTHWEST)

ASSETS_PATH = "Assets"
TEXTURE_PATH = "Textures"
SWORD_TEXTURE_PATH = "Sword"
REGENERATABLES_TEXTURE_PATH = "Regeneratables"
SOUND_PATH = "Sounds"
TEXTURE_FILE_EXT = "png"
SOUND_FILE_EXT = "mp3"

TEXTURE_BACKGROUND_NAME = "background"
TEXTURE_ICON_NAME = "icon"
TEXTURE_SLIME_NAME = "slime"
TEXTURE_GOLDEN_SLIME_NAME = "golden_slime"
TEXTURE_SPEED_MUSH_NAME = "speed_mush"
TEXTURE_TELESHROOM_NAME = "teleshroom"

TEXTURE_DIAG_SIZE = {WIDTH: 60, HEIGHT: 60}  # Diagonal textures size (nw ne sw se)
TEXTURE_PERP_VERT_SIZE = {WIDTH: 24, HEIGHT: 80}  # Perpendicular textures size (n s)
TEXTURE_PERP_HORZ_SIZE = {WIDTH: 80, HEIGHT: 24}  # Perpendicular textures size (e w)

TEXTURE_NORTH = load_texture(DIRECTION_NORTH, subdir=SWORD_TEXTURE_PATH)
TEXTURE_NORTHWEST = load_texture(DIRECTION_NORTHWEST, subdir=SWORD_TEXTURE_PATH)
TEXTURE_NORTHEAST = load_texture(DIRECTION_NORTHEAST, subdir=SWORD_TEXTURE_PATH)
TEXTURE_EAST = load_texture(DIRECTION_EAST, subdir=SWORD_TEXTURE_PATH)
TEXTURE_SOUTH = load_texture(DIRECTION_SOUTH, subdir=SWORD_TEXTURE_PATH)
TEXTURE_SOUTHWEST = load_texture(DIRECTION_SOUTHWEST, subdir=SWORD_TEXTURE_PATH)
TEXTURE_SOUTHEAST = load_texture(DIRECTION_SOUTHEAST, subdir=SWORD_TEXTURE_PATH)
TEXTURE_WEST = load_texture(DIRECTION_WEST, subdir=SWORD_TEXTURE_PATH)

MASK_TEXTURE_NORTH = pygame.mask.from_surface(TEXTURE_NORTH)
MASK_TEXTURE_NORTHWEST = pygame.mask.from_surface(TEXTURE_NORTHWEST)
MASK_TEXTURE_NORTHEAST = pygame.mask.from_surface(TEXTURE_NORTHEAST)
MASK_TEXTURE_EAST = pygame.mask.from_surface(TEXTURE_EAST)
MASK_TEXTURE_SOUTH = pygame.mask.from_surface(TEXTURE_SOUTH)
MASK_TEXTURE_SOUTHWEST = pygame.mask.from_surface(TEXTURE_SOUTHWEST)
MASK_TEXTURE_SOUTHEAST = pygame.mask.from_surface(TEXTURE_SOUTHEAST)
MASK_TEXTURE_WEST = pygame.mask.from_surface(TEXTURE_WEST)

TEXTURE_BACKGROUND = load_texture(TEXTURE_BACKGROUND_NAME)
TEXTURE_ICON = load_texture(TEXTURE_ICON_NAME)

TEXTURE_SLIME = load_texture(TEXTURE_SLIME_NAME, subdir=REGENERATABLES_TEXTURE_PATH)
TEXTURE_GOLDEN_SLIME = load_texture(TEXTURE_GOLDEN_SLIME_NAME, subdir=REGENERATABLES_TEXTURE_PATH)
TEXTURE_SPEED_MUSH = load_texture(TEXTURE_SPEED_MUSH_NAME, subdir=REGENERATABLES_TEXTURE_PATH)
TEXTURE_TELESHROOM = load_texture(TEXTURE_TELESHROOM_NAME, subdir=REGENERATABLES_TEXTURE_PATH)

pygame.mixer.init()

SOUND_TING_NAME = "ting"
SOUND_BACKGROUND_NAMES = ["background", "stargazer", "funny"]
BACKGROUND_SONGS = []

for song in SOUND_BACKGROUND_NAMES:
    BACKGROUND_SONGS.append(pygame.mixer.Sound(f"{ASSETS_PATH}\\{SOUND_PATH}\\{song}.{SOUND_FILE_EXT}"))

SOUND_TING = pygame.mixer.Sound(f"{ASSETS_PATH}\\{SOUND_PATH}\\{SOUND_TING_NAME}.{SOUND_FILE_EXT}")

TEXTURE_MASK_MATCH = {DIRECTION_NORTH: MASK_TEXTURE_NORTH, DIRECTION_NORTHWEST: MASK_TEXTURE_NORTHWEST,
                      DIRECTION_NORTHEAST: MASK_TEXTURE_NORTHEAST, DIRECTION_EAST: MASK_TEXTURE_EAST,
                      DIRECTION_SOUTH: MASK_TEXTURE_SOUTH, DIRECTION_SOUTHWEST: MASK_TEXTURE_SOUTHWEST,
                      DIRECTION_SOUTHEAST: MASK_TEXTURE_SOUTHEAST, DIRECTION_WEST: MASK_TEXTURE_WEST}

CONST_DIRECTION_TEXTURE_MATCH = {DIRECTION_NORTH: TEXTURE_NORTH, DIRECTION_NORTHWEST: TEXTURE_NORTHWEST,
                                 DIRECTION_NORTHEAST: TEXTURE_NORTHEAST, DIRECTION_EAST: TEXTURE_EAST,
                                 DIRECTION_SOUTH: TEXTURE_SOUTH, DIRECTION_SOUTHWEST: TEXTURE_SOUTHWEST,
                                 DIRECTION_SOUTHEAST: TEXTURE_SOUTHEAST, DIRECTION_WEST: TEXTURE_WEST}


DIRECTION_TEXTURE_MATCH = {DIRECTION_NORTH: TEXTURE_NORTH.copy(), DIRECTION_NORTHWEST: TEXTURE_NORTHWEST.copy(),
                           DIRECTION_NORTHEAST: TEXTURE_NORTHEAST.copy(), DIRECTION_EAST: TEXTURE_EAST.copy(),
                           DIRECTION_SOUTH: TEXTURE_SOUTH.copy(), DIRECTION_SOUTHWEST: TEXTURE_SOUTHWEST.copy(),
                           DIRECTION_SOUTHEAST: TEXTURE_SOUTHEAST.copy(), DIRECTION_WEST: TEXTURE_WEST.copy()}


def load_direction_texture_match(direction):
    if direction in DIRECTION_TEXTURE_MATCH:
        DIRECTION_TEXTURE_MATCH[direction] = CONST_DIRECTION_TEXTURE_MATCH[direction].copy()


MOVE_DIRECTION_MATCH = {(0, -1): DIRECTION_NORTH, (1, 0): DIRECTION_EAST,
                        (0, 1): DIRECTION_SOUTH, (-1, 0): DIRECTION_WEST,
                        (1, -1): DIRECTION_NORTHEAST, (1, 1): DIRECTION_SOUTHEAST,
                        (-1, -1): DIRECTION_NORTHWEST, (-1, 1): DIRECTION_SOUTHWEST}

DIRECTION_MOVE_MATCH = {DIRECTION_NORTH: (0, -1), DIRECTION_EAST: (1, 0),
                        DIRECTION_SOUTH: (0, 1), DIRECTION_WEST: (-1, 0),
                        DIRECTION_NORTHEAST: (1, -1), DIRECTION_SOUTHEAST: (1, 1),
                        DIRECTION_NORTHWEST: (-1, -1), DIRECTION_SOUTHWEST: (-1, 1)}

EFFECT_SPEED_MUSH_POWER = 2
EFFECT_SPEED_MUSH_DURATION = 25
EFFECT_TELESHROOM_ANIMATION_DURATION = 30
EFFECT_SLIME_SCORE = 1
EFFECT_GOLDEN_SLIME_SCORE = 15
EFFECT_GOLDEN_SLIME_DASH_IMMUNITY = 5  # How many ticks before golden slime can be hit

DASH_POWER = 3
DASH_DURATION = 20  # Ticks
DASH_COOLDOWN = 120
DASH_MOVE_COOLDOWN = 12

STATS_VELOCITY = "velocity"
STATS_SCORE = "score"
STATS_MOVABLE = "movable"

SWORD_ANIMATION_DELAY = 5
SWORD_SPEED = 7
SCREEN_PADDING = 50

SETTINGS_TICK_RATE = "tick_rate"
TICK_RATE = 60