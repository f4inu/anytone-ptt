#!/usr/bin/env python3

import BLE_GATT
from pyautogui import press

button_address = '00:1B:10:60:B0:2A'
button_uuid = '0000ff02-0000-1000-8000-00805f9b34fb'

def notify_handler(value):
	#print(f"Received: {bytes(value).decode('UTF-8')}")
	press(' ')

button = BLE_GATT.Central(button_address)
button.connect()
button.on_value_change(button_uuid, notify_handler)
button.wait_for_notifications()
