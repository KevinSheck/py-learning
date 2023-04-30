pause2 = 0

def on_forever():
    global pause2
    pause2 = 100000
    led.plot(0, 0)
    control.wait_micros(pause2)
    led.unplot(0, 0)
    control.wait_micros(pause2)
basic.forever(on_forever)
