import pygame as pg
import sys
import random

pg.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (235, 28, 36)
max_heart = 5
start_heart = 3
now_heart = 3
score = 0

sc = pg.display.set_mode((1540, 800))

first = True
start = False
settings = False
about = False
close = False
save = False
end_level = False
choice = True
guessed_letters = []
screen_word = ''
secret_word = ''
user_letters = []
line = list('QWERTYUIOPASDFGHJKLZXCVBNM')

CHILLER = 'data/CHILLER.ttf'
words = 'data/words.txt'
screen_start = pg.image.load('data/first.png')
play = pg.image.load('data/play.png')
next_pic = pg.image.load('data/next.png')
next_pic.set_colorkey(white)
exit_pic = pg.image.load('data/exit.png')
exit_pic.set_colorkey(white)
new_game = pg.image.load('data/new_game.png')
new_game.set_colorkey(white)
red_heart = pg.image.load('data/red_heart.png')
red_heart.set_colorkey(white)
grey_heart = pg.image.load('data/grey_heart.png')
grey_heart.set_colorkey(white)
metal = pg.image.load('data/metal.jpg')
left_arrow = pg.image.load('data/left_arrow.png')
left_arrow.set_colorkey(white)
right_arrow = pg.image.load('data/right_arrow.png')
right_arrow.set_colorkey(white)
sure_settings = pg.image.load('data/sure_settings.png')
sure_exit = pg.image.load('data/sure_exit.png')
about_pic = pg.image.load('data/about.png')

