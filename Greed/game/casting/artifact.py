from game.casting.actor import Actor

class Artifact(Actor):
    
    def __init__(self):

        self._points = 1



    def set_points(self, points):

        self._points = points



    def get_points(self):

        return self._points