#! /usr/bin/python3
import sys
import os
import time

class Wifi:
    def __init__(self, channel=" ", signal=" ", ssid=" ", encryption_type=" ", password=" "):
        self.channel = channel
        self.signal = signal
        self.ssid = ssid
        self.encryption_type = encryption_type
        self.password = password

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    @property
    def signal(self):
        return self._signal

    @signal.setter
    def signal(self, value):
        self._signal = value

    @property
    def ssid(self):
        return self._ssid

    @ssid.setter
    def ssid(self, value):
        self._ssid = value

    @property
    def encryption_type(self):
        return self._encryption_type

    @encryption_type.setter
    def encryption_type(self, value):
        self._encryption_type = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,value):
        self._password = value


    def connect(self):
        if self._encryption_type != "off":
            os.popen('cat >/etc/wpa_supplicant/wpa_supplicant-wlan0.conf <<EOF\ncountry=CH\nctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\n\nnetwork={\n\tssid="%s"\n\tpsk="%s"\n\tkey_mgmt= %s\n}\nEOF' %(self._ssid, self._password, self._encryption_type))
            state = os.popen('wpa_cli -i wlan0 reconfigure').read()
            print(state)

            if state.rstrip() == "OK":
                time.sleep(5)

                status = os.popen('wpa_cli -i wlan0 status | grep wpa_state').read()
                status = status.split('wpa_state=', 1)[1]
                status = status.rstrip()


                if status == "COMPLETED":
                    os.popen("sed -i '/channel=/c\channel= %s' /etc/hostapd/hostapd.conf" %self._channel)
                    os.popen('systemctl daemon-reload')

                    print(status)

                else:
                    print("Password is incorrect, you lost the connection")

            else:
                print("Password is incorrect")

        else:
            print("Couldn't connect to Network")



