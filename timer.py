import time

class Timer():
    """ Simple time coordinator.

    Typical use is for timing game loops.
    """
    def __init__(self):
        self.start_time = self.get_time()

    def get_time(self):
        """ Simply converts unix time to milliseconds. """
        return time.time() * 1000

    def get_ticktime(self):
        """ Returns time since last call of tick(). """
        return self.get_time() - self.start_time

    def tick(self):
        """ Resets ticks time. """
        self.start_time = self.get_time()
