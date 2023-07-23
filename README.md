# SumoBot using Microbit 🦾

This script enables you to control a bot using a BBC Microbit microcontroller. The bot uses ultrasonic sensors, QTI sensors, and IR sensors for obstacle detection and navigation. Additionally, a custom 3D-printed bumper is used to enhance the bot's physical design.

## Components & Libraries 📚

To implement this project, you will need the following:

- Microbit microcontroller
- Cyberbot library for MicroPython (imported as "cyberbot")
- Random module for generating random delays (imported as "randint")
- time_pulse_us module from the machine library for measuring time (imported as "time_pulse_us")
- qti module for reading inputs from QTI sensors (imported as "qti")
- PyAutoGUI module for controlling the computer's cursor (imported as "pyautogui")
- OpenCV library for computer vision tasks (imported as "cv2")

## How It Works ⛭

1. Setup: The code begins by declaring the required pins and initializing the bot's motors. The servo motors for controlling the bot's motion are connected to pins 18 and 19. The ultrasonic sensor is connected to pins 13 (trig) and 14 (echo).

2. Control Functions: Several functions are defined to control the bot's movement. These functions include moving the bot forward, backward, left, right, left backward, and right backward. Each function adjusts the servo motor speeds accordingly.

3. Main Loop: The main loop runs continuously and performs the following steps:

   - Ultrasonic Distance Measurement: The code measures the distance using the ultrasonic sensor connected to the trig and echo pins. It calculates the distance based on the time taken for the ultrasonic pulse to travel and returns the distance in centimeters.

   - QTI Sensor and IR Sensor Inputs: The code reads the inputs from the QTI sensors and IR sensors. It determines the sensor patterns and detects whether an object is present based on the threshold values.

   - Bot Navigation: The code uses conditional statements to control the bot's behavior based on the sensor inputs and detected patterns. It defines different actions for various scenarios, including moving forward, turning left, turning right, moving backward, and random turning.

   - Display and Delay: The code displays appropriate messages and images on the Microbit's LED display to indicate the bot's current behavior. It also introduces random delays for certain actions using the sleep() function.

4. Custom Bumper: The README mentions the use of a custom 3D-printed bumper designed using AutoCAD. The bumper enhances the bot's physical design and provides additional protection or functionality.

Please ensure that you have the necessary hardware components and dependencies installed before running the code. Modify the code as needed to adjust the motor speeds, sensor thresholds, or other parameters based on your specific requirements.

## Acknowledgments 🫴

This project was built in the TEJ4M0 course for the SumoBot competition. The 3D-printed custom bumper enhances the bot's design and showcases the integration of hardware and software components. Please look at the TinkerCAD circuit as well as the SumoBot images in the repository for a better idea of what the project is :)

Feel free to explore and experiment with the code, hardware, and customization options to create your own unique bot project!

