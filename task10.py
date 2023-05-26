class MealyError(Exception):
    pass


class Mealy:
    def init(self):
        self.cond = 'A'

    def scale(self):
        if self.cond == 'A':
            self.cond = 'B'
            return 0
        if self.cond == 'C':
            self.cond = 'D'
            return 3
        if self.cond == 'F':
            self.cond = 'H'
            return 7
        if self.cond == 'H':
            self.cond = 'E'
            return 11
        raise MealyError('scale')

    def hike(self):
        if self.cond == 'B':
            self.cond = 'C'
            return 1
        if self.cond == 'D':
            self.cond = 'E'
            return 4
        if self.cond == 'F':
            self.cond = 'A'
            return 8
        raise MealyError('hike')

    def make(self):
        if self.cond == 'B':
            self.cond = 'H'
            return 2
        if self.cond == 'E':
            self.cond = 'F'
            return 5
        raise MealyError('make')

    def crush(self):
        if self.cond == 'F':
            self.cond = 'G'
            return 6
        if self.cond == 'G':
            self.cond = 'H'
            return 9
        if self.cond == 'H':
            self.cond = 'D'
            return 10
        raise MealyError('crush')


def test():
    m = Mealy()
    m.scale()
    try:
        m.crush()
    except MealyError:
        pass
    try:
        m.scale()
    except MealyError:
        pass
    m.hike()
    try:
        m.hike()
    except MealyError:
        pass
    try:
        m.make()
    except MealyError:
        pass
    m.scale()
    m.hike()
    m.make()
    m.crush()
    m.crush()
    m.scale()
    m.make()
    m.hike()
    m.scale()
    m.make()
    m.crush()
    m.hike()
    m.make()
    m.scale()
    main()


def main():
    return Mealy()
