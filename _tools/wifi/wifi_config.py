#! /usr/bin/python3
# main.py
import sys
import subprocess
import os
import iw_parse
import re
from wifi import Wifi

wifis = []

def main():
    if len(sys.argv)>= 2:
        if sys.argv[1] == "--ssid" or sys.argv[1] == "-s":
            listWifi()

        elif (sys.argv[1] == "--connect" or sys.argv[1] == "-c") and len(sys.argv) == 4:
            ssid = sys.argv[2]
            psk = sys.argv[3]
            wifi = Wifi()

            p = scanWifi()


            wifi = next((x for x in wifis if x.ssid == ssid), None)
            if wifi != None:
                wifi.password = psk

                wifi.connect()
                print(wifi.ssid)
                print(wifi.channel)
                print(wifi.signal)
                print(wifi.encryption_type)

            else:
                print("SSID not found.")
        else:
                print("Wrong command.")


def listWifi():
        stream = os.popen("sudo iwlist wlan0 scan | grep ESSID: | sed 's/.*ESSID:\"//' | sed 's/.$//' | sort | uniq").read().split()
        for line in stream:
                if("\\x00\\x00\\x00" not in line):
	                print(line)
#        print(stream)


def scanWifi():
    content = iw_parse.scan(interface='wlan0')
    cells = iw_parse.parse(content)


    isFirstWifi = True
    wifi = Wifi()

    for cell in cells:
        if re.search('channel', str(cell)) is not None:
            if isFirstWifi == True:
                isFirstWifi = False

            if isFirstWifi == False:
                wifis.append(wifi)

            wifi = Wifi()

            tempchannel = re.search("'channel': '(.*)', 'signal_quality':", str(cell))
            wifi.channel = tempchannel.group(1).strip("\'")
            #print(wifi.channel)

        if re.search('signal_level_dBm', str(cell)) is not None:
            tempsignal_level = re.search("'signal_level_dBm': '(.*)', 'encryption':", str(cell))
            wifi.signal = tempsignal_level.group(1).strip("\'")
            #print(wifi.signal)

        if re.search('encryption', str(cell)) is not None:
            tempencryption = re.search("'encryption': '(.*)', 'essid':", str(cell))
            wifi.encryption_type = tempencryption.group(1).strip("\'")
            #print(wifi.encryption_type)

        if re.search('essid', str(cell)) is not None:
            tempssid = re.search("'essid': '(.*)'}", str(cell))
            wifi.ssid = tempssid.group(1).strip("\'")
            #print(wifi.ssid)

if __name__ == '__main__':
    main()


