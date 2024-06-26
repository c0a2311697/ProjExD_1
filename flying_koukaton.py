import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kouka3_img = pg.image.load("fig/3.png")
    kouka3_img = pg.transform.flip(kouka3_img, True, False)
    kouka3_rct = kouka3_img.get_rect()
    kouka3_rct.center = 300,200


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg_img2, [-x+4800, 0])


        key_lst = pg.key.get_pressed()

        x1 = -1
        y1 = 0
        if key_lst[pg.K_UP]:
            x1 = 0
            y1 = -1
        if key_lst[pg.K_DOWN]:
            x1 = 0
            y1 = 1
        if key_lst[pg.K_LEFT]:
            x1 = -1
            y1 = 0
        if key_lst[pg.K_RIGHT]:
            x1 = 2
            y1 = 0
        kouka3_rct.move_ip((x1, y1))
  

        screen.blit(kouka3_img, kouka3_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()