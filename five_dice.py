import random
import gamebox
import pygame
import os


camera = gamebox.Camera(800, 600)

game_state = 'start_screen'

hands = gamebox.from_image(400, 500, 'https://i.kym-cdn.com/photos/images/original/001/583/323/9cb.png')
hands.scale_by(0.4)
hands.rotate(180)

dice_1 = random.randrange(1, 7)
dice_2 = random.randrange(1, 7)
dice_3 = random.randrange(1, 7)
dice_4 = random.randrange(1, 7)
dice_5 = random.randrange(1, 7)

dice_1_state = 'none'
dice_2_state = 'none'
dice_3_state = 'none'
dice_4_state = 'none'
dice_5_state = 'none'

dice_1_score = 0
dice_2_score = 0
dice_3_score = 0
dice_4_score = 0
dice_5_score = 0

die_number_1 = gamebox.from_text(400, 210, '1', 24, 'white')
die_number_2 = gamebox.from_text(300, 210, '2', 24, 'white')
die_number_3 = gamebox.from_text(500, 210, '3', 24, 'white')
die_number_4 = gamebox.from_text(350, 310, '4', 24, 'white')
die_number_5 = gamebox.from_text(450, 310, '5', 24, 'white')
die_numbers = [die_number_1, die_number_2, die_number_3, die_number_4, die_number_5]

# Dice 1
outline1 = gamebox.from_color(400, 225, 'black', 50, 5)
outline2 = gamebox.from_color(400, 275, 'black', 50, 5)
outline3 = gamebox.from_color(375, 250, 'black', 5, 50)
outline4 = gamebox.from_color(425, 250, 'black', 5, 50)
space1 = gamebox.from_color(400, 250, 'white', 45, 45)
# Dice 2
outline5 = gamebox.from_color(300, 225, 'black', 50, 5)
outline6 = gamebox.from_color(300, 275, 'black', 50, 5)
outline7 = gamebox.from_color(275, 250, 'black', 5, 50)
outline8 = gamebox.from_color(325, 250, 'black', 5, 50)
space2 = gamebox.from_color(300, 250, 'white', 45, 45)
# Dice 3
outline9 = gamebox.from_color(500, 225, 'black', 50, 5)
outline10 = gamebox.from_color(500, 275, 'black', 50, 5)
outline11 = gamebox.from_color(475, 250, 'black', 5, 50)
outline12 = gamebox.from_color(525, 250, 'black', 5, 50)
space3 = gamebox.from_color(500, 250, 'white', 45, 45)
# Dice 4
outline13 = gamebox.from_color(350, 325, 'black', 50, 5)
outline14 = gamebox.from_color(350, 375, 'black', 50, 5)
outline15 = gamebox.from_color(375, 350, 'black', 5, 50)
outline16 = gamebox.from_color(325, 350, 'black', 5, 50)
space4 = gamebox.from_color(350, 350, 'white', 45, 45)
# Dice 5
outline17 = gamebox.from_color(450, 325, 'black', 50, 5)
outline18 = gamebox.from_color(450, 375, 'black', 50, 5)
outline19 = gamebox.from_color(425, 350, 'black', 5, 50)
outline20 = gamebox.from_color(475, 350, 'black', 5, 50)
space5 = gamebox.from_color(450, 350, 'white', 45, 45)


outlines = [outline1, outline2, outline3, outline4, outline5, outline6, outline7, outline8, outline9, outline10,
            outline11, outline12, outline13, outline14, outline15, outline16, outline17, outline18, outline19,
            outline20]

outlines_yellow1 = gamebox.from_color(400, 250, 'yellow', 45, 45)
outlines_yellow2 = gamebox.from_color(300, 250, 'yellow', 45, 45)
outlines_yellow3 = gamebox.from_color(500, 250, 'yellow', 45, 45)
outlines_yellow4 = gamebox.from_color(350, 350, 'yellow', 45, 45)
outlines_yellow5 = gamebox.from_color(450, 350, 'yellow', 45, 45)

