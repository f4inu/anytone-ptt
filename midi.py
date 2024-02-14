#!/usr/bin/env python3

# pip3 install BLE_GATT
# pip3 install mido
# pip3 install python-rtmidi

import BLE_GATT
import mido
from mido import Message

button_address = '00:1B:10:60:B0:2A'
button_uuid = '0000ff02-0000-1000-8000-00805f9b34fb'

outport = mido.open_output('Anytone virtual midi port', virtual=True)

msgOn = Message('note_on', note=60)
msgOff = Message('note_off', note=60)

def notify_handler(value):
	print(f"Received: {bytes(value).decode('UTF-8')}")
	btn_value = int.from_bytes(value, byteorder='little')
	print(btn_value)
	if btn_value == 211867225157:
		print('pressed')
		outport.send(msgOn)
	elif btn_value == 216162192453:
		print('released')
		outport.send(msgOff)


button = BLE_GATT.Central(button_address)
button.connect()
button.on_value_change(button_uuid, notify_handler)
button.wait_for_notifications()
outport.close()
