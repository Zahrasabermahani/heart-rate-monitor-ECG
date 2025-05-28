# Real-Time Heart Rate Monitoring using AD8232 and Raspberry Pi Pico for IOT
# heart-rate-monitor-ECG

Real-time heart rate detection using Raspberry Pi Pico, AD8232 ECG sensor, and OLED display (IoT Master Project)



This project implements a real-time heart rate monitor using the AD8232 ECG sensor and Raspberry Pi Pico (or ESP32). It reads the analog ECG signal, detects pulses, calculates BPM (Beats Per Minute), and displays the result on a 128x64 OLED screen.

## 🔧 Components Used
- Raspberry Pi Pico (or ESP32)
- AD8232 ECG Sensor
- OLED Display (128x64, I2C-based)
- ECG Electrodes
- Jumper Wires
- Breadboard

##  How It Works
1. The AD8232 ECG sensor captures the heart's electrical signals.
2. The signal is read using an ADC pin on the Pico.
3. The code checks if the signal exceeds a certain threshold to detect a heartbeat.
4. The number of heartbeats is counted over a period of 15 seconds.
5. The BPM is calculated and displayed live on the OLED.

##  Files Included
- `project2.py`: Main Python script for heartbeat detection and OLED display.
- `Metropolia_Poster_Template.pptx`: Final academic poster of the project.
- `images/`: Sample images showing the setup, electrodes, and live display.

##  Highlights of the Code
- Proper use of hardware libraries: `Pin`, `ADC`, `I2C` for Raspberry Pi Pico.
- OLED initialized via `SSD1306_I2C` for real-time output.
- Custom pulse detection using a defined threshold (`threshold = 50000`).
- Heartbeat counting over a time interval (15 seconds) and BPM calculation.
- Displays final BPM both in terminal and on OLED screen.
- Clean structure and easy-to-read logic with optional interrupt handling.

## 💡 Possible Improvements
- Extend measurement duration to 30+ seconds for more accurate BPM.
- Add error handling for sensor disconnection.
- Use smoothing or averaging filters for noisy analog signals.
