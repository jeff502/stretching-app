import pygame
from stretch_timer import StretchTimer
"""
Create a simple GUI with a timer on it and three buttons, `Start`, `Stop` and `Pause`.
Functionality should be to alternate between three separate countdowns. 5, 15, 30 second intervals.
I want a small delay between each countdown. 5 seconds of down time between each `countdown interval`

I need unique sound effects for the interval countdowns and the rest countdown.

countdown prep -> 5 -> countdown prep -> 15 countdown prep -> 30 (longer countdown after, or different sound effect)
"""


def main():
    pygame.init()
    stretch = StretchTimer()
    stretch.start()


if __name__ == '__main__':
    main()
