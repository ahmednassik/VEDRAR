# VEDRAR - Vehicle Event Data Recorder and Review System

VEDRAR is a combination of hardware technologies like proximity sensor, Arduino board and raspberry pi with software tecnologies like MySql database, Machine Learning etc.

The system aims to introduce a device that records the necessary driving data for a period of the drive with the aid of various sensors. The data is used to categorize the driver into a good or bad category of driving. The real-time data from sensors are fed into the system and stored in a memory. This data is processed and analyzed using machine learning algorithm to review the driver’s performance and evaluate his present status of driving skills. This categorization will be provided before the road transportation authority making it a criterion to pass the driving test.

According to WHO stats, traffic injuries caused an estimated 1.25 million deaths every year
i.e., 1 death/25 s. Apart from death, between 20-50 million people suffer from nonfatal injuries
resulting in permanent disability. Almost half of the traffic deaths are among pedestrians, cyclists
and motorcyclists. Adults between 15 and 44 years account for a fifty-nine percentage of global
traffic death. Road traffic injuries cause considerable economic losses to individuals, families, and
nation as a whole. Only 28 countries, representing seven percent of the world’s population have
adequate laws that address all five risk factors (speed, drunk driving, helmets, seat-belts and child
restraints). Without sustained action, road traffic deaths are predicted to be the 7th leading cause
of death by 2020. Ninety percent of the road traffic deaths happen in low- and middle- income
countries. This calls for the need of a low cost efficient safety device.

We are introducing a system similar to Event Data Recorders in aircraft. VEDRAR -
Vehicle Event Data Recorder and Review system acquires various data’s depending on different
driving parameters. The system is mainly committed into two approaches:
1. 1. A data acquisition part
2. 2. A review system.

The system first tracks and records the data of vehicle activities during a drive. Then a
review about the driver is carried out and driving feedback is provided to the driver and required
authorities and finally evaluate and categorize drivers into good or bad. And thus leading to better
drivers and safer roads.


## Hardware Requirements

### 1. Proximity sensor