start_screen = gamebox.from_text(400, 175, 'Press space bar to begin', 32, 'white')
instructions = gamebox.from_text(400, 70, 'Click to roll die', 32, 'white')
instructions_2 = gamebox.from_text(400, 70, 'Choose at least one die to keep', 32, 'white')
instructions_2_1 = gamebox.from_text(400, 120, 'Press the number(s) for which die to keep', 32, 'white')
instructions_2_2 = gamebox.from_text(400, 170, 'Press the space bar to continue', 32, 'white')

roll_tri = 0

total_score = 0

high_scores_list = []
average_total = 0
average_list = []
f = open('high_scores.txt')
for line in f:
    dingy = line.strip('\n')
    dingy = int(dingy)
    high_scores_list.append(dingy)
    average_total += dingy
    average_list.append(dingy)
high_scores_list.sort()
if len(high_scores_list) >= 10:
    high_score_1 = gamebox.from_text(400, 300, '1. ' + str(high_scores_list[0]), 24, 'white')
    high_score_2 = gamebox.from_text(400, 325, '2. ' + str(high_scores_list[1]), 24, 'white')
    high_score_3 = gamebox.from_text(400, 350, '3. ' + str(high_scores_list[2]), 24, 'white')
    high_score_4 = gamebox.from_text(400, 375, '4. ' + str(high_scores_list[3]), 24, 'white')
    high_score_5 = gamebox.from_text(400, 400, '5. ' + str(high_scores_list[4]), 24, 'white')
    high_score_6 = gamebox.from_text(400, 425, '5. ' + str(high_scores_list[5]), 24, 'white')
    high_score_7 = gamebox.from_text(400, 450, '5. ' + str(high_scores_list[6]), 24, 'white')
    high_score_8 = gamebox.from_text(400, 475, '5. ' + str(high_scores_list[7]), 24, 'white')
    high_score_9 = gamebox.from_text(400, 500, '5. ' + str(high_scores_list[8]), 24, 'white')
    high_score_10 = gamebox.from_text(400, 525, '5. ' + str(high_scores_list[9]), 24, 'white')
    high_scores = [high_score_1, high_score_2, high_score_3, high_score_4, high_score_5, high_score_6, high_score_7,
                   high_score_8, high_score_9, high_score_10]
average = average_total / len(average_list)
average = str(average)
average = average[:5]
average_display = gamebox.from_text(100, 50, 'Average score: ' + average, 24, 'white')


def roll():
    global dice_1, dice_2, dice_3, dice_4, dice_5
    if dice_1_state != 'done':
        dice_1 = random.randrange(1, 7)
    if dice_2_state != 'done':
        dice_2 = random.randrange(1, 7)
    if dice_3_state != 'done':
        dice_3 = random.randrange(1, 7)
    if dice_4_state != 'done':
        dice_4 = random.randrange(1, 7)
    if dice_5_state != 'done':
        dice_5 = random.randrange(1, 7)


def space_color():
    if dice_1_state != 'done':
        camera.draw(space1)
    if dice_1_state == 'done':
        camera.draw(outlines_yellow1)
    if dice_2_state != 'done':
        camera.draw(space2)
    if dice_2_state == 'done':
        camera.draw(outlines_yellow2)
    if dice_3_state != 'done':
        camera.draw(space3)
    if dice_3_state == 'done':
        camera.draw(outlines_yellow3)
    if dice_4_state != 'done':
        camera.draw(space4)
    if dice_4_state == 'done':
        camera.draw(outlines_yellow4)
    if dice_5_state != 'done':
        camera.draw(space5)
    if dice_5_state == 'done':
        camera.draw(outlines_yellow5)


