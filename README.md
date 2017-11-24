# Control RGB LED using MQTT with Raspberry Pi 3
Control your RGB LEDs on a Raspberry Pi using MQTT Protocol from your Mobile Application

## Project Overview

This Project will help you remotely control the RGB LEDs using MQTT protocol with  Raspberry pi 3.

MQTT is a Client Server publish/subscribe messaging transport protocol. It is light weight, open, simple, and designed so as to be easy to implement. These characteristics make it ideal for use in many situations, including constrained environments such as for communication in Machine to Machine (M2M) and Internet of Things (IoT) contexts where a small code footprint is required and/or network bandwidth is at a premium.

Check more details on MQTT [here.](https://www.hivemq.com/blog/mqtt-essentials-part-1-introducing-mqtt)

## Flow chart of the Demo:

![led_mqtt 3](https://user-images.githubusercontent.com/29800208/33128344-1764569a-cfb2-11e7-9670-14cc931bb3a8.png)

## Basic Steps:

1. Basic Installation setup of Raspberry Pi 3
2. Connect the LEDs to the Raspberry Pi 3
3. Configuring the MQTT Dashboard App on Android
4. Programming the Raspberry Pi

## Requirements

### Hardware

1. Raspberry pi 3 (with Raspbian Jessie OS)
2. Micro-USB cable for power
3. Breadboard
4. RGB LEDs(3 Separate Color LEDs or a Single RGB LED)
5. Three 330 Ohm resistors
6. Jumper wires
7. HDMI cable/ LAN Cable to program

### Software

- Python

```sh
sudo apt-get update
sudo apt-get install python3
```

- Clone the Git repository
```sh
git clone https://github.com/Hariharnath-Paduchuru/MQTT_Controlled_RGB_LED_RaspberryPi_Demo
```

The latest stable version is available in the Python Package Index (PyPi) and can be installed using

    pip install paho-mqtt

Or with ``virtualenv``:

     virtualenv paho-mqtt
     source paho-mqtt/bin/activate
     pip install paho-mqtt

 To obtain the full code, including examples and tests, you can clone the git repository:

     git clone https://github.com/eclipse/paho.mqtt.python

 Once you have the code, it can be installed from your repository as well:

    cd paho.mqtt.python
    python setup.py install

### Step 1:

- Setup the Raspberry pi as per the initial setup mentioned [here](https://raspberrypihq.com/booting-the-raspberry-pi-for-the-first-time/)

### Step 2:

- Connecting Raspberry pi with RGB LEDs. Make the connections as mentioned in the below pictures.

![led_connection12](https://user-images.githubusercontent.com/29800208/33161001-b3c737e8-d046-11e7-9e8a-203de5346b97.png)


#### Note:  The Pin positions connected to the Raspberry pi in the above image is for representational Purpose only, follow the pin numbers and below pinout image to connect the LEDs to the exact position

- Power up your raspberry pi, take a breadboard, LEDs, Resistors and jumper wires.

- LEDs are a very useful, cheap, and efficient way of producing light, but you do have to be careful how you use them. If they are connected directly to a voltage source (such as a GPIO output) that is greater than about 1.7 volts, they will draw a very large current. This can often be enough to either destroy the LED or whatever is providing the current—which is not good if your Raspberry Pi is providing the current.

- They have a long leg and a slightly shorter leg. The **long leg goes to the plus side with Resistor in series** and the **shorter leg to the negative (or 0v) side/Ground**. If we&#39;ve cut the legs short, then another way is to look at the side of the LED glass – there will be a flat section. Think of the flat as a minus sign and connect that to the 0v side of the circuit.

![Raspberry pi pinout](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png)

- The resistor is a 330 Ohm connected in between long leg or plus side of LED and the respective GPIO Pins
  - Red LED is connected to the GPIO 21 of pi
  - Green LED is connected to GPIO 12 of pi
  - Blue LED is connected to GPIO 6 of pi
  - Ground can be connected to any Ground pins available on Pi(39,6,9,etc)


The Final Setup should look like this 

![rgbled](https://user-images.githubusercontent.com/29800208/33162042-6d72cbfc-d04d-11e7-8bcf-882c14b86b80.jpg)

### Step 3:
 
Download the App in Play Store : IoT MQTT Dashboard

[https://play.google.com/store/apps/details?id=com.thn.iotmqttdashboard&amp;hl=en](https://play.google.com/store/apps/details?id=com.thn.iotmqttdashboard&amp;hl=en)

1. Open the app and click on the + icon to create a new client and fill the details as per the below screenshot

2. Open the Created Client and under the Publish Tab, Click on the + Icon to add the Component.

![screenshots1](https://user-images.githubusercontent.com/29800208/33159561-fd22e37c-d039-11e7-845b-39f38d7fd766.png)

3. Select Text Component from the list

4. Fill the details for the properties of text components as per the below screenshot and Create

![screenshots2](https://user-images.githubusercontent.com/29800208/33159562-ffac76f8-d039-11e7-9e29-7f0dc1a1d779.png)

5. Now enter the Text such as Red,Green,Blue,None,All in the text field to publish a message

6. You can see the message being published as shown in the marked area

![screenshots3](https://user-images.githubusercontent.com/29800208/33159564-0376725c-d03a-11e7-98fb-18a26dcb6f1c.png)

   If you want to create the Button instead of text, Select Button in Step 3 and skip the steps 4 to 6.

7. Select the Button Component from the List and fill the details as per the below screenshot

8. You can now view both text and Button in this screenshot, click on the button created to publish a message

![screenshots4](https://user-images.githubusercontent.com/29800208/33159566-05171954-d03a-11e7-917a-ead45ec4777d.png)

9. This is the fully developed application where all the buttons are created to publish a message.

   ![screenshots5](https://user-images.githubusercontent.com/29800208/33159567-066f9240-d03a-11e7-9e5b-8e10fa820641.png)

### Step 5:

Open the console in Raspberry pi

    cd

Clone the git Repo if not done earlier

```sh
git clone https://github.com/Hariharnath-Paduchuru/MQTT_Controlled_RGB_LED_RaspberryPi_Demo

ls MQTT_Controlled_RGB_LED_RaspberryPi_Demo

sudo nano RGBLEDControl_v2.py
```

Check if the topic mentioned here is same as you have subscribed, If not modify the file and click on ctrl + o and ctrl + x

```sh
sudo python RGBLEDControl_v2.py
```


Now open the MQTT Dashboard app in the mobile and Click on the Buttons or write the appropriate text to send the message and control the LEDs
