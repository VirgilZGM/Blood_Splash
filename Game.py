monster_x = 50
monster_y = 50
monster1_x = 100
monster1_y = 100
monster2_x = 900
monster2_y = 50
monster3_x = 25
monster3_y = 50
monster4_x = 1
monster4_y = 500
monster5_x = 900
monster5_y = 400


monster_speed_x = 2
monster_speed_y = 1
monster1_speed_x = 3
monster1_speed_y = 4
monster2_speed_x = 5
monster2_speed_y = 6
monster3_speed_x = 7
monster3_speed_y = 6
monster4_speed_x = 9
monster4_speed_y = 10
monster5_speed_x = 12
monster5_speed_y = 11


mouse_x = 400
mouse_y = 300
mState = 0

import pygame
import random

pygame.init()

font = pygame.font.Font("D:\\pythonProject\\.venv\\type.ttf", 50)

scr = pygame.display.set_mode((960,540))
pygame.display.set_caption("嘿嘿嘿")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
fps = 30
number = 0

# 创建怪物精灵组


frames1 = []
for i in range(9):
    image = pygame.image.load(f"D:\\pythonProject\\.venv\\monster\\Monster{i+1}.png")
    frames1.append(image)

frames2 = []
for i in range(4):
    blood = pygame.image.load(f"D:\\pythonProject\\.venv\\blood\\blood{i}.png")
    frames2.append(blood)

bg = pygame.image.load('D:\\pythonProject\\.venv\\Image\\bg.png')
gunsight = pygame.image.load('D:\\pythonProject\\.venv\\Image\\gunsight.png')
score = pygame.image.load('D:\\pythonProject\\.venv\\Image\\ScoreBoard.png')