def tick(keys):
    global game_state, dice_1, dice_2, dice_3, dice_4, dice_5, roll_tri, total_score, dice_1_state, dice_2_state, \
        dice_3_state, dice_4_state, dice_5_state, dice_1_score, dice_2_score, dice_3_score, dice_4_score, dice_5_score
    camera.clear('green')
    camera.draw(average_display)
    roll_tri = pygame.mouse.get_pressed()
    if game_state == 'start_screen':
        camera.draw(start_screen)
        if len(high_scores_list) >= 10:
            for score in high_scores:
                camera.draw(score)
        if pygame.K_SPACE in keys:
            game_state = 'gametime'
    if game_state == 'gametime':
        for thing in outlines:
            camera.draw(thing)
        space_color()
        for number in die_numbers:
            camera.draw(number)
        camera.draw(hands)
        camera.draw(instructions)
        if roll_tri[0] == 1:
            roll()
            game_state = 'choose_die'
    if game_state == 'choose_die':
        for thing in outlines:
            camera.draw(thing)
        space_color()
        for number in die_numbers:
            camera.draw(number)
        camera.draw(hands)
        camera.draw(instructions_2)
        camera.draw(instructions_2_1)
        camera.draw(instructions_2_2)
        if pygame.K_1 in keys:
            dice_1_state = 'done'
        if pygame.K_2 in keys:
            dice_2_state = 'done'
        if pygame.K_3 in keys:
            dice_3_state = 'done'
        if pygame.K_4 in keys:
            dice_4_state = 'done'
        if pygame.K_5 in keys:
            dice_5_state = 'done'
        if pygame.K_SPACE in keys:
            game_state = 'gametime'
    if dice_1_state == 'done' and dice_2_state == 'done' and dice_3_state == 'done' and dice_4_state == 'done' and \
            dice_5_state == 'done':
        dice_1_score = dice_1
        dice_2_score = dice_2
        dice_3_score = dice_3
        dice_4_score = dice_4
        dice_5_score = dice_5
        if dice_1_score == 3:
            dice_1_score = 0
        if dice_2_score == 3:
            dice_2_score = 0
        if dice_3_score == 3:
            dice_3_score = 0
        if dice_4_score == 3:
            dice_4_score = 0
        if dice_5_score == 3:
            dice_5_score = 0
        game_state = 'game_finished'
    if game_state == 'game_finished':
        for thing in outlines:
            camera.draw(thing)
        space_color()
        total_score = dice_1_score + dice_2_score + dice_3_score + dice_4_score + dice_5_score
        camera.draw(gamebox.from_text(400, 75, 'Total Score: ' + str(total_score), 32, 'white'))

    if game_state != 'start_screen':
        if dice_1 == 1:
            camera.draw(gamebox.from_circle(400, 250, 'black', 5))
        if dice_1 == 2:
            camera.draw(gamebox.from_circle(390, 240, 'black', 5))
            camera.draw(gamebox.from_circle(410, 260, 'black', 5))
        if dice_1 == 3:
            camera.draw(gamebox.from_circle(400, 250, 'black', 5))
            camera.draw(gamebox.from_circle(390, 240, 'black', 5))
            camera.draw(gamebox.from_circle(410, 260, 'black', 5))
        if dice_1 == 4:
            camera.draw(gamebox.from_circle(390, 240, 'black', 5))
            camera.draw(gamebox.from_circle(410, 260, 'black', 5))
            camera.draw(gamebox.from_circle(390, 260, 'black', 5))
            camera.draw(gamebox.from_circle(410, 240, 'black', 5))
        if dice_1 == 5:
            camera.draw(gamebox.from_circle(400, 250, 'black', 5))
            camera.draw(gamebox.from_circle(390, 240, 'black', 5))
            camera.draw(gamebox.from_circle(410, 260, 'black', 5))
            camera.draw(gamebox.from_circle(390, 260, 'black', 5))
            camera.draw(gamebox.from_circle(410, 240, 'black', 5))
        if dice_1 == 6:
            camera.draw(gamebox.from_circle(410, 250, 'black', 5))
            camera.draw(gamebox.from_circle(390, 250, 'black', 5))
            camera.draw(gamebox.from_circle(390, 240, 'black', 5))
            camera.draw(gamebox.from_circle(410, 260, 'black', 5))
            camera.draw(gamebox.from_circle(390, 260, 'black', 5))
            camera.draw(gamebox.from_circle(410, 240, 'black', 5))
        if dice_2 == 1:
            camera.draw(gamebox.from_circle(300, 250, 'black', 5))
        if dice_2 == 2:
            camera.draw(gamebox.from_circle(290, 240, 'black', 5))
            camera.draw(gamebox.from_circle(310, 260, 'black', 5))
        if dice_2 == 3:
            camera.draw(gamebox.from_circle(300, 250, 'black', 5))
            camera.draw(gamebox.from_circle(290, 240, 'black', 5))
            camera.draw(gamebox.from_circle(310, 260, 'black', 5))
        if dice_2 == 4:
            camera.draw(gamebox.from_circle(290, 240, 'black', 5))
            camera.draw(gamebox.from_circle(310, 260, 'black', 5))
            camera.draw(gamebox.from_circle(290, 260, 'black', 5))
            camera.draw(gamebox.from_circle(310, 240, 'black', 5))
        if dice_2 == 5:
            camera.draw(gamebox.from_circle(300, 250, 'black', 5))
            camera.draw(gamebox.from_circle(290, 240, 'black', 5))
            camera.draw(gamebox.from_circle(310, 260, 'black', 5))
            camera.draw(gamebox.from_circle(290, 260, 'black', 5))
            camera.draw(gamebox.from_circle(310, 240, 'black', 5))
        if dice_2 == 6:
            camera.draw(gamebox.from_circle(290, 250, 'black', 5))
            camera.draw(gamebox.from_circle(310, 250, 'black', 5))
            camera.draw(gamebox.from_circle(290, 240, 'black', 5))
            camera.draw(gamebox.from_circle(310, 260, 'black', 5))
            camera.draw(gamebox.from_circle(290, 260, 'black', 5))
            camera.draw(gamebox.from_circle(310, 240, 'black', 5))
        if dice_3 == 1:
            camera.draw(gamebox.from_circle(500, 250, 'black', 5))
        if dice_3 == 2:
            camera.draw(gamebox.from_circle(490, 240, 'black', 5))
            camera.draw(gamebox.from_circle(510, 260, 'black', 5))
        if dice_3 == 3:
            camera.draw(gamebox.from_circle(500, 250, 'black', 5))
            camera.draw(gamebox.from_circle(490, 240, 'black', 5))
            camera.draw(gamebox.from_circle(510, 260, 'black', 5))
        if dice_3 == 4:
            camera.draw(gamebox.from_circle(490, 240, 'black', 5))
            camera.draw(gamebox.from_circle(510, 260, 'black', 5))
            camera.draw(gamebox.from_circle(490, 260, 'black', 5))
            camera.draw(gamebox.from_circle(510, 240, 'black', 5))
        if dice_3 == 5:
            camera.draw(gamebox.from_circle(500, 250, 'black', 5))
            camera.draw(gamebox.from_circle(490, 240, 'black', 5))
            camera.draw(gamebox.from_circle(510, 260, 'black', 5))
            camera.draw(gamebox.from_circle(490, 260, 'black', 5))
            camera.draw(gamebox.from_circle(510, 240, 'black', 5))
        if dice_3 == 6:
            camera.draw(gamebox.from_circle(510, 250, 'black', 5))
            camera.draw(gamebox.from_circle(490, 250, 'black', 5))
            camera.draw(gamebox.from_circle(490, 240, 'black', 5))
            camera.draw(gamebox.from_circle(510, 260, 'black', 5))
            camera.draw(gamebox.from_circle(490, 260, 'black', 5))
            camera.draw(gamebox.from_circle(510, 240, 'black', 5))
        if dice_4 == 1:
            camera.draw(gamebox.from_circle(350, 350, 'black', 5))
        if dice_4 == 2:
            camera.draw(gamebox.from_circle(340, 340, 'black', 5))
            camera.draw(gamebox.from_circle(360, 360, 'black', 5))
        if dice_4 == 3:
            camera.draw(gamebox.from_circle(350, 350, 'black', 5))
            camera.draw(gamebox.from_circle(340, 340, 'black', 5))
            camera.draw(gamebox.from_circle(360, 360, 'black', 5))
        if dice_4 == 4:
            camera.draw(gamebox.from_circle(340, 340, 'black', 5))
            camera.draw(gamebox.from_circle(360, 360, 'black', 5))
            camera.draw(gamebox.from_circle(340, 360, 'black', 5))
            camera.draw(gamebox.from_circle(360, 340, 'black', 5))
        if dice_4 == 5:
            camera.draw(gamebox.from_circle(350, 350, 'black', 5))
            camera.draw(gamebox.from_circle(340, 340, 'black', 5))
            camera.draw(gamebox.from_circle(360, 360, 'black', 5))
            camera.draw(gamebox.from_circle(340, 360, 'black', 5))
            camera.draw(gamebox.from_circle(360, 340, 'black', 5))
        if dice_4 == 6:
            camera.draw(gamebox.from_circle(340, 350, 'black', 5))
            camera.draw(gamebox.from_circle(360, 350, 'black', 5))
            camera.draw(gamebox.from_circle(340, 340, 'black', 5))
            camera.draw(gamebox.from_circle(360, 360, 'black', 5))
            camera.draw(gamebox.from_circle(340, 360, 'black', 5))
            camera.draw(gamebox.from_circle(360, 340, 'black', 5))
        if dice_5 == 1:
            camera.draw(gamebox.from_circle(450, 350, 'black', 5))
        if dice_5 == 2:
            camera.draw(gamebox.from_circle(440, 340, 'black', 5))
            camera.draw(gamebox.from_circle(460, 360, 'black', 5))
        if dice_5 == 3:
            camera.draw(gamebox.from_circle(450, 350, 'black', 5))
            camera.draw(gamebox.from_circle(440, 340, 'black', 5))
            camera.draw(gamebox.from_circle(460, 360, 'black', 5))
        if dice_5 == 4:
            camera.draw(gamebox.from_circle(440, 340, 'black', 5))
            camera.draw(gamebox.from_circle(460, 360, 'black', 5))
            camera.draw(gamebox.from_circle(440, 360, 'black', 5))
            camera.draw(gamebox.from_circle(460, 340, 'black', 5))
        if dice_5 == 5:
            camera.draw(gamebox.from_circle(450, 350, 'black', 5))
            camera.draw(gamebox.from_circle(440, 340, 'black', 5))
            camera.draw(gamebox.from_circle(460, 360, 'black', 5))
            camera.draw(gamebox.from_circle(440, 360, 'black', 5))
            camera.draw(gamebox.from_circle(460, 340, 'black', 5))
        if dice_5 == 6:
            camera.draw(gamebox.from_circle(440, 350, 'black', 5))
            camera.draw(gamebox.from_circle(460, 350, 'black', 5))
            camera.draw(gamebox.from_circle(440, 340, 'black', 5))
            camera.draw(gamebox.from_circle(460, 360, 'black', 5))
            camera.draw(gamebox.from_circle(440, 360, 'black', 5))
            camera.draw(gamebox.from_circle(460, 340, 'black', 5))

    camera.display()


gamebox.timer_loop(30, tick)

if os.path.exists('high_scores.txt'):
    with open('high_scores.txt', 'a') as fstream:
        print(total_score, file=fstream)
if not os.path.exists('high_scores.txt'):
    with open('high_scores.txt', 'w') as fstream:
        print(total_score, file=fstream)
