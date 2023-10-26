import datetime
import pygame as pg


def get_key_pressed():
    keys = pg.key.get_pressed()
    if keys[pg.K_0]:
        return '0'
    elif keys[pg.K_1]:
        return '1'
    elif keys[pg.K_2]:
        return '2'
    elif keys[pg.K_3]:
        return '3'
    elif keys[pg.K_4]:
        return '4'
    elif keys[pg.K_5]:
        return '5'
    elif keys[pg.K_6]:
        return '6'
    elif keys[pg.K_7]:
        return '7'
    elif keys[pg.K_8]:
        return '8'
    elif keys[pg.K_9]:
        return '9'
    elif keys[pg.K_BACKSPACE]:
        return '-1'


class Vehicle:

    def __init__(self, vehicle_type, idx, size):
        self.size = size
        self.id = idx + 1
        self.vehicle_type = str(vehicle_type)
        self.parked = True
        self.expected_back = None
        self.light_grey = (150, 150, 150)
        self.dark_grey = (30, 30, 30)
        self.grey = (80, 80, 80)
        self.red = (47, 7, 0)
        self.green = (0, 100, 7)
        self.black = (0, 0, 0)
        self.surf = pg.Surface((size[0] - 100, 50))
        self.rect = pg.Rect((0,0),(self.size[0] - 100, 50))
        self.b_surface = pg.Surface((600, 400))
        self.s = pg.Surface((596, 396))
        self.s_rect = pg.Rect((200, 300), (600, 400))
        self.text = ["", "", ""]

        self.i_box = [pg.Rect((252, 402), (96, 46)), pg.Rect((402, 402), (96, 46)), pg.Rect((552, 402), (96, 46))]
        self.chosen = 3

        self.button_down = False
        self.accept = pg.Rect((50, 300), (100, 50))
        self.accept_s = pg.Surface((100, 50))

    def take(self, duration=(0, 0, 0), return_date=(1, 0, 0, 0, 0, 0)):
        # duration is (days, hours, minutes)
        # return_date is (Year, Month, Day, Hour, Minute, Seconds)



        if duration != (0, 0, 0):

            self.parked = False

            cur_date = datetime.datetime.now()
            time_change = datetime.timedelta(days=duration[0])
            cur_date += time_change
            time_change = datetime.timedelta(hours=duration[1])
            cur_date += time_change
            time_change = datetime.timedelta(minutes=duration[2])
            self.expected_back = cur_date + time_change

        #elif return_date != (0, 0, 0, 0, 0):
        #    self.expected_back = datetime.datetime(return_date[0], return_date[1], return_date[2],
        #                                           return_date[3], return_date[4], 0)


        return

    def returned(self):
        self.parked = True

        return

    def build_click(self, root):

        if self.parked:

            self.b_surface.fill(self.light_grey)
            self.s.fill(self.dark_grey)

            ibg_box_day = pg.Surface((100, 50))
            ibg_box_day.fill(self.light_grey)
            it_box_day = pg.Surface((96, 46))
            it_box_day.fill(self.dark_grey)
            pg.draw.rect(ibg_box_day, self.dark_grey, self.i_box[0])
            ibg_box_day.blit(it_box_day, (2, 2))

            ibg_box_hour = pg.Surface((100, 50))
            ibg_box_hour.fill(self.light_grey)
            it_box_hour = pg.Surface((96, 46))
            it_box_hour.fill(self.dark_grey)
            pg.draw.rect(ibg_box_hour, self.dark_grey, self.i_box[1])
            ibg_box_hour.blit(it_box_hour, (2, 2))

            ibg_box_min = pg.Surface((100, 50))
            ibg_box_min.fill(self.light_grey)
            it_box_min = pg.Surface((96, 46))
            it_box_min.fill(self.dark_grey)
            pg.draw.rect(ibg_box_min, self.dark_grey, self.i_box[2])
            ibg_box_day.blit(it_box_min, (2, 2))

            font = pg.font.SysFont("Arial", 15)
            text = font.render("DAYS: ", True, self.light_grey)
            self.s.blit(text, (50, 80))

            text = font.render("HOURS: ", True, self.light_grey)
            self.s.blit(text, (200, 80))

            text = font.render("MINUTES: ", True, self.light_grey)
            self.s.blit(text, (350, 80))

            text = font.render(self.text[0], True, self.light_grey)
            it_box_day.blit(text, (5, 12))

            text = font.render(self.text[1], True, self.light_grey)
            it_box_hour.blit(text, (5, 12))

            text = font.render(self.text[2], True, self.light_grey)
            it_box_min.blit(text, (5, 12))

            self.accept_s.fill(self.grey)
            text = font.render("Accept", True, self.light_grey)
            self.accept_s.blit(text, (5, 12))

            t = "HOW LONG DO YOU WANT TO TAKE: " + self.vehicle_type.upper()
            text = font.render(t, True, self.light_grey)
            self.s.blit(text, (10, 10))

            ibg_box_day.blit(it_box_day, (2, 2))
            ibg_box_hour.blit(it_box_hour, (2, 2))
            ibg_box_min.blit(it_box_min, (2, 2))


            self.s.blit(self.accept_s, self.accept.topleft)

            self.s.blit(ibg_box_day, (50, 100))
            self.s.blit(ibg_box_hour, (200, 100))
            self.s.blit(ibg_box_min,(350, 100))



            self.b_surface.blit(self.s, (2, 2))
            root.blit(self.b_surface, (200, 300))

            return root

        else:
            self.s.fill(self.dark_grey)
            font = pg.font.SysFont("Arial", 15)
            self.accept_s.fill(self.grey)
            text = font.render("Return", True, self.light_grey)
            self.accept_s.blit(text, (5, 12))

            self.s.blit(self.accept_s, self.accept.topleft)

            self.b_surface.blit(self.s, (2, 2))
            root.blit(self.b_surface, (200, 300))

            return root



    def entry(self, index):

        n = get_key_pressed()
        if n == '-1':
            self.text[index] = self.text[index][:-1]

        if not self.button_down:
            self.button_down = True
            if n is None:
                pass
            else:
                self.text[index] += n



    def gen_surf(self, surface, position):

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
            try:
                t = str(self.expected_back.day) + "/" + str(self.expected_back.month) + "/" + str(self.expected_back.year) +\
                    " @" + str(self.expected_back.hour) + ":" + str(self.expected_back.minute)

                text = font.render(t, True, self.black)
            except AttributeError:
                pass


        parked_surf.blit(text, (11, 9))
        self.surf.blit(parked_surf, (501, 1))
        self.rect = pg.Rect(position,(self.size[0] - 100, 50))
        surface.blit(self.surf, position)

        return surface