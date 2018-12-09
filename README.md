# An Overheat Sensor with Raspberry Pi and HDC1008 sensor 

## Table of Contents

I. [Introduction](#introduction)

II. [Overheat Sensor Materials](#overheat-sensor-materials)

III. [Overheat Sensor Schedule](#overheat-sensor-schedule)

IV. [Overheat Sensor Assembly](#overheat-sensor-assembly)

V. [Overheat Sensor Power Up + Testing](#overheat-sensor-power-up-and-testing)

VI. [Image Creation and Enterprise Wifi](#image-creation-and-enterprise-wi-fi)

==============================================================================

### I. Introduction

HDC1008 
### II. Overheat Sensor Materials
	
###### Additional items that are only added to those devices in the Humber Parts Crib



### III. Overheat Sensor Schedule


### IV. Overheat Sensor Assembly
![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Documentation/Fritzing/DucNguyen_HDC1008_pcb.png)
![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Images/IMG_8704.JPG)
![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Images/IMG_8708.JPG)
![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Images/PCB_1.jpg)
![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Images/PCB_2.jpg)

### V. Overheat Sensor Power Up and Testing

![alt text](https://github.com/ngtrangminhduc/OverheatSensor/blob/master/2018_Images/PythonCode.png)

### VI. Image Creation and Enterprise Wi-Fi

Connecting to Enterprise Wi-Fi can be a challenge but the graphical desktop has come a long way from where it was, please share your respective successes in situations where the GUIs do not work - here is my configuration:

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
	ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
	update_config=1
	network={
        ssid="myWi-Fi@Humber"
        proto=RSN
        key_mgmt=WPA-EAP
        pairwise=CCMP
        auth_alg=OPEN
        eap=PEAP
        identity="n12345678"
        password="aaaAAA12"
        phase2="auth=MSCHAPV2"
	}
	```

	I have been told that more recently the Prototype Lab staff have said to use:
	```
	sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
	```

	Add the follow to file and fill in identity and password field save and restart RPI:
	```
	network={
	ssid="myWi-Fi@Humber"
	priority=999
	proto=RSN
	key_mgmt=WPA-EAP
	pairwise=CCMP
	auth_alg=OPEN
	eap=PEAP
	identity="STUDENT ID"
	password="PASSWORD"
	phase1="peaplabel=0"
	phase2="auth=MSCHAPV2"
	}
	```
	Even more recently the Prototype Lab staff have successfully tested the 
	following sample configuration file. The configuration includes sections 
	for Humber’s myWi-fi, Eduroam, home WPA encrypted networks, and open networks like “Welcome To Humber”.:
	```
	# Sample configuration file for Raspberry Pi to connect to various WiFi networks.
	# /etc/wpa_supplicant/wpa_supplicant.conf

	ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
	update_config=1
	country=CA

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
