# Pivotino

Display auto rotation device  
Auto Pivot using Arduino  

Pivtino automatically rotates the monitor screen through serial communication with PC.

```c
serialDic={'5':'5','6':'6'}  # You should put your Arduino serial number in this dictionary.

def waitForSerialInit():
    #print("\n=Currently available Arduino Uno devices=")
    while True:
        for arduino in serial.tools.list_ports.comports():
            if arduino.vid == 9025 and arduino.pid == 67: # Arduino Uno vid & pid***
            # This program uses the vid & pid of Adunino Uno. 
            # For this reason, you need to modify the code to match the code you use.
                sn = arduino.serial_number
                
                #print("*S/N : [" + sn + "]" )
                if sn in serialDic:
                    print("\nConnected to serial number [" + sn + "]" )
                    arduDev = arduino.device
                else:
                    arduDev = "anywhere"

        com_Port = [str(arduDev)]

        for device_Port in com_Port:
            try:
                serialFromArduino = initSerial(device_Port)
                print("device found on " + device_Port)
                return serialFromArduino
            except Exception:
                print("Failed to device on " + device_Port)
        time.sleep(5)

```  



Add the shortcut to the startup program.
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp  

# Updadte
### 2019-01-27 
edit? baud rate and rename some variables
### 2019-01-28 
edit? import win32 using DEVMODE(Structures) add def rotateTO()
edit? referred from "https://docs.microsoft.com/ko-kr/previous-versions/ms812499(v=msdn.10)"
edit? and "https://docs.microsoft.com/ko-kr/windows/desktop/api/winuser/nf-winuser-changedisplaysettingsexa"
edit? No longer using additional third-party application(display.exe)
### 2019-02-02
edit? waitForSerialInit() From now on, waitForSerialInit () function will automatically find the Arduino Uno devices.


# Credits
Changes were made by Heejoong Kim (in 2019) 