running = True
index1 = 0
index2 = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouse_x,mouse_y = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_x > monster_x and mouse_x < monster_x + 50:
                if mouse_y > monster_y and mouse_y < monster_y + 50:
                    mState = 1
                    number += 1
            if mouse_x > monster1_x and mouse_x < monster1_x + 50:
                if mouse_y > monster1_y and mouse_y < monster1_y + 50:
                    mState = 2
                    number += 1
            if mouse_x > monster2_x and mouse_x < monster2_x + 50:
                if mouse_y > monster2_y and mouse_y < monster2_y + 50:
                    mState = 3
                    number += 1
            if mouse_x > monster3_x and mouse_x < monster3_x + 50:
                if mouse_y > monster3_y and mouse_y < monster3_y + 50:
                    mState = 4
                    number += 1
            if mouse_x > monster4_x and mouse_x < monster4_x + 50:
                if mouse_y > monster4_y and mouse_y < monster4_y + 50:
                    mState = 5
                    number += 1
            if mouse_x > monster5_x and mouse_x < monster5_x + 50:
                if mouse_y > monster5_y and mouse_y < monster5_y + 50:
                    mState = 6
                    number += 1

    scr.blit(bg, (0, 0))
    scr.blit(score, (0, 0))
    font_surface = font.render(str(number), True, (255, 255, 255))
    scr.blit(font_surface,(50,40))

    if mState == 0:
        clock.tick(fps)
        monster_x = monster_x + monster_speed_x
        monster_y = monster_y + monster_speed_y

        if monster_x > 960 or monster_x < 0:
            monster_speed_x = -monster_speed_x
        if monster_y > 540 or monster_y < 0:
            monster_speed_y = -monster_speed_y

        scr.blit(frames1[index1], (monster_x, monster_y))

        if index1 < 8:
            index1 += 1
        else:
            index1 = 0

        scr.blit(gunsight,[mouse_x-25,mouse_y-25])
        font_surface = font.render(str(number), True, (255, 255, 255))
        scr.blit(font_surface, (50, 40))
        pygame.display.update()  # 刷新窗口

    if mState == 1:
        clock.tick(fps)
        monster1_x = monster1_x + monster1_speed_x
        monster1_y = monster1_y + monster1_speed_y

        if monster1_x > 960 or monster1_x < 0:
            monster1_speed_x = -monster1_speed_x
        if monster1_y > 540 or monster1_y < 0:
            monster1_speed_y = -monster1_speed_y

        if index1 < 8:
            index1 += 1
        else:
            index1 = 0

        scr.blit(bg, (0, 0))
        scr.blit(frames2[index2], (monster_x, monster_y))

        if index2 < 3:
            index2 += 1

        scr.blit(frames1[index1], (monster1_x, monster1_y))

        scr.blit(score, (0, 0))
        scr.blit(gunsight, [mouse_x - 25, mouse_y - 25])

        font_surface = font.render(str(number), True, (255, 255, 255))
        scr.blit(font_surface, (50, 40))
        pygame.display.update()

    if mState == 2:
        clock.tick(fps)
        monster2_x = monster2_x + monster2_speed_x
        monster2_y = monster2_y + monster2_speed_y

        if monster2_x > 960 or monster2_x < 0:
            monster2_speed_x = -monster2_speed_x
        if monster2_y > 540 or monster2_y < 0:
            monster2_speed_y = -monster2_speed_y

        if index1 < 8:
            index1 += 1
        else:
            index1 = 0

        scr.blit(bg, (0, 0))
        scr.blit(frames2[index2], (monster1_x, monster1_y))

        if index2 < 3:
            index2 += 1

        scr.blit(frames1[index1], (monster2_x, monster2_y))
        scr.blit(score, (0, 0))
        scr.blit(gunsight, [mouse_x - 25, mouse_y - 25])

        font_surface = font.render(str(number), True, (255, 255, 255))
        scr.blit(font_surface, (50, 40))
        pygame.display.update()

    if mState == 3:
        clock.tick(fps)
        monster3_x = monster3_x + monster3_speed_x
        monster3_y = monster3_y + monster3_speed_y

        if monster3_x > 960 or monster3_x < 0:
            monster3_speed_x = -monster3_speed_x
        if monster3_y > 540 or monster3_y < 0:
            monster3_speed_y = -monster3_speed_y

        if index1 < 8:
            index1 += 1
        else:
            index1 = 0

        scr.blit(bg, (0, 0))
        scr.blit(frames2[index2], (monster2_x, monster2_y))

        if index2 < 3:
            index2 += 1

        scr.blit(frames1[index1], (monster3_x, monster3_y))
        scr.blit(score, (0, 0))
        scr.blit(gunsight, [mouse_x - 25, mouse_y - 25])

        font_surface = font.render(str(number), True, (255, 255, 255))
        scr.blit(font_surface, (50, 40))
        pygame.display.update()
    if mState == 4:
        clock.tick(fps)
        monster4_x = monster4_x + monster4_speed_x
        monster4_y = monster4_y + monster4_speed_y

        if monster4_x > 960 or monster4_x < 0:
            monster4_speed_x = -monster4_speed_x
        if monster4_y > 540 or monster4_y < 0:
            monster4_speed_y = -monster4_speed_y

        if index1 < 8:
            index1 += 1
        else:
            index1 = 0

        scr.blit(bg, (0, 0))
        scr.blit(frames2[index2], (monster3_x, monster3_y))

        if index2 < 3:
            index2 += 1

        scr.blit(frames1[index1], (monster4_x, monster4_y))
        scr.blit(score, (0, 0))
        scr.blit(gunsight, [mouse_x - 25, mouse_y - 25])

        font_surface = font.render(str(number), True, (255, 255, 255))
        scr.blit(font_surface, (50, 40))
        pygame.display.update()
    if mState == 5:
        clock.tick(fps)
        monster5_x = monster5_x + monster5_speed_x
        monster5_y = monster5_y + monster5_speed_y

        if monster5_x > 960 or monster5_x < 0:
            monster5_speed_x = -monster5_speed_x
        if monster5_y > 540 or monster5_y < 0:
            monster5_speed_y = -monster5_speed_y

        if index1 < 8:
            index1 += 1
        else:
            index1 = 0

        scr.blit(bg, (0, 0))
        scr.blit(frames2[index2], (monster4_x, monster4_y))

        if index2 < 3:
            index2 += 1

        scr.blit(frames1[index1], (monster5_x, monster5_y))
        scr.blit(score, (0, 0))
        scr.blit(gunsight, [mouse_x - 25, mouse_y - 25])

        font_surface = font.render(str(number), True, (255, 255, 255))
        scr.blit(font_surface, (50, 40))
        pygame.display.update()
    if mState == 6:
        clock.tick(fps)

        scr.blit(bg, (0, 0))

        if index2 < 3:
            index2 += 1

        win = font.render("YOU WIN!", True, (255, 255, 255))
        text_x = (scr.get_width() - win.get_width()) // 2
        text_y = (scr.get_height() - win.get_height()) // 2
        scr.blit(frames2[index2], (monster5_x, monster5_y))
        scr.blit(score, (0, 0))
        font_surface = font.render(str(number), True, (255, 255, 255))
        scr.blit(font_surface, (50, 40))
        scr.blit(win, (text_x, text_y))
        pygame.display.update()

pygame.quit()
