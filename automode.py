#!/usr/bin/python3

import sys
import subprocess
import time
import miio.airpurifier
import os

IP = "Enter here your Purifier IP"
token = "Enter here your Purifier Token"
MiAir = miio.airpurifier.AirPurifier(IP, token)

#######
while True:

	os.system('clear')
	aqi = MiAir.status().aqi
	print (time.ctime())
	print ("PM 2.5: ", aqi, "ug/m3")
	if (aqi > 160):
		print ("Power: 16")
		MiAir.set_favorite_level(16)
		
	elif (aqi > 140):
		print ("Power: 14")
		MiAir.set_favorite_level(14)

	elif (aqi > 120):
		print ("Power: 12")
		MiAir.set_favorite_level(12)
		
	elif (aqi > 90):
		print ("Power: 10")
		MiAir.set_favorite_level(10)
			
	elif (aqi > 50):
		print ("Power: 8")
		MiAir.set_favorite_level(8)
			
	elif (aqi > 35):
		print ("Power: 5")
		MiAir.set_favorite_level(5)
	
	elif (aqi > 30):
		print ("Power: 5")
		MiAir.set_favorite_level(5)
	
	elif (aqi > 24):
		print ("Power: 4")
		MiAir.set_favorite_level(4)
	
	elif (aqi > 18):
		print ("Power: 3")
		MiAir.set_favorite_level(3)

	elif (aqi > 10):
		print ("Power: 2")
		MiAir.set_favorite_level(2)
		dif = aqi + 4
		
	elif (aqi > 5):
		print ("Power: 2")
		MiAir.set_favorite_level(2)
		
	elif (aqi <= 4):
		print ("Power: 1")
		MiAir.set_favorite_level(1)
	print ("Sleep 120s")
	time.sleep(120)
	
		

