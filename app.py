import streamlit as st
from PIL import Image
import time
from gtts import gTTS
import wikipedia
import datetime
import webbrowser
#import playsound
#import pywhatkit
import speech_recognition as sr
import warnings
warnings.filterwarnings('ignore')

info = ''

def talk(text):                         
      speech = gTTS(text, lang = 'en', slow = False)
      speech.save('trans.mp3') 
      audio_file = open('trans.mp3', 'rb')            
      audio_bytes = audio_file.read()            
      st.audio(audio_bytes, format='audio/ogg',start_time=0)
	
def start_function():
    talk("Hi, my name is Max. I am professor Nguyen's assistant bot. How may I help you with first five chapters, or related topics?")
    r = sr.Recognizer()

    with sr.Microphone() as source:                
        while True:
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio)
                if 'no' in command:   
                    info='On behalf of professor Nguyen, thank you for studying. Chat with you later. Bye.'
                    talk(info)
                    break
                else:
                    run_query(command)
                    talk('do you have another question?')
            except:
                pass

def run_query(input):
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
        info = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is ' + info)
    elif 'what date is it' in input:
        info = datetime.datetime.now().date()
        talk(info)
        
    # CHAPTER ONE: MEASUREMENT
    
    elif 'what is science' in input:
        info = 'Science is a systematically organized body of knowledge on a particular subject.'
    elif 'physical science' in input:
        info = ('there are five major divisions in physical science: physics, chemistry, astronomy, geology and meteorology.')
    elif 'what is physics' in input:
        info = ('Physics is a major division of physical science. It is concerned with the basic principle and concepts of matter and energy')
    elif 'what is chemistry' in input:
        info = ('Chemistry deals with the composition, structure, and reactions of matter.')
    elif 'what is astronomy' in input:
        info = ('Astronomy is the study of the universe: space, time, matter, energy')
    elif 'what is geology' in input:
        info = ('Geology is the science of the planet Earth: composition, structure, processes, history')
    elif 'what is meteorology' in input:
        info = ('Meteorology is the study of the atmosphere.')
    elif 'human senses' in input:
        info = ('There are five human senses: sight, hearing, touch, smell, taste.')
    elif 'unit system' in input:
        info = ('In SI system, the standard unit for length is meter, for mass is kilogram and for time is second.')
    elif 'what is one meter' == input:
        info = ('In SI system, meter is the base units of distance. One meter is the distance traveled by light in a vacuum in 1 per 299,792,458 seconds.')
    elif 'what is kilogram' in input:
        info = ("In SI system, kilogram is the base units of mass. One kilogram equals Planck's constant divided by 6.62607015 x 10^-34 second/m^2.")
    elif 'what is a second' == input:
        info = ("In SI system, second is the base units of time. One second is exactly 9,192,631,770 cycles of radiation of an atom of caesium-133.")
    elif 'SI units' in input:
        info = ("SI units is the international system of units. It is the modern form of the metric system. It is the only system of measurement with"
		" an official status in nearly every country in the world.")
    elif 'what is time' == input:
        info = ("Time is the indefinite continued progress of existence and events that occur in an apparently irreversible succession from the past," 
		" through the present, into the future. In terms of mesurement, the second is the standard unit of time."
		" Time is often referred to as a fourth dimension, along with three spatial dimensions.")
    elif 'what is space' == input:
        info = ("Space is the boundless three-dimensional extent in which objects and events have relative position and direction."
		" Physical space is often conceived in three linear dimensions," 
		" although modern physicists usually consider it, with time, to be part of a boundless four-dimensional continuum known as spacetime.")
    # CHAPTER TWO: MOTION
    
    elif 'what is inertia' in input:
        info = 'Inertia is the tendency of an object to remain at rest or remain in motion. Inertia is related to mass of an object.'
    elif 'what is mass' in input:
        info = ('Mass is amount of matter in a substance. Unit of mass in SI system is kilogram.')
    elif 'what is weight' in input:
        info = ('Weight is different with mass. Weight is the product of mass and gravitational acceleration. Unit of of weight in SI system is Newton.')
    elif 'what is motion' in input:
        info = ('An object is in motion when it is undergoing a continuous change in position.')
    elif 'what is distance' in input:
        info = ('Distance is the actual length of the path taken by an object. It is a scalar quatity. unit of distance in SI system is meter.')
    elif 'displacement' in input:
        info = ('Displacement is a vector quantity. Displacement is the simply the straight-line distance between where the object started and"
		" where it ended up plus direction.')
    elif 'what is velocity' in input:
        info = ('Velocity is a vector. It equals displacement divided by time. Unit of velocity in SI system is meter per second.')
    elif 'what is speed' in input:
        info = ('Speed is a scalar quatity. average speed equals distance traveled divided by time to travel the distance. Unit of speed in SI system is meter per second.')
    elif 'uniform circular motion' in input:
        info = ('Uniform circular motion is the motion of an object in a circle at a constant speed. An object in uniform ciruclar motion"
		" has acceleration named centripetal acceleration.')
    elif 'linear motion' in input:
        info = ('Linear motion is the motion in one direction.')
    elif 'what is acceleration' in input:
        info = ('In linear motion, acceleration is the time rate of change of velocity. Unit of acceleration is meter per second squared.')
    elif 'centripetal acceleration' in input:
        info = ("Magnitude of centripetal acceleration equals square of speed divided by the radius of the circular path."
		" Its direction points to the center of the circular path.")
    elif 'Distance traveled by a dropped object' in input:
        info = ('Distance traveled by a dropped object d = 0.5*g*t^2. Where g is 9.8 meter per second squared.')
        
    # CHAPTER THREE: FORCE & MOTION
    
    elif "newton's laws" in input:
        info = ('There are three laws of Newton in classical mechancis.')
    elif "what is force" in input:
        info = ('In classical mechanics, a force is an action that tends to maintain or alter the motion of an object or to distort it."
		" Unit of force in SI system is Newton.')
    elif "first law of newton" in input:
        info = ('An object will remain at rest or in uniform motion in a straight line unless acted on by an external force.')
    elif "second law of newton" in input:
        info = ('The acceleration produced by an unbalanced force acting on an object is directly proportional to the magnitude of the force,"
		" and inversely proportional to the mass of the object.')
    elif "third law of newton" in input:
        info = ('For every action there is an equal and opposite reaction')
    elif "newton's gravitational law" in input:
        info = ('Every particle in the universe attracts every other particle with a force that is directly proportional to the product of their masses,"
		" and inversely proportional to the square of the distance between them.')
    elif "newton's law of gravitation" in input:
        info = ('Every particle in the universe attracts every other particle with a force that is directly proportional to the product of their masses,"
		" and inversely proportional to the square of the distance between them.')
    elif 'what is torque' in input:
        info = ('Torque is a vector quantity. It is the vector product of force and lever arm.')
    elif 'linear momentum' in input:
        info = ('Linear momentum is the product of mass and velocity of an object. It is a vector quantity.')
    elif 'conservation of linear momentum' in input:
        info = ('The linear momentum of an object remains constant if there is no external, unbalanced force acting on it.')
    elif 'conservation of angular momentum' in input:
        info = ('The angular momentum of an object remains constant if there is no external unbalanced torque acting on it.')
    elif 'what is angular momentum' in input:
        info = ('Angular momentum is a vector quantity. It is the product of mass and velocity of an object and distance from the object to the axis of rotation.')
        
    # CHAPTER FOUR: WORK & ENERGY
    
    elif 'what is work' in input:
        info = ('In physics, work applied on an object is the product of distance object moved and horizontal component of force applied on the object."
		" Unit of work in SI system is joule.')
    elif 'what is energy' in input:
        info = ('Energy is the capacity of doing work. Unit of energy is joule.')
    elif 'kinetic energy' in input:
        info = ('Kinetic energy is the energy of motion. It equals one half of mass time velocity squared. It is always positive.')
    elif 'potential energy' in input:
        info = ('Potential energy is the energy of position. It is equal to the weight of the object multiplied by the height. it can be negative.')
    elif 'work and kinetic energy' == input:
        info = ('Work done on the moving object is equal to the change in kinetic energy.')
    elif 'work and potential energy' in input:
        info = ('Work done by or against gravity sis equal to the change in potential energy.')
    elif 'conservation of energy' in input:
        info = ('Total energy of an isolated system remains constant. Energy cannot be created or destroyed, but it can change from one form to another form of energy.')
    elif 'what is power' in input:
        info = ('Power is the time rate of change of work. Unit of power in SI system is Watt.')
    elif 'forms of energy' in input:
        info = ('Common forms of energy are: chemical energy, electrical energy, nuclear energy, thermal energy, and hydroelectric energy')
    elif 'energy sources' in input:
        info = ('Common energy sources are coal, oil, natural gas, nuclear, hydroelectric, and renewable sources such as solar, wind, biofuels, biomass, geothermal, and tides.')
             
    # CHAPTER FIVE: TEMPERATURE & HEAT
    
    elif 'what is substance' == input:
        info = (' A substance is a form of matter that has constant chemical composition and characteristic properties.')
    elif 'how to compute heat' in input:
        info = ("First, determine how many steps for the process of changing phases and temperatures. Apply formula H = mass times specific heat,"
		" times the change in temperature, if there is no phase change in each step.  Apply formula H = mass time latent heat of fusion or vaporization,"
		" if there is a phase change in each step. The final answer is the total of heat from all steps")
    elif 'main topics of chapter five' in input:
        info = ("In this chapter, we study temperature, heat, specific heat, latent heat of fusion and vaporization, entropy, ideal gas law, thermodynamics laws."
		" We also learn how to calculate heat necessary to change a substance's phase or substance's temperature") 
    elif 'what is temperature' in input:
        info = ('Temperature is a measure of the average kinetic energy of the molecules of a substance. Unit of temperature in SI system is kelvin.')
    elif 'what is thermometer' in input:
        info = ('Thermometer is an instrument to measure temperature.')
    elif 'what is heat' == input:
        info = ('Heat is the form of energy that is transferred between systems or objects with different temperatures.')
    elif 'unit of heat' in input:
        info = ('Because heat is energy, unit of heat in SI system is joule. However, traditional unit of heat is calorie.')
    elif "what is unit of heat" in input:
        info = ('Unit of heat in SI system is joule.')
    elif "what is calorie" == input:
        info = ('A calorie is the amount of heat necessary to raise one gram of pure water by on celsius degree at normal atmospheric pressure."
		" One food Calorie is equal to 1000 calories or 4186 joules.')
    elif 'what is specific heat' == input:
        info = ('Specific heat is the amount of heat nessesary to raise the temperature of one kilogram of the subtance one celsius degree.')
    elif 'specific heat capacity' in input:
        info = ('Specific heat capacity is the same as specific heat. Specific heat is the amount of heat nessesary to raise the temperature of"
		" one kilogram of the subtance one celsius degree.')
    elif input == 'what is specific heat of water':
        info = ('Water has highest specific heat capacity 4186 joule per kilogram per celsius')
    elif 'specific heat of iron' in input:
        info = ('Specific heat capacity of iron is 440 joule per kilogram per celsius')
    elif 'specific heat of aluminum' in input:
        info = ('Specific heat capacity of aluminum is 920 joule per kilogram per celsius')
    elif 'specific heat of copper' in input:
        info = ('Specific heat capacity of copper is 385 joule per kilogram per celsius')
    elif 'specific heat of mercury' in input:
        info = ('Specific heat capacity of mercury is 138 joule per kilogram per celsius')
    elif 'specific heat of wood' in input:
        info = ('Specific heat capacity of wood is 1700 joule per kilogram per celsius')
    elif 'specific heat of ice' in input:
        info = ('Specific heat capacity of ice is 2100 joule per kilogram per celsius')
    elif 'specific heat of alcohol' in input:
        info = ('Specific heat capacity of alcohol is 2510 joule per kilogram per celsius')
    elif 'specific heat of air' in input:
        info = ('Specific heat capacity of air is 1000 joule per kilogram per celsius')
    elif 'what is latent heat' == input:
        info = ('Latent heat is energy absorbed or released by a substance during a change in its physical state or phase that occurs without changing its temperature.')
    elif 'what is latent heat of vaporization' == input:
        info = ('Latent heat of vaporization is the latent heat in case of liquid change phase to gas.')
    elif 'what is latent heat of fusion' == input:
        info = ('Latent heat of fusion is the latent heat in case of solid change phase to liquid.')
    elif 'latent heat of fusion of lead' in input:
        info = ('Latent heat of fusion of lead is 23000 joule per kilogram')
    elif 'latent heat of fusion of nitrogen' in input:
        info = ('Latent heat of fusion of nitrogen is 25700 joule per kilogram')
    elif 'latent heat of fusion of oxygen' in input:
        info = ('Latent heat of fusion of oxygen is 13900 joule per kilogram')
    elif 'latent heat of fusion of silicon' in input:
        info = ('Latent heat of fusion of silicon is 1790 kilo joule per kilogram')
    elif 'latent heat of fusion of water' in input:
        info = ('Latent heat of fusion of water is 335 kilo joule per kilogram')
    elif 'latent heat of vaporization of water' in input:
        info = ('Latent heat of vaporization of water is 2265 kilo joule per kilogram')
    elif 'latent heat of vaporization of alcohol' in input:
        info = ('Latent heat of vaporization of alcohol is 855 kilo joule per kilogram')
    elif 'latent heat of vaporization of helium' in input:
        info = ('Latent heat of vaporization of helium is 21000 joule per kilogram')
    elif 'phases of matter' in input:
        info = ('There are four common phases of matter: solid, liquid, gas and plasma.')
    elif 'what is solid' == input:
        info = ('A solid has relatively fixed molecules and a definite shape and volume.')
    elif 'what is gas' == input:
        info = ('A gas is made up of rapidly moving molecules and assumes the size and shape of its container.')
    elif 'what is liquid' == input:
        info = ('A liquid is an arrangement of molecules that may move and assume the shape of the container.')
    elif 'what is plasma' == input:
        info = ('Plasma is a hot gas of electrically charged particles.')
    elif 'heat transfer' in input:
        info = ('Heat transfer is accomplished by three methods: conduction, convection, and radiation.')
    elif 'what is conduction' in input:
        info = ('Conduction is the transfer of heat by molecular collisions, kinetic energy.')
    elif 'what is convection' in input:
        info = ('Convection is the transfer of heat by the movement of a substance, or mass, from one place to another.')
    elif 'what is radiation' in input:
        info = ('Radiation is the process of transferring energy by means of electromagnetic waves.')
    elif 'what is an ideal gas' in input:
        info = ('An ideal gas is one in which the molecules are point particles and interact by collision, no attraction.')
    elif 'pressure' in input:
        info = ('Pressure is defined as the force per unit area. unit of pressure in SI system is pascal or Newton per meter squared.')
    elif 'ideal gas law' in input:
        info = ('The pressure of an ideal gas is directly proportional to the number of molecules and to the kelvin temperature. and inversely proportional to the volume.')
    elif 'what is thermodynamics' == input:
        info = ('Thermodynamics means the dynamics of heat. Its study includes the production of heat, the flow of heat, and the conversion of heat to work.')
    elif 'first law of thermodynamics' in input:
        info = ('First law of thermodynamics is also called conservation of energy law. Energy cannot be created or destroyed,"
		" but it can be changed from one form to another. In other words, heat add to a system equals the change in internal energy of the system"
		" plus work done by the system.')
    elif 'second law of thermodynamics' in input:
        info = ('It is impossible for heat to flow spontaneously from a colder body to a hotter body. In other words, the entropy of an isolated system never decreases.')
    elif 'third law of thermodynamics' in input:
        info = ('It is impossible to attain a teperature of absolute zero in kelvin scale.')
    elif 'what is heat pump' in input:
        info = ('A heat pump is a device that uses work input to transfer heat from a low temperature reservoir to a high temperature reservoir.')
    elif 'entropy' in input:
        info = ('Entropy is a mathematical quantity. Entropy can be expressed as a measure of the disorder of a system. The total entropy of"
		" the universe increases in every natural process.')
    elif 'what is heat engine' in input:
        info = ('A heat engine is a device for producing motive power from heat, such as a gasoline engine or steam engine. ') 
		
    # CHAPTER 11: THE CHEMICAL ELEMENTS
    
    elif "divisions of chemistry" in input:
        info = ("There are five major divisions in chemistry: physical chemistry, organic chemistry, inorganic chemistry, biochemistry, and analytic chemistry.")
    elif "what is analytical chemistry" == input:
        info = ("Analytical chemistry identifies what substances are present in a material and determines how much of each substance is present.")
    elif "what is inorganic chemistry" == input:
        info = ("Organic chemistry is the study of compounds that contain carbon and hydrogen. The study of all other chemical compounds is called inorganic chemistry.")
    elif "classification of matter" in input:
        info = ("In chemistry, matter can be classified into pure substances and mixtures.")
    elif "pure substance" in input:
        info = ("In chemistry, a pure substance is a sample of matter with both definite and constant composition and distinct chemical properties."
	       " Examples of pure substances include chemical elements and compounds. Alloys and other solutions may also be considered pure if they have a constant composition.")
   
    # CHAPTER 12: CHEMICAL BONDING
    
    elif "types of chemical bonds" in input:
        info = ("There are three main types of chemical bonds: ionic, covalent, and hydrogen bonds. Hydrogen bond is a particularly weak chemical bonding." 
		" Ionic and covalent bonds are strong interactions that require a larger energy input to break apart.")
    elif "what is ionic bonding" == input:
        info = ("Ionic bonding is a type of chemical bonding that involves the electrostatic attraction between oppositely charged ions,"
		" or between two atoms with sharply different electronegativities, and is the primary interaction occurring in ionic compounds."
		" When an element donates an electron from its outer shell, a positive ion is formed. The element accepting the electron is now negatively charged."
		" Because positive and negative charges attract, these ions stay together and form an ionic bond, or a bond between ions.")
    elif "what is covalent bonding" == input:
        info = ("Covalent bondings are strong chemical bonds between two or more atoms. These bonds form when an electron is shared between two elements"
		" and are the strongest and most common form of chemical bond in living organisms. Covalent bonds form between the elements that make up"
		" the biological molecules in our cells. Unlike ionic bonds, covalent bonds do not dissociate in water."
		" For example, the hydrogen and oxygen atoms that combine to form water molecules are bound together by covalent bonds.") 
    elif "what is hydrogen bonding" in input:
        info = ("Hydrogen bonding is a particularly weak type of chemical bonding that arises in molecules containing hydrogen and a small, highly electronegative atom"
		" such as Oxygen, Flourine and Nitrogen. Here, the hydrogen atom develops a partially positive charge and is attracted to the neighboring atoms"
		" holding a partially negative charge.")
    elif "polar covalent bonding" in input:
        info = ("In covalent bonding, the electrons involved in the bond between two atoms are shared. However, unless the atoms are of the same element,"
	       " the bonding electrons will spend more time around the more nonmetallic element. That is, the sharing is unequal. Such a bond is called a polar covalent bond.")
    elif "what is electronegativity" in input:
        info = ("Electronegativity is a measure of the ability of an atom in a molecule to draw bonding electrons to itself."
	       " Electronegativity increases from left to right across a period and decreases down a group in periodic table, just as does the nonmetallic character.")
    elif "law of conservation of mass" in input:
        info = ("The law of conservation of mass, dates from Antoine Lavoisier's 1789 discovery, states that mass in an isolated system is neither created nor destroyed"
		" by chemical reactions or physical transformations.") 
    elif "law of definite proportion" in input:
        info = ("In 1799, the French chemist Joseph Proust discovered that, different samples of a pure compound always contain the same elements"
		" in the same proportion by mass. When a compound is broken down, its elements are found to be in a definite proportion by mass."
		" Conversely, when the same compound is made from its elements, the elements will combine in that same proportion by mass.")
    elif "what is lewis symbol" in input:
        info = ("American chemist Gilbert Newton Lewis developed electron dot symbols to help explain chemical bonding."
		" In a Lewis symbol, the nucleus and the inner electrons of an atom or ion are represented by the element's symbol,"
		" and the valence electrons are shown as dots arranged in four groups of one or two dots around the symbol.")
    elif "father of chemistry" in input:
        info = ("French chemist Antoine Lavoisier (1743-1794) is known as 'The Father of Chemistry'. He made chemistry a modern science, just as Galileo and Newton"
		" had done for physics more than a century earlier.")
    elif "lewis structure" in input:
        info = ("Lewis structures use Lewis symbols to show valence electrons in molecules and ions of compounds.")
    elif "photochromic sunglasses" in input:
        info = ("Lewis structures use Lewis symbols to show valence electrons in molecules and ions of compounds.")
    else:
        if 'wikipedia' and 'what' in input:
            info = wikipedia.summary(input,sentences=1)
    talk(info)
    time.sleep(10)
    st.write(info)

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
    st.title('Virtual Assistant for Introduction to Physical Science')
    st.text('@Author: Thomas Nguyen Date: 28 Feb 2021')

    image = Image.open('max.png')
    st.image(image)

    html_temp = """
	<div style="background-color:brown; padding:10px">
	<h2 style="color:white; text-align:center;">My name is Mia - Virtual assistant chat bot.</h2>
	</div>
	"""
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.text('Hi Students, ask me some questions about first five chapters:')
    st.text('Measurement, Motion, Force, Work & Energy, Temperature & Heat') 
    st.text("For example: 'what is displacement, inertia, linear momentum, second law of Newton, specific heat, entropy, first law of thermodynamics,... ") 
    
    user_input = st.text_input("Type your question here OR type 'exit' to quit chat bot.")
    user_input = user_input.lower()
    if user_input:
        if 'exit' == user_input:
            info = ('On behalf of professor Nguyen, thank you for studying. Bye!')
            talk(info)
            time.sleep(4)
            st.write(info)
        else:
            run_query(user_input)
    #st.text("Say 'No' to stop the conversation or click 'Stop' button on the top right corner.")


    #button_start = st.button('Chat With Max')
    #if button_start:
    	#start_function()

############################################################################      
