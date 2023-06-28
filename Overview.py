# IMPORTANT
# Command to run the file is : 'streamlit run {filename}.py' open your cmd in the folder with the file and run the command
# IMPORTANT

import streamlit as st
from datetime import datetime
import time as ti

st.set_page_config(
    page_title='Overview',
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded",
)
thing = 0

st.title('hi')

if st.button('Source Code'):
    thing = + 1
else:
    pass
if thing == 1:
    code = '''https://github.com/fuzzybuzzyboy/py'''
    st.code(code, language='Text')
    thing = 0
else:
    thing = 0

st.title('UPDATE INFO :')
st.write('### [:] Entire tab system to sidebar with pages.')
st.write('# \n ##### [/] = Fixed\n ##### [//] = Reverted\n ##### [///] = Working on\n ##### [:] = Changed something\n ##### [+] = Added\n ##### [-] = Removed\n\n\n ##### also pls tell me about bugs and other things so i can fix them (on discord) :)')
with st.sidebar:
    with st.empty():
        if st.button('Clock'):
            while True:
                t = 1
                time_now1 = datetime.now().strftime("%D")
                while True:
                    time_now = datetime.now().strftime("%H:%M:%S")
                    st.write(f'# Clock\n    Current time : {time_now}\n    Date : {time_now1}\n##### Reminder, the clock will vanish when creating a new load-out. The clock button will show up.')
                    time_later = datetime.now().strftime("%S")
                    t += 1
                    ti.sleep(1)
