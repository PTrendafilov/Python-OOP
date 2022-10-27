from abc import ABC, abstractmethod


class Horse:
    def __init__(self, type, name, speed):
        self.type = type
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) < 4:
            raise ValueError(f'Horse name {value} is less than 4 symbols!')
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if (self.type=='Appaloosa' and value>120) or (self.type=='Thoroughbred' and value>140):
            raise ValueError('Horse speed is too high!')
        self.__speed = value

    def train(self):
        if self.type =='Appaloosa':
            self.speed+=2
        else:
            self.speed+=3
