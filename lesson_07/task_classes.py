if __name__ == '__main__':


    class Vehikle:

        def __init__(self, price, speed, year):
            self.prise = price
            self.speed = speed
            self.year = year



    class Plane(Vehikle):
        def __init__(self, price, speed, year, hi, passengers):
            Vehikle.__init__(price)
            super().__init__(speed)
            super().__init__(year)
            self.hi = hi
            self.passengers = passengers


    class Ship(Vehikle):
        def __init__(self, price, speed, year, passengers, port):
            super().__init__(price)
            super().__init__(speed)
            super().__init__(year)
            self.passengers = passengers
            self.port = port

