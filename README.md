The purpose of this script is to leverage the Azure Speech API to transcribe an audio stream.  This script targets usage on Windows machines.


Audio Stream - By default, this is your microphone.  You can pass your computer's audio output to a "microphone" input by using software such as Voicemeeter (https://www.vb-audio.com/Voicemeeter/)

Transcription - The transcription will be printed to screen and written/appended to the .txt file passed as an argument.

Instructions:

1. Git clone this repo.
2. Create a virtual environment:
    ```
    py -m venv env
    ```
3. Activate environment
    ```
    env\Scripts\activate
    ```
4. Install requirements
    ```
    pip install azure-cognitiveservices-speech
    ```
5. In the same directory as the script, create a keys.json file with your Azure Speech API key and region. region syntax examples: eastus2, westus
    ```
    {
        "speech_key":"YOUR KEY HERE",
        "speech_region":"YOUR REGION HERE"
    }
    ```
6. Script usage:
    ```
    # Syntax is:
    # speech_transcription.py <filename.txt>, example:
    py speech_transcription.py transcript.txt
    ```
7. Press ctrl+c to exit the program.

Sources:
Sample code from https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/samples/python/console used as a base.
