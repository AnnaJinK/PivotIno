
# @ file PivotInoBLE.py
# @ author Heejoong 
# @ 2019-01-16 ~
# @ 2019-01-27 edit? baud rate and rename some variables
# @ 2019-01-28 edit? import win32 using DEVMODE(Structures) add def rotateTO()
# @     "      edit? referred from "https://docs.microsoft.com/ko-kr/previous-versions/ms812499(v=msdn.10)"
# @     "      edit? and "https://docs.microsoft.com/ko-kr/windows/desktop/api/winuser/nf-winuser-changedisplaysettingsexa"
# @     "      edit? No longer using additional third-party application(display.exe)
# @ 2019-02-02 edit? waitForSerialInit() From now on, waitForSerialInit () function will automatically find the Arduino Uno devices.
# @ 2019-04-30 this program for Arduino Pro Mini 3.3v This device communicates using Bluetooth. Therefore, com_port search function(using S/N) has been removed. ('^ ';)
 
import win32api as win32
import win32con
import serial
import string
import time
import traceback

def initSerial(device_Port):
    serialFromArduino = serial.Serial(device_Port, 115200, timeout=1, xonxoff=False, rtscts=False, dsrdtr=False)
    serialFromArduino.flushInput()
    serialFromArduino.flushOutput()
    return serialFromArduino

# Changing Screen Orientation Programmatically
def rotateTO(rotateDic):
    display_num = 0 # display 1
    device = win32.EnumDisplayDevices(None,display_num)
    dm = win32.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
    if 0 != dm:
        dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
        dm.DisplayOrientation = int(rotateDic/90)
        iRet = win32.ChangeDisplaySettings(dm, 0);
    if win32con.DISP_CHANGE_SUCCESSFUL != iRet:
        print("Failed(Already) to rotate "+str(rotateDic)+" degrees")
    return win32.ChangeDisplaySettingsEx(device.DeviceName,dm)
# this code referred from "https://docs.microsoft.com/ko-kr/previous-versions/ms812499(v=msdn.10)"


def waitForSerialInit():
    com_Port = ["COM7"]
    while True:
        for device_Port in com_Port:
            try:
                serialFromArduino = initSerial(device_Port)
                print("device found on " + device_Port)
                return serialFromArduino
            except Exception:
                print("Failed to device on " + device_Port)
        time.sleep(5)

# if you want just add "Flip":"180"
rotateDic = {"Right":"90", "Idle":"0", "Left":"270"}

Serial_OP = "Rotate <"
Serial_ED = ">"

serialFromArduino = waitForSerialInit()

while True:
    try:
        line = serialFromArduino.readline().decode("utf-8")
    except Exception:
        print("I have a bad feeling about this..")
        traceback.print_exc()
        print("Something wrong, Check your device.!")
        time.sleep(5)
        print("trying to initialise serial..")
        serialFromArduino = waitForSerialInit()
        continue

    if line == "":
        continue

    print("line: " + line)

    if line.find(Serial_OP) == 0:
        
        direction = line.replace(Serial_OP,"")
        direction = direction[0:direction.find(Serial_ED)]
        print("direction: " + direction)

        if direction in rotateDic:
            print("Display rotate to : " + rotateDic[direction])
            rotateTO(int(rotateDic[direction]))
        else:
            print("invalid direction: " + direction)
            print("ignoring")
