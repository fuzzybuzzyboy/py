import random
import streamlit as st
import time as ti
from datetime import datetime

st.set_page_config(
    page_title='Loadout Generater',
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded",
)

#login.test()

a = ''
b = ''
c = ''
d = ''
e = ''
f = ''
slottwo1 = 'None'
slotthree1 = 'None'
slotfour1 = 'None'
slotfive1 = 'None'
button = 1
thing = 0

shot = int(st.selectbox(
    'Shotguns.',
    (1, 2, 3)))
gun = st.selectbox(
    'Assault-Rifles.',
    (1, 2, 3, 4))
smg1 = st.selectbox(
    'SMGs.',
    (1, 2, 3, 4))

for i in range(button):
    shotgun = random.randint(1, int(shot))
    ar = random.randint(1, int(gun))
    smg = random.randint(1, int(smg1))
    movement = random.randint(1, 2)
    healing = random.randint(1, 7)
    button = 0
    if shotgun == 1:
        a = '\'Sharp Tooth Shotgun\''
        rarity_shot = random.randint(1, 4)
        if rarity_shot == 1:
            shotgun1 = 'Uncommon'
        elif rarity_shot == 2:
            shotgun1 = 'Rare'
        elif rarity_shot == 3:
            shotgun1 = 'Epic'
        elif rarity_shot == 4:
            shotgun1 = 'Legendary'
    elif shotgun == 2:
        a = '\'Maven Auto Shotgun\''
        rarity_shot = random.randint(1, 6)
        if rarity_shot == 1:
            shotgun1 = 'Common'
        elif rarity_shot == 2:
            shotgun1 = 'Uncommon'
        elif rarity_shot == 3:
            shotgun1 = 'Rare'
        elif rarity_shot == 4:
            shotgun1 = 'Epic'
        elif rarity_shot == 5:
            shotgun1 = 'Legendary'
        elif rarity_shot == 6:
            shotgun1 = 'Exotic'
    elif shotgun == 3:
        a = '\'Infiltrator Pump Shotgun\''
        rarity_shot = random.randint(1, 6)
        if rarity_shot == 1:
            shotgun1 = 'Common'
        elif rarity_shot == 2:
            shotgun1 = 'Uncommon'
        elif rarity_shot == 3:
            shotgun1 = 'Rare'
        elif rarity_shot == 4:
            shotgun1 = 'Epic'
        elif rarity_shot == 5:
            shotgun1 = 'Legendary'
        elif rarity_shot == 6:
            shotgun1 = 'Mythic'
            a = 'Enhanced Infiltrator Pump Shotgun'
    if ar == 1:
        b = '\'Twin Mag Assault Rifle\''
        rarity_ar = random.randint(1, 5)
        if rarity_ar == 1:
            ar1 = 'Common'
        elif rarity_ar == 2:
            ar1 = 'Uncommon'
        elif rarity_ar == 3:
            ar1 = 'Rare'
        elif rarity_ar == 4:
            ar1 = 'Epic'
        elif rarity_ar == 5:
            ar1 = 'Legendary'
    elif ar == 2:
        b = '\'Havoc Suppressed Assault Rifle\''
        rarity_ar = random.randint(1, 6)
        if rarity_ar == 1:
            ar1 = 'Common'
        elif rarity_ar == 2:
            ar1 = 'Uncommon'
        elif rarity_ar == 3:
            ar1 = 'Rare'
        elif rarity_ar == 4:
            ar1 = 'Epic'
        elif rarity_ar == 5:
            ar1 = 'Legendary'
        elif rarity_ar == 6:
            ar1 = 'Mythic'
            b = 'Heart\'s Havoc Suppressed Rifle'
    elif ar == 3:
        b = '\'Sticky Grenade Launcher\''
        rarity_ar = random.randint(1, 2)
        if rarity_ar == 1:
            ar1 = 'Epic'
        elif rarity_ar == 2:
            ar1 = 'Legendary'
    elif ar == 4:
        b = '\'Thermal DMR\''
        rarity_ar = random.randint(1, 5)
        if rarity_ar == 1:
            ar1 = 'Uncommon'
        elif rarity_ar == 2:
            ar1 = 'Rare'
        elif rarity_ar == 3:
            ar1 = 'Epic'
        elif rarity_ar == 4:
            ar1 = 'Legendary'
        elif rarity_ar == 5:
            ar1 = 'Mythic'
            b = 'Diamond\'s Thermal DMR'
    if smg == 1:
        c = '\'Submachine Gun\''
        rarity_smg = random.randint(1, 5)
        if rarity_smg == 1:
            smg2 = 'Common'
        elif rarity_smg == 2:
            smg2 = 'Uncommon'
        elif rarity_smg == 3:
            smg2 = 'Rare'
        elif rarity_smg == 4:
            smg2 = 'Epic'
        elif rarity_smg == 5:
            smg2 = 'Legendary'
    elif smg == 2:
        c = '\'Combat SMG\''
        rarity_smg = random.randint(1, 5)
        if rarity_smg == 1:
            smg2 = 'Common'
        elif rarity_smg == 2:
            smg2 = 'Uncommon'
        elif rarity_smg == 3:
            smg2 = 'Rare'
        elif rarity_smg == 4:
            smg2 = 'Epic'
        elif rarity_smg == 5:
            smg2 = 'Legendary'
    elif smg == 3:
        c = '\'Tactical Pistol\''
        rarity_smg = random.randint(1, 6)
        if rarity_smg == 1:
            smg2 = 'Common'
        elif rarity_smg == 2:
            smg2 = 'Uncommon'
        elif rarity_smg == 3:
            smg2 = 'Rare'
        elif rarity_smg == 4:
            smg2 = 'Epic'
        elif rarity_smg == 5:
            smg2 = 'Legendary'
        elif rarity_smg == 6:
            smg2 = 'Mythic'
    elif smg == 4:
        c = '\'Run \'N\' Gun SMG\''
        smg2 = 'Exotic'
    if healing == 1:
        f = '\'Mini Shield Potion\''
    elif healing == 2:
        f = '\'Shield Potion\''
    elif healing == 3:
        f = '\'Med-kit\''
    elif healing == 4:
        f = '\'Slap Juice\''
    elif healing == 5:
        f = '\'Chug Cannon\''
    elif healing == 6:
        f = '\'Meat\''
    elif healing == 7:
        f = '\'Fish\''
    if movement == 1:
        e = '\'Rocket Ram\''
        movement1 = 'Rare'
    elif movement == 2:
        e = '\'Crash Pad Jr.\''
        movement1 = 'Uncommon'
