import control
import motor

motor.init()

try:
    control.control_direction()

except KeyboardInterrupt:
    motor.stop_all()
