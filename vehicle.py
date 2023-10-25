import datetime
import pygame as pg

class Vehicle:

    def __init__(self, vehicle_type, idx, size):
        self.size = size
        self.id = idx + 1
        self.vehicle_type = str(vehicle_type)
        self.parked = True
        self.expected_back = None
        self.light_grey = (150, 150, 150)
        self.dark_grey = (30, 30, 30)
        self.red = (47, 7, 0)
        self.green = (0, 100, 7)
        self.black = (0, 0, 0)
        self.surf = pg.Surface((size[0] - 100, 50))

    def take(self, duration=(0, 0, 0), return_date=(0, 0, 0, 0, 0, 0)):
        # duration is (days, hours, minutes)
        # return_date is (Year, Month, Day, Hour, Minute, Seconds)

        self.parked = False

        if duration != (0, 0, 0):

            cur_date = datetime.datetime.now()
            time_change = datetime.timedelta(days=duration[0])
            cur_date += time_change
            time_change = datetime.timedelta(hours=duration[1])
            cur_date += time_change
            time_change = datetime.timedelta(minutes=duration[2])
            self.expected_back = cur_date + time_change

        elif return_date != (0, 0, 0, 0, 0):
            self.expected_back = datetime.datetime(return_date[0], return_date[1], return_date[2],
                                                   return_date[3], return_date[4], 0)


        return

    def returned(self):
        self.parked = True

        return

    def take_interface(self, root):

        b_surface = pg.Surface((600, 400))
        b_surface.fill(self.light_grey)

        surf = pg.Surface((596, 396))
        surf.fill(self.dark_grey)

        while True:

            b_surface.blit(surf, (2, 2))
            root.blit(b_surface)
            
            return root

    def gen_Surf(self, surface, position):

        font = pg.font.SysFont("Comic Sans MS", 20)

        id_surf = pg.Surface((48, 48))
        type_surf = pg.Surface((449, 48))
        parked_surf = pg.Surface((398, 48))

        self.surf.fill(self.light_grey)

        if self.id < 10:
            idx = "0" + str(self.id)

        else:
            idx = str(self.id)



        if self.parked:
            id_surf.fill(self.green)
            type_surf.fill(self.green)
            parked_surf.fill(self.green)

        else:
            id_surf.fill(self.red)
            type_surf.fill(self.red)
            parked_surf.fill(self.red)

        text = font.render(idx, True, self.black)
        id_surf.blit(text, (11, 9))

        self.surf.blit(id_surf, (1, 1))

        text = font.render(self.vehicle_type, True, self.black)
        type_surf.blit(text, (11, 9))
        self.surf.blit(type_surf, (51, 1))

        if self.parked:
            text = font.render("Available", True, self.black)

        else:
            t = str(self.expected_back.day) + "/" + str(self.expected_back.month) + "/" + str(self.expected_back.year) +\
                " @" + str(self.expected_back.hour) + ":" + str(self.expected_back.minute)

            text = font.render(t, True, self.black)


        parked_surf.blit(text, (11, 9))
        self.surf.blit(parked_surf, (501, 1))

        surface.blit(self.surf, position)

        return surface