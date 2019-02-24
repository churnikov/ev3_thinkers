from ev3dev import ev3

left_wheel = ev3.MediumMotor('outA')
right_wheel = ev3.MediumMotor('outB')
infra_sensor = ev3.InfraredSensor('in1')
touch_sensor = ev3.TouchSensor('in2')

def forward():
    left_wheel.run_forever(speed_sp=500)
    right_wheel.run_forever(speed_sp=500)


def turn():
    left_wheel.run_forever(speed_sp=500, time_sp=3000)


def stop():
    left_wheel.stop()
    right_wheel.stop()


while True:

    if not touch_sensor.value():
        forward()
    else:
        turn()
