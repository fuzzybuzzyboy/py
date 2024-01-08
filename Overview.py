import streamlit as st, time
from datetime import datetime

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

st.title('hi')

st.divider()

st.title('UPDATE INFO :')
st.write('### [:] Changed weapons to chapter 5 season 1 weapons.')
st.write("### [+] Added weapon mods, added to loadout the modded items.")
st.write("### [+] Added medallions.")
st.write("### [:] Shortend the code for the custom loadout.")
st.write("### [///] Updating the loadout generater.")
st.write('# \n ##### [/] = Fixed\n ##### [//] = Reverted\n ##### [///] = Working on\n ##### [:] = Changed something\n ##### [+] = Added\n ##### [-] = Removed\n\n\n ##### also pls tell me about bugs and other things so i can fix them (on discord) :)')

with st.sidebar:
    st.link_button("Github", "https://github.com/fuzzybuzzyboy/py")
    st.link_button("Discord", "https://discord.gg/HVEGufPNnF")
    st.divider()
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
