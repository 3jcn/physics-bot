import streamlit as st
from PIL import Image
import string
import random
import time
import speech_recognition as sr
from querydata import run_query, talk
import warnings
warnings.filterwarnings('ignore')


def wakeWord(text):
    wake_list = ['max', 'hi max', 'hey max', 'hello max', 'hola max']
    text = text.lower()
    for phrase in wake_list:
        if phrase in text:
            return True
    return False

def start_function():
    talk("Hi, my name is Max. I am professor Nguyen's assistant.")
    talk("How may I help you with chapter 5, temperature and heat, or related topics?")
    r = sr.Recognizer()

    with sr.Microphone() as source:                
        while True:
            #r.energy_threshold = 5000
            #r.adjust_for_ambient_noise(source,duration=2)
            #r.dynamic_energy_threshold = True
            #r.pause_threshold = 0.5
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio)
                #command = command.lower()
                #print("You said: " + command) 

                if 'no' in command:   
                    out='On behalf of professor Nguyen, thank you for studying. Chat with you later. Bye.'
                    talk(out)
                    break
                else:
                    #if(wakeWord(command)==True):
                    run_query(command)
                    talk('do you have another question?')
            except:
                pass
	
#################################################################################
header = st.beta_container()

st.markdown("""
	<style>
	.main{
	background-color: #f5f5f5;
	}
        .stButton>button {
        background-color: #0000ff;
        color: #ffffff;
        }
        .stTextInput>div>div>input {
        background-color: yellow;
        color: brown;
        }
	</style>
	""",
	unsafe_allow_html=True
)

with header:
    st.title('Virtual Assistant for Introductory of Physical Science - PSC 110')
    st.text('@Author: Thomas Nguyen Date: 28 Feb 2021')

    image = Image.open('max.png')
    st.image(image,width=240,height=300)

    html_temp = """
	<div style="background-color:brown; padding:10px">
	<h2 style="color:white; text-align:center;">My name is Max. I am professor Nguyen's assistant.</h2>
	</div>
	"""
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.text('Hi Students, ask me some questions about physical science!')
    st.text("For example: 'what is temperature, specific heat, entropy, first law of thermodynamics,... ") 
    st.text("If you are tired, you can ask me to play music by saying: play 'song name or artist name'")
    st.text("or 'who is ..?', 'what time is it?', 'what date is it?'...")
    
    user_input = st.text_input("Enter your question here OR click 'Chat With Max' button")
    if user_input:
        if 'no' in user_input:
            talk('on behalf of professor Nguyen, thank you for studying. bye.')
        else:
            run_query(user_input)
    st.text("Say 'No' to stop the conversation or click 'Stop' button on the top right corner.")
    button_start = st.button('Chat With Max')
    if button_start:
    	start_function()

############################################################################       
# Unintelligible Speech: When Python cannot match some audio to text, it raises an UnknownValueError exception.
