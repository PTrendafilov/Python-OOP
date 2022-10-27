from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        self.speed += 3