import streamlit as st
from PIL import Image
import time
from gtts import gTTS
import wikipedia
import datetime
import webbrowser
import os
#import playsound 
import speech_recognition as sr
import warnings
warnings.filterwarnings('ignore')


def talk(text):                         
      speech = gTTS(text, lang = 'en', slow = False)
      speech.save('trans.mp3')                          
      audio_file = open('trans.mp3', 'rb')   
      audio_bytes = audio_file.read()         
      #playsound(audio_bytes)      
      st.audio(audio_bytes, format='audio/ogg',start_time=0)
      os.remove("trans.mp3")
	
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

def run_query(input):
    outp = ''
    if 'play' in input:
        song = input.replace('play','')
        talk('playing...'+ song)
        pywhatkit.playonyt(song)
    elif 'who is' in input:
        person = input.replace('who is','')
        info = wikipedia.summary(person,1)
        talk(info)
    elif 'search google' in input:
        pywhatkit.search(input)
        talk('searching from google')
    elif 'what time is it' in input:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is ' + time)
    elif 'what date is it' in input:
        date = datetime.datetime.now().date()
        talk(date)
        
    # CHAPTER ONE: MEASUREMENT
    
    elif 'what is science' in input:
        outp = 'Science is a systematically organized body of knowledge on a particular subject.'
        talk(outp)
    elif 'physical science' in input:
        talk('there are five major divisions in physical science: physics, chemistry, astronomy, geology and meteorology.')
    elif 'what is physics' in input:
        talk('Physics is a major division of physical science. it is concerned with the basic principle and concepts of matter and energy')
    elif 'what is chemistry' in input:
        talk('Chemistry deals with the composition, structure, and reactions of matter.')
    elif 'what is astronomy' in input:
        talk('what is astronomy is the study of the universe: space, time, matter, energy')
    elif 'what is geology' in input:
        talk('Geology is the science of the planet Earth: composition, structure, processes, history')
    elif 'what is meteorology' in input:
        talk('meteorology is the study of the atmosphere.')
    elif 'human senses' in input:
        talk('there are five human senses: sight, hearing, touch, smell, taste.')
    elif 'unit system' in input:
        talk('in SI system, the standard unit for length is meter, for mass is kilogram and for time is second.')
    
    # CHAPTER TWO: MOTION
    
    elif 'what is inertia' in input:
        talk('Inertia is the tendency of an object to remain at rest or remain in motion. Inertia is related to mass of an object.')
    elif 'what is mass' in input:
        talk('mass is amount of matter in a substance. unit of mass in SI system is kilogram.')
    elif 'what is weight' in input:
        talk('weight is different with mass. weight is the product of mass and gravitational acceleration. unit of of weight in SI system is newton.')
    elif 'what is motion' in input:
        talk('An object is in motion when it is undergoing a continuous change in position.')
    elif 'what is distance' in input:
        talk('Distance is the actual length of the path taken by an object. it is a scalar quatity. unit of distance in SI system is meter.')
    elif 'displacement' in input:
        talk('displacement is a vector quantity.')
        talk('displacement is the simply the straight-line distance between where the object started and where it ended up plus direction.')
    elif 'what is velocity' in input:
        talk('velocity is a vector. it equals displacement divided by time. unit of velocity in SI system is meter per second.')
    elif 'what is speed' in input:
        talk('speed is a scalar quatity. average speed equals distance traveled divided by time to travel the distance. unit of speed in SI system is meter per second.')
    elif 'uniform circular motion' in input:
        talk('uniform circular motion is the motion of an object in a circle at a constant speed.')
        talk('an object in uniform ciruclar motion has acceleration named centripetal acceleration.')
    elif 'linear motion' in input:
        talk('linear motion is the motion in one direction.')
    elif 'what is acceleration' in input:
        talk('in linear motion, acceleration is the time rate of change of velocity. unit of acceleration is meter per second squared.')
    elif 'centripetal acceleration' in input:
        talk("magnitude of centripetal acceleration equals square of speed divided by the radius of the circular path. it's direction points to the center of the circular path.")
    elif 'Distance traveled by a dropped object' in input:
        talk('distance traveled by a dropped object d = 0.5*g*t^2. where g is 9.8 meter per second squared.')
        
    # CHAPTER THREE: FORCE & MOTION
    
    elif "newton's laws" in input:
        talk('there are three laws of Newton in classical mechancis.')
    elif "first law of newton" in input:
        talk('an object will remain at rest or in uniform motion in a straight line unless acted on by an external force.')
    elif "second law of newton" in input:
        talk('the acceleration produced by an unbalanced force acting on an object is directly proportional to the magnitud of the force')
        talk('and inversely proportional to the mass of the object.')
    elif "third law of newton" in input:
        talk('for every action there is an equal and opposite reaction')
    elif "newton's gravitational law" in input:
        talk('every particle in the universe attracts every other particle with a force that is directly proportional to the product of their masses')
        talk('and inversely proportional to the square of the distance between them.')
    elif "newton's law of gravitation" in input:
        talk('every particle in the universe attracts every other particle with a force that is directly proportional to the product of their masses')
        talk('and inversely proportional to the square of the distance between them.')
    elif 'what is torque' in input:
        talk('torque is a vector quantity. it is the vector product of force and lever arm.')
    elif 'linear momentum' in input:
        talk('linear momentum is the product of mass and velocity of an object. it is a vector quantity.')
    elif 'conservation of linear momentum' in input:
        talk('the linear momentum of an object remains constant if there is no external, unbalanced force acting on it.')
    elif 'conservation of angular momentum' in input:
        talk('the angular momentum of an object remains constant if there is no external unbalanced torque acting on it.')
    elif 'what is angular momentum' in input:
        talk('angular momentum is a vector quantity.')
        talk('it is the product of mass and velocity of an object and distance from the object to the axis of rotation.')
        
    # CHAPTER FOUR: WORK & ENERGY
    
    elif 'what is work' in input:
        talk('In physics, work applied on an object is the product of distance object moved and horizontall component of force applied on the object ')
        talk('unit of work in SI system is joule.')
    elif 'what is energy' in input:
        talk('energy is the capacity of doing work. unit of energy is joule.')
    elif 'kinetic energy' in input:
        talk('kinetice energy is the energy of motion. it equals one half of mass time velocity squared. it is always positive.')
    elif 'potential energy' in input:
        talk('potential energy is the energy of position. it is equal to the weight of the object multiplied by the height. it can be negative.')
    elif 'work and kinetic energy' in input:
        talk('work done on the moving object is equal to the change in kinetic energy.')
    elif 'work and potential energy' in input:
        talk('work done by or against gravity sis equal to the change in potential energy.')
    elif 'conservation of energy' in input:
        talk('total energy of an isolated system remains constant.')
        talk('energy cannot be created or destroyed, but it can change from one form to another form of energy.')
    elif 'what is power' in input:
        talk('power is the time rate of change of work. unit of power in SI system is Watt.')
    elif 'forms of energy' in input:
        talk('common forms of energy are: chemical energy, electrical energy, nuclear energy, thermal energy, and hydroelectric energy')
    elif 'energy sources' in input:
        talk('common energy sources are coal, oil, natural gas, nuclear, hydroelectric, and renewable sources such as ')
        talk('solar, wind, biofuels, biomass, geothermal, and tides.')
             
    # CHAPTER FIVE: TEMPERATURE & HEAT
    
    elif 'what is substance' == input:
        talk(' a substance is a form of matter that has constant chemical composition and characteristic properties.')
    elif 'how to compute heat' in input:
        talk("first, determine how many steps for the process of changing phases and temperatures")
        talk("apply formula H = mass times specific heat, times the change in temperature, if there is no phase change in each step")
        talk("apply formula H = mass time latent heat of fusion or vaporization, if there is a phase change in each step")
        talk("the answer is the total of heat for all steps")
    elif 'main topics of chapter five' in input:
        talk('In this chapter, we study temperature, heat, specific heat, latent heat of fusion and vaporization, entropy, ideal gas law, thermodynamics laws')
        talk("we also learn how to calculate heat necessary to change a substance's phase or substance's temperature") 
    elif 'what is temperature' in input:
        talk('temperature is a measure of the average kinetic energy of the molecules of a substance.')
        talk('unit of temperature in SI system is kelvin.')
    elif 'what is thermometer' in input:
        talk('thermometer is an instrument to measure temperature.')
    elif 'what is heat' == input:
        talk('Heat is the form of energy that is transferred between systems or objects with different temperatures.')
    elif 'unit of heat' in input:
        talk('because heat is energy, unit of heat in SI system is joule. However, traditional unit of heat is calorie.')
    elif "what is unit of heat" in input:
        talk('unit of heat in SI system is joule.')
    elif "what is calorie" == input:
        talk('a calorie is the amount of heat necessary to raise one gram of pure water by on celsius degree at normal atmospheric pressure')
        talk('one food Calorie is equal to 1000 calories or 4186 joules.')
    elif 'what is specific heat' == input:
        talk('specific heat is the amount of heat nessesary to raise the temperature of one kilogram of the subtance one celsius degree.')
    elif 'specific heat capacity' in input:
        talk('specific heat capacity is the same as specific heat')
        talk('specific heat is the amount of heat nessesary to raise the temperature of one kilogram of the subtance one celsius degree.')
    elif input == 'what is specific heat of water':
        talk('water has highest specific heat capacity 4186 joule per kilogram per celsius')
    elif 'specific heat of iron' in input:
        talk('specific heat capacity of iron is 440 joule per kilogram per celsius')
    elif 'specific heat of aluminum' in input:
        talk('specific heat capacity of aluminum is 920 joule per kilogram per celsius')
    elif 'specific heat of copper' in input:
        talk('specific heat capacity of copper is 385 joule per kilogram per celsius')
    elif 'specific heat of mercury' in input:
        talk('specific heat capacity of mercury is 138 joule per kilogram per celsius')
    elif 'specific heat of wood' in input:
        talk('specific heat capacity of wood is 1700 joule per kilogram per celsius')
    elif 'specific heat of ice' in input:
        talk('specific heat capacity of ice is 2100 joule per kilogram per celsius')
    elif 'specific heat of alcohol' in input:
        talk('specific heat capacity of alcohol is 2510 joule per kilogram per celsius')
    elif 'specific heat of air' in input:
        talk('specific heat capacity of air is 1000 joule per kilogram per celsius')
    elif 'what is latent heat' == input:
        talk('latent heat is energy absorbed or released by a substance during a change in its physical state or phase that occurs without changing its temperature.')
    elif 'what is latent heat of vaporization' == input:
        talk('latent heat of vaporization is the latent heat in case of liquid change phase to gas.')
    elif 'what is latent heat of fusion' == input:
        talk('latent heat of fusion is the latent heat in case of solid change phase to liquid.')
    elif 'latent heat of fusion of lead' in input:
        talk('latent heat of fusion of lead is 23000 joule per kilogram')
    elif 'latent heat of fusion of nitrogen' in input:
        talk('latent heat of fusion of nitrogen is 25700 joule per kilogram')
    elif 'latent heat of fusion of oxygen' in input:
        talk('latent heat of fusion of oxygen is 13900 joule per kilogram')
    elif 'latent heat of fusion of silicon' in input:
        talk('latent heat of fusion of silicon is 1790 kilo joule per kilogram')
    elif 'latent heat of fusion of water' in input:
        talk('latent heat of fusion of water is 335 kilo joule per kilogram')
    elif 'latent heat of vaporization of water' in input:
        talk('latent heat of vaporization of water is 2265 kilo joule per kilogram')
    elif 'latent heat of vaporization of alcohol' in input:
        talk('latent heat of vaporization of alcohol is 855 kilo joule per kilogram')
    elif 'latent heat of vaporization of helium' in input:
        talk('latent heat of vaporization of helium is 21000 joule per kilogram')
    elif 'phases of matter' in input:
        talk('there are four common phases of matter: solid, liquid, gas and plasma.')
    elif 'what is solid' == input:
        talk('a solid has relatively fixed molecules and a definite shape and volume.')
    elif 'what is gas' == input:
        talk('a gas is made up of rapidly moving molecules and assumes the size and shape of its container.')
    elif 'what is liquid' == input:
        talk('a liquid is an arrangement of molecules that may move and assume the shape of the container.')
    elif 'what is plasma' == input:
        talk('plasma is a hot gas of electrically charged particles.')
    elif 'heat transfer' in input:
        talk('heat transfer is accomplished by three methods: conduction, convection, and radiation.')
    elif 'what is conduction' in input:
        talk('conduction is the transfer of heat by molecular collisions, kinetic energy.')
    elif 'what is convection' in input:
        talk('convection is the transfer of heat by the movement of a substance, or mass, from one place to another.')
    elif 'what is radiation' in input:
        talk('radiation is the process of transferring energy by means of electromagnetic waves.')
    elif 'what is an ideal gas' in input:
        talk('an ideal gas is one in which the molecules are point particles and interact by collision, no attraction.')
    elif 'pressure' in input:
        talk('pressure is defined as the force per unit area. unit of pressure in SI system is pascal or Newton per meter squared.')
    elif 'ideal gas law' in input:
        talk('the pressure of an ideal gas is derectly proportional to the number of molecules and to the kelvin temperature')
        talk('and inversely proportional to the volume.')
    elif 'what is thermodynamics' == input:
        talk('thermodynamics means the dynamics of heat.')
        talk('its study includes the production of heat, the flow of heat, and the conversion of heat to work.')
    elif 'first law of thermodynamics' in input:
        talk('first law of thermodynamics is also called conservation of energy law')
        talk('energy cannot be created or destroyed, but it can be changed from one form to another.')
        talk('in other words, heat add to a system equals the change in internal energy of the system pluse work done by the system.')
    elif 'second law of thermodynamics' in input:
        talk('it is impossible for heat to flow spontaneously from a colder body to a hotter body.')
        talk('in other words, the entropy of an isolated system never decreases.')
    elif 'third law of thermodynamics' in input:
        talk('it is impossible to attain a teperature of absolute zero in kelvin scale.')
    elif 'what is heat pump' in input:
        talk('a heat pump is a device that uses work input to transfer heat from a low temperature reservoir to a high temperature reservoir.')
    elif 'entropy' in input:
        outp ='entropy is a mathematical quantity. entropy can be expressed as a measure of the disorder of a system.'
        talk(outp)
        outp = 'the total entropy of the universe increases in every natural process.'
        talk(outp)    
    elif 'what is heat engine' in input:
        outp='a heat engine is a device for producing motive power from heat, such as a gasoline engine or steam engine. '
        talk(oupt)
    elif 'from wikipedia' in input:
        outp = wikipedia.summary(input,1)
        talk(outp)
    else:
        if 'wikipedia' and 'what' in input:
            outp=wikipedia.summary(input,sentences=1)
            talk(outp)

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
    st.image(image)

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
    
    user_input = st.text_input("Enter your question here OR click 'Chat With Max' button:")
    if user_input:
        if 'no' == user_input:
            talk('on behalf of professor Nguyen, thank you for studying. bye.')
        else:
            run_query(user_input)
    st.text("Say 'No' to stop the conversation or click 'Stop' button on the top right corner.")


    button_start = st.button('Chat With Max')
    if button_start:
    	start_function()

############################################################################      
