import os
import csv

cars_path = "./data/cars.csv"
trucks_path = "./data/trucks.csv"
user_path = "./data/user.csv"

def load():
    data = [[],[[], []]]

    with open(cars_path, 'r', newline='\n', encoding='utf-8') as file:

        csv_reader = csv.reader(file, delimiter='|')
        csv_stuff = csv_reader

        for vehicle in csv_stuff:
            vehicle_data = []
            for row in vehicle:
                vehicle_data.append(row)

            if len(data[1][0]) == 0:
                data[1][0] = [vehicle_data]
            else:
                data[1][0].append(vehicle_data)


    #TODO: WHEN USERS ARE IMPLEMENTED UNCOMMENT FOLLOWING:
    with open(trucks_path, 'r', newline='\n', encoding='utf-8') as file:

        csv_reader = csv.reader(file, delimiter='|')
        csv_stuff = csv_reader

        for vehicle in csv_stuff:
            vehicle_data = []
            for row in vehicle:
                vehicle_data.append(row)

            if len(data[1][0]) == 0:
                data[1][1] = [vehicle_data]
            else:
                data[1][1].append(vehicle_data)

    #with open(user_path, 'r', newline='\n', encoding='utf-8') as file:
#
    #    csv_reader = csv.reader(file, delimiter='|')
    #    csv_stuff = csv_reader
    #
    #    for user in csv_stuff:
    #        user_data = []
    #        for row in user:
    #            user_data.append(row)
#
    #        if len(data[0][0]) == 0:
    #            data[0][1] = [user_data]
    #        else:
    #            data[0][1].append(user_data)

    return data


def save(data):     # DATA IN THIS FORMAT : [USER_DATA, VEHICLES]; VEHICLES : [CARS, TRUCKS]!!!

    with open(cars_path, 'w', newline='\n', encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter='|')
        csv_writer.writerows(data[1][0])

    with open(trucks_path, 'w', newline='\n', encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter='|')
        csv_writer.writerows(data[1][1])

    #TODO: WHEN USERS ARE IMPLEMENTED UNCOMMENT FOLLOWING:

    #with open(user_path, 'w', newline='\n', encoding='utf-8') as file:
    #    csv_writer = csv.writer(file, delimiter='|')
    #    csv_writer.writerows(data)




    return
