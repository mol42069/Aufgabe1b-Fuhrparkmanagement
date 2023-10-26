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

class List:

    def __init__(self, inventory, starting_pos=50):
        self.position = (50, starting_pos)
        self.inventory = inventory
        self.surf = pg.Surface((900, len(inventory[0]) * 50))
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

    def new_vehicle(self, root):
        vehicle_name_bg = pg.Surface((500, 50))
        vehicle_name_bg.fill(self.light_grey)
        vehicle_name_surf = pg.Surface((496, 46))
        vehicle_name_surf.fill(self.dark_grey)
        vehicle_name_bg.blit(vehicle_name_surf, (2, 2))

        font = pg.font.SysFont("Arial", 15)
        text = font.render(self.vehicle_text, True, self.light_grey)
        vehicle_name_surf.blit(text, (5, 12))

        accept_surf = pg.Surface((100, 50))
        accept_surf.fill(self.grey)
        text = font.render(self.vehicle_text, True, self.light_grey)
        accept_surf.blit(text, (5, 12))


        self.new_surf_bg.fill(self.light_grey)
        self.new_surf.fill(self.dark_grey)
        text = font.render("Vehicle Name: ", True, self.light_grey)
        self.new_surf.blit(text, (50, 80))
        self.new_surf.blit(vehicle_name_bg, (50, 100))
        self.new_surf.blit(accept_surf, (50, 300))

        root.blit(self.new_surf_bg, (200, 300))
        root.blit(self.new_surf, (202, 302))

        return root

    def click(self, pos):
        if self.car:
            for vehicle in self.inventory[0]:
                if vehicle.rect.collidepoint(pos):
                    return vehicle

        else:
            for vehicle in self.inventory[1]:
                if vehicle.rect.collidepoint(pos):
                    return vehicle


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

        for x, vehicle in enumerate(inv):
            pos = (0, x * 50)
            self.surf = vehicle.gen_surf(self.surf, pos)

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
