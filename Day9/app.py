import speech_recognition as sr
import streamlit as st

st.title("Voice Input program 🔊") # Displays the title of the program

audio_file = st.audio_input("click on the mic to start speaking 🗣️") # Recieves the audio input of the user 

if audio_file:# Checks if the user has provided an audio input
    recognizer = sr.Recognizer() # Creates an instance of the Recognizer class from the speech_recognition library
    
    with sr.AudioFile(audio_file) as source:# Opens the audio file as a source for the recognizer
        audio_data =recognizer.record(source)# Records the audio data from the source and stores it in the audio_data variable
    
    try:
        text = recognizer.recognize_google(audio_data,language ="en-US")# Uses the recognize_google method of the recognizer to convert the audio data into text using Google's speech recognition API. The language parameter is set to "en-US" to specify that the input is in English (United States).
        st.write("You said:", text)# Displays the recognized text on the Streamlit app using the st.write() function.
    except sr.UnknownValueError:# Catches the UnknownValueError exception that may occur if the recognizer is unable to understand the audio input.
        st.error("Couldn't understand the audio please try again") 
    except sr.RequestError:# Catches the RequestError exception that may occur if there is an issue with the request to the Google speech recognition API.
        st.error("No internet connection please check your network")       
        
            






