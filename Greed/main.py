
import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.service.keyboard_service import KeyboardService
from game.service.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point



FRAME_RATE = 12

MAX_X = 900

MAX_Y = 600

CELL_SIZE = 15

FONT_SIZE = 15

CAPTION = 'GREED'

COLS = 60

ROWS = 40

WHITE = Color(255, 255, 255)

DEFAULT_ARTIFACTS = 40

    
def main():
    

    cast = Cast(COLS, ROWS, CELL_SIZE)

    

    

    score = Actor()

    score.set_text("Score: 0")

    score.set_font_size(FONT_SIZE)

    score.set_color(WHITE)

    score.set_position(Point(CELL_SIZE, 0))

    cast.add_actor("scores", score)

    

    

    x = int(MAX_X / 2)

    y = int(MAX_Y - FONT_SIZE * 2)

    position = Point(x, y)    



    robot = Actor()

    robot.set_text("#")

    robot.set_font_size(FONT_SIZE)

    robot.set_color(WHITE)

    robot.set_position(position)

    cast.add_actor("robots", robot)

    
    for n in range(DEFAULT_ARTIFACTS):  

        text = random.choice(['*', 'o'])

        

        x = random.randint(1, COLS - 1)

        y = random.randint(1, ROWS - 1)

        position = Point(x, y)

        position = position.scale(CELL_SIZE)


        r = random.randint(0, 255)

        g = random.randint(0, 255)

        b = random.randint(0, 255)

        color = Color(r, g, b)

        

        artifact = Artifact()

        artifact.set_text(text)

        artifact.set_font_size(FONT_SIZE)

        artifact.set_color(color)

        artifact.set_position(position)                    

        artifact.set_velocity(Point(0,1))    

        cast.add_actor("artifacts", artifact)



    keyboard_service = KeyboardService(CELL_SIZE)

    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)

    director = Director(keyboard_service, video_service)

    director.start_game(cast)





if __name__ == "__main__":

    main()