while True:
    while first:
        sc.blit(screen_start, (0, 0))
        pg.display.update()
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                pos = pg.mouse.get_pos()

                if 114 <= pos[0] <= 534:

                    if 120 <= pos[1] <= 274:
                        start = True

                    elif 459 <= pos[1] <= 615:
                        about = True

                    elif 627 <= pos[1] <= 782:
                        close = True
                    first = False

                elif 44 <= pos[0] <= 590 and 286 <= pos[1] <= 447:
                    settings = True
                    first = False

        pg.time.wait(10)

    if start:
        def new_word():
            guessed_ls = []
            user_ls = []
            word = random.choice(open(words, 'r').readline().split()).upper()
            screen = list("_" * len(word))
            return guessed_ls, word, screen, user_ls


        def update_new_letter(screen):
            sc.blit(play, (0, 0))
            sc.blit(pg.font.Font(CHILLER, 90).render(secret_word, True, black), (0, 0))
            d_x = 65
            s_x = 1095 - len(secret_word) * d_x / 2
            s_y = 300
            for e in range(0, len(secret_word)):
                sc.blit(pg.font.Font(CHILLER, 100).render(screen[e], True, white), (s_x + d_x * e, s_y))


        def keyboard(user_ls):
            d_x = 89.5
            d_y = 125
            for f in range(0, 26):
                s_x = 661
                s_y = 425
                if f <= 9:
                    if line[f] in user_ls:
                        sc.blit(pg.font.Font(CHILLER, 90).render(line[f], True, red), (s_x + d_x * f, s_y))
                    else:
                        sc.blit(pg.font.Font(CHILLER, 90).render(line[f], True, white), (s_x + d_x * f, s_y))
                elif 10 <= f <= 18:
                    s_x += d_x / 2
                    s_y += d_y
                    if line[f] in user_ls:
                        sc.blit(pg.font.Font(CHILLER, 90).render(line[f], True, red), (s_x + d_x * (f - 10), s_y))
                    else:
                        sc.blit(pg.font.Font(CHILLER, 90).render(line[f], True, white), (s_x + d_x * (f - 10), s_y))
                else:
                    s_x += 1.5 * d_x
                    s_y += d_y * 2
                    if line[f] in user_ls:
                        sc.blit(pg.font.Font(CHILLER, 90).render(line[f], True, red), (s_x + d_x * (f - 19), s_y))
                    else:
                        sc.blit(pg.font.Font(CHILLER, 90).render(line[f], True, white), (s_x + d_x * (f - 19), s_y))


        def hearts():
            d_x = 70
            s_x = 1520 - start_heart * d_x
            s_y = 20
            for g in range(0, start_heart):
                if g < start_heart - now_heart:
                    sc.blit(grey_heart, (s_x + d_x * g, s_y))
                else:
                    sc.blit(red_heart, (s_x + d_x * g, s_y))


        def print_score():
            screen_score = "SCORE:" + str(round(score))
            sc.blit(pg.font.Font(CHILLER, 90).render(screen_score, True, white), (665, 5))


        def new_level(sc_word):
            update_new_letter(sc_word)
            keyboard(user_letters)
            hearts()
            print_score()


        def end_g(indexes, lst_screen_word):
            sc.blit(metal, (0, 0))
            screen_score = "SCORE:" + "  " + str(round(score))
            sc.blit(pg.font.Font(CHILLER, 90).render(screen_score, True, white), (30, 200))

            d_x = 45
            s_x = 500
            s_y = 300
            for h in range(0, len(secret_word)):
                if h in indexes:
                    sc.blit(pg.font.Font(CHILLER, 100).render(lst_screen_word[h], True, white), (s_x + d_x * h, s_y))
                else:
                    sc.blit(pg.font.Font(CHILLER, 100).render(lst_screen_word[h], True, red), (s_x + d_x * h, s_y))

            sc.blit(pg.font.Font(CHILLER, 90).render('EXECUTIONER:', True, white), (30, 300))
            sc.blit(exit_pic, (162, 490))
            sc.blit(new_game, (10, 640))
            pg.display.update()
            pg.time.wait(15)


        def animation():
            r_line = ''
            indexes = []
            lst_line = list(line)
            lst_screen_word = list(screen_word)
            for i in range(0, 26):
                num = random.randint(0, len(lst_line) - 1)
                r_line += lst_line[num]
                lst_line.pop(num)
            for i in range(0, len(screen_word)):
                if screen_word[i] != "_":
                    indexes.append(i)
            for i in range(0, len(screen_word)):
                if screen_word[i] == "_":
                    b = True
                    for a in range(0, 26):
                        if b:
                            lst_screen_word.pop(i)
                            lst_screen_word.insert(i, line[a])
                            end_g(indexes, lst_screen_word)
                            if lst_screen_word[i] == secret_word[i]:
                                b = False
            return False


        if not save:
            save = False
            animation_end = True
            guessed_letters, secret_word, screen_word, user_letters = new_word()
            now_heart = 0 + start_heart
        new_level(screen_word)
        pg.display.update()

        while start:
            for i in pg.event.get():
                if now_heart == 0:
                    end_game = True
                else:
                    end_game = False

                    if len(guessed_letters) == len(secret_word):
                        end_level = True
                    else:
                        end_level = False

                if i.type == pg.QUIT:
                    sys.exit()
                elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                    pos = pg.mouse.get_pos()
                    if 0 <= pos[0] <= 72 and 0 <= pos[1] <= 56:
                        save = True
                        first = True
                        start = False
                elif i.type == pg.KEYDOWN:
                    if i.key == pg.K_ESCAPE:
                        first = True
                        start = False
                        save = True

                    elif 97 <= i.key <= 122 and not end_level and not end_game:
                        letter = chr(i.key).upper()
                        if letter not in user_letters:
                            user_letters.append(letter)

                            minus_heart = True
                            for a in range(0, len(secret_word)):

                                if secret_word[a] == letter and a not in guessed_letters:
                                    minus_heart = False
                                    guessed_letters.append(a)

                                    if len(guessed_letters) == len(secret_word):
                                        end_level = True
                                    else:
                                        end_level = False

                                    for a in range(0, len(guessed_letters)):
                                        screen_word.pop(guessed_letters[a])
                                        screen_word.insert(guessed_letters[a], secret_word[guessed_letters[a]])

                                    update_new_letter(screen_word)

                            if minus_heart:
                                now_heart -= 1
                                if now_heart == 0:
                                    end_game = True
                                else:
                                    end_game = False
                            else:
                                score += (12 * now_heart) / (start_heart * (start_heart + 1))

                            hearts()
                            print_score()

                        keyboard(user_letters)

                if end_level:
                    animation_end = True
                    sc.blit(next_pic, (145, 450))
                    sc.blit(exit_pic, (145, 600))
                    if i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                        pos = pg.mouse.get_pos()
                        if 145 <= pos[0] <= 497 and 600 <= pos[1] <= 742:
                            first = True
                            start = False
                        elif 145 <= pos[0] <= 497 and 450 <= pos[1] <= 592:
                            guessed_letters, secret_word, screen_word, user_letters = new_word()
                            new_level(screen_word)

                    elif i.type == pg.KEYDOWN:
                        if i.key == pg.K_ESCAPE:
                            first = True
                            start = False
                        elif i.key == pg.K_SPACE:
                            guessed_letters, secret_word, screen_word, user_letters = new_word()
                            new_level(screen_word)

                if end_game:
                    save = False
                    if animation_end:
                        animation_end = animation()
                    if i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                        pos = pg.mouse.get_pos()
                        if 162 <= pos[0] <= 509 and 490 <= pos[1] <= 632:
                            score = 0
                            now_heart += start_heart
                            first = True
                            start = False
                        elif 10 <= pos[0] <= 672 and 640 <= pos[1] <= 782:
                            animation_end = True
                            score = 0
                            now_heart = 0 + start_heart
                            guessed_letters, secret_word, screen_word, user_letters = new_word()
                            new_level(screen_word)

                    elif i.type == pg.KEYDOWN:
                        if i.key == pg.K_ESCAPE:
                            score = 0
                            now_heart += start_heart
                            first = True
                            start = False
                        elif i.key == pg.K_SPACE:
                            score = 0
                            now_heart += start_heart
                            guessed_letters, secret_word, screen_word, user_letters = new_word()
                            new_level(screen_word)

                pg.display.update()

            pg.time.wait(10)

    elif settings and ((not save) or (len(user_letters) == 0 and score == 0)):
        save = False


        def new_heart_settings():
            d_x = 70
            s_x = 910
            s_y = 350
            sc.blit(play, (0, 0))

            for k in range(0, max_heart):
                if k < max_heart - start_heart:
                    sc.blit(grey_heart, (s_x + d_x * k, s_y))
                else:
                    sc.blit(red_heart, (s_x + d_x * k, s_y))

            if start_heart != max_heart:
                sc.blit(left_arrow, (846, 347))
            if start_heart != 1:
                sc.blit(right_arrow, (1265, 347))


        sc.blit(play, (0, 0))
        new_heart_settings()
        pg.display.update()

        while settings:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                    pos = pg.mouse.get_pos()
                    if 0 <= pos[0] <= 72 and 0 <= pos[1] <= 56:
                        settings = False
                        first = True
                    elif 910 <= pos[0] <= 1256 and 350 <= pos[1] <= 410:
                        start_heart = max_heart - (pos[0] - 910) // 70
                        sc.blit(pg.font.Font(CHILLER, 90).render(str(start_heart), True, white), (pos[0], pos[1]))
                    elif 846 <= pos[0] <= 901 and 347 <= pos[1] <= 411 and start_heart != max_heart:
                        start_heart += 1
                    elif 1256 <= pos[0] <= 1311 and 347 <= pos[1] <= 411 and start_heart != 1:
                        start_heart -= 1
                    now_heart = 0 + start_heart
                    new_heart_settings()

                pg.display.update()

            pg.time.wait(10)

    elif settings and save:
        sc.blit(sure_settings, (0, 0))
        pg.display.update()

        while settings and save:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                    pos = pg.mouse.get_pos()
                    if 692 <= pos[0] <= 1037 and 498 <= pos[1] <= 637:
                        first = True
                        settings = False
                    elif 1100 <= pos[0] <= 1445 and 498 <= pos[1] <= 637:
                        settings = True
                        save = False
                        score = 0

            pg.time.wait(10)

    elif about:
        sc.blit(about_pic, (0, 0))
        pg.display.update()

        while about:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                    pos = pg.mouse.get_pos()
                    if 0 <= pos[0] <= 68 and 0 <= pos[1] <= 57:
                        about = False
                        first = True

            pg.time.wait(10)

    elif close:
        sc.blit(sure_exit, (0, 0))
        pg.display.update()
        while close:
            for m in pg.event.get():
                if m.type == pg.QUIT:
                    sys.exit()
                elif m.type == pg.MOUSEBUTTONDOWN and m.button == 1:
                    pos = pg.mouse.get_pos()
                    if 1111 <= pos[0] <= 1457 and 477 <= pos[1] <= 617:
                        sys.exit()
                    elif 704 <= pos[0] <= 1050 and 477 <= pos[1] <= 617:
                        close = False
                        first = True

            pg.time.wait(10)
