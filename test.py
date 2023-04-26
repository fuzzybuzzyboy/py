# IMPORTANT IMPORTANT
# Command to run the file is : 'streamlit run {filename}.py' open your cmd in the folder with the file and run the command
# IMPORTANT IMPORTANT

import random
import streamlit as st
from datetime import datetime
import time as ti

st.set_page_config(
    page_title='test',
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)
a = ''
b = ''
c = ''
d = ''
e = ''
f = ''
button = 1
thing = 0
tab1, tab2, tab3 = st.tabs(["Loadout Generator", "Custom Loadout", "Info"])
with tab1:
    shot = st.selectbox(
        'Shotguns.',
        ('1', '2', '3'))
    gun = st.selectbox(
        'Assault-Rifles.',
        ('1', '2', '3', '4'))
    smg1 = st.selectbox(
        'SMGs.',
        ('1', '2', '3'))
    sniper1 = st.selectbox(
        'Snipers. (keep at 1 for heavy)',
        ('1', '2'))
    move = st.selectbox(
        'Mobility (keep at 1 for blade)',
        ('1', '2'))

    for i in range(button):
        shotgun = random.randint(1, int(shot))
        ar = random.randint(1, int(gun))
        smg = random.randint(1, int(smg1))
        healing = random.randint(1, 10)
        sniper = random.randint(1, int(sniper1))
        if move == 1:
            movebb = 'Kinetic blade'
        else:
            mobility = random.randint(1, int(move))
        button = 0
        if shotgun == 1:
            a = '\'Havoc Pump Shotgun\''
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
            a = '\'Combat Shotgun\''
            rarity_shot = random.randint(1, 4)
            if rarity_shot == 1:
                shotgun1 = 'Uncommon'
            elif rarity_shot == 2:
                shotgun1 = 'Rare'
            elif rarity_shot == 3:
                shotgun1 = 'Epic'
            elif rarity_shot == 4:
                shotgun1 = 'Legendary'
        if ar == 1:
            b = '\'Overclocked Pulse Rifle\''
            ar1 = 'Mythic'
        elif ar == 2:
            b = '\'Red-Eye Assault Rifle\''
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
                ar1 = 'Exotic'
        elif ar == 3:
            b = '\'Havoc Suppressed Assault Rifle\''
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
        elif ar == 4:
            b = '\'Cobra DMR\''
            rarity_ar = random.randint(1, 4)
            if rarity_ar == 1:
                ar1 = 'Uncommon'
            elif rarity_ar == 2:
                ar1 = 'Rare'
            elif rarity_ar == 3:
                ar1 = 'Epic'
            elif rarity_ar == 4:
                ar1 = 'Legendary'
        if smg == 1:
            c = '\'Twin-Mag SMG\''
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
                smg2 = 'Exotic'
        elif smg == 2:
            c = '\'Run \'N\' Gun SMG\''
            smg2 = 'Exotic'
        elif smg == 3:
            c = '\'Tactical Pistol\''
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
        if healing == 1:
            e = '\'Mini Shield Potion\''
        elif healing == 2:
            e = '\'Shield Potion\''
        elif healing == 3:
            e = '\'Chug Splash\''
        elif healing == 4:
            e = '\'Shield Keg\''
        elif healing == 5:
            e = '\'Med Mist\''
        elif healing == 6:
            e = '\'Med-kit\''
        elif healing == 7:
            e = '\'Slap Juice\''
        elif healing == 8:
            e = '\'Chug Cannon\''
        elif healing == 9:
            e = '\'Meat\''
        elif healing == 10:
            e = '\'Fish\''
        if sniper == 1:
            f = 'Heavy Sniper Rifle'
            rarity_sniper = random.randint(1, 3)
            if rarity_sniper == 1:
                sniper2 = 'Rare'
            elif rarity_sniper == 2:
                sniper2 = 'Epic'
            elif rarity_sniper == 3:
                sniper2 = 'Legendary'
        elif sniper == 2:
            f = '\'Dragon\'s Breath Sniper\''
            sniper2 = 'Exotic'
        if mobility == 1:
            movebb = 'Kinetic blade'
            moveblade = random.randint(1, 2)
            if moveblade == 1:
                moveblade1 = 'Epic'
            elif moveblade == 2:
                moveblade1 = 'Rare'
        elif mobility == 2:
            movebb = 'ODM Gear'
            moveblade1 = 'Mythic'
    col1, col2 = st.columns(2)

    with col1:
        tab1b, tab2b, tab3b = st.tabs(["Base", "Regular", "Json"])

        with tab1b:
            st.write(
                f'# Load-Out\n    Shotgun = {a}\n    Assault-Rifle : {b}\n    Smg : {c}\n    Mobility : '
                f'\'{movebb}\'\n    Healing-Type : {e}\n    Other(Sniper\'s) : {f}')

        with tab2b:
            st.write(
                f'# Load-Out  \n##### Shotgun = {a}\n#####    Assault-Rifle : {b}\n#####    Smg : {c}'
                f'\n#####    Mobility : \'{movebb}\'\n#####    Healing-Type : {e}\n#####    Other(Sniper\'s) : {f}')

        with tab3b:
            st.json({
                'Load-Out': [
                    f'Shotgun = {a}',
                    f'Assault-Rifle = {b}',
                    f'Smg = {c}',
                    f'Mobility = \'{movebb}\'',
                    f'Healing-Type = {e}',
                    f'Other(Sniper\'s) : {f}'
                ],
            })
        with col2:
            taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])

            with taba1:
                st.write(f'# Rarity\n    Shotgun : {shotgun1}\n    Assault-Rifle : {ar1}\n    Smg : {smg2}\n    Mobility : {moveblade1}\n    Other(Sniper\'s) : {sniper2}')

            with taba2:
                st.write(f'# Rarity  \n##### Shotgun : {shotgun1}\n#####    Assault-Rifle : {ar1}\n#####    Smg : {smg2}\n#####    Mobility : {moveblade1}\n#####    Other(Sniper\'s) : {sniper2}')

            with taba3:
                st.json({
                    'Rarity': [
                        f'Shotgun : {shotgun1}',
                        f'Assault-Rifle : {ar1}',
                        f'Smg : {smg2}',
                        f'Mobility : {moveblade1}',
                        f'Other(Sniper\'s) : {sniper2}'
                    ],
                })
    if st.button('Randomize Load-Out'):
        button = + 1
    else:
        ''
