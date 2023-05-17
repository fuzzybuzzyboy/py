# IMPORTANT IMPORTANT
# Command to run the file is : 'streamlit run {filename}.py' open your cmd in the folder with the file and run the command
# IMPORTANT IMPORTANT

# anything before the message below was not counted.
# THIS FILE CONTAINS 808 WRITTEN LINES OF CODE OR 34518 LETTERS OR 2829 WORDS

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
slottwo1 = 'None'
slotthree1 = 'None'
slotfour1 = 'None'
slotfive1 = 'None'
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
        elif smg == 3:
            c = '\'Run \'N\' Gun SMG\''
            smg2 = 'Exotic'
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
                f'\'{movebb}\'\n    Healing : {e}\n    Other(Snipers) : {f}')

        with tab2b:
            st.write(
                f'# Load-Out  \n##### Shotgun = {a}\n#####    Assault-Rifle : {b}\n#####    Smg : {c}'
                f'\n#####    Mobility : \'{movebb}\'\n#####    Healing : {e}\n#####    Other(Snipers) : {f}')

        with tab3b:
            st.json({
                'Load-Out': [
                    f'Shotgun = {a}',
                    f'Assault-Rifle = {b}',
                    f'Smg = {c}',
                    f'Mobility = \'{movebb}\'',
                    f'Healing = {e}',
                    f'Other(Snipers) : {f}'
                ],
            })
        with col2:
            taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])

            with taba1:
                st.write(f'# Rarity\n    Shotgun : {shotgun1}\n    Assault-Rifle : {ar1}\n    Smg : {smg2}\n    Mobility : {moveblade1}\n    Healing : no\n    Other(Snipers) : {sniper2}')

            with taba2:
                st.write(f'# Rarity  \n##### Shotgun : {shotgun1}\n#####    Assault-Rifle : {ar1}\n#####    Smg : {smg2}\n#####    Mobility : {moveblade1}\n#####    Healing : no\n#####    Other(Snipers) : {sniper2}')

            with taba3:
                st.json({
                    'Rarity': [
                        f'Shotgun : {shotgun1}',
                        f'Assault-Rifle : {ar1}',
                        f'Smg : {smg2}',
                        f'Mobility : {moveblade1}',
                        f'Healing : no',
                        f'Other(Snipers) : {sniper2}'
                    ],
                })
    if st.button('Randomize Load-Out'):
        button = + 1
    else:
        ''
