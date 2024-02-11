import network
import time

station = network.WLAN(network.STA_IF)
station.active(True)

#station.connect("TP-Link_900E_5G", "nba14135")
station.connect("HUAWEI Y9 Prime 2019", "20553102")
time.sleep(3)
print("Connection :",station.isconnected())
print("Configuration :",station.ifconfig())


