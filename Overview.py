import streamlit as st, time, os
from datetime import datetime

st.set_page_config(
    page_title='Overview',
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'Get help': 'https://github.com/fuzzybuzzyboy/py', 'Report a bug': "https://github.com/fuzzybuzzyboy/py", 'About': "Random items generator for fortnite (no this doesn't inject into your game and do something blah blah blah)"})

st.title('Hi')
st.divider()
st.title('UPDATE INFO :')
st.write('### [:] Changed weapons to chapter 5 season 1 weapons. (Loadout generator, Custom loadout)')
st.write("### [+] Added weapon mods (Loadout generator, Custom loadout)")
st.write("### [+] Added medallions. (Loadout generator, Custom loadout)")
st.write("### [:] Shorter code (Loadout generator, Custom loadout)")
st.write('### [:] Nice ui now (Loadout generator, Custom loadout)')
st.write("### [+] Loadout generator loadout now shows medallions amount and other. (examples in folder called 'pictures')")
st.write('# \n ##### [/] = Fixed\n ##### [:] = Changed something\n ##### [+] = Added\n ##### [-] = Removed\n\n\n ##### also pls tell me about bugs and other things so i can fix them (on discord) :)')

with st.sidebar:
    st.link_button("Github", "https://github.com/fuzzybuzzyboy/py")
    st.link_button("Discord", "https://discord.gg/HVEGufPNnF")
    if st.button('Clock'):
        with st.empty():
            while True:
                time_now1, time_now = datetime.now().strftime("%D"), datetime.now().strftime("%H:%M:%S")
                st.write(f'# Clock\n    Time : {time_now}\n    Date : {time_now1}', format="markdown")
                time.sleep(1)
