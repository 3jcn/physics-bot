import streamlit as st
from PIL import Image
import string
import dominate
import random
import time
import speech_recognition as sr
from querydata import run_query, talk
from dominate.tags import *
import warnings
warnings.filterwarnings('ignore')


def start_function():
    talk("Hi, my name is Max. I am professor Nguyen's assistant.")
    talk("How may I help you with chapter 5, temperature and heat, or related topics?")
    r = sr.Recognizer()

    with sr.Microphone() as source:                
        while True:
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio)
                if 'no' in command:   
                    out='On behalf of professor Nguyen, thank you for studying. Chat with you later. Bye.'
                    talk(out)
                    break
                else:
                    run_query(command)
                    talk('do you have another question?')
            except:
                pass
	
def create_page():
    doc = dominate.document(title='Virtual Physics Bot')
    with doc.head:
        link(rel='stylesheet', href='style.css')
        script(type='text/javascript', src='script.js')
    with doc:
        with div(cls='header'):
            h1('Virtual Assistant for Introductory of Physical Science - PSC 110')
            img('max.png')
            p("@Author: Thomas Nguyen Date: 28 Feb 2021")
            h2("My name is Max. I am professor Nguyen's assistant.")
            p("Hi Students, ask me some questions about physical science. For example: 'what is temperature, specific heat, entropy, first law of thermodynamics,...If you are tired, you can ask me to play music by saying: play 'song name or artist name' or 'who is ..?', 'what time is it?', 'what date is it?'...")

    with div(cls='control'):  
        user_input = input_("Type a question")
        button(
            "Chat with Max",
            type="button",
            _class="btn btn-primary btn-md reportng-button-class",
            data_toggle="run_query(user_input)",
            data_target="#%s" 
        )  

    with open('index.html','w') as file:
        file.write(doc.render())

create_page()