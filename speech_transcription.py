import azure.cognitiveservices.speech as speechsdk
import time
import os
import platform
import sys
import json

# Used Voicemeeter to transform computer audio output to microphone input (https://www.vb-audio.com/Voicemeeter/)

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").

# Welcome
print('*'*50)
print('* Microsoft Speech Service - Sample Transcription *')
print('*'*50)

# Load keys from keys.json
print("\tLoading Keys from keys.json.")
with open('keys.json', 'r') as json_file:
    keys = json.load(json_file)
    print('\tKeys loaded.')


speech_key, service_region = keys.get("speech_key"), keys.get("speech_region")
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)





# Transcription File
transcript_file_name = sys.argv[1]
if os.path.exists(transcript_file_name) == False:
    print('\tCreating file: {}'.format(transcript_file_name))
    with open(transcript_file_name, "w+"):
        pass
else:
    print('\tAppending to file: {}'.format(transcript_file_name))
    

done = False

def stop_cb(evt):
    """callback that stops continuous recognition upon receiving an event `evt`"""
    print('CLOSING on {}'.format(evt))
    speech_recognizer.stop_continuous_recognition()
    done = True

def log_recognized(transcript_segment):
    print('RECOGNIZED: {}'.format(transcript_segment))
    with open(transcript_file_name, 'a') as f:
        f.write('{}\n'.format(transcript_segment))

print("\tPress Ctrl+C to exit the program.")
print("\tBegin Audio Transcription")
print('*'*50)

# Connect callbacks to the events fired by the speech recognizer
speech_recognizer.recognizing.connect(lambda evt: print('\tRECOGNIZING: {}'.format(evt.result.text)))
speech_recognizer.recognized.connect(lambda evt: log_recognized(evt.result.text))
speech_recognizer.session_started.connect(lambda evt: evt)
speech_recognizer.session_stopped.connect(lambda evt: evt)
speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

# stop continuous recognition on either session stopped or canceled events
speech_recognizer.session_stopped.connect(stop_cb)
speech_recognizer.canceled.connect(stop_cb)

# Start continuous speech recognition
speech_recognizer.start_continuous_recognition()

try:
    while not done:
        time.sleep(.5)
except KeyboardInterrupt:
    print('*'*50)
    sys.exit('* Exiting Program *')
    print('*'*50)
