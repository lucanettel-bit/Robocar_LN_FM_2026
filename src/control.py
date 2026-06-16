import json
import time

import motor
import sensor

with open("config.json") as file:
    config = json.load(file)


def control_direction():
    last_sensor = "middle"

    while True:
        if sensor.detected_middle_right():
            motor.slight_turn_right()

        elif sensor.detected_middle_left():
            motor.slight_turn_left()

        elif sensor.detected_middle():
            motor.forward()
            last_sensor = "middle"

        elif sensor.detected_left():
            motor.turn_left()
            last_sensor = "left"

        elif sensor.detected_right():
            motor.turn_right()
            last_sensor = "right"

        elif sensor.detected_none():
            if last_sensor == "middle":
                motor.forward()

            if last_sensor == "right":
                motor.turn_right()

            if last_sensor == "left":
                motor.turn_left()
        sleep = config["sleep"]
        time.sleep(sleep)
