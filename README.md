# An Overheat Sensor with Raspberry Pi and HDC1008 sensor

## Table of Contents
1. [Introduction](#introduction)
2. [Overheat Sensor Specifications](#overheat-sensor-specifications)
3. [Overheat Sensor Design Files](#overheat-sensor-electronic-design-files)
4. [Overheat Sensor Assembly](#overheat-sensor-assembly)
5. [Student Raspberry Pi Image Creation and Test Code](#student-raspberry-pi-image-creation-and-test-code)
6. [Enterprise Wi-Fi](#enterprise-wi-fi)



### Introduction


### Overheat Sensor Specifications

	
###### Additional items that are only added to those devices in the Humber Parts Crib



### Overheat Sensor Electronic Design Files

1.  The Fritzing file is available here: <TBD>
2.  It has a breadboard view:
3.  It has a schematic view:
4.  It has a PCB view:
6.  A Bill Of Materials can be exported: [BOM]
7.  As well as Gerber files: [RS-274X](https://github.com/six0four/StudentSenseHat/blob/master/electronics/Gerber_RS-274X).

### Overheat Sensor Assembly

### Student Raspberry Pi Image Creation and Test Code

1.	Building the Humber image for the Sense Hat: [https://github.com/six0four/StudentSenseHat/blob/master/cribpisdcard.md](https://github.com/six0four/StudentSenseHat/blob/master/cribpisdcard.md)  
	Note that apt-get puts the installed packages into
    /var/cache/apt/archives/ so a zip of the files from there would
    complement the script used by these instructions.

5.  Open a terminal and type:
	```
	git clone https://github.com/six0four/StudentSenseHat.git
	cd StudentSenseHat/firmware
	gcc -Wall -o traffic2B traffic2B.c -lwiringPi
	sudo ./traffic2B
	```
	write to your blog what happens with your LED.
	
6.	From the Start Menu->Preferences->Raspberry Pi Configuration->Interfaces set I2C to Enabled.

7.	Return to your terminal and type:
    ```Shell
	make
	sudo ./ghmain
	```
	write to your blog what happens.

8.	You can read the OS date with:
    ```Shell
	date
	```
	You can set the OS date with:
	```Shell
	sudo date –s “29 AUG 1997 13:00:00”
	```
	You can write the OS date to the RTC with:
	```Shell
	sudo hwclock –w
	```
	You can read the RTC date with:
	```Shell
	sudo hwclock -r
	```
	
9.	Things to consider for your particular application: boot options (Gui to terminal), and permissions when auto mounting usb keys.
	
10.  Use <http://sourceforge.net/projects/win32diskimager/> to read the image
    into a file.

### Enterprise Wi-Fi

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
