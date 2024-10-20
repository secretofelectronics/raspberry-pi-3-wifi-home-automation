import RPi.GPIO as gpio        # Import the RPi.GPIO library for controlling GPIO pins
from flask import Flask        # Import the Flask framework to create a web server

app = Flask(__name__)          # Create a Flask application instance

# Set the GPIO pin numbering mode to BOARD, which uses the physical pin numbers on the Raspberry Pi
gpio.setmode(gpio.BOARD)

# Set up physical pins 3, 5, 7, and 8 as output pins
gpio.setup(3, gpio.OUT)
gpio.setup(5, gpio.OUT)
gpio.setup(7, gpio.OUT)
gpio.setup(8, gpio.OUT)

# Define global variables to track the states of four LEDs (True = ON, False = OFF)
global state1
global state2
global state3
global state4

# Initialize the states of all LEDs to True (ON)
state1 = True
state2 = True
state3 = True
state4 = True

# Define a route for controlling the LED connected to physical pin 3
@app.route('/led1')
def fun1():
    global state1  # Declare that we're modifying the global state1 variable
    if state1:     # If the LED is currently ON
        state1 = False  # Turn it OFF
    else:
        state1 = True   # Otherwise, turn it ON
    gpio.output(3, state1)  # Set the state of physical pin 3 to the new state
    return f'The LED on pin 3 is set to {state1}'  # Return a message showing the current state

# Define a route for controlling the LED connected to physical pin 5
@app.route('/led2')
def fun2():
    global state2  # Declare that we're modifying the global state2 variable
    if state2:     # If the LED is currently ON
        state2 = False  # Turn it OFF
    else:
        state2 = True   # Otherwise, turn it ON
    gpio.output(5, state2)  # Set the state of physical pin 5 to the new state
    return f'The LED on pin 5 is set to {state2}'  # Return a message showing the current state

# Define a route for controlling the LED connected to physical pin 7
@app.route('/led3')
def fun3():  # Note: function name was corrected to avoid duplicate function names
    global state3  # Declare that we're modifying the global state3 variable
    if state3:     # If the LED is currently ON
        state3 = False  # Turn it OFF
    else:
        state3 = True   # Otherwise, turn it ON
    gpio.output(7, state3)  # Set the state of physical pin 7 to the new state
    return f'The LED on pin 7 is set to {state3}'  # Return a message showing the current state

# Define a route for controlling the LED connected to physical pin 8
@app.route('/led4')
def fun4():  # Note: function name was corrected to avoid duplicate function names
    global state4  # Declare that we're modifying the global state4 variable
    if state4:     # If the LED is currently ON
        state4 = False  # Turn it OFF
    else:
        state4 = True   # Otherwise, turn it ON
    gpio.output(8, state4)  # Set the state of physical pin 8 to the new state
    return f'The LED on pin 8 is set to {state4}'  # Return a message showing the current state

# Run the Flask web application, allowing users to control the LEDs via the defined routes
app.run()