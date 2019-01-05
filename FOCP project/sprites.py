import pygame, sys, random, math
from game_global import *

# Player

class WheelSprite(pygame.sprite.Sprite):

    def __init__(self, anchor):
        super().__init__()
        self.list_image = [pygame.image.load('wheel2.png'), pygame.image.load('empty.png')]
        self.direction = 0
        self.anchor = anchor

    def update(self):
        self.direction += (self.anchor.k_right + self.anchor.k_left)
        #u = 0
        if self.anchor.speed == 0 and not self.anchor.shooting: self.image = self.list_image[1]
        else:
            self.image = pygame.transform.rotate(self.list_image[0], self.direction * MOVE_SPEED * 10)
            #u = 1
        self.rect = self.image.get_rect()
        x, y = self.anchor.position
        # if u: y -= 100 # for inserting face as image2
        self.rect.center = (x, y+50)

class Gun(pygame.sprite.Sprite):

    def __init__(self, anchor):
        super().__init__()
        self.list_image = [pygame.image.load('armed_gun.png'), pygame.transform.flip(pygame.image.load('armed_gun.png'), True, False), pygame.image.load('empty.png')]
        self.anchor = anchor
        self.target = (0, 0)
        self.delay = 0

    def update(self):

        if self.anchor.shooting:
            adj = self.anchor.target[0] - self.anchor.rect.center[0]
            if adj == 0: adj = 0.01
            opp = -(self.anchor.target[1] - self.anchor.rect.center[1])
            angle = math.degrees(math.atan(opp/adj))
            if self.anchor.target[0] > self.anchor.rect.center[0]:
                self.image = pygame.transform.rotate(pygame.transform.flip(self.list_image[0], True, False), angle)
                self.anchor.src_image = self.anchor.list_image[2]
            elif self.anchor.target[0] < self.anchor.rect.center[0]:
                self.anchor.src_image = self.anchor.list_image[1]
                self.image = pygame.transform.rotate(self.list_image[0], angle)
                
        else: self.image = self.list_image[2]
        self.rect = self.image.get_rect()
        x, y = self.anchor.position
        self.rect.center = (x, y - 12)