with tab2:
    tab1, tab2, tab3aa = st.tabs(["Customize", "Loadout", "Info"])
    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            slot_one = st.selectbox(
                'Slot 1',
                ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Mobility', 'Healing', 'Sniping'))
            slot_two = st.selectbox(
                'Slot 2',
                ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Mobility', 'Healing', 'Sniping'))
            slot_three = st.selectbox(
                'Slot 3',
                ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Mobility', 'Healing', 'Sniping'))
            slot_four = st.selectbox(
                'Slot 4',
                ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Mobility', 'Healing', 'Sniping'))
            slot_five = st.selectbox(
                'Slot 5',
                ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Mobility', 'Healing', 'Sniping'))
        with col2:
            # Slot one
            if slot_one == 'Shotgun':
                shotgun11 = st.selectbox(
                    'Shotgun s1',
                    ('Havoc Pump Shotgun', 'Maven Auto Shotgun', 'Combat Shotgun'))
            elif slot_one == 'SMG':
                smg11 = st.selectbox(
                    'SMG s1',
                    ('Twin-Mag SMG', 'Run \'N\' Gun SMG', 'Tactical Pistol'))
            elif slot_one == 'Assault-Rifle':
                ar11 = st.selectbox(
                    'Assault-Rifle s1',
                    ('Overclocked Pulse Rifle', 'Red-Eye Assault Rifle', 'Havoc Suppressed Assault Rifle', 'Cobra DMR'))
            elif slot_one == 'Mobility':
                move11 = st.selectbox(
                    'Mobility s1',
                    ('Kinetic Blade', 'ODM Gear'))
            elif slot_one == 'Healing':
                heal11 = st.selectbox(
                    'Healing s1',
                    ('Slurp Juice', 'Chug Splash', 'Fish', 'Shield Fish'))
            elif slot_one == 'Sniping':
                snipe11 = st.selectbox(
                    'Sniper s1',
                    ('Heavy Sniper Rifle', 'Dragon\'s Breath Sniper'))
            # Slot two
            if slot_two == 'Shotgun':
                shotgun12 = st.selectbox(
                    'Shotgun s2',
                    ('Havoc Pump Shotgun ', 'Maven Auto Shotgun', 'Combat Shotgun'))
            elif slot_two == 'SMG':
                smg12 = st.selectbox(
                    'SMG s2',
                    ('Twin-Mag SMG ', 'Run \'N\' Gun SMG', 'Tactical Pistol'))
            elif slot_two == 'Assault-Rifle':
                ar12 = st.selectbox(
                    'Assault-Rifle s2',
                    ('Overclocked Pulse Rifle ', 'Red-Eye Assault Rifle', 'Havoc Suppressed Assault Rifle', 'Cobra DMR'))
            elif slot_two == 'Mobility':
                move12 = st.selectbox(
                    'Mobility s2',
                    ('Kinetic Blade ', 'ODM Gear'))
            elif slot_two == 'Healing':
                heal12 = st.selectbox(
                    'Healing s2',
                    ('Slurp Juice ', 'Chug Splash', 'Fish', 'Shield Fish'))
            elif slot_two == 'Sniping':
                snipe12 = st.selectbox(
                    'Sniper s2',
                    ('Heavy Sniper Rifle ', 'Dragon\'s Breath Sniper'))
            # Slot three
            if slot_three == 'Shotgun':
                shotgun13 = st.selectbox(
                    'Shotgun s3',
                    ('Havoc Pump Shotgun  ', 'Maven Auto Shotgun', 'Combat Shotgun'))
            elif slot_three == 'SMG':
                smg13 = st.selectbox(
                    'SMG s3',
                    ('Twin-Mag SMG  ', 'Run \'N\' Gun SMG', 'Tactical Pistol'))
            elif slot_three == 'Assault-Rifle':
                ar13 = st.selectbox(
                    'Assault-Rifle s3',
                    ('Overclocked Pulse Rifle  ', 'Red-Eye Assault Rifle', 'Havoc Suppressed Assault Rifle', 'Cobra DMR'))
            elif slot_three == 'Mobility':
                move13 = st.selectbox(
                    'Mobility s3',
                    ('Kinetic Blade  ', 'ODM Gear'))
            elif slot_three == 'Healing':
                heal13 = st.selectbox(
                    'Healing s3',
                    ('Slurp Juice  ', 'Chug Splash', 'Fish', 'Shield Fish'))
            elif slot_three == 'Sniping':
                snipe13 = st.selectbox(
                    'Sniper s3',
                    ('Heavy Sniper Rifle  ', 'Dragon\'s Breath Sniper'))
            # Slot four
            if slot_four == 'Shotgun':
                shotgun14 = st.selectbox(
                    'Shotgun s4',
                    ('Havoc Pump Shotgun   ', 'Maven Auto Shotgun', 'Combat Shotgun'))
            elif slot_four == 'SMG':
                smg14 = st.selectbox(
                    'SMG s4',
                    ('Twin-Mag SMG   ', 'Run \'N\' Gun SMG', 'Tactical Pistol'))
            elif slot_four == 'Assault-Rifle':
                ar14 = st.selectbox(
                    'Assault-Rifle s4',
                    ('Overclocked Pulse Rifle   ', 'Red-Eye Assault Rifle', 'Havoc Suppressed Assault Rifle', 'Cobra DMR'))
            elif slot_four == 'Mobility':
                move14 = st.selectbox(
                    'Mobility s4',
                    ('Kinetic Blade   ', 'ODM Gear'))
            elif slot_four == 'Healing':
                heal4 = st.selectbox(
                    'Healing s4',
                    ('Slurp Juice   ', 'Chug Splash', 'Fish', 'Shield Fish'))
            elif slot_four == 'Sniping':
                snipe14 = st.selectbox(
                    'Sniper s4',
                    ('Heavy Sniper Rifle   ', 'Dragon\'s Breath Sniper'))
            # Slot five
            if slot_five == 'Shotgun':
                shotgun15 = st.selectbox(
                    'Shotgun s5',
                    ('Havoc Pump Shotgun    ', 'Maven Auto Shotgun', 'Combat Shotgun'))
            elif slot_five == 'SMG':
                smg15 = st.selectbox(
                    'SMG s5',
                    ('Twin-Mag SMG    ', 'Run \'N\' Gun SMG', 'Tactical Pistol'))
            elif slot_five == 'Assault-Rifle':
                ar15 = st.selectbox(
                    'Assault-Rifle s5',
                    ('Overclocked Pulse Rifle    ', 'Red-Eye Assault Rifle', 'Havoc Suppressed Assault Rifle', 'Cobra DMR'))
            elif slot_five == 'Mobility':
                move15 = st.selectbox(
                    'Mobility s5',
                    ('Kinetic Blade    ', 'ODM Gear'))
            elif slot_five == 'Healing':
                heal15 = st.selectbox(
                    'Healing s5',
                    ('Slurp Juice    ', 'Chug Splash', 'Fish', 'Shield Fish'))
            elif slot_five == 'Sniping':
                snipe15 = st.selectbox(
                    'Sniper s5',
                    ('Heavy Sniper Rifle    ', 'Dragon\'s Breath Sniper'))
    with tab2:
        st.info('Not finished yet', icon="ℹ")
    with tab3aa:
        st.info('Not finished yet', icon="ℹ")
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.title('UPDATE INFO :')
        st.write('### [/] Fixed/changed full loadout system to an actual working tab')
        st.write('### [/] Fixed spelling error on shield fish in loadout>Customize')
        st.write('### [>] will add your custom loadout to loadout>loadout')
        st.write('### [>] will add video for loadout>info tab')

        st.write('# \n ##### [/] = Fixed\n ##### [:] = Changed something\n ##### [+] = Added\n ##### [-] = Removed\n ##### [>] = Will add at some point')
    with col2:
        st.title('SITE INFO :')
        st.write('### Rarity system in sidebar')
        st.write('### You can download the Source Code from the site or check my github for it')
        st.write('### \'How does the loadout tab work?\' video in third tab (at some point)')
with st.sidebar:
    if st.button('Source Code'):
        thing = + 1
    else:
        ''
    if thing == 1:
        code = '''https://github.com/fuzzybuzzyboy/py'''
        st.code(code, language='Text')
        thing = 0
    else:
        thing = 0
    video_file = open('video.mov', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.download_button(
        label='Download Video As .mov',
        data=video_file,
        file_name='Video',
        mime='',
    )
    site = open('i.py', 'rb')
    st.download_button(
        label='Download Site As .py File',
        data=site,
        file_name='Code.py',
    )
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
