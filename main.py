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

    scrolled = 0
    mouse_press = False
    for x in range(19):
        cars.append(vehicle.Vehicle("car", x, screen_size))
        trucks.append(vehicle.Vehicle("Truck", x , screen_size))



    cars[0].vehicle_type = "Volkswagen Golf-4"
    cars[0].take((0, 5, 30))

    inv = [cars, trucks]
    v = None

    new_v_window = False

    car_list = table.List(inv)

    pg.init()
    pg.display.init()
    root = pg.display.set_mode(screen_size)

    if car_list.car:
        if (len(car_list.inventory[0]) * 50) + 50 > screen_size[1]:
            max_scroll = (len(car_list.inventory[0]) * 50) - screen_size[1] + 50

        else:
            max_scroll = 0

    else:
        if (len(car_list.inventory[1]) * 50) + 50 > screen_size[1]:
            max_scroll = (len(car_list.inventory[1]) * 50) - screen_size[1] + 50

        else:
            max_scroll = 0

    temp = None

    while running:
        pg.display.update()
        root.fill(dark_grey)
        root = car_list.draw(root)
        pos = pg.mouse.get_pos()
        car_list.scrolled = scrolled

        if v is not None:
            root = v.build_click(root)
            temp = v

        elif new_v_window:
            root = car_list.new_vehicle(root)

        if not new_v_window:
            car_list.vehicle_text = ''

        if temp is not None and v is None:
            temp.text = ["", "", ""]



        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False
                exit()

            if event.type == pg.MOUSEWHEEL:

                scrolled -= 20 * event.y
                if scrolled < 0:
                    scrolled = 0
                elif scrolled > max_scroll:
                    scrolled = max_scroll

            if event.type != pg.KEYDOWN:
                if v is not None:
                    v.button_down = False
            else:
                if new_v_window:
                    car_list.new_vehicle_entry()

                if v is not None:
                    if v.chosen == 0:
                        v.entry(0)


                    elif (v.i_box[1].collidepoint(pos) and pg.mouse.get_pressed()[0]) or v.chosen == 1:
                        v.entry(1)
                        v.chosen = 1

                    elif (v.i_box[2].collidepoint(pos) and pg.mouse.get_pressed()[0]) or v.chosen == 2:
                        v.entry(2)
                        v.chosen = 2

        k = pg.key.get_pressed()
        if pg.mouse.get_pressed()[0] or k[pg.K_KP_ENTER] or k[pg.K_RETURN]:
            pos = pg.mouse.get_pos()
            temp_pos = (pos[0] - 50, pos[1])

            if car_list.car_rect.collidepoint(temp_pos):
                car_list.car = True

            elif car_list.truck_rect.collidepoint(temp_pos):
                car_list.car = False

            elif car_list.new_rect.collidepoint(temp_pos):
                new_v_window = True

            else:
                if not mouse_press and not car_list.new_win.collidepoint(pos) and new_v_window:
                    mouse_press = True
                    new_v_window = False

                elif new_v_window:
                    mouse_press = True

                elif v is None:
                    if not mouse_press:
                        pos = (pos[0] - 50, pos[1] - 50 + scrolled)
                        v = car_list.click(pos)

                    mouse_press = True

                elif (not v.s_rect.collidepoint(pos)) and not mouse_press:
                    v = None
                    mouse_press = True



            if v is not None and not mouse_press:

                mouse_press = True

                temp_pos = (pos[0] - 200, pos[1] - 300)

                if v.i_box[0].collidepoint(pos):
                    v.chosen = 0

                elif v.i_box[1].collidepoint(pos):
                    v.chosen = 1

                elif v.i_box[2].collidepoint(pos):
                    v.chosen = 2

                elif v.accept.collidepoint(temp_pos):
                    if v.parked:
                        for x, t in enumerate(v.text):
                            if t == '':
                                v.text[x] = "0"

                        duration = (int(v.text[0]), int(v.text[1]), int(v.text[2]))

                        try:
                            v.take(duration=duration)
                            v = None
                        except AttributeError:
                            v.parked = True

                    else:
                        v.returned()
                        v= None

                else:
                    v.chosen = 3

            if new_v_window:
                temp_pos = (pos[0], pos[1])
                if car_list.accept.collidepoint(temp_pos):
                    new_v_window = False
                    car_list.new_vehicle_accept()

                    if car_list.car:
                        if (len(car_list.inventory[0]) * 50 ) + 50 >  screen_size[1]:
                            max_scroll = (len(car_list.inventory[0]) * 50) - screen_size[1] + 50

                        else: max_scroll = 0

                    else:
                        if (len(car_list.inventory[1]) * 50 ) + 50 >  screen_size[1]:
                            max_scroll = (len(car_list.inventory[1]) * 50) - screen_size[1] + 50

                        else: max_scroll = 0


            #TODO: IMPLEMENT NEW VEHICLE STUFF

        else:
            mouse_press = False







def key_pressed():
    return



if __name__ == "__main__":
    main()
