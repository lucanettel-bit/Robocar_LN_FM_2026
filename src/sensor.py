from gpiozero import LineSensor

sensor_left = LineSensor(14)
sensor_right = LineSensor(23)
sensor_middle = LineSensor(15)

detected_line = 1
no_line = 0


def detected_left():
    return sensor_left.value == detected_line


def detected_right():
    return sensor_right.value == detected_line


def detected_middle():
    return sensor_middle.value == detected_line


def detected_middle_left():
    return sensor_left.value == sensor_middle.value == detected_line


def detected_middle_right():
    return sensor_right.value == sensor_middle.value == detected_line


def detected_all():
    return (
        sensor_left.value == sensor_middle.value == sensor_right.value == detected_line
    )


def detected_right_left():
    return sensor_left.value == sensor_right.value == detected_line


def detected_none():
    return sensor_left.value == sensor_right.value == sensor_middle.value == no_line
