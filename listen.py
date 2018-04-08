#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import time

import speech_recognition as sr

filename = 'all.txt'


# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        f = open(filename, 'a')
        text = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + text)
        f.write(text)
        f.write(' ')
        f.close()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

print("Will start listening")
# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback, phrase_time_limit=20)
# `stop_listening` is now a function that, when called, stops background listening

# do some unrelated computations for t seconds
tt = 300
lim = int(tt/5) + 1
for _ in range(lim): time.sleep(5)  # we're still listening even though the main thread is doing other things

# calling this function requests that the background listener stop listening
stop_listening()

print("Stopped listening")
# do some more unrelated things
#while True: time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping
