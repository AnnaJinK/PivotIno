# PivotIno

Display auto rotation device  
Auto Pivot using Arduino  

![pivotinogif1](https://user-images.githubusercontent.com/34006003/56954299-6ae33200-6b79-11e9-8809-79b16fbc414e.gif)

Pivtino automatically rotates the display screen through serial communication with PC.

### Required Python Library 
pip install pyserial  
pip install pypiwin32  

### Used hardware
BlunoBeetle, MPU6050 or  
Arduino Pro Mini 3.3v, MPU6050, HC-06

```c
serialDic={'5':'5','6':'6'}  # You should put your Arduino serial number in this dictionary.

def waitForSerialInit():
    #print("\n=Currently available Arduino Uno devices=")
    while True:
        for arduino in serial.tools.list_ports.comports():
            if arduino.vid == 9025 and arduino.pid == 67: # Arduino Uno vid & pid
            # This program uses the vid & pid of Adunino Uno. 
            # For this reason, you need to modify it with your device.
```  
Add the shortcut to the startup program.  
root : C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp  

# Updadte
### 2019-01-27 
edit? baud rate and rename some variables  
### 2019-01-28 
import win32 using DEVMODE(Structures) add def rotateTO()  
referred from "https://docs.microsoft.com/ko-kr/previous-versions/ms812499(v=msdn.10)" and "https://docs.microsoft.com/ko-kr/windows/desktop/api/winuser/nf-winuser-changedisplaysettingsexa"  
No longer using additional third-party application(display.exe)  
### 2019-02-02
From now on, waitForSerialInit () function will automatically find the Arduino Uno devices.  
### 2019-04-30
Added Arduino Pro Mini version of PivotIno. There is not much change in source code.  
[Blog]:https://annajin28.blogspot.com/2019/04/arduino.html "Arduino Pro Mini version"
# Credits
Changes were made by Heejoong Kim (in 2019) 

