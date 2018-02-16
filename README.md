# Display-IP
Displaying the Raspberry Pi IP Address on boot time with the PaPiRus

# Initialization
Visit [PaPiRuS Github Page](https://github.com/PiSupply/PaPiRus) and setup PaPiRus on the Raspberry Pi or you can run their  script to do an automatic setup/installation:
```
# Run this line and PaPiRus will be setup and installed
curl -sSL https://pisupp.ly/papiruscode | sudo bash
```
To do a manual setup/installation, you would need to visit [PaPiRuS Github Page.](https://github.com/PiSupply/PaPiRus)
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

Shutdown/reboot the Raspberry Pi to see the IP Address on the screen

# Kill Script
Aftering your IP address is displayed and are able to login to your Rasberry Pi, you might want to kill the script. 
### Automatic
If this is the only python script running,
```
$ sudo killall python
```
This will kill all the python scripts
### Manual
If this is the only script you want to kill, find the PID number and kill it. You can find the PID number by entering the following command:
```
$ ps aux | grep -i python
```
This will display all the python scripts running. You will want to find the script(s) that match the path you entered in your _/etc/profile_ file. After locating it, grab the PID number which is in the second column in every row, its next to either _pi_ or _root_ and enter the following command to kill that script:
```
$ sudo kill <PID_Number>
```