![UV Sensor](https://user-images.githubusercontent.com/66065921/111907761-c45dee00-8a7c-11eb-8a7a-45b07246f57e.png)


 A proximity sensor is an electronic sensor that can detect the presence of objects within
 its vicinity without any actual physical contact. In order to sense objects, the proximity sensor
 19radiates or emits a beam of electromagnetic radiation, usually in the form of infrared light, and
 senses the reflection in order to determine the object’s proximity or distance from the sensor.


 As shown above the HC-SR04 Ultrasonic (US) sensor is a 4 pin module, whose pin names
 are Vcc, Trigger, Echo and Ground respectively. This sensor is a very popular sensor used in many
 applications where measuring distance or sensing objects are required. The module has two eyes
 like projects in the front which forms the Ultrasonic transmitter and Receiver. The sensor works
 with the simple high school formula that is : 
 
 Distance=Speed × time 
 
 The Ultrasonic transmitter transmits an ultrasonic wave, this wave travels in air and when it
 gets objected by any material it gets reflected back toward the sensor this reflected wave is observed
 by the Ultrasonic receiver module

### 2. Accelerometer

![Accelometer](https://user-images.githubusercontent.com/66065921/111907946-5bc34100-8a7d-11eb-8520-e9ff80396911.png)


GY-61 DXL335 3-Axis Accelerometer Module is a three axis accelerometer sensor module
based on ADXL335 integrated circuit. The ADXL335 is a triple axis accelerometer with extremely
low noise and power consumption. The sensor has a full sensing range of +/-3g. It can measure the
static acceleration of gravity in tilt-senRaspberry Pi Zero Wsing applications, as well as dynamic acceleration resulting
from motion, shock, or vibration.

### 3. Raspberry Pi Zero W

![RaspberryPI](https://user-images.githubusercontent.com/66065921/111908012-9927ce80-8a7d-11eb-9c09-f537a2824c33.png)
    
    
It is a fully working 32-bit computer with a 1 GHz ARMv6 single core microprocessor
(ARM1176) , a VideoCore 4 GPU, and 512 MB of memory. The GPU is capable of driving a full
HD display at 60 fps. You also get access to the 40 General Purpose Input and Output (GPIO)
ports, however the header is unpopulated, meaning there are no pins. Because of its size and use of
an energy-efficient ARM-based processor, the Raspberry Pi Zero can be powered from an external battery pack, like the ones you use to charge your mobile phone on 
the go. This is a great solution for headless setups for use on robots or other embedded projects.


### 4. Hall Effect Sensor

![Hall Effect Sensor](https://user-images.githubusercontent.com/66065921/111908099-e4da7800-8a7d-11eb-9be6-6c047b250b53.png)
      
A Hall effect sensor is a device that is used to measure the magnitude of a magnetic field.
Its output voltage is directly proportional to the magnetic field strength through it.

Hall effect sensors are used for proximity sensing, positioning, speed detection, and current
sensing applications.

Frequently, a Hall sensor is combined with threshold detection so that it acts as and is
called a switch. Commonly seen in industrial applications such as the pictured pneumatic cylinder,
they are also used in consumer equipment; for example some computer printers use them to detect
missing paper and open covers. The


        
# Project Overview
  
  VEDRAR is an electronic recording device which is used to store three characteristics of
driving data namely speed, proximity and tilting angle of steering. Speed as it implies defines the current speed of the vehicle, proximity describes the nearness or closeness in space between
the parent vehicle any nearby vehicle, and the tilt angle is the angle at which the steering must be
turned for a comfortable drive.

![Block Diagram](https://user-images.githubusercontent.com/66065921/111908173-3a168980-8a7e-11eb-8576-8a969f3e8f85.png)

VEDRAR collect and store this data when the machine analyses
the data to give a review of the current movement of the vehicle, to the driver. So any variation
in any of the three characteristics during a safe drive is noticed and informed so that driver can
take precaution an improve the condition. the required speed and tilt angle for specific proximity
and vice-versa equilibrium condition is saved in the machine and any variation in this equilibrium
condition is reviewed and also is steering tilt variation if any is detected and recorded and to the
driver as navigation. VEDRAR also upload all the vehicle stored data in a cloud so that as in
any conventional machine mechanisms, These data can be made use in case of an accident for the
detection of its cause.

Through our project, we tried to establish two application of VEDRAR:

One, to record
the vehicle data and store them for further use and second, to make use of these stored data to
provide the driver a review of the current drive.

Our project deals with a recomendation system that takes the driver data from the database
and provide it into a machine learning algorithm that classifies the driver into a good or bad driver.

This system looks forward to solve the current unsatisfactory driving test process .A driver
can be analysed for a time period based on which he can be classified.

![FlowChart](https://user-images.githubusercontent.com/66065921/111908290-a8f3e280-8a7e-11eb-9b1e-de2c12398c22.png)


We have established a system that can retrive driver data and analyse the driving skills of a
user based on different driver parameters. The driver data is collected from the vehicle after each
drive using different sensors placed at appropriate positions of the vehicle.The various sensors used
are Ultrasonic sensor to measure proximity, Hall-effect sensor to measure speed and accelerometer
to measure tilt angle of the steering. These datas are first locally collected in a common raspberry-
pi module. The data is transferred to a cloud storage/ database created using XAMP.

The different driver parameters stored in the cloud are retrieved to the machine learning
system. These datas are fed to the machine learning algorithm based on SVM. The algorithm
runs the different driver parameter datas and compares different datas at the same time instant
and provides a result. The datas are used to clssify the driver into a good or bad driver category.
This categorisation of driver based on various parameters and the classification into good or bad
category over a period of time can be used by traffic authorities to approve or decline licenses. The
data stored in the cloud can be retrieved in case of accidents to understand driver situations and
make better judgements on the faulty. The data can also be used by the driver itself to understand
the areas he needs to improve thereby making him a better driver ecentually leading to better
drivers and safer roads.
