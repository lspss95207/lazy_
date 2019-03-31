import RPi.GPIO as GPIO


class Servo:
    def __init__(self,PWM_FREQ = 50):
        self.PWM_FREQ = PWM_FREQ
        self.angle = 0

        
    def __exit__(self, exc_type, exc_value, traceback):
        self.pwm.stop()
        GPIO.cleanup()

    def attach(self,PIN):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)
        
        self.pwm = GPIO.PWM(PIN, self.PWM_FREQ)
        self.pwm.start(0)

        
    def write(self, angle):
        self.angle = angle

        dc = duty_cycle = (0.05 * self.PWM_FREQ) + (0.19 * self.PWM_FREQ * angle / 180)

        self.pwm.ChangeDutyCycle(dc)
         
    def read(self):
        return self.angle
