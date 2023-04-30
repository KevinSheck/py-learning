MicroSecsInSeconds = 1000000
pauseInSeconds = 0.5
pauseInMicroSeconds = MicroSecsInSeconds * pauseInSeconds

def on_forever():
    led.plot(0, 0)
    control.wait_micros(pauseInMicroSeconds)
    led.unplot(0, 0)
    control.wait_micros(pauseInMicroSeconds)
basic.forever(on_forever)
