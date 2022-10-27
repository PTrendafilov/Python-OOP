from project.jockey import Jockey
from project.horse_specification.horse import Horse
from project.horse_race import HorceRace


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f'Horse {horse_name} has been already added!')
        if horse_type == 'Appaloosa' or horse_type == 'Thoroughbred':
            new_horse = Horse(horse_type, horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, name, age):
        for jockey in self.jockeys:
            if jockey.name == name:
                raise Exception(f'Jockey {name} has been already added!')
        new_jockey = Jockey(name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {name} is added."

    def create_horse_race(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                raise Exception(f'Race {race_type} has been already created!')
        new_race = HorceRace(race_type)
        self.horse_races.append(new_race)
        return f'Race {new_race.race_type} is created.'

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        our_jockey = ''
        our_horses = []
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                our_jockey = jockey
        if our_jockey == '':
            raise Exception(f'Jockey {jockey_name} could not be found!')
        for horse in self.horses:
            if horse.type == horse_type:
                our_horses.append(horse)
        if not our_horses:
            raise f'Horse breed {horse_type} could not be found!'
        our_horse = our_horses.pop()
        self.horses.remove(our_horse)
        if our_jockey.horse is None:
            our_jockey.horse = our_horse
            return f'Jockey {jockey_name} will ride the horse {our_horse.name}.'
        else:
            return f"Jockey {jockey_name} already has a horse."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        our_race = None
        for horse_race in self.horse_races:
            if horse_race.race_type==race_type:
                our_race = horse_race
        if our_race is None:
            raise Exception(f'Race {race_type} could not be found!')
        our_jockey = ''
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                our_jockey = jockey
        if our_jockey == '':
            raise Exception(f'Jockey {jockey_name} could not be found!')
        if our_jockey.horse==None:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')
        jockeys_race = ''
        for horse_race in self.horse_races:
            if our_jockey in horse_race.jockeys:
                return f'Jockey {jockey_name} has been already added to the {horse_race.race_type} race.'
        our_race.jockeys.append(our_jockey)
        return f'Jockey {jockey_name} added to the {race_type} race.'

    def start_horse_race(self,race_type):
        our_race = ''
        for horse_race in self.horse_races:
            if horse_race.race_type==race_type:
                our_race = horse_race
        if our_race=='':
            raise Exception(f'Race {race_type} could not be found!')
        if len(our_race.jockeys)<2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')
        max_speed = -1
        for jockey in our_race.jockeys:
            if jockey.horse.speed>max_speed:
                max_speed=jockey.horse.speed
        for jockey in our_race.jockeys:
            if jockey.horse.speed == max_speed:
                return f"The winner of the {race_type} race, with a speed of {max_speed}km/h is {jockey.name}! Winner's horse: {jockey.horse.name}."

