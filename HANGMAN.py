import pygame as pg
import sys
import random

pg.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (235, 28, 36)
max_heart = 7
start_heart = 6
now_heart = 0 + start_heart
score = 0
max_hints = 3
start_hints = 1
now_hints = 0 + start_hints

sc = pg.display.set_mode((1540, 800))

first = True
start = False
hint = False
settings = False
about = False
close = False
save = False
end_level = False
animation_end = True
choice = True
minus_hint = True

guessed_letters = []
screen_word = ''
secret_word = ''
user_letters = []
line = list('QWERTYUIOPASDFGHJKLZXCVBNM')
vowel = "AEIUO"

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
metal = pg.image.load('data/metal.png')
left_arrow = pg.image.load('data/left_arrow.png')
left_arrow.set_colorkey(white)
right_arrow = pg.image.load('data/right_arrow.png')
right_arrow.set_colorkey(white)
sure_settings = pg.image.load('data/sure_settings.png')
sure_exit = pg.image.load('data/sure_exit.png')
about_pic = pg.image.load('data/about.png')
bulb_pic = pg.image.load('data/bulb.png')
bulb_pic.set_colorkey(white)
hint_pic = pg.image.load('data/hint_screen.png')

while True:
    if first:
        sc.blit(screen_start, (0, 0))
        pg.display.update()
        while first:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1:
                    pos = pg.mouse.get_pos()
                    first = False

                    if 114 <= pos[0] <= 534 and 120 <= pos[1] <= 274:
                        start = True

                    elif 114 <= pos[0] <= 534 and 459 <= pos[1] <= 615:
                        about = True

                    elif 114 <= pos[0] <= 534 and 627 <= pos[1] <= 782:
                        close = True

                    elif 44 <= pos[0] <= 590 and 286 <= pos[1] <= 447:
                        settings = True

                    else:
                        first = True

            pg.time.wait(10)

    elif start:
        def new_word():
            guessed_ls = []
            user_ls = []
            word = random.choice(open(words, 'r').readline().split()).upper()
            screen = list("_" * len(word))
            return guessed_ls, word, screen, user_ls


        def update_new_letter(screen):
            sc.blit(play, (0, 0))
            #sc.blit(pg.font.Font(CHILLER, 90).render(secret_word, True, black), (0, 0))
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
            animation_end = True
            guessed_letters, secret_word, screen_word, user_letters = new_word()
            now_heart = 0 + start_heart
            now_hints = 0 + start_hints
        if start_hints != 0:
            sc.blit(bulb_pic, (470, 0))
            sc.blit(pg.font.Font(CHILLER, 90).render("X" + str(now_hints), True, white), (470 + 78, 0))
        new_level(screen_word)
        end_level = False
        end_game = False
        if now_heart <= 0:
            end_game = True
        elif len(guessed_letters) == len(secret_word):
            end_level = True
        pg.display.update()

        while start:
            for i in pg.event.get():
                if now_heart <= 0:
                    end_game = True
                elif len(guessed_letters) == len(secret_word):
                    end_level = True

                if i.type == pg.QUIT:
                    sys.exit()
                elif i.type == pg.MOUSEBUTTONDOWN and i.button == 1 and not end_game and not end_level:
                    pos = pg.mouse.get_pos()
                    if 0 <= pos[0] <= 72 and 0 <= pos[1] <= 56:
                        save = True
                        first = True
                        start = False
                    elif 470 <= pos[0] <= 548 and 0 <= pos[1] <= 95 and (now_hints != 0 or not minus_hint):
                        save = True
                        hint = True
                        start = False
                        if minus_hint:
                            minus_hint = False
                            now_hints -= 1
                elif i.type == pg.KEYDOWN and not end_game and not end_level:
                    if i.key == pg.K_ESCAPE:
                        first = True
                        start = False
                        save = True

                    elif 97 <= i.key <= 122:
                        minus_hint = True
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

                                    for a in range(0, len(guessed_letters)):
                                        screen_word.pop(guessed_letters[a])
                                        screen_word.insert(guessed_letters[a], secret_word[guessed_letters[a]])

                                    update_new_letter(screen_word)

                            if minus_heart:
                                if letter in vowel:
                                    now_heart -= 2
                                else:
                                    now_heart -= 1
                                if now_heart <= 0:
                                    end_game = True
                            else:
                                score += (42 * now_heart) / (start_heart * (start_heart + 1))

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
                            end_level = False
                            guessed_letters, secret_word, screen_word, user_letters = new_word()
                            new_level(screen_word)

                    elif i.type == pg.KEYDOWN:
                        if i.key == pg.K_ESCAPE:
                            first = True
                            start = False
                        elif i.key == pg.K_SPACE:
                            guessed_letters, secret_word, screen_word, user_letters = new_word()
                            new_level(screen_word)

                elif end_game:
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
                            end_game = False
                            now_hints = 0 + start_hints
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

                elif start_hints != 0:
                    sc.blit(bulb_pic, (470, 0))
                    sc.blit(pg.font.Font(CHILLER, 90).render("X" + str(now_hints), True, white), (470 + 78, 0))

                pg.display.update()

            pg.time.wait(10)

    elif hint:
        words1 = open(words, 'r').readline().split()
        words2 = []
        for i in words1:
            if len(i) == len(secret_word):
                words2.append(i.upper())
        words1 = []
        for i in range(0, len(words2)):
            ap = True
            for a in range(0, len(secret_word)):
                if (screen_word[a] != "_" and screen_word[a] != words2[i][a]) or\
                        (screen_word[a] == "_" and words2[i][a] in user_letters):
                    ap = False
            if ap:
                words1.append(words2[i])


        def hints():
            sc.blit(hint_pic, (0, 0))
            if len(words1) <= 18 * m:
                for i in range(0, len(words1)):
                    sc.blit(pg.font.Font(CHILLER, 50).render(words1[i], True, white),
                            (73 + (i % m) * k * len(secret_word), (i // m) * 48))
            else:
                for i in range(g * m, min((g + 1) * m * 18, len(words1))):
                    sc.blit(pg.font.Font(CHILLER, 50).render(words1[i], True, white),
                            (73 + (i % m) * k * len(secret_word), (i // m - g) * 48))

            pg.display.update()


        g = 0
        k = 26
        m = 1467 // (k * len(secret_word))
        hints()
        while hint:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                elif i.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if 0 <= pos[0] <= 74 and 0 <= pos[1] <= 63 and i.button == 1:
                        start = True
                        hint = False
                    elif i.button == 4:
                        if g <= len(words1) // m - 14:
                            g += 1
                            hints()
                    elif i.button == 5:
                        if g >= 1:
                            g -= 1
                            hints()

            pg.time.wait(10)

    elif settings and ((not save) or (len(user_letters) == 0 and score == 0)):
        save = False
        s_x = 1000
        s_y = 450

        def new_heart_settings():
            d_x = 70
            s_x = 1087 - 35 * max_heart
            s_y = 350
            sc.blit(play, (0, 0))

            for k in range(0, max_heart):
                if k < max_heart - start_heart:
                    sc.blit(grey_heart, (s_x + d_x * k, s_y))
                else:
                    sc.blit(red_heart, (s_x + d_x * k, s_y))

            if start_heart != max_heart:
                sc.blit(left_arrow, (1023 - 35 * max_heart, 347))
            if start_heart != 1:
                sc.blit(right_arrow, (1092 + 35 * max_heart, 347))
            now_heart = 0 + start_heart

        def new_hints_settings():
            sc.blit(bulb_pic, (s_x, s_y))
            sc.blit(pg.font.Font(CHILLER, 90).render("X" + str(start_hints), True, white), (s_x + 78, s_y))
            if start_hints != max_hints:
                sc.blit(left_arrow, (s_x - 60, s_y + 15))
            if start_hints != 0:
                sc.blit(right_arrow, (s_x + 165, s_y + 15))
            now_hints = 0 + start_hints

        sc.blit(play, (0, 0))
        new_heart_settings()
        new_hints_settings()
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
                    elif 1087 - 35 * max_heart <= pos[0] <= 1087 + 35 * max_heart and 350 <= pos[1] <= 410:
                        start_heart = max_heart - (pos[0] - 1087 + 35 * max_heart) // 70
                        sc.blit(pg.font.Font(CHILLER, 90).render(str(start_heart), True, white), (pos[0], pos[1]))
                    elif 1023 - 35 * max_heart <= pos[0] <= 1078 - 35 * max_heart and\
                            347 <= pos[1] <= 411 and start_heart != max_heart:
                        start_heart += 1
                    elif 1092 + 35 * max_heart <= pos[0] <= 1147 + 35 * max_heart and\
                            347 <= pos[1] <= 411 and start_heart != 1:
                        start_heart -= 1
                    elif s_x - 60 <= pos[0] <= s_x - 5 and s_y + 15 <= pos[1] <= s_y + 79 and start_hints != max_hints:
                        start_hints += 1
                    elif s_x + 165 <= pos[0] <= s_x + 220 and s_y + 15 <= pos[1] <= s_y + 79 and start_hints != 0:
                        start_hints -= 1
                    new_heart_settings()
                    new_hints_settings()

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
