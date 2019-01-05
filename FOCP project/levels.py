import pygame, sys, random
from game_global import *
from sprites import *

# Level Classes

class Level():

    def __init__(self, player, active_group):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.obj_list = pygame.sprite.Group()
        self.active_list = active_group
        self.complete = False
        self.player = player
        self.goal = []
        self.target = 0
        self.border = pygame.image.load('screen border black.png')
        self.bg = WHITE
        self.fg = BLACK
        self.level_name = 'Level 00'
        self.text_position = (width - 150, 40)
        self.star_array = [(500, 350),
                           (1600, 350),
                           (500, 750),
                           (1600, 750),
                           (1000, 550),
                           (1000, 150)]

        self.level_array = [(1000, 250),
        (1000, 650),
        (1600, 450),
        (500, 450)]


    def update(self):

        self.platform_list.update()
        self.enemy_list.update()
        self.obj_list.update()
        collide = pygame.sprite.spritecollideany(self.player, self.obj_list)
        for i in self.goal:
            if collide is i:
                collide.kill()
                self.target -= 1
        if self.target == 0: self.complete = True
            

    def draw(self, screen):

        screen.fill(self.bg)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.obj_list.draw(screen)

        #stam - bar#
        pygame.draw.rect(screen, BLUE, (50,70,self.player.stam,20))
        stam_surf = blackadderitc_font.render('Stamina',True,self.fg)
        screen.blit(stam_surf,(50,40))

        #Level Display
        self.level_surf = blackadderitc_font.render(self.level_name,True,self.fg)
        screen.blit(self.level_surf,self.text_position)
        screen.blit(self.border, (0,0))
        

class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)

        level = [(500, 1000),
                 (1000, 1000),
                 (1500, 1000)]

        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)
 
        self.goal = [Star((1600, 900))]
        self.target = 1
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 01'


class Level_02(Level):
    """ Definition for level 1. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with width, height, x, and y of platform
        level = [(400, 850),
                 (1000, 650),
                 (1000, 250),
                 (500, 1000),
                 (1000, 1000),
                 (1500, 1000)]
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)
        self.platform_list.add(PlatSprite('base.png', (1600, 450), self.active_list, True))
        self.goal = [Star((1000, 150)), Star((400, 750))]
        self.target = 2
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 02'

class Level_03(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        level = [(1000, 250),
                 (1000, 650),
                 (1600, 450),
                 (500, 450),
                 (500, 850),
                 (1600, 850),
                 (1000, 1000)]
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.goal = [Star((500, 350)), Star((1600, 350)), Star((500, 750)), Star((1600, 750)), Star((1000, 550)), Star((1000, 900))]
        self.target = 6
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 03'

class Level_04(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000),
                 (1000, 250),
                 (1000, 650),
                 (1600, 450),
                 (500, 450)]
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.goal = [Star((500, 350)), Star((1600, 350)), Star((1000, 550)), Star((1000, 150))]
        self.target = 4
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 04'

class Level_05(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000),
                 (1000, 250),
                 (1000, 650),
                 (1600, 450),
                 (500, 450)]
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 05'

class Level_06(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1

        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 06'

class Level_07(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
            
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 07'

class Level_08(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 08'

class Level_09(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 09'

class Level_10(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 10'


class Level_11(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 11'

class Level_12(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 12'

class Level_13(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 13'

class Level_14(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 14'

class Level_15(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 15'
        
class Level_16(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 16'
        
class Level_17(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 17'

class Level_18(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 18'

class Level_19(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 19'
        
class Level_20(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        star_list = self.star_array[:]
        stars_count = random.randint(1, 6)
        stars = stars_count
        for i in range(stars_count):
            index = random.randint(0,stars_count - 1)
            self.goal += [Star(star_list[index])]
            star_list.remove(star_list[index])
            stars_count -= 1
        
        level_list = self.level_array[:]
        levels_count = random.randint(1, 4)
        levels = levels_count

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000)]
        
        for i in range(levels_count):
            index = random.randint(0, levels_count - 1)
            level += [level_list[index]]
            level_list.remove(level_list[index])
            levels_count -= 1
 
        # Go through the array above and add platforms
        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.target = stars
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Level 20'


class Level_End(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)

        level = [(500, 1000),
                (1000, 1000),
                (1500, 1000),
                (0, 1000),
                (2000, 1000)]

        for platform in level:
            block = PlatSprite('base.png', platform, self.active_list)
            self.platform_list.add(block)

        self.goal = [Star((width/2, 400))]
        self.target = -1
        for i in self.goal: self.obj_list.add(i)

        self.level_name = 'YOU WIN'
        self.text_position = (width/2 - 100, height/2 - 100)

class Level_Lose(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, active_group):
        """ Create level 1. """

        Level.__init__(self, player, active_group)

        self.goal = [Star((width/2 - 125, 450)), Star((width/2 + 100, 450))]
        self.target = -1
        for i in self.goal: self.obj_list.add(i)

        self.bg = GREY
        self.fg = WHITE
        self.level_name = 'YOU LOSE'
        self.text_position = (width/2 - 100, height/2 - 100)
    
class Level_Nightmare(Level):

    def __init__(self, player, active_group):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player, active_group)
 
        # Array with type of platform, and x, y location of the platform.
        level = [(1000, 250),
                 (1000, 650),
                 (1600, 450),
                 (500, 450),
                 (500, 1000),
                 (1500, 1000),
                 (1000, 1000)]
 
        # Go through the array above and add platforms
        
        for platform in level:
            block = PlatSprite('base_neo.png', platform, self.active_list)
            self.platform_list.add(block)
        self.platform_list.add(PlatSprite('base_neo.png', (1500, 750), self.active_list, True))
        self.platform_list.add(PlatSprite('base_neo.png', (500, 750), self.active_list, True))

        self.goal = [Star((500, 350)), Star((1600, 350)), Star((500, 750)), Star((1600, 750)), Star((1000, 550)), Star((1000, 150))]
        self.target = -1
        for i in self.goal: self.obj_list.add(i)
        self.level_name = 'Nightmare'
        self.bg = GREY
        self.fg = WHITE
