#Importing the libraries
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as paho

#Set the pin numbering mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Assign the LEDS to pins
RedLED = 21;
GreenLED = 12;
BlueLED = 6;

#set the pins as output
GPIO.setup(RedLED,GPIO.OUT)
GPIO.setup(GreenLED,GPIO.OUT)
GPIO.setup(BlueLED,GPIO.OUT)

#Initialize the values to zero/Low
GPIO.output(RedLED, 0)
GPIO.output(RedLED, 0)
GPIO.output(RedLED, 0)

#Callback fn to call on subscribe
def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribed: "+str(mid)+" "+str(granted_qos))

#callback fn to call on receiving a msg from a subscribed topic
def on_message(client, userdata, msg):
	#Reset the pin values to zero
	GPIO.output(GreenLED,GPIO.LOW)
	GPIO.output(BlueLED,GPIO.LOW)
	GPIO.output(RedLED,GPIO.LOW)
	print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
	
	#Check the Values using if else meaning High indicating ON and Low indicating OFF
	if str(msg.payload).strip().lower() == 'red':
		GPIO.output(RedLED,GPIO.HIGH)
	elif str(msg.payload).strip().lower() == 'green':
		GPIO.output(GreenLED,GPIO.HIGH)
	elif str(msg.payload).strip().lower() == 'blue':
		GPIO.output(BlueLED,GPIO.HIGH)
	elif str(msg.payload).strip().lower() == 'all':
		GPIO.output(GreenLED,GPIO.HIGH)
		GPIO.output(BlueLED,GPIO.HIGH)
		GPIO.output(RedLED,GPIO.HIGH)
	elif str(msg.payload).strip().lower() == 'none':
		GPIO.output(GreenLED,GPIO.LOW)
		GPIO.output(BlueLED,GPIO.LOW)
		GPIO.output(RedLED,GPIO.LOW)

try:
	#Initialize the MQTT Client and callback functions
	client = paho.Client()
	client.on_subscribe = on_subscribe
	client.on_message = on_message
	#Host/Broker and port
	client.connect("iot.eclipse.org", 1883)
	#Topic and Qos
	client.subscribe("hari/ledstatus", qos=1)
	client.loop_forever()
except:
	pass
finally:
	GPIO.cleanup() 