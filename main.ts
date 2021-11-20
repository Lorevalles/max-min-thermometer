input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(min2)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showNumber(max2)
    basic.clearScreen()
})
let min2 = 0
let max2 = 0
let currenttemperature = input.temperature()
max2 = currenttemperature
min2 = currenttemperature
basic.forever(function on_forever() {
    
    basic.showString(".")
    currenttemperature = input.temperature()
    if (currenttemperature < min2) {
        min2 = currenttemperature
    }
    
    if (currenttemperature > max2) {
        max2 = currenttemperature
    }
    
    basic.pause(1000)
    basic.clearScreen()
    basic.pause(1000)
})
