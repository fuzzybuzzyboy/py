# IMPORTANT
# Command to run the file is : 'streamlit run {filename}.py' open your cmd in the folder with the file and run the command
# IMPORTANT

import streamlit as st
from datetime import datetime
import time

st.set_page_config(
    page_title='Overview',
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help': 'https://github.com/fuzzybuzzyboy/py',
        'Report a bug': "https://github.com/fuzzybuzzyboy/py",
        'About': "Random items generator for fortnite (no this doesn't inject into your game and do something blah blah blah)"
    }
)

code = '''https://github.com/fuzzybuzzyboy/py'''
thing = 0

st.title('hi')

st.title('UPDATE INFO :')
st.write('#### [+] Saving configs now works with computer names instead of calling the file \'config_sys.txt\' or whatever it was called before. This update is mainly to fix the stupid streamlit hosting thing but ik it wont fix it')
st.write('### [+] Now saving configs saves to a folder called \'configs\' the folder is requierd for saving configs.')
st.write('### [+] You can now see all weapons currently being used in the \'weapons.md\' file on github')
st.write('### [:] Updated to all new weapons.')
st.write('### [:]/[+] Update/add menu_items')
st.write('### [:]/[+] REDO OF LOADOUT GEN!!!')
st.write('# \n ##### [/] = Fixed\n ##### [//] = Reverted\n ##### [///] = Working on\n ##### [:] = Changed something\n ##### [+] = Added\n ##### [-] = Removed\n\n\n ##### also pls tell me about bugs and other things so i can fix them (on discord) :)')

#with st.sidebar:
#    with st.empty():
#        if st.button('Clock'):
#            time_now = datetime.now().strftime("%H:%M:%S")
#            time_now1 = datetime.now().strftime("%D")
#            st.write(f'# Clock\n    Current time : {time_now}\n    Date : {time_now1}')

with st.sidebar:
    st.code(f'Code at : \n{code}', language='Text')
            
with st.sidebar:
    with st.empty():
        if st.button('Clock'):
            while True:
                t = 1
                time_now1 = datetime.now().strftime("%D")
                while True:
                    time_now = datetime.now().strftime("%H:%M:%S")
                    st.write(f'# Clock\n    Current time : {time_now}\n    Date : {time_now1}')
                    time_later = datetime.now().strftime("%S")
                    t += 1
                    time.sleep(1)
