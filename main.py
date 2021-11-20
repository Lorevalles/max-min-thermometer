def on_button_pressed_a():
    basic.show_number(min2)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(max2)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

min2 = 0
max2 = 0
currenttemperature = input.temperature()
max2 = currenttemperature
min2 = currenttemperature

def on_forever():
    global currenttemperature, min2, max2
    basic.show_string(".")
    currenttemperature = input.temperature()
    if currenttemperature < min2:
        min2 = currenttemperature
    if currenttemperature > max2:
        max2 = currenttemperature
    basic.pause(1000)
    basic.clear_screen()
    basic.pause(1000)
basic.forever(on_forever)
