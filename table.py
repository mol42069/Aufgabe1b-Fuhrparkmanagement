import pygame as pg

class List:

    def __init__(self, inventory, starting_pos=50):
        self.position = (50, starting_pos)
        self.inventory = inventory
        self.surf = pg.Surface((900, len(inventory[0]) * 50))
        self.new_tab = pg.Surface((98, 48))
        self.car_tab = pg.Surface((399, 48))
        self.car_rect = pg.Rect((101, 1),(399, 48))
        self.truck_tab = pg.Surface((398, 48))
        self.truck_rect = pg.Rect((501, 1),(399, 48))
        self.car = True
        self.black = (0, 0, 0)
        self.dark_grey = (30, 30, 30)
        self.grey = (90, 90, 90)
        self.light_grey = (150, 150, 150)


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
            self.surf = vehicle.gen_Surf(self.surf, pos)

        root.blit(self.surf, self.position)

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
