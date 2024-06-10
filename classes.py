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

    def start_race(self):
        Race().start_race()


class Track:
    line_1 = ["_", "|", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|", "_"]
    line_2 = ["_", "|", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|", "_"]

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
            self.move_cars()
            if self.get_winner() == True:
                self.ended = True
            time.sleep(1)

    def move_cars(self):
        if self.move_car(self.car_1, self.track.line_1) or self.move_car(self.car_2, self.track.line_2):
            return True
        return False

    def move_car(self, car: Car, line: list):
        current_position: int = line.index(car.model)
        new_position: int = current_position + car.speed
        if new_position >= len(line) - 1:
            line[current_position] = "_"
            line[-1] = car.model
            return True
        if new_position <= 1:
            new_position = 2
        line[current_position] = "_"
        line[new_position] = car.model
        return False

    def get_winner(self):
        car_1_finished = None
        car_2_finished = None

        if self.track.line_1[-1] <= "X":
            car_1_finished = True
        if self.track.line_2[-1] <= "0":
            car_2_finished = True
        if car_1_finished and car_2_finished:
            print("it's a DRAW!!")
            return True
        elif car_1_finished:
            print("Car X is the winner")
            return True
        elif car_2_finished:
            print("Car 0 is the winner")
            return True
        return False
