from machine import Pin, ADC, I2C
import time
from ssd1306 import SSD1306_I2C

WIDTH =128
HEIGHT= 64
#Create the I2C connection
i2c = I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
#Initialize the OLED display
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
 
# Setup
led = Pin(15, Pin.OUT)         # LED on GP15
pulse_sensor = ADC(1)          # ADC1 = GP27
 
# Threshold for detecting a pulse
threshold = 50000
last_beat_time = time.ticks_ms()
beat_count = 0
 
print("Reading pulse from GP27 (ADC1)...")
start_time = time.ticks_ms()
duration = 15000  # 15 seconds to calculate BPM

def update_display(messages):
    oled.fill(0)
    start_line = max(0, len(messages) - 8)
    for i, msg in enumerate(messages[start_line:]):
        oled.text(msg, 0, i * 8)
    oled.show()
 
try:
    while time.ticks_diff(time.ticks_ms(), start_time) < duration:
        value = pulse_sensor.read_u16()
        if value > threshold:
            current_time = time.ticks_ms()
            if time.ticks_diff(current_time, last_beat_time) > 300:
                beat_count += 1
                last_beat_time = current_time
                led.toggle()
                print("Heartbeat detected! Count:", beat_count)
 
        time.sleep(0.01)
 
    total_time = time.ticks_diff(time.ticks_ms(), start_time)
    bpm = (beat_count * 60000) // total_time
    print("Estimated Heart Rate: {} BPM".format(bpm))
    update_display("heart rate", bpm)
 
except KeyboardInterrupt:
    print("Measurement stopped.")