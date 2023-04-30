let MicroSecsInSeconds = 1000000
let pauseInSeconds = 0.5
let pauseInMicroSeconds = MicroSecsInSeconds * pauseInSeconds
basic.forever(function on_forever() {
    led.plot(0, 0)
    control.waitMicros(pauseInMicroSeconds)
    led.unplot(0, 0)
    control.waitMicros(pauseInMicroSeconds)
})
