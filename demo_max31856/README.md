# Set  your Python install to Python 3 Default
There's a few ways to do this, we recommend something like this

sudo apt-get install -y python3 git python3-pip
sudo update-alternatives --install /usr/bin/python python $(which python2) 1
sudo update-alternatives --install /usr/bin/python python $(which python3) 2
sudo update-alternatives --config python
# Enable I2C and SPI
A vast number of our CircuitPython drivers use I2C and SPI for interfacing so you'll want to get those enabled.

You only have to do this once per Raspberry Pi but by default both interfaces are disabled!

Enable I2C
Enable SPI
Once you're done with both and have rebooted, verify you have the I2C and SPI devices with the command

ls /dev/i2c* /dev/spi*

You should see the response

/dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1

sensors_ls.png
# Enabling Second SPI
If you are using the main SPI port for a display or something and need another hardware SPI port, you can enable it by adding the line

dtoverlay=spi1-3cs

to the bottom of /boot/config.txt and rebooting. You'll then see the addition of some /dev/spidev1.x devices:

sensors_image.png
# Make sure you're using Python 3!
The default python on your computer may not be python 3. Python 2 is officially discontinued and all our libraries are Python 3 only.

We'll be using python3 and pip3 in our commands, use those versions of python and pip to make sure you're using 3 and not 2

# Install Python libraries
Now you're ready to install all the python support

Run the following command to install the Raspberry PI GPIO library:

pip3 install RPI.GPIO

sensors_rpigpio.png
Run the following command to install adafruit_blinka

pip3 install adafruit-blinka

sensors_pip.png
The computer will install a few different libraries such as adafruit-pureio (our ioctl-only i2c library), spidev (for SPI interfacing), Adafruit-GPIO (for detecting your board) and of course adafruit-blinka

That's pretty much it! You're now ready to test.
# Blinka Test

```python
import board
import digitalio
import busio

print("Hello blinka!")

# Try to great a Digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")

# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")

print("done!")

