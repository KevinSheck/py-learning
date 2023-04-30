let pause2 = 0
basic.forever(function on_forever() {
    
    pause2 = 100000
    led.plot(0, 0)
    control.waitMicros(pause2)
    led.unplot(0, 0)
    control.waitMicros(pause2)
})
