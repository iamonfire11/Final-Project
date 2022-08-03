#PI 0 CODE

import sounddevice as sd
from scipy.io.wavfile import write
import datetime, os
from pydub import AudioSegment
from pydub.playback import play
from flask import Flask, flash, request, jsonify, redirect, url_for
#from werkzeug.utils import secure_filename
from smbus2 import SMBus
from mlx90614 import MLX90614
import time
import requests


#------------BEGIN TEMPERATURE MEASUREMENT------------
def writeTemp():
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)
    mlxtemp = sensor.get_object_1()
    print(mlxtemp)
    if (mlxtemp>44):
        mlxtemp = mlxtemp-7.5
    if(mlxtemp<35):
         mlxtemp = sensor.get_object_1()+4.5
    
    mlxtempround = round(mlxtemp,2)
    print (f"The temp is:{mlxtempround}")
    bus.close()
    time.sleep(10)
    return mlxtempround
#------------TEMPERATURE MEASUREMENT FINISHED--------

#-------------RECORD AUDIO-------------
def recordaudio():
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write("Saved_Audio/unprocessed_audio.wav", fs, myrecording)  # Save as WAV file
    #-----Increase audio volume by 25dB
    louder_audio = AudioSegment.from_file(file = "Saved_Audio/unprocessed_audio.wav",format = "wav") +25
    #save louder song 
    louder_audio.export("Saved_Audio/processed_audio.wav", format='wav')
    print(f"Saved file at: {datetime.datetime.now()}")
    #------------AUDIO RECORDING FINISHED-----------------

#------------UPLOAD AUDIO AND TEMPERATURE------------
def uploadfile(temp):
    dfile = {'upload_file':open("/home/<path>/Saved_Audio/processed_audio.wav", "rb")}
    url = "http://<ipaddress>:3000/home"
    values = {'temperature': temp}
    test_res = requests.post(url, files = dfile, data=values)
    #print(test_res.prepare().body.decode('ascii')) 
    if test_res.ok:
        print(" File uploaded successfully ! ")
        print(test_res.text)
    else:
        print(" Please Upload again ! ")

	# files = {'file_being_uploaded':open("/home/<path>/Saved_Audio/processed_audio.wav", "rb")}
	# response = request.post("http://<ipaddress>:3000/home", files=files, data=values)
	# os.remove("/home/<path>/Saved_Audio/audio.wav")

#Go on indefinitely
#while(True):
recordaudio()
temp = writeTemp()
uploadfile(temp)
    

