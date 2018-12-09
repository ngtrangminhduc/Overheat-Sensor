# An Overheat Sensor with Raspberry Pi and HDC1008 sensor 

## Table of Contents

I. [Introduction](#Introduction)

II. [Overheat Sensor Materials](#Overheat%Sensor%Materials)

III. [Overheat Sensor Schedule](#Overheat%Sensor%Schedule)

IV. [Overheat Sensor Assembly](#Overheat%Sensor%Assembly)

V. [Overheat Sensor Power Up + Testing](#Overheat%Sensor%Power%Up%And%Testing)

VI. [Image Creation and Enterprise Wifi](#Image%Creation%And%Enterprise%Wi-Fi)


### I. Introduction

Raspberry Pi gets overheat easily when combined with other components, and can hardly be noticed if put inside cases. Internal hardware can be damaged if no immediate resolutions are taken.

HDC1008 is a Temperature and Humidity sensor that can solve the problem. It8 has a wide range of temperature with +-0.2 Celsius degree, making it a very accurate sensor to detect any temperature change, and to ensure a spontaneous reaction from the users. Its low power consumption and two operation modes (sleep and measurement) allow itself to fit battery / power harvesting applications.

**Note**: This sensor is now classified as **Obsolete** in most of electronic websites, due to the coming of many new upgraded sensors

The whole operation of the project can be demonstrated through this XML diagram: 

![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Documentation/Pseudo%20Code%20and%20XML/UML%20Diagram.jpg)

For convenient purposes, this documentation will focus mainly on the production of the sensor only. 

 
### II. Overheat Sensor Materials

The components for this project are:
- Raspberry Pi 3B+
- HDC1008 Temperature & Humidity Sensor  
- PCB
- I2C LED Screen (Optional)
![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Images/IMG_8704.JPG)

- 6-pin headers
- 2x20-pin header

![alt text](https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master/2018_Images/6PinsStackableHeader.jpg)
![alt text](https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master/2018_Images/2x20Pins.jpeg)

The softwares for this project are:
- Remote Desktop Connection / VNC Viewer
- Fritzing (for designing purposes) (can be freely used in the Lab)
- CorelDraw (for designing purposes) (can be freely used in the Lab)

Total budget for this project is approximately 190$. More details can be found in the <a href="https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master/2018_Documentation/Proposal%2C%20Budget%2C%20Project%20Schedule/Budget.xlsx">budget</a>.

The HDC1008 sensor should be ordered as soon as possible, as it may take up 2 weeks to 1 month due to its unpopularity

### III. Overheat Sensor Schedule
Overall, if all materials are present, then it should not take more than 3 days to build a complete, functional product. Most of the time will be spent on installing the SD card and building the case for the Raspberry Pi, while the coding is rather simple.

This is the schedule I followed for the whole semester

![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Documentation/Proposal%2C%20Budget%2C%20Project%20Schedule/Project%20Schedule.jpg)

### IV. Overheat Sensor Assembly

#### IV.1 Printed Circuit Board

A PCB is required to connect the Sensor to the Raspberry Pi without using jumper wires and such. The design file of PCB can be found <a href="https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master/2018_Documentation/Fritzing/DucNguyen_HDC1008.zip">here</a>.
This is the Breadboard view of the project:

![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Documentation/Fritzing/DucNguyen_HDC1008_bb.jpg)

The PCB View was designed, based on the Breadboard View by using Fritzing.

![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Documentation/Fritzing/DucNguyen_HDC1008_pcb.png)

Soldering can be done in the Lab, which may take you 30mins to 2hours, depends on how comfortable you are in soldering:

![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Images/IMG_8708.JPG)

This is the finished PCB

![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Images/PCB_1.jpg)
![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Images/PCB_2.jpg)

#### IV.2 Raspberry Pi Case

The design file of Raspberry Pi Case can be found in I drive --> DropBoxes --> mdrk0011 --> Pickup --> CENG317 --> Pi2CaseX7.cdr . The case should be redesigned based on the Pi's new size (when the PCB is attached) + its functionality. Kelly and Vlad in the Prototype Lab are very informative and helpful on assisting students with using CorelDraw.

My design file can be found here  <a href="https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master//2018_Documentation/Pi%20Case%20-%20Overheat%20Sensor.cdr">here</a>. This is a picture of the design in CorelDraw 

![alt text](https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master/2018_Images/RaspberryPiCase.jpg)

The file should be emailed to the Prototype Lab (prototypelab@humber.ca). The case will be laser cut and completed in 1-2 days time. 

![alt text](https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master/2018_Images/RaspberryPiandCase.jpg)

This is the final product when everything's assembled together

![alt text](https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master/2018_Images/RaspberryPiComplete.jpg)

### V. Overheat Sensor Power Up and Testing

This is the first power up time of the Overheat Sensor. Connections are properly made by looking at the pinout of the Raspberry Pi

![alt text](https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master/2018_Images/IMG_8826.JPG)

This is the output. Temperature and Humidity are shown every 0.5s. The sensor works fine under 0x40. It can work under 0x41 or 0x42 as well if it is **manufactured by Adafruit**. The souce code can be found <a href="https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master//2018_SourceCode/hdc1008.py">here</a>

![alt text](https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master/2018_Images/RaspberryPiInAction.jpg)

![alt text](https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master/2018_Images/PythonCode2.png)


### VI. Image Creation and Enterprise Wi-Fi

#### VI.1 Image Creation

1. Format an at least class 10 minimum of 8GB SD card with: https://www.sdcard.org/downloads/formatter_4/index.html With SD Card Formatter (https://www.sdcard.org/downloads/formatter_4/)

2. Download, unzip, and copy the folder contents of http://downloads.raspberrypi.org/NOOBS/images/NOOBS-2017-08-17/NOOBS_v2_4_3.zip into the SD card

3. Insert the SD Card into the Raspberry Pi. For first time usage, a HDMI cable and a separate screen is required. 

**Note: The SD Card is now readable by only the Raspberry Pi. By re-inserting the SD card back into your PC, there's a high chance of corrupting the SD card and resulting in re-installation**

4. Perform necessary update as instructed by the Pi.

5. Open the terminal in the top left corner of the screen and input the following lines (this takes quite a long time):

wget https://raw.githubusercontent.com/six0four/StudentSenseHat/master/firmware/hshcribv01.sh \  
-O /home/pi/hshcribv01.sh  
chmod u+x /home/pi/hshcribv01.sh  
/home/pi/hshcribv01.sh

**Note: If there's error running the code, you can download the script <a href="https://raw.githubusercontent.com/ngtrangminhduc/OverheatSensor/master//2018_SourceCode/hshcribv01.sh">here</a> and run it manually on your pi**

6. Reboot


#### VI.2 Enterprise Wi-Fi

It will be more convenient to connect to the Raspberry Pi through Wi-Fi. This is the instruction for connection the Raspberry Pi to the Humber Wifi:

1.  In /etc/network/interfaces:
	```
	auto lo
	iface lo inet loopback
	iface eth0 inet dhcp
	allow-hotplug wlan0
	iface wlan0 inet manual
	wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
	iface default inet dhcp
	```

2.  In /etc/wpa_supplicant/wpa_supplicant.conf:

    ```
	sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
	```

    ```
	# sample network configuration for Humber College myWi-Fi
	# change text in <> to your account values (remove the < and > while doing this )
	network={
		ssid="myWi-Fi@Humber"
		key_mgmt=WPA-EAP
		auth_alg=OPEN
		eap=PEAP
		identity="<YourHCNetID>"
		password="<YourHCnetPassword>"
		phase1="peaplabel=0"
		phase2="auth=MSCHAPV2"
		priority=999
		proactive_key_caching=1
	}

	# Sample network configuration for joining Eduroam Wi-Fi network
	# change text in <> to your account values (remove the < and > while doing this )
	network={
		ssid="eduroam"
		scan_ssid=1
		key_mgmt=WPA-EAP
		eap=PEAP
		identity="<YourHCnetID>@humber.ca"
		password="<YourHCnetPassword>"
		phase1="peaplabel=0"
		phase2="auth=MSCHAPV2"
		proactive_key_caching=1

	}

	# Sample network configuration for joining a home wi-fi network.
	# change text in <> to your network values (remove the < and > while doing this )
	network={
		ssid="<yourNetworkSSID"
		psk="<yourNetworkPassword>"
		proto=RSN
		key_mgmt=WPA-PSK
		pairwise=CCMP
		auth_alg=OPEN
	}

	#Sample networtk configuration for joining open, unsecured network
	network={
		ssid="<yourNetworkSSID>"
		key_mgmt=NONE
	}
	```

3.  Download Humber Certificate (For HumberSecure).cer from https://its.humber.ca/wireless/humbersecure/

4.  Reboot

5. If you have trouble connecting the Pi through Ethernet Cable, it's best to use Advanced IP Scanner and search for the Pi's IP Address.