col1, col2 = st.columns(2)

with col1:
    tab1b, tab2b, tab3b = st.tabs(["Base", "Regular", "Json"])

    with tab1b:
        st.write(
            f'# Load-Out\n    Shotgun = {a}\n    Assault-Rifle : {b}\n    Smg : {c}'
            f'\n    Movement : {e}\n    Healing : {f}')

    with tab2b:
        st.write(
            f'# Load-Out  \n##### Shotgun = {a}\n#####    Assault-Rifle : {b}\n#####    Smg : {c}'
            f'\n#####    Movement : {e}\n#####    Healing : {f}')

    with tab3b:
        st.json({
            'Load-Out': [
                f'Shotgun = {a}',
                f'Assault-Rifle = {b}',
                f'Smg = {c}',
                f'Movement = {e}',
                f'Healing = {f}'
            ],
        })
with col2:
        taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])

        with taba1:
            st.write(f'# Rarity\n    Shotgun : {shotgun1}\n    Assault-Rifle : {ar1}\n    Smg : {smg2}\n    Movement : {movement1}\n    Healing : no')

        with taba2:
            st.write(f'# Rarity  \n##### Shotgun : {shotgun1}\n#####    Assault-Rifle : {ar1}\n#####    Smg : {smg2}\n#####    Movement : {movement1}\n#####    Healing : no')

        with taba3:
            st.json({
                'Rarity': [
                    f'Shotgun : {shotgun1}',
                    f'Assault-Rifle : {ar1}',
                    f'Smg : {smg2}',
                    f'Movement : {movement1}'
                    f'Healing : None'
                ],
            })
st.divider()
if st.button('Randomize Load-Out'):
    button = + 1
else:
    pass
with st.sidebar:
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
