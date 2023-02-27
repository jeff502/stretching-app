import pygame
from stretch_timer import StretchTimer


def main():
    pygame.init()
    stretch = StretchTimer()
    stretch.start()


if __name__ == '__main__':
    main()
