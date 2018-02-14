# Display-IP
Displaying the Raspberry Pi IP Address on boot time with the PaPiRus

# Initialization
If you haven't already, go to [PaPiRuS Github Page](https://github.com/PiSupply/PaPiRus) and setup PaPiRus on the Raspberry Pi

# Boot Time
Navigate to:
```
$ sudo vim /etc/profile
```
Add the full python script path to the bottom of the text file:
```
sudo python /your_directory_path_to_the_script/ip.py
```
Save and exit the text file by hitting _esc_ and then entering _:wq_

Shutdown or reboot the Raspberry Pi to see the IP Address on the screen

# Kill Script
Aftering getting your IP address for the Raspberry Pi, you might want to kill the script. To do that, open the terminal and enter the following command:
```
$ ps aux | grep -i python
```
Find the python script and kill it by entering the PID number
```
sudo kill <PID_Number>
```
The PID number is the second column in the row, it next to either _pi_ or _root_

Or if this is the only python script running,
```
sudo killall python
```
This will kill all the python scripts