with tab2:
    tab1, tab2, tab3aa = st.tabs(["Customize", "Loadout", "Info"])
    with tab1:
        col1, col2, col3 = st.columns(3)
        with col1:
            slotone = st.selectbox(
                'Slot 1',
                ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Mobility', 'Healing', 'Sniping'))
            slottwo = st.selectbox(
                'Slot 2',
                ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Mobility', 'Healing', 'Sniping'))
            slotthree = st.selectbox(
                'Slot 3',
                ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Mobility', 'Healing', 'Sniping'))
            slotfour = st.selectbox(
                'Slot 4',
                ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Mobility', 'Healing', 'Sniping'))
            slotfive = st.selectbox(
                'Slot 5',
                ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Mobility', 'Healing', 'Sniping'))
        with col2:
            # Slot one
            if slotone == 'Shotgun':
                slotone1 = st.selectbox(
                    'Shotgun s1',
                    ('Havoc Pump Shotgun', 'Maven Auto Shotgun', 'Combat Shotgun'))
            elif slotone == 'SMG':
                slotone1 = st.selectbox(
                    'SMG s1',
                    ('Twin-Mag SMG', 'Run \'N\' Gun SMG', 'Tactical Pistol'))
            elif slotone == 'Assault-Rifle':
                slotone1 = st.selectbox(
                    'Assault-Rifle s1',
                    ('Overclocked Pulse Rifle', 'Red-Eye Assault Rifle', 'Havoc Suppressed Assault Rifle', 'Cobra DMR'))
            elif slotone == 'Mobility':
                slotone1 = st.selectbox(
                    'Mobility s1',
                    ('Kinetic Blade', 'ODM Gear'))
            elif slotone == 'Healing':
                slotone1 = st.selectbox(
                    'Healing s1',
                    ('Slurp Juice', 'Chug Splash', 'Fish', 'Sheild Fish'))
            elif slotone == 'Sniping':
                slotone1 = st.selectbox(
                    'Sniper s1',
                    ('Heavy Sniper Rifle', 'Dragon\'s Breath Sniper'))
            # Slot two
            if slottwo == 'Shotgun':
                slottwo1 = st.selectbox(
                    'Shotgun s2',
                    ('Havoc Pump Shotgun ', 'Maven Auto Shotgun', 'Combat Shotgun'))
            elif slottwo == 'SMG':
                slottwo1 = st.selectbox(
                    'SMG s2',
                    ('Twin-Mag SMG ', 'Run \'N\' Gun SMG', 'Tactical Pistol'))
            elif slottwo == 'Assault-Rifle':
                slottwo1 = st.selectbox(
                    'Assault-Rifle s2',
                    ('Overclocked Pulse Rifle ', 'Red-Eye Assault Rifle', 'Havoc Suppressed Assault Rifle', 'Cobra DMR'))
            elif slottwo == 'Mobility':
                slottwo1 = st.selectbox(
                    'Mobility s2',
                    ('Kinetic Blade ', 'ODM Gear'))
            elif slottwo == 'Healing':
                slottwo1 = st.selectbox(
                    'Healing s2',
                    ('Slurp Juice ', 'Chug Splash', 'Fish', 'Sheild Fish'))
            elif slottwo == 'Sniping':
                slottwo1 = st.selectbox(
                    'Sniper s2',
                    ('Heavy Sniper Rifle ', 'Dragon\'s Breath Sniper'))
            # Slot three
            if slotthree == 'Shotgun':
                slotthree1 = st.selectbox(
                    'Shotgun s3',
                    ('Havoc Pump Shotgun  ', 'Maven Auto Shotgun', 'Combat Shotgun'))
            elif slotthree == 'SMG':
                slotthree1 = st.selectbox(
                    'SMG s3',
                    ('Twin-Mag SMG  ', 'Run \'N\' Gun SMG', 'Tactical Pistol'))
            elif slotthree == 'Assault-Rifle':
                slotthree1 = st.selectbox(
                    'Assault-Rifle s3',
                    ('Overclocked Pulse Rifle  ', 'Red-Eye Assault Rifle', 'Havoc Suppressed Assault Rifle', 'Cobra DMR'))
            elif slotthree == 'Mobility':
                slotthree1 = st.selectbox(
                    'Mobility s3',
                    ('Kinetic Blade  ', 'ODM Gear'))
            elif slotthree == 'Healing':
                slotthree1 = st.selectbox(
                    'Healing s3',
                    ('Slurp Juice  ', 'Chug Splash', 'Fish', 'Sheild Fish'))
            elif slotthree == 'Sniping':
                slotthree1 = st.selectbox(
                    'Sniper s3',
                    ('Heavy Sniper Rifle  ', 'Dragon\'s Breath Sniper'))
            # Slot four
            if slotfour == 'Shotgun':
                shotgun14 = st.selectbox(
                    'Shotgun s4',
                    ('Havoc Pump Shotgun   ', 'Maven Auto Shotgun', 'Combat Shotgun'))
                slotfour1 = shotgun14
            elif slotfour == 'SMG':
                smg14 = st.selectbox(
                    'SMG s4',
                    ('Twin-Mag SMG   ', 'Run \'N\' Gun SMG', 'Tactical Pistol'))
                slotfour1 = smg14
            elif slotfour == 'Assault-Rifle':
                ar14 = st.selectbox(
                    'Assault-Rifle s4',
                    ('Overclocked Pulse Rifle   ', 'Red-Eye Assault Rifle', 'Havoc Suppressed Assault Rifle', 'Cobra DMR'))
                slotfour1 = ar14
            elif slotfour == 'Mobility':
                move14 = st.selectbox(
                    'Mobility s4',
                    ('Kinetic Blade   ', 'ODM Gear'))
                slotfour1 = move14
            elif slotfour == 'Healing':
                heall4 = st.selectbox(
                    'Healing s4',
                    ('Slurp Juice   ', 'Chug Splash', 'Fish', 'Sheild Fish'))
                slotfour1 = heall4
            elif slotfour == 'Sniping':
                snipe14 = st.selectbox(
                    'Sniper s4',
                    ('Heavy Sniper Rifle   ', 'Dragon\'s Breath Sniper'))
                slotfour1 = snipe14
            # Slot five
            if slotfive == 'Shotgun':
                shotgun15 = st.selectbox(
                    'Shotgun s5',
                    ('Havoc Pump Shotgun    ', 'Maven Auto Shotgun', 'Combat Shotgun'))
                slotfive1 = shotgun15
            elif slotfive == 'SMG':
                smg15 = st.selectbox(
                    'SMG s5',
                    ('Twin-Mag SMG    ', 'Run \'N\' Gun SMG', 'Tactical Pistol'))
                slotfive1 = smg15
            elif slotfive == 'Assault-Rifle':
                ar15 = st.selectbox(
                    'Assault-Rifle s5',
                    ('Overclocked Pulse Rifle    ', 'Red-Eye Assault Rifle', 'Havoc Suppressed Assault Rifle', 'Cobra DMR'))
                slotfive1 = ar15
            elif slotfive == 'Mobility':
                move15 = st.selectbox(
                    'Mobility s5',
                    ('Kinetic Blade    ', 'ODM Gear'))
                slotfive1 = move15
            elif slotfive == 'Healing':
                heal15 = st.selectbox(
                    'Healing s5',
                    ('Slurp Juice    ', 'Chug Splash', 'Fish', 'Sheild Fish'))
                slotfive1 = heal15
            elif slotfive == 'Sniping':
                snipe15 = st.selectbox(
                    'Sniper s5',
                    ('Heavy Sniper Rifle    ', 'Dragon\'s Breath Sniper'))
                slotfive1 = snipe15
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
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotone1 == 'Maven Auto Shotgun':
                slotoner = st.selectbox(
                    'Shotgun rarity s1',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slotone1 == 'Combat Shotgun':
                slotoner = st.selectbox(
                    'Shotgun rarity s1',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slotone1 == 'Overclocked Pulse Rifle':
                slotoner = st.selectbox(
                    'AR rarity s1',
                    ('Mythic', ''))
            elif slotone1 == 'Red-Eye Assault Rifle':
                slotoner = st.selectbox(
                    'AR rarity s1',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
            elif slotone1 == 'Havoc Suppressed Assault Rifle':
                slotoner = st.selectbox(
                    'AR rarity s1',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotone1 == 'Cobra DMR':
                slotoner = st.selectbox(
                    'AR rarity s1',
                    ('Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slotone1 == 'Twin-Mag SMG':
                slotoner = st.selectbox(
                    'SMG rarity s1',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
            elif slotone1 == 'Tactical Pistol':
                slotoner = st.selectbox(
                    'SMG Rarity s1',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotone1 == 'Run \'N\' Gun SMG':
                slotoner = st.selectbox(
                    'SMG rarity s1',
                    ('Exotic', ''))
            elif slotone1 == 'Heavy Sniper Rifle':
                slotoner = st.selectbox(
                    'Sniper rarity s1',
                    ('Rare', 'Epic', 'Legendary'))
            elif slotone1 == 'Dragon\'s Breath Sniper':
                slotoner = st.selectbox(
                    'Sniper rarity s1',
                    ('Exotic', ''))
            elif slotone1 == 'Kinetic Blade':
                slotoner = st.selectbox(
                    'Mobility rarity s1',
                    ('Epic', 'Rare'))
            elif slotone1 == 'ODM Gear':
                slotoner = st.selectbox(
                    'Mobility rarity s1',
                    ('Mythic', ''))
            if slottwo == 'None':
                pass
            elif slottwo1 == 'Havoc Pump Shotgun ': # space
                slottwor = st.selectbox(
                    'Shotgun rarity s2',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slottwo1 == 'Maven Auto Shotgun':
                slottwor = st.selectbox(
                    'Shotgun rarity s2',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slottwo1 == 'Combat Shotgun':
                slottwor = st.selectbox(
                    'Shotgun rarity s2',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slottwo1 == 'Overclocked Pulse Rifle ': # space
                slottwor = st.selectbox(
                    'AR rarity s2',
                    ('Mythic ', ''))
            elif slottwo1 == 'Red-Eye Assault Rifle':
                slottwor = st.selectbox(
                    'AR rarity s2',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
            elif slottwo1 == 'Havoc Suppressed Assault Rifle':
                slottwor = st.selectbox(
                    'AR rarity s2',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slottwo1 == 'Cobra DMR':
                slottwor = st.selectbox(
                    'AR rarity s2',
                    ('Uncommon ', 'Rare', 'Epic', 'Legendary'))
            elif slottwo1 == 'Twin-Mag SMG ': # space
                slottwor = st.selectbox(
                    'SMG rarity s2',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
            elif slottwo1 == 'Tactical Pistol':
                slottwor = st.selectbox(
                    'SMG Rarity s2',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slottwo1 == 'Run \'N\' Gun SMG':
                slottwor = st.selectbox(
                    'SMG rarity s2',
                    ('Exotic ', ''))
            elif slottwo1 == 'Heavy Sniper Rifle ': # space
                slottwor = st.selectbox(
                    'Sniper rarity s2',
                    ('Rare ', 'Epic', 'Legendary'))
            elif slottwo1 == 'Dragon\'s Breath Sniper':
                slottwor = st.selectbox(
                    'Sniper rarity s2',
                    ('Exotic ', ''))
            elif slottwo1 == 'Kinetic Blade ': # space
                slottwor = st.selectbox(
                    'Mobility rarity s2',
                    ('Epic ', 'Rare'))
            elif slottwo1 == 'ODM Gear':
                slottwor = st.selectbox(
                    'Mobility rarity s2',
                    ('Mythic ', ''))
            if slotthree == 'None':
                pass
            elif slotthree1 == 'Havoc Pump Shotgun  ': # space
                slotthreer = st.selectbox(
                    'Shotgun rarity s3',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotthree1 == 'Maven Auto Shotgun':
                slotthreer = st.selectbox(
                    'Shotgun rarity s3',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slotthree1 == 'Combat Shotgun':
                slotthreer = st.selectbox(
                    'Shotgun rarity s3',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slotthree1 == 'Overclocked Pulse Rifle  ': # space
                slotthreer = st.selectbox(
                    'AR rarity s3',
                    ('Mythic', ''))
            elif slotthree1 == 'Red-Eye Assault Rifle':
                slotthreer = st.selectbox(
                    'AR rarity s3',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
            elif slotthree1 == 'Havoc Suppressed Assault Rifle':
                slotthreer = st.selectbox(
                    'AR rarity s3',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotthree1 == 'Cobra DMR':
                slotthreer = st.selectbox(
                    'AR rarity s3',
                    ('Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slotthree1 == 'Twin-Mag SMG  ': # space
                slotthreer = st.selectbox(
                    'SMG rarity s3',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
            elif slotthree1 == 'Tactical Pistol':
                slotthreer = st.selectbox(
                    'SMG Rarity s3',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotthree1 == 'Run \'N\' Gun SMG':
                slotthreer = st.selectbox(
                    'SMG rarity s3',
                    ('Exotic', ''))
            elif slotthree1 == 'Heavy Sniper Rifle  ': # space
                slotthreer = st.selectbox(
                    'Sniper rarity s3',
                    ('Rare', 'Epic', 'Legendary'))
            elif slotthree1 == 'Dragon\'s Breath Sniper':
                slotthreer = st.selectbox(
                    'Sniper rarity s3',
                    ('Exotic', ''))
            elif slotthree1 == 'Kinetic Blade  ': # space
                slotthreer = st.selectbox(
                    'Mobility rarity s3',
                    ('Epic', 'Rare'))
            elif slotthree1 == 'ODM Gear':
                slotthreer = st.selectbox(
                    'Mobility rarity s3',
                    ('Mythic', ''))
            if slotfour == 'None':
                pass
            elif slotfour1 == 'Havoc Pump Shotgun   ': # space
                slotfourr = st.selectbox(
                    'Shotgun rarity s4',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotfour1 == 'Maven Auto Shotgun':
                slotfourr = st.selectbox(
                    'Shotgun rarity s4',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slotfour1 == 'Combat Shotgun':
                slotfourr = st.selectbox(
                    'Shotgun rarity s4',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slotfour1 == 'Overclocked Pulse Rifle   ': # space
                slotfourr = st.selectbox(
                    'AR rarity s4',
                    ('Mythic ', ''))
            elif slotfour1 == 'Red-Eye Assault Rifle':
                slotfourr = st.selectbox(
                    'AR rarity s4',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
            elif slotfour1 == 'Havoc Suppressed Assault Rifle':
                slotfourr = st.selectbox(
                    'AR rarity s4',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotfour1 == 'Cobra DMR':
                slotfourr = st.selectbox(
                    'AR rarity s4',
                    ('Uncommon ', 'Rare', 'Epic', 'Legendary'))
            elif slotfour1 == 'Twin-Mag SMG   ': # space
                slotfourr = st.selectbox(
                    'SMG rarity s4',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
            elif slotfour1 == 'Tactical Pistol':
                slotfourr = st.selectbox(
                    'SMG Rarity s4',
                    ('Common ', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotfour1 == 'Run \'N\' Gun SMG':
                slotfourr = st.selectbox(
                    'SMG rarity s4',
                    ('Exotic ', ''))
            elif slotfour1 == 'Heavy Sniper Rifle   ': # space
                slotfourr = st.selectbox(
                    'Sniper rarity s4',
                    ('Rare ', 'Epic', 'Legendary'))
            elif slotfour1 == 'Dragon\'s Breath Sniper':
                slotfourr = st.selectbox(
                    'Sniper rarity s4',
                    ('Exotic ', ''))
            elif slotfour1 == 'Kinetic Blade   ': # space
                slotfourr = st.selectbox(
                    'Mobility rarity s4',
                    ('Epic ', 'Rare'))
            elif slotfour1 == 'ODM Gear':
                slotfourr = st.selectbox(
                    'Mobility rarity s4',
                    ('Mythic ', ''))
            if slotfive == 'None':
                pass
            elif slotfive1 == 'Havoc Pump Shotgun    ': # space
                slotfiver = st.selectbox(
                    'Shotgun rarity s5',
                    ('Common', 'Uncommon ', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotfive1 == 'Maven Auto Shotgun':
                slotfiver = st.selectbox(
                    'Shotgun rarity s5',
                    ('Common', 'Uncommon ', 'Rare', 'Epic', 'Legendary'))
            elif slotfive1 == 'Combat Shotgun':
                slotfiver = st.selectbox(
                    'Shotgun rarity s5',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slotfive1 == 'Overclocked Pulse Rifle    ': # space
                slotfiver = st.selectbox(
                    'AR rarity s5',
                    ('Mythic', ''))
            elif slotfive1 == 'Red-Eye Assault Rifle':
                slotfiver = st.selectbox(
                    'AR rarity s5',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
            elif slotfive1 == 'Havoc Suppressed Assault Rifle':
                slotfiver = st.selectbox(
                    'AR rarity s5',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotfive1 == 'Cobra DMR':
                slotfiver = st.selectbox(
                    'AR rarity s5',
                    ('Uncommon', 'Rare', 'Epic', 'Legendary'))
            elif slotfive1 == 'Twin-Mag SMG    ': # space
                slotfiver = st.selectbox(
                    'SMG rarity s5',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Exotic'))
            elif slotfive1 == 'Tactical Pistol':
                slotfiver = st.selectbox(
                    'SMG Rarity s5',
                    ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'))
            elif slotfive1 == 'Run \'N\' Gun SMG':
                slotfiver = st.selectbox(
                    'SMG rarity s5',
                    ('Exotic', ''))
            elif slotfive1 == 'Heavy Sniper Rifle    ': # space
                slotfiver = st.selectbox(
                    'Sniper rarity s5',
                    ('Rare', 'Epic', 'Legendary'))
            elif slotfive1 == 'Dragon\'s Breath Sniper':
                slotfiver = st.selectbox(
                    'Sniper rarity s5',
                    ('Exotic', ''))
            elif slotfive1 == 'Kinetic Blade    ': # space
                slotfiver = st.selectbox(
                    'Mobility rarity s5',
                    ('Epic', 'Rare'))
            elif slotfive1 == 'ODM Gear':
                slotfiver = st.selectbox(
                    'Mobility rarity s5',
                    ('Mythic', ''))
    with tab2:
        if slotone == 'None' or slottwo == 'None' or slotthree == 'None' or slotfour == 'None' or slotfive == 'None':
            st.error('Create your loadout before checking this tab.')
        else:
            col1, col2 = st.columns(2)
            with col1:
                taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])

                with taba1:
                    st.write(f'# Custom loadout\n    {slotone} : {slotone1}\n    {slottwo} : {slottwo1}\n    {slotthree} : {slotthree1}\n    {slotfour} : {slotfour1}\n    {slotfive} : {slotfive1}')

                with taba2:
                    st.write(f'# Custom loadout  \n##### {slotone} : {slotone1}\n#####    {slottwo} : {slottwo1}\n#####    {slotthree} : {slotthree1}\n#####    {slotfour} : {slotfour1}\n#####    {slotfive} : {slotfive1}')

                with taba3:
                    st.json({
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
                    st.write(f'# Custom loadout rarity\n    {slotone} : {slotoner}\n    {slottwo} : {slotoner}\n    {slotthree} : {slotthreer}\n    {slotfour} : {slotfourr}\n    {slotfive} : {slotfiver}')

                with taba2:
                    st.write(f'# Custom loadout rarity  \n##### {slotone} : {slotoner}\n#####    {slottwo} : {slotoner}\n#####    {slotthree} : {slotthreer}\n#####    {slotfour} : {slotfourr}\n#####    {slotfive} : {slotfiver}')

                with taba3:
                    st.json({
                        'Custom loadout rarity': [
                            f'{slotone} : {slotoner}',
                            f'{slottwo} : {slottwor}',
                            f'{slotthree} : {slotthreer}',
                            f'{slotfour} : {slotfourr}',
                            f'{slotfive} : {slotfiver}'
                        ],
                    })
    with tab3aa:
        st.info('Not finished yet', icon="ℹ️")
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.title('UPDATE INFO :')
        st.write('### [+] Entire custom loadout tab finished.')
        st.write('### [:] When selecting rarity in custom loadout single rarity items would bug')
        st.write('### [///] Custom Loadout>Info Is in progress')
        st.write('# \n ##### [/] = Fixed\n ##### [//] = Reverted\n ##### [///] = Working on\n ##### [:] = Changed something\n ##### [+] = Added\n ##### [-] = Removed\n ##### [>] = Add later\n\n\n ##### also pls tell me about bugs and other things so i can fix them (on discord) :)')
    with col2:
        st.title('SITE INFO :')
        st.write('### You can download the Source Code from the sidebar or check my github for it')
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
