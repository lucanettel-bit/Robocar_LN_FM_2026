import json
import logging

import board
from adafruit_pca9685 import PCA9685

with open("config.json") as file:
    config = json.load(file)

log = logging.getLogger(__name__)

# create I²C bus interface
i2c = board.I2C()
# create PCA9685 instance
pca = PCA9685(i2c)

current_speed_front_left = 0
current_speed_front_right = 0
current_speed_rear_left = 0
current_speed_rear_right = 0


def init():
    log.info("initialize the PWM module")
    pca.frequency = config["pca_frequency"]
    pca.channels[0].duty_cycle = 0
    pca.channels[1].duty_cycle = 0
    pca.channels[2].duty_cycle = 0
    pca.channels[3].duty_cycle = 0
    pca.channels[4].duty_cycle = 0
    pca.channels[5].duty_cycle = 0
    pca.channels[6].duty_cycle = 0
    pca.channels[7].duty_cycle = 0
    pass


def stop_all():
    global \
        current_speed_front_left, \
        current_speed_front_right, \
        current_speed_rear_left, \
        current_speed_rear_right
    pca.channels[0].duty_cycle = 0
    pca.channels[1].duty_cycle = 0
    pca.channels[2].duty_cycle = 0
    pca.channels[3].duty_cycle = 0
    pca.channels[4].duty_cycle = 0
    pca.channels[5].duty_cycle = 0
    pca.channels[6].duty_cycle = 0
    pca.channels[7].duty_cycle = 0
    current_speed_front_left = 0
    current_speed_front_right = 0
    current_speed_rear_left = 0
    current_speed_rear_right = 0


max_speed = 100


def front_left(speed=0):
    global current_speed_front_left
    if abs(speed) > max_speed:
        log.error(f"speed {speed} outside of range 0-100")
        return

    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_front_left = speed

    if speed >= 0:
        pca.channels[0].duty_cycle = 0
        pca.channels[1].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[0].duty_cycle = motor_speed
        pca.channels[1].duty_cycle = 0


def front_right(speed=0):
    global current_speed_front_right
    if abs(speed) > max_speed:
        log.error(f"speed {speed} outside of range 0-100")
        return

    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_front_right = speed

    if speed >= 0:
        pca.channels[7].duty_cycle = 0
        pca.channels[6].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[7].duty_cycle = motor_speed
        pca.channels[6].duty_cycle = 0


def rear_left(speed=0):
    global current_speed_rear_left
    if abs(speed) > max_speed:
        log.error(f"speed {speed} outside of range 0-100")
        return

    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_rear_left = speed

    if speed >= 0:
        pca.channels[3].duty_cycle = 0
        pca.channels[2].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[3].duty_cycle = motor_speed
        pca.channels[2].duty_cycle = 0


def rear_right(speed=0):
    global current_speed_rear_right
    if abs(speed) > max_speed:
        log.error(f"speed {speed} outside of range 0-100")
        return

    motor_speed = int((abs(speed) * 0xFFFF) / 100)
    current_speed_rear_right = speed

    if speed >= 0:
        pca.channels[4].duty_cycle = 0
        pca.channels[5].duty_cycle = motor_speed
    if speed < 0:
        pca.channels[4].duty_cycle = motor_speed
        pca.channels[5].duty_cycle = 0


main_speed = config["main_speed"]


def forward():
    rear_left(main_speed)
    front_left(main_speed)
    rear_right(main_speed)
    front_right(main_speed)


outer_turn_speed = config["outer_turn_speed"]
inner_turn_speed = config["inner_turn_speed"]


def turn_right():
    rear_left(outer_turn_speed)
    front_left(outer_turn_speed)
    rear_right(inner_turn_speed)
    front_right(inner_turn_speed)


def turn_left():
    rear_left(inner_turn_speed)
    front_left(inner_turn_speed)
    rear_right(outer_turn_speed)
    front_right(outer_turn_speed)


slight_outer_turn_speed = config["slight_outer_turn_speed"]
slight_inner_turn_speed = config["slight_inner_turn_speed"]


def slight_turn_right():
    rear_left(slight_outer_turn_speed)
    front_left(slight_outer_turn_speed)
    rear_right(slight_inner_turn_speed)
    front_right(slight_inner_turn_speed)


def slight_turn_left():
    rear_left(slight_inner_turn_speed)
    front_left(slight_inner_turn_speed)
    rear_right(slight_outer_turn_speed)
    front_right(slight_outer_turn_speed)
