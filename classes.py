#
# START |X_________________________________________| FINISH
# START |0_________________________________________| FINISH
#
# START |__X_______________________________________| FINISH
# START |_0________________________________________| FINISH
#
# START |_____X____________________________________| FINISH
# START |___0______________________________________| FINISH
#
# START |______X___________________________________| FINISH
# START |_________0________________________________| FINISH
#
import random
import time


class Game:
    game_is_running = True

    def __init__(self):
        print("Welcome to the car racing game!")

    @staticmethod
    def start_race():
        Race().start_race()


class Track:
    line_1 = ["_", "|", "_", "_", "_", "_", "_", "_", "_", "_", "_", "||", "_"]
    line_2 = ["_", "|", "_", "_", "_", "_", "_", "_", "_", "_", "_", "||", "_"]

    def __init__(self, car_1, car_2):
        self.line_1[0] = car_1
        self.line_2[0] = car_2

    def get_start_finish(self):
        print("START " + "".join(self.line_1) + " FINISH")
        print("START " + "".join(self.line_2) + " FINISH")


class Car:
    def __init__(self, model):
        self.model = model
        self.speed = random.randint(1, 3)


class Race:
    def __init__(self):
        self.car_1 = Car("X")
        self.car_2 = Car("0")
        self.track = Track(self.car_1.model, self.car_2.model)
        self.ended = False

    def start_race(self):
        while not self.ended:
            self.track.get_start_finish()
            if self.get_winner():
                self.ended = True
            self.move_cars()
            time.sleep(1)

    def move_cars(self):
        self.move_car(self.car_1, self.track.line_1)
        self.move_car(self.car_2, self.track.line_2)

    @staticmethod
    def move_car(car: Car, line: list):
        current_position: int = line.index(car.model)
        new_car_position: int = current_position + car.speed
        if new_car_position >= len(line) - 1:
            line[current_position] = "_"
            line[-1] = car.model
            return True
        elif new_car_position >= line.index(line[-2]):
            line[current_position] = "|"
            line[-1] = "|"
        if new_car_position <= 1:
            new_car_position = 2
        line[current_position] = "_"
        line[new_car_position] = car.model
        return False

    def get_winner(self):
        car_1_position = self.track.line_1.index("X")
        car_2_position = self.track.line_2.index("0")
        finish_line = self.track.line_1.index(self.track.line_1[-2])
        if car_1_position > finish_line and car_2_position > finish_line:
            print("It's a tie!")
            return True
        elif car_1_position > finish_line:
            print("Car X is the winner!")
            return True
        elif car_2_position > finish_line:
            print("Car 0 is the winner!")
            return True
        return False
