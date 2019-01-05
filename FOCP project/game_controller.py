# INITIALISATION
import pygame, sys, os
sys.path.append('D:\Dropbox\Python Projects\FOCP project')
from game_global import *
from sprites import *
from levels import *
from pygame.locals import *
pygame.init()

def main_menu():
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    button1 = Button('Start', (width/2 - 250, height/2 - 200))
    button2 = Button('Exit', (width/2 - 250, height/2))
    button_list = [button1, button2]
    x = 0
    current_selection = button_list[x]
    background = pygame.image.load('Hexagonal_Wallpaper.png')
    background_rect = background.get_rect()
    scroll_range = [0, background_rect.right]
    scroll_speed = 1
    current_x = 0
    particle_group = pygame.sprite.Group()

    done = True

    while done:
        # USER INPUT
        for event in pygame.event.get():
            if event.type == PARTICLESPAWN:
                particle = Particle('particle_ferozi_temp.png')
                particle.rect.centery = random.randint(0, 10)
                particle.rect.centerx = random.randint(5, width - 5)
                particle_group.add(particle)                
            
            if not hasattr(event, 'key'): continue
            down = event.type == KEYDOWN
            if event.key == K_UP: x += 1 * down
            if event.key == K_DOWN: x -= 1 * down
            if event.key == K_RETURN:
                if current_selection is button1: main()
                if current_selection is button2: done = False

            if x < 0: x = len(button_list) + x
            if x >= len(button_list): x = x - len(button_list)
            current_selection = button_list[x]


        # RENDERING
        # If the player gets to the end of the level, go to the next level
        for i in button_list:
            if i is current_selection: i.selected = True
            else: i.selected = False

        screen.blit(background, (current_x, 0))
        current_x -= scroll_speed
        if current_x < width - background_rect.right: current_x = 0

        particle_group.update()
        particle_group.draw(screen)
        for i in button_list:
            i.update()
            i.draw(screen)
        clock.tick(FPS)
        pygame.display.flip()

def main():
    # CREATE THE PLAYER
    rect = screen.get_rect()
    x, y = rect.center
    start_point = (x, height - height/8)
    player = RobotSprite(start_point)
    wheel = WheelSprite(player)
    gun = Gun(player)
    crosshair = pygame.image.load('crosshair_blue.png').convert_alpha()
    active_group = pygame.sprite.RenderPlain(player, wheel, gun)

    time = 0

    # CREATE THE LEVELS

    level_list = []
    level_list.append(Level_01(player, active_group))
    level_list.append(Level_02(player, active_group))
    level_list.append(Level_03(player, active_group))
    level_list.append(Level_04(player, active_group))
    level_list.append(Level_05(player, active_group))
    level_list.append(Level_06(player, active_group))
    level_list.append(Level_07(player, active_group))
    level_list.append(Level_08(player, active_group))
    level_list.append(Level_09(player, active_group))
    level_list.append(Level_10(player, active_group))
    level_list.append(Level_11(player, active_group))
    level_list.append(Level_12(player, active_group))
    level_list.append(Level_13(player, active_group))
    level_list.append(Level_14(player, active_group))
    level_list.append(Level_15(player, active_group))
    level_list.append(Level_16(player, active_group))
    level_list.append(Level_17(player, active_group))
    level_list.append(Level_18(player, active_group))
    level_list.append(Level_19(player, active_group))
    level_list.append(Level_20(player, active_group))

    # SET THE CURRENT LEVEL

    current_level_no = 0
    current_level = level_list[current_level_no]
    temp_level = Level_Nightmare(player, active_group)

    player.level = current_level

    done = True
    restart = False
        
    while done:
        # USER INPUT
        for event in pygame.event.get():

            if event.type == PARTICLESPAWN:
                particle = Particle('particle_ash.png')
                particle.rect.centery = random.randint(0, 10)
                particle.rect.centerx = random.randint(5, width - 5)
                active_group.add(particle)

            if event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:
                player.shooting = True
            if event.type == MOUSEBUTTONUP:
                player.shooting = False
            
            if not hasattr(event, 'key'): continue
            down = event.type == KEYDOWN
            
            if event.key == K_LSHIFT:
                player.MAX_SPEED = (down * 5) + 5
                player.stam_change = 1 - (down * 3)
            if event.key == K_LCTRL:
                player.MAX_SPEED = (down * 50) + 5
                player.speed *= 25
                player.stam_change = 1 - (down * 25)
            if event.key == K_d: player.k_right = down * -MOVE_SPEED
            elif event.key == K_a: player.k_left = down * MOVE_SPEED
            if event.key == K_ESCAPE: done = False
            if event.key == K_SPACE: player.k_jump = down * player.JUMP
            if event.key == K_TAB and event.type == KEYDOWN:
                current_level, temp_level = temp_level, current_level
                player.level = current_level
            if event.key == K_RETURN and restart: main()

        player.target = pygame.mouse.get_pos()


        if player.shooting:
            gun.delay += (pygame.time.get_ticks() - time)
            if gun.delay > 5000:
                active_group.add(Bullet(player))
                gun.delay = 0
                time = pygame.time.get_ticks()

        # RENDERING
        active_group.update()
        current_level.update()

        # If the player gets to the end of the level, go to the next level
        if current_level.complete:
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
            else:
                current_level = Level_End(player, active_group)
                restart = True
            player.level = current_level

        if player.rect.bottom == height:
            current_level = Level_Lose(player, active_group)
            player.level = current_level
            restart = True
        
        current_level.draw(screen)
        active_group.draw(screen)
        x, y = pygame.mouse.get_pos()
        screen.blit(crosshair, (x - 25, y - 25))
        clock.tick(FPS)
        pygame.display.flip()
        
main_menu()

pygame.quit()

