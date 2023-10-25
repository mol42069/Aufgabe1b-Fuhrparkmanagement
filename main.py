import vehicle
import table
import pygame as pg

#GLOBALS:

running = True
dark_grey = (30, 30, 30)
screen_size = (1000, 1000)

def main():
    global running, screen_size
    cars = []
    trucks = []

    for x in range(11):
        cars.append(vehicle.Vehicle("car", x, screen_size))
        trucks.append(vehicle.Vehicle("Truck", x , screen_size))

    cars[2].vehicle_type = "Volkswagen Golf-4"
    cars[2].take((0, 5, 30))

    inv = [cars, trucks]

    car_list = table.List(inv)

    pg.init()
    pg.display.init()
    root = pg.display.set_mode(screen_size)

    while running:
        root.fill(dark_grey)
        root = car_list.draw(root)
        pg.display.update()

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False
                exit()

            if event.type == pg.KEYDOWN:
                key_pressed()

        if pg.mouse.get_pressed()[0]:
            pos = pg.mouse.get_pos()

            if car_list.car_rect.collidepoint(pos):
                car_list.car = True

            if car_list.truck_rect.collidepoint(pos):
                car_list.car = False

            #TODO: IMPLEMENT NEW VEHICLE STUFF



def key_pressed():
    return


def print_screen(cars, trucks):
    if cars is not None:
        for car in cars:
            ident = car.id
            if ident < 10:
                ident = "0" + str(ident)

            if car.parked:
                print(str(ident) + " | " + car.vehicle_type + "   | Available")

            else:
                print(str(ident) + " | " + car.vehicle_type + "   | " +
                      str(car.expected_back.day) + "/" + str(car.expected_back.month) + "/" + str(car.expected_back.year) +
                      " @" + str(car.expected_back.hour) + ":" + str(car.expected_back.minute))

    if trucks is not None:
        for truck in trucks:
            ident = truck.id
            if ident < 10:
                ident = "0" + str(ident)

            if truck.parked:
                print(str(ident) + " | " + truck.vehicle_type + " | Available")

            else:
                print(str(ident) + " | " + truck.vehicle_type + " | " +
                      str(truck.expected_back.day) + "/" + str(truck.expected_back.month) + "/" + str(truck.expected_back.year) +
                      " @" + str(truck.expected_back.hour) + ":" + str(truck.expected_back.minute))


if __name__ == "__main__":
    main()
