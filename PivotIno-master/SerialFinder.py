import serial.tools.list_ports  # For listing available serial ports

dev = serial.tools.list_ports.comports()
ports=[]

for d in dev:
    ports.append((d.device, d.serial_number))
print('\nDetected serial ports:')
for d in ports:
    print("Port:" + str(d[0]) + "\tSerial Number:" + str(d[1]))
