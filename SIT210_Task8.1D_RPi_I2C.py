#lovleen kala 

# Import necessary libraries
import smbus  # This library is used for I2C communication
import time   # This library is used for time-related functions

# Define BH1750 sensor constants
BH1750 = 0x23  # I2C Address of the BH1750 sensor
CONTINUOUS_HIGH_RES_MODE_1 = 0x10  # This code corresponds to a specific mode of the sensor

# Initialize the SMBus (I2C) communication on bus 1
bus = smbus.SMBus(1)  # Initialize communication on I2C bus 1

# Function to read light intensity from the BH1750 sensor
def ReadBH1750(device_address):
    # Read data from I2C interface
    data = bus.read_i2c_block_data(device_address, CONTINUOUS_HIGH_RES_MODE_1)  # Read data from the sensor
    # Calculate light intensity in lux based on sensor data format and sensitivity
    result = (data[1] + (256 * data[0])) / 1.2  # Calculate light intensity based on the sensor's data format and sensitivity
    return result

# Main program
try:
    # Continuous loop for monitoring light level
    while True:
        # Read light level from the BH1750 sensor
        LightLevel = ReadBH1750(BH1750)  # Call the ReadBH1750 function and get the light level
        
        # Determine the light level category and print an appropriate message
        if LightLevel < 5:
            print("Too Dark")  # If light level is less than 5 lux, print "Too Dark"
        elif LightLevel < 10:
            print("Dark")  # If light level is between 5 and 10 lux, print "Dark"
        elif LightLevel < 20:
            print("Medium")  # If light level is between 10 and 20 lux, print "Medium"
        elif LightLevel < 25:
            print("Bright")  # If light level is between 20 and 25 lux, print "Bright"
        else:
            print("Too Bright")  # If light level is greater than or equal to 25 lux, print "Too Bright"
        
        # Pause for 1 second before the next reading
        time.sleep(1)  # Pause the program for 1 second
                
except KeyboardInterrupt:
    # Handle keyboard interrupt by cleaning up GPIO
    GPIO.cleanup()  # If a keyboard interrupt occurs, clean up GPIO (even though it's not used in this code)
