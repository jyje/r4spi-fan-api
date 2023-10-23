"""Fan Services"""

import threading, time
import RPi.GPIO as GPIO
from fan.services.cluster import service as cluster_service

# Configuration
FAN_PIN            = 18     # BCM pin used to drive PWM fan
PWM_FREQ           = 1000   # [Hz] Noctua PWM control
REFRESH_TIME       = 30     # [s] Time to wait between each refresh
DUTY_CYCLE_INITIAL = 50     # [%] Fan speed
DUTY_CYCLE_STEP    = 2      # [%] Fan speed step


class FanService():
    """Rasberry Pi Fan Controller Service"""

    def __init__(self):
        self.is_fan_on = False

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(FAN_PIN, GPIO.OUT)
        self.fan = GPIO.PWM(FAN_PIN, PWM_FREQ)
        self.fan.start(0)

        self.duty_cycle        = DUTY_CYCLE_INITIAL
        

    async def get_duty_cycle(self):
        """Returns the fan speed"""
        return self.duty_cycle


    def set_fan_speed(self):
        """Sets the fan speed"""

        print("Fan is on")
        while self.is_fan_on:
            current_temperature = cluster_service.prometheus_maximum_temperture()
            target = cluster_service.target_temperture

            if current_temperature > target:
                self.duty_cycle = min(100, self.duty_cycle + DUTY_CYCLE_STEP)
            else:
                self.duty_cycle = max(0, self.duty_cycle - DUTY_CYCLE_STEP)

            self.fan.ChangeDutyCycle(self.duty_cycle)
            print(f"Temperture: {current_temperature}")
            print(f"Duty cycle: {self.duty_cycle}")
            time.sleep(REFRESH_TIME)
        print("Fan is off")


    async def enable(self):
        """Turns the fan on"""
        self.is_fan_on = True

        self.thread = threading.Thread(
            target = self.set_fan_speed,
        )
        self.thread.start()

        return { "is_fan_on": self.is_fan_on }


    async def disable(self):
        """Turns the fan off"""
        self.is_fan_on = False

        del self.thread

        return { "is_fan_on": self.is_fan_on }


service = FanService()
