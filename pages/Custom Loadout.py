import streamlit as st
import os
# print(st.session_state.session_id)
from datetime import datetime
import time

st.set_page_config(
    page_title='Custom Loadout',
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded",
)

tab1, tab2 = st.tabs(["Customize", "Loadout"])
with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        slotone = st.selectbox(
            'Slot 1',
            ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Healing'))
        slottwo = st.selectbox(
            'Slot 2',
            ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Healing'))
        slotthree = st.selectbox(
            'Slot 3',
            ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Healing'))
        slotfour = st.selectbox(
            'Slot 4',
            ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Healing'))
        slotfive = st.selectbox(
            'Slot 5',
            ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Healing'))
    with col2:
        # Slot one
        if slotone == 'Shotgun':
            slotone1 = st.selectbox(
                'Shotgun s1',
                ('Havoc Pump Shotgun', 'Drum Shotgun', 'Maven Auto Shotgun'))
        elif slotone == 'SMG':
            slotone1 = st.selectbox(
                'SMG s1',
                ('Submachine Gun', 'Tactical Pistol', 'Combat SMG', 'Run \'N\' Gun SMG'))
        elif slotone == 'Assault-Rifle':
            slotone1 = st.selectbox(
                'Assault-Rifle s1',
                ('MK-Alpha Assault Rifle', 'FlapJack Rifle', 'Explosive Repeater Rifle', 'Havoc Suppressed Assault Rifle', 'Thermal DMR'))
        elif slotone == 'Healing':
            slotone1 = st.selectbox(
                'Healing s1',
                ('Slurp Juice', 'Fish', 'Sheild Fish'))
        # Slot two
        if slottwo == 'Shotgun':
            slottwo1 = st.selectbox(
                'Shotgun s2',
                ('Havoc Pump Shotgun ', 'Drum Shotgun', 'Maven Auto Shotgun'))
        elif slottwo == 'SMG':
            slottwo1 = st.selectbox(
                'SMG s2',
                ('Submachine Gun ', 'Tactical Pistol', 'Combat SMG', 'Run \'N\' Gun SMG'))
        elif slottwo == 'Assault-Rifle':
            slottwo1 = st.selectbox(
                'Assault-Rifle s2',
                ('MK-Alpha Assault Rifle ', 'FlapJack Rifle', 'Explosive Repeater Rifle', 'Havoc Suppressed Assault Rifle', 'Thermal DMR'))
        elif slottwo == 'Healing':
            slottwo1 = st.selectbox(
                'Healing s2',
                ('Slurp Juice ', 'Fish', 'Sheild Fish'))
        # Slot three
        if slotthree == 'Shotgun':
            slotthree1 = st.selectbox(
                'Shotgun s3',
                ('Havoc Pump Shotgun  ', 'Drum Shotgun', 'Maven Auto Shotgun'))
        elif slotthree == 'SMG':
            slotthree1 = st.selectbox(
                'SMG s3',
                ('Submachine Gun  ', 'Tactical Pistol', 'Combat SMG', 'Run \'N\' Gun SMG'))
        elif slotthree == 'Assault-Rifle':
            slotthree1 = st.selectbox(
                'Assault-Rifle s3',
                ('MK-Alpha Assault Rifle  ', 'FlapJack Rifle', 'Explosive Repeater Rifle', 'Havoc Suppressed Assault Rifle', 'Thermal DMR'))
        elif slotthree == 'Healing':
            slotthree1 = st.selectbox(
                'Healing s3',
                ('Slurp Juice  ', 'Fish', 'Sheild Fish'))
        # Slot four
        if slotfour == 'Shotgun':
            shotgun14 = st.selectbox(
                'Shotgun s4',
                ('Havoc Pump Shotgun   ', 'Drum Shotgun', 'Maven Auto Shotgun'))
            slotfour1 = shotgun14
        elif slotfour == 'SMG':
            smg14 = st.selectbox(
                'SMG s4',
                ('Submachine Gun   ', 'Tactical Pistol', 'Combat SMG', 'Run \'N\' Gun SMG'))
            slotfour1 = smg14
        elif slotfour == 'Assault-Rifle':
            ar14 = st.selectbox(
                'Assault-Rifle s4',
                ('MK-Alpha Assault Rifle   ', 'FlapJack Rifle', 'Explosive Repeater Rifle', 'Havoc Suppressed Assault Rifle', 'Thermal DMR'))
            slotfour1 = ar14
        elif slotfour == 'Healing':
            heall4 = st.selectbox(
                'Healing s4',
                ('Slurp Juice   ', 'Fish', 'Sheild Fish'))
            slotfour1 = heall4
        # Slot five
        if slotfive == 'Shotgun':
            shotgun15 = st.selectbox(
                'Shotgun s5',
                ('Havoc Pump Shotgun    ', 'Drum Shotgun', 'Maven Auto Shotgun'))
            slotfive1 = shotgun15
        elif slotfive == 'SMG':
            smg15 = st.selectbox(
                'SMG s5',
                ('Submachine Gun    ', 'Tactical Pistol', 'Combat SMG', 'Run \'N\' Gun SMG'))
            slotfive1 = smg15
        elif slotfive == 'Assault-Rifle':
            ar15 = st.selectbox(
                'Assault-Rifle s5',
                ('MK-Alpha Assault Rifle     ', 'FlapJack Rifle', 'Explosive Repeater Rifle', 'Havoc Suppressed Assault Rifle', 'Thermal DMR'))
            slotfive1 = ar15
        elif slotfive == 'Healing':
            heal15 = st.selectbox(
                'Healing s5',
                ('Slurp Juice    ', 'Fish', 'Sheild Fish'))
            slotfive1 = heal15
    with col3:
        slotoner = 'None'
        slottwor = 'None'
        slotthreer = 'None'
        slotfourr = 'None'
        slotfiver = 'None'
        if slotone == 'None':
            pass
        elif slotone1 == 'Havoc Pump Shotgun':
            slotoner = st.selectbox(
                'Shotgun rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Drum Shotgun':
            slotoner = st.selectbox(
                'Shotgun rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotone1 == 'Maven Auto Shotgun':
            slotoner = st.selectbox(
                'Shotgun rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
        elif slotone1 == 'MK-Alpha Assault Rifle':
            slotoner = st.selectbox(
                'AR rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotone1 == 'FlapJack Rifle':
            slotoner = st.selectbox(
                'AR rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotone1 == 'Explosive Repeater Rifle':
            slotoner = st.selectbox(
                'AR rarity s1',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Havoc Suppressed Assault Rifle':
            slotoner = st.selectbox(
                'AR rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotone1 == 'Thermal DMR':
            slotoner = st.selectbox(
                'AR rarity s1',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Submachine Gun':
            slotoner = st.selectbox(
                'SMG rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Tactical Pistol':
            slotoner = st.selectbox(
                'SMG Rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotone1 == 'Combat SMG':
            slotoner = st.selectbox(
                'SMG rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Run \'N\' Gun SMG':
            slotoner = st.selectbox(
                'SMG rarity s1',
                ('Exotic', ''))
        if slottwo == 'None':
            pass
        elif slottwo1 == 'Havoc Pump Shotgun ':  # space
            slottwor = st.selectbox(
                'Shotgun rarity s2',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Drum Shotgun':
            slottwor = st.selectbox(
                'Shotgun rarity s2',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slottwo1 == 'Maven Auto Shotgun':
            slottwor = st.selectbox(
                'Shotgun rarity s2',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
        elif slottwo1 == 'MK-Alpha Assault Rifle ':  # space
            slottwor = st.selectbox(
                'AR rarity s2',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slottwo1 == 'FlapJack Rifle':
            slottwor = st.selectbox('FlapJack Rifle', 
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slottwo1 == 'Explosive Repeater Rifle':
            slottwor = st.selectbox(
                'AR rarity s2',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Havoc Suppressed Assault Rifle':
            slottwor = st.selectbox(
                'AR rarity s2',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slottwo1 == 'Thermal DMR':
            slottwor = st.selectbox(
                'AR rarity s2',
                ('Uncommon ', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Submachine Gun ':  # space
            slottwor = st.selectbox(
                'SMG rarity s2',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Combat SMG':
            slottwor = st.selectbox(
                'SMG rarity s2',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))  
        elif slottwo1 == 'Tactical Pistol':
            slottwor = st.selectbox(
                'SMG Rarity s2',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slottwo1 == 'Run \'N\' Gun SMG':
            slottwor = st.selectbox(
                'SMG rarity s2',
                ('Exotic ', ''))
        if slotthree == 'None':
            pass
        elif slotthree1 == 'Havoc Pump Shotgun  ':  # space
            slotthreer = st.selectbox(
                'Shotgun rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Maven Auto Shotgun':
            slotthreer = st.selectbox(
                'Shotgun rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
        elif slotthree1 == 'Drum Shotgun':
            slotthreer = st.selectbox(
                'Shotgun rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotthree1 == 'Overclocked Pulse Rifle  ':  # space
            slotthreer = st.selectbox(
                'AR rarity s3',
                ('Mythic', ''))
        elif slotthree1 == 'MK-Alpha Assault Rifle  ': # space
            slotthreer = st.selectbox(
                'AR rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotthree1 == 'FlapJack Rifle':
            slotthreer = st.selectbox(
                'AR rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotthree1 == 'Explosive Repeater Rifle':
            slotthreer = st.selectbox(
                'AR rarity s3',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Havoc Suppressed Assault Rifle':
            slotthreer = st.selectbox(
                'AR rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotthree1 == 'Thermal DMR':
            slotthreer = st.selectbox(
                'AR rarity s3',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Submachine Gun  ':  # space
            slottwor = st.selectbox(
                'SMG rarity s3',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Combat SMG':  # space
            slotthreer = st.selectbox(
                'SMG rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Tactical Pistol':
            slotthreer = st.selectbox(
                'SMG Rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotthree1 == 'Run \'N\' Gun SMG':
            slotthreer = st.selectbox(
                'SMG rarity s3',
                ('Exotic', ''))
        if slotfour == 'None':
            pass
        elif slotfour1 == 'Havoc Pump Shotgun   ':  # space
            slotfourr = st.selectbox(
                'Shotgun rarity s4',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Maven Auto Shotgun':
            slotfourr = st.selectbox(
                'Shotgun rarity s4',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
        elif slotfour1 == 'Drum Shotgun':
            slotfourr = st.selectbox(
                'Shotgun rarity s4',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotfour1 == 'MK-Alpha Assault Rifle   ': # space
            slotfourr = st.selectbox(
                'AR rarity s4',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotfour1 == 'FlapJack Rifle':
            slotfourr = st.selectbox(
                'AR rarity s4',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotfour1 == 'Explosive Repeater Rifle':
            slotfourr = st.selectbox(
                'AR rarity s4',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Havoc Suppressed Assault Rifle':
            slotfourr = st.selectbox(
                'AR rarity s4',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotfour1 == 'Thermal DMR':
            slotfourr = st.selectbox(
                'AR rarity s4',
                ('Uncommon ', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Submachine Gun   ': # space
            slottwor = st.selectbox(
                'SMG rarity s4',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Combat SMG': # space
            slottwor = st.selectbox(
                'SMG rarity s4',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))            
        elif slotfour1 == 'Tactical Pistol':
            slotfourr = st.selectbox(
                'SMG Rarity s4',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotfour1 == 'Run \'N\' Gun SMG':
            slotfourr = st.selectbox(
                'SMG rarity s4',
                ('Exotic ', ''))
        if slotfive == 'None':
            pass
        elif slotfive1 == 'Havoc Pump Shotgun    ':  # space
            slotfiver = st.selectbox(
                'Shotgun rarity s5',
                ('Common', 'Uncommon ', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Maven Auto Shotgun':
            slotfiver = st.selectbox(
                'Shotgun rarity s5',
                ('Common', 'Uncommon ', 'Rare', 'Epic', 'Legendary', 'Exotic'))
        elif slotfive1 == 'Drum Shotgun':
            slotfiver = st.selectbox(
                'Shotgun rarity s5',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotfive1 == 'MK-Alpha Assault Rifle     ': # space
            slotfiver = st.selectbox(
                'AR rarity s5',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotfive1 == 'Explosive Repeater Rifle':
            slotfiver = st.selectbox(
                'AR rarity s5',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))        
        elif slotfive1 == 'Havoc Suppressed Assault Rifle':
            slotfiver = st.selectbox(
                'AR rarity s5',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotfive1 == 'Cobra DMR':
            slotfiver = st.selectbox(
                'AR rarity s5',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Submachine Gun    ':  # space
            slotfiver = st.selectbox(
                'SMG rarity s5',
                ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Combat SMG':  # space
            slotfiver = st.selectbox(
                'SMG rarity s5',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Tactical Pistol':
            slotfiver = st.selectbox(
                'SMG Rarity s5',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
        elif slotfive1 == 'Run \'N\' Gun SMG':
            slotfiver = st.selectbox(
                'SMG rarity s5',
                ('Exotic', ''))
with tab2:
    if slotone == 'None' or slottwo == 'None' or slotthree == 'None' or slotfour == 'None' or slotfive == 'None':
        st.error('Create/complete your loadout before checking this tab.')
    else:
        col1, col2 = st.columns(2)
        with col1:
            taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])

            with taba1:
                tt = st.empty()
                tt.write(
                    f'# Custom loadout\n    {slotone} : {slotone1}\n    {slottwo} : {slottwo1}\n    {slotthree} : {slotthree1}\n    {slotfour} : {slotfour1}\n    {slotfive} : {slotfive1}')

            with taba2:
                tt1 = st.empty()
                tt1.write(
                    f'# Custom loadout  \n##### {slotone} : {slotone1}\n#####    {slottwo} : {slottwo1}\n#####    {slotthree} : {slotthree1}\n#####    {slotfour} : {slotfour1}\n#####    {slotfive} : {slotfive1}')

            with taba3:
                tt2 = st.empty()
                tt2.json({
                    'Custom loadout': [
                        f'{slotone} : {slotone1}',
                        f'{slottwo} : {slottwo1}',
                        f'{slotthree} : {slotthree1}',
                        f'{slotfour} : {slotfour1}',
                        f'{slotfive} : {slotfive1}'
                    ],
                })
        with col2:
            taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])

            with taba1:
                t = st.empty()
                t.write(
                    f'# Custom loadout rarity\n    {slotone} : {slotoner}\n    {slottwo} : {slottwor}\n    {slotthree} : {slotthreer}\n    {slotfour} : {slotfourr}\n    {slotfive} : {slotfiver}')

            with taba2:
                t1 = st.empty()
                t1.write(
                    f'# Custom loadout rarity  \n##### {slotone} : {slotoner}\n#####    {slottwo} : {slottwor}\n#####    {slotthree} : {slotthreer}\n#####    {slotfour} : {slotfourr}\n#####    {slotfive} : {slotfiver}')

            with taba3:
                t2 = st.empty()
                t1.json({
                    'Custom loadout rarity': [
                        f'{slotone} : {slotoner}',
                        f'{slottwo} : {slottwor}',
                        f'{slotthree} : {slotthreer}',
                        f'{slotfour} : {slotfourr}',
                        f'{slotfive} : {slotfiver}'
                    ],
                })
        st.divider()

    # The checks for st.session_state.session_id might not work on if you downloaded the file and ran it from your own computer. Please keep that in mind

    if 'session_id' not in st.session_state:
        st.session_state.session_id = None

    def get_user_id():
        query_params = st.experimental_get_query_params()
        return query_params.get('user_id', [None])[0]

    if st.button('Save Config'):
        user_id = get_user_id()
        if user_id is None:
            st.error("Unable to determine user ID.")
        else:
            file_name = f"configuration_{user_id}.txt"

            if os.path.exists(file_name):
                os.remove(file_name)

            with open(file_name, "a") as f:
                f.write(
                    f'{slotone}\n{slotone1}\n{slotoner}\n{slottwo}\n{slottwo1}\n{slottwor}\n{slotthree}\n{slotthree1}\n{slotthreer}\n{slotfour}\n{slotfour1}\n{slotfourr}\n{slotfive}\n{slotfive1}\n{slotfiver}'
                )
            st.success(f"Saved config to file '{file_name}'", icon="✅")

    if st.button('Load Config'):
        user_id = get_user_id()
        if user_id is None:
            st.error("Unable to determine user ID.")
        else:
            file_name = f"configuration_{user_id}.txt"

            if os.path.exists(file_name):
                with open(file_name, "r") as file:
                    lines = [line.strip() for line in file.readlines()]

                if len(lines) == 15:
                    slotone = lines[0]
                    slotone1 = lines[1]
                    slotoner = lines[2]
                    slottwo = lines[3]
                    slottwo1 = lines[4]
                    slottwor = lines[5]
                    slotthree = lines[6]
                    slotthree1 = lines[7]
                    slotthreer = lines[8]
                    slotfour = lines[9]
                    slotfour1 = lines[10]
                    slotfourr = lines[11]
                    slotfive = lines[12]
                    slotfive1 = lines[13]
                    slotfiver = lines[14]

                    st.success("Loaded configuration from file.")
                else:
                    st.error("Invalid configuration file. Expected 15 lines.")
            else:
                st.error("File doesn't exist. Please create/save a configuration.")
thing = 0
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
                    st.write(
                        f'# Clock\n    Current time : {time_now}\n    Date : {time_now1}\n##### Reminder, the clock will vanish when creating a new load-out. The clock button will show up.')
                    time_later = datetime.now().strftime("%S")
                    t += 1
                    time.sleep(1)

    st.warning('When loading a custom configuration it will only show in \'Loadout\'. If you check \'Customize\' you will see whatever was there before you loaded a configuration')
