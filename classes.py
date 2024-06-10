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
        Race()


class Track:
    line_1 = ["_", "|", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]
    line_2 = ["_", "|", "_", "_", "_", "_", "_", "_", "_", "_", "_", "|"]

    def __init__(self, car_1, car_2):
        self.length = 24
        self.line_1 = ["_" for _ in range(self.length)]
        self.line_2 = ["_" for _ in range(self.length)]
        self.line_1[0] = car_1
        self.line_2[0] = car_2

    def get_start_finish(self):
        print("START _|" + "".join(self.line_1) + "|_ FINISH")
        print("START _|" + "".join(self.line_2) + "|_ FINISH")


class Car:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed
        self.position = 0


class Race:
    def __init__(self):
        self.car_1 = Car("X", random.randint(1, 3))
        self.car_2 = Car("0", random.randint(1, 3))
        self.track = Track(self.car_1.model, self.car_2.model)
        self.start_race()

    def start_race(self):
        while True:
            self.move_cars()
            self.track.get_start_finish()
            if self.get_winner():
                break
            time.sleep(1)

    def move_cars(self):
        self.move_car(self.car_1, self.track.line_1)
        self.move_car(self.car_2, self.track.line_2)

    def move_car(self, car, line):
        line[car.position] = "_"
        car.position += random.randint(1, 3)
        if car.position >= len(line) - 1:
            car.position = len(line) - 1
        line[car.position] = car.model

    def get_winner(self):
        if self.car_1.position == len(self.track.line_1) - 1:
            print("Car X WINS!!")
            return True
        if self.car_2.position == len(self.track.line_2) - 1:
            print("Car 0 WINS!!")
            return True
        return False