class Bullet(pygame.sprite.Sprite):

    def __init__(self, anchor):
        super().__init__()
        self.src_image = pygame.image.load('laser_red.png').convert_alpha()
        self.target = anchor.target
        self.speed = 30
        adj = self.target[0] - anchor.rect.center[0]
        if adj == 0: adj = 0.01
        opp = -(self.target[1] - anchor.rect.center[1])
        angle = math.degrees(math.atan(opp/adj))
        self.m = opp/adj
        self.image = pygame.transform.rotate(self.src_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = anchor.rect.center
        self.anchor = anchor

    def update(self):
        x, y = self.target
        if self.m == -1: self.m = -0.99
        dx = ((self.speed**2)/abs(self.m + 1))**0.5
        dy = self.m*dx
        if self.target[0] < self.anchor.rect.centerx:
            dx *= -1
            dy *= -1
        self.rect.centerx += dx
        self.rect.centery -= dy

        if self.rect.right > width or self.rect.left < 0 or self.rect.bottom > height or self.rect.top < 0:
            self.kill()
        

class Particle(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-2, 2)

    def update(self):
        self.rect.centery += self.speedy
        self.rect.centerx += self.speedx
        if self.rect.right > width or self.rect.left < 0 or self.rect.bottom > height:
            self.kill()
        
class RobotSprite(pygame.sprite.Sprite):
    MAX_SPEED = 5
    VELOCITY = 0
    FRICTION_FACTOR = 0.25
    JUMP = 30
    BASE = [width, height]
    speed =  0
    k_left = k_right = k_jump = 0
    level = None
    max_stam = 200
    stam = max_stam
    stam_change = 0.5
    cooldown = True
    shooting = False
    target = (0, 0)

    def __init__(self, position):
        super().__init__()
        self.list_image = [pygame.image.load('robot character front.png').convert_alpha(), pygame.image.load('robot character side.png').convert_alpha(), pygame.transform.flip(pygame.image.load('robot character side.png').convert_alpha(), True, False)]
        self.rect = self.list_image[0].get_rect()
        self.position = position

    def newBase(self):
        self.rect.y += 2
        collide = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        if collide:
            self.moving = False
            for i in collide:
                rect = i.rect
                if rect.bottom > self.rect.bottom and not rect.top < self.rect.top:
                    self.BASE[1] = rect.top
                else:
                    if self.rect.right > rect.right: self.rect.left = clip(self.rect.left, rect.right, self.BASE[0])
                    elif self.rect.left < rect.left: self.rect.right = clip(self.rect.right, 0, rect.left)
                    else:
                        self.rect.top = clip(self.rect.bottom, 0, rect.bottom)
                        self.VELOCITY = 0
        else: self.BASE[1] = height

    def jump(self):
        self.rect.y += 2
        hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        
        if len(hit_list) > 0:
            self.VELOCITY = self.k_jump
            if self.k_jump != 0: self.BASE[1] = height
        else: self.BASE[1] = height
        self.position = self.rect.center

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        x, y = self.rect
        position = x, y - 100
        screen.blit(self.image2, position)

    def move(self):
        self.speed += (self.k_right + self.k_left)
        if self.speed > self.FRICTION_FACTOR:
            self.speed -= self.FRICTION_FACTOR
            if not self.shooting: self.src_image = self.list_image[1]
        elif self.speed < -self.FRICTION_FACTOR:
            self.speed += self.FRICTION_FACTOR
            if not self.shooting: self.src_image = self.list_image[2]
        else:
            self.speed = 0
            if not self.shooting: self.src_image = self.list_image[0]
        
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        if self.speed < -self.MAX_SPEED:
            self.speed = -self.MAX_SPEED
        x, y = self.position
        x += -self.speed
        y -= self.VELOCITY
        if self.VELOCITY > -self.JUMP: self.VELOCITY += gravity
        else: self.VELOCITY = -self.JUMP
        self.position = (x, y)
        self.image = self.src_image
        self.rect = self.image.get_rect()        
        self.rect.center = self.position
        self.newBase()
        self.rect.left = clip(self.rect.left, 0, self.BASE[0])
        self.rect.right = clip(self.rect.right, 0, self.BASE[0])
        self.rect.top = clip(self.rect.top, 0, self.BASE[1])
        self.rect.bottom = clip(self.rect.bottom, 0, self.BASE[1])
        self.jump()

    def update(self):
        self.stam += self.stam_change
        if self.stam < 1:
            self.stam = 1
            self.cooldown = False
        elif self.stam > self.max_stam: self.stam = self.max_stam
        if self.stam > 20: self.cooldown = True
        if not self.cooldown: self.MAX_SPEED = 5
        self.move()

# Environment

class PlatSprite(pygame.sprite.Sprite):

    def __init__(self, image, position, active_group, moving = False, speed = 2.5):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = speed
        self.moving = moving
        self.moverange = [self.rect.center[1] - 100, self.rect.center[1] + 100]
        self.active_group = active_group

    def update(self):

        if self.moving:
            if self.rect.centery < self.moverange[0] or self.rect.centery > self.moverange[1]: self.speed *= -1
            self.rect.centery += self.speed
            
        collide = pygame.sprite.spritecollideany(self, self.active_group)
        if type(collide) is Bullet: collide.kill()

class Star(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load('star.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed = 1
        self.moverange = [self.rect.y - 30, self.rect.y + 30]

    def update(self):
        if self.rect.centery < self.moverange[0] or self.rect.centery > self.moverange[1]: self.speed *= -1
        self.rect.centery += self.speed

#Button

class Button():
    def __init__(self, text, position):
        self.image_list = ['Button_Black.png', 'Button_Ferozi.png']
        self.image = pygame.image.load(self.image_list[0])
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.selected = False
        self.surf = menu_font.render(text, True, WHITE)
        
    def update(self):
        if self.selected: self.image = pygame.image.load(self.image_list[1])
        else: self.image = pygame.image.load(self.image_list[0])
        

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)
        screen.blit(self.surf, (self.rect.x + 400, self.rect.y + 100))
        
        
