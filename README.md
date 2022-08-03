# Final-Project
Final year Capstone Project

The system here is "Temperature and Cough Rate Monitoring at Workstations."
The system is required to :
> Record cough sounds and determine the cough rate.
> Record temperature using a contactless temperature sensor. 
> Use a server.
> Show scalability in design.
> Send a warning email if the temperature is too high or the user is coughing too much.
> Have a webpage showing various data relating to the system ie cough rate and temperature per workstation.

Raspberry Pi Zero is used for the recording of audio and temperature of the user. Then this data is uploaded to a local server, hosted on a Raspberry Pi 4 Model B.
The RPi4B hosts the server, receives the files that were uploaded by the RPi0 and processes the data. 
The audio recording is run through a YamNet model to determine how many coughs were in that recording via MATLAB.
The temp and cough rate are then stored in a cloud database (MongoDB) where that data is then reflected on a webpage. 
If the temp or cough rate is too high :- temp(>38 C) & cough rate > 18 per day 
              then a warning email with the respective parameters is sent to the admin or manager of the system via SMTP.
