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

code = '''https://github.com/fuzzybuzzyboy/py'''

st.title('hi')

st.title('UPDATE INFO :')
st.write('### [:] Changed in loadout gen and custom loadout \'Burst Assualt Rifle\' to \'Heavy Assault Rifle\'')
st.write('### [+] Loadout Generater can now show in \'Others\' healing items (Chug Jug, Small Shield Potion, Shield Potion, Medkit)')
st.write('### [+] Six Shooter.')
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
