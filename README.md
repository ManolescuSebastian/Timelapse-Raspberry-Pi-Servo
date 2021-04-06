# Timelapse-Raspberry-Pi-Servo
Raspberry pi project with camera and servo motors that is used for time lapses and temperature value read


-----------------------------------

<h2><b>Project in progress</b></h2>

-----------------------------------

Timelapse Demo
-----
Will be added soon

Breadboard
-----
<img src="https://github.com/ManolescuSebastian/Timelapse-Raspberry-Pi-Servo/blob/main/readme_resources/raspberry_pi_timelapse_bb.png" width="81%"></img>

Components
-----
* 1 x Raspberry pi
* 1 x Camera
* 2 x Servo motors
* 1 x DHT11 temperature-humidity sensor
* 1 x prototype pcb
* 1 x 40 pin gpio connector header


Pin connections
-----

Raspberry Pi | Components
------------ | -------------
GPIO 17 | Servo Motor 1
GPIO 27 | Servo Motor 2
GPIO 22 | DHT11
GPIO 2 | VCC
GPIO 1 | GND
 
Run commands and install requirements
------
pip3 install -r requirements.txt        
sudo apt-get install libgpiod2

Run application on home network
-----
Open terminal and type <b>python main.py</b> or <b>python3 main.py</b>

License
------
         

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
