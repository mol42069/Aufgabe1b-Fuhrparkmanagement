import pygame as pg
import vehicle

def get_key_pressed():
    keys = pg.key.get_pressed()

    key = ''

    if keys[pg.K_BACKSPACE]:
        return False

    if keys[pg.K_0] or keys[pg.K_KP0]:
        key = '0'
    elif keys[pg.K_1] or keys[pg.K_KP1]:
        key = '1'
    elif keys[pg.K_2] or keys[pg.K_KP2]:
        key = '2'
    elif keys[pg.K_3] or keys[pg.K_KP3]:
        key = '3'
    elif keys[pg.K_4] or keys[pg.K_KP4]:
        key = '4'
    elif keys[pg.K_5] or keys[pg.K_KP5]:
        key = '5'
    elif keys[pg.K_6] or keys[pg.K_KP6]:
        key = '6'
    elif keys[pg.K_7] or keys[pg.K_KP7]:
        key = '7'
    elif keys[pg.K_8] or keys[pg.K_KP8]:
        key = '8'
    elif keys[pg.K_9] or keys[pg.K_KP9]:
        key = '9'
    elif keys[pg.K_a]:
        key = 'a'
    elif keys[pg.K_b]:
        key = 'b'
    elif keys[pg.K_c]:
        key = 'c'
    elif keys[pg.K_d]:
        key = 'd'
    elif keys[pg.K_e]:
        key = 'e'
    elif keys[pg.K_f]:
        key = 'f'
    elif keys[pg.K_g]:
        key = 'g'
    elif keys[pg.K_h]:
        key = 'h'
    elif keys[pg.K_i]:
        key = 'i'
    elif keys[pg.K_j]:
        key = 'j'
    elif keys[pg.K_k]:
        key = 'k'
    elif keys[pg.K_l]:
        key = 'l'
    elif keys[pg.K_m]:
        key = 'm'
    elif keys[pg.K_n]:
        key = 'n'
    elif keys[pg.K_o]:
        key = 'o'
    elif keys[pg.K_p]:
        key = 'p'
    elif keys[pg.K_q]:
        key = 'q'
    elif keys[pg.K_r]:
        key = 'r'
    elif keys[pg.K_s]:
        key = 's'
    elif keys[pg.K_t]:
        key = 't'
    elif keys[pg.K_u]:
        key = 'u'
    elif keys[pg.K_v]:
        key = 'v'
    elif keys[pg.K_w]:
        key = 'w'
    elif keys[pg.K_x]:
        key = 'x'
    elif keys[pg.K_y]:
        key = 'y'
    elif keys[pg.K_z]:
        key = 'z'
    elif keys[pg.K_SPACE]:
        key = ' '
    elif keys[pg.K_COLON]:
        key = ','
    elif keys[pg.K_PERIOD]:
        key = '.'
    elif keys[pg.K_MINUS]:
        key = '-'

    if keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]:
        key = key.upper()

    return key

class List:

    def __init__(self, starting_pos=50):
        self.position = (50, starting_pos)
        self.inventory = [[],[]]
        self.surf = pg.Surface((900, len(self.inventory[0]) * 50))
        self.new_tab = pg.Surface((98, 48))
        self.new_rect = pg.Rect((1, 1),(98, 48))
        self.car_tab = pg.Surface((399, 48))
        self.car_rect = pg.Rect((101, 1),(399, 48))
        self.truck_tab = pg.Surface((398, 48))
        self.truck_rect = pg.Rect((501, 1),(399, 48))
        self.car = True
        self.black = (0, 0, 0)
        self.dark_grey = (30, 30, 30)
        self.grey = (90, 90, 90)
        self.light_grey = (150, 150, 150)
        self.scrolled = 0

        self.new_win = pg.Rect((200, 300), (600, 400))

        self.new_surf = pg.Surface((596, 396))
        self.new_surf_bg = pg.Surface((600, 400))
        self.vehicle_name_rect = pg.Rect((250, 400),(500, 50))
        self.vehicle_text = ""

        self.accept = pg.Rect((250, 600), (100, 50))
        self.button_down = False

    def new_vehicle(self, root):
        vehicle_name_bg = pg.Surface((500, 50))
        vehicle_name_bg.fill(self.light_grey)
        vehicle_name_surf = pg.Surface((496, 46))
        vehicle_name_surf.fill(self.dark_grey)


        font = pg.font.SysFont("Arial", 15)
        text = font.render(self.vehicle_text, True, self.light_grey)
        vehicle_name_surf.blit(text, (5, 12))

        accept_surf = pg.Surface((100, 50))
        accept_surf.fill(self.grey)
        text = font.render("Accept", True, self.light_grey)
        accept_surf.blit(text, (5, 12))

        vehicle_name_bg.blit(vehicle_name_surf, (2, 2))

        self.new_surf_bg.fill(self.light_grey)
        self.new_surf.fill(self.dark_grey)
        text = font.render("Vehicle Name: ", True, self.light_grey)
        self.new_surf.blit(text, (50, 80))
        self.new_surf.blit(vehicle_name_bg, (50, 100))
        self.new_surf.blit(accept_surf, (50, 300))


        root.blit(self.new_surf_bg, (200, 300))
        root.blit(self.new_surf, (202, 302))

        return root

    def new_vehicle_entry(self):
        n = get_key_pressed()
        try:
            if n == False:
                self.vehicle_text = self.vehicle_text[:-1]
            else:
                self.button_down = True
                self.vehicle_text += n
        except TypeError:
            pass

    def new_vehicle_accept(self):

        if self.car:
            new_car = vehicle.Vehicle(self.vehicle_text, len(self.inventory[0]))
            self.inventory[0].append(new_car)
        else:
            new_car = vehicle.Vehicle(self.vehicle_text, len(self.inventory[1]))
            self.inventory[1].append(new_car)

    def click(self, pos):
        if self.car:
            for v in self.inventory[0]:
                if v.rect.collidepoint(pos):
                    return v

        else:
            for v in self.inventory[1]:
                if v.rect.collidepoint(pos):
                    return v


    def draw(self, root):

        if self.car:
            inv = self.inventory[0]
            self.surf = pg.Surface((900, len(self.inventory[0]) * 50))
            self.car_tab.fill(self.dark_grey)
            self.truck_tab.fill(self.grey)

        else:
            inv = self.inventory[1]
            self.surf = pg.Surface((900, len(self.inventory[1]) * 50))
            self.car_tab.fill(self.grey)
            self.truck_tab.fill(self.dark_grey)

        for x, v in enumerate(inv):
            pos = (0, x * 50)
            self.surf = v.gen_surf(self.surf, pos)

        root.blit(self.surf, (self.position[0], self.position[1] - self.scrolled))

        c_surf = pg.Surface((900, 50))
        c_surf.fill(self.light_grey)
        self.new_tab.fill(self.grey)

        font = pg.font.SysFont("Comic Sans MS", 20)

        text = font.render("New", True, self.black)
        self.new_tab.blit(text, (11, 9))
        c_surf.blit(self.new_tab, (1, 1))

        text = font.render("Car", True, self.black)
        self.car_tab.blit(text, (11, 9))
        c_surf.blit(self.car_tab, (101, 1))

        text = font.render("Truck", True, self.black)
        self.truck_tab.blit(text, (11, 9))
        c_surf.blit(self.truck_tab, (501, 1))

        root.blit(c_surf, (50, 0))

        return root
