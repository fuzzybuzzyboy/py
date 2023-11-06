import streamlit as st
import os, time, platform
from datetime import datetime

st.set_page_config(
    page_title='Custom Loadout',
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help': 'https://github.com/fuzzybuzzyboy/py',
        'Report a bug': "https://github.com/fuzzybuzzyboy/py",
        'About': "Random items generator for fortnite (no this doesn't inject into your game and do something blah blah blah)"
    }
)

login = platform.node()

Folder_Path = "configs"
File_Path = os.path.join(Folder_Path, login)

tab1, tab2 = st.tabs(["Customize", "Loadout"])
with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        slotone = st.selectbox(
            'Slot 1',
            ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Snipers', 'Explosives', 'Other'))
        slottwo = st.selectbox(
            'Slot 2',
            ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Snipers', 'Explosives', 'Other'))
        slotthree = st.selectbox(
            'Slot 3',
            ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Snipers', 'Explosives', 'Other'))
        slotfour = st.selectbox(
            'Slot 4',
            ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Snipers', 'Explosives', 'Other'))
        slotfive = st.selectbox(
            'Slot 5',
            ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Snipers', 'Explosives', 'Other'))
    with col2:
        # Slot one
        if slotone == 'Shotgun':
            slotone1 = st.selectbox(
                'Shotgun s1',
                ('Tactical Shotgun', 'Pump Shotgun', 'Heavy Shotgun'))
        elif slotone == 'SMG':
            slotone1 = st.selectbox(
                'SMG s1',
                ('Submachine Gun', 'Suppressed Submachine Gun', 'Pistol', 'Suppressed Pistol'))
        elif slotone == 'Assault-Rifle':
            slotone1 = st.selectbox(
                'Assault-Rifle s1',
                ('Assault Rifle', 'Suppressed Assualt Rifle', 'Burst Assualt Rifle', 'Tactical Assualt Rifle', 'Scoped Assualt Rifle'))
        elif slotone == 'Snipers':
            slotone1 = st.selectbox(
                'Snipers s1',
                ('Hunting Rifle', 'Bolt-Action Sniper Rifle', 'Semi-Automatic Sniper Rifle'))
        elif slotone == 'Explosives':
            slotone1 = st.selectbox(
                'Explosives s1',
                ('Rocket Launcher', 'Grenade Launcher'))
        elif slotone == 'Other':
            slotone1 = st.selectbox(
                'Other s1',
                ('Light Machine Gun', 'Hand Cannon', 'Chug Jug', 'Shield Potion', 'Small Shield Potion', 'Medkit', 'Mushroom', 'Corn', 'Coconut', 'Cabbage', 'Banana', 'Apple'))
        # Slot two
        if slottwo == 'Shotgun':
            slottwo1 = st.selectbox(
                'Shotgun s2',
                ('Tactical Shotgun ', 'Pump Shotgun', 'Heavy Shotgun'))
        elif slottwo == 'SMG':
            slottwo1 = st.selectbox(
                'SMG s2',
                ('Submachine Gun ', 'Suppressed Submachine Gun', 'Pistol', 'Suppressed Pistol'))
        elif slottwo == 'Assault-Rifle':
            slottwo1 = st.selectbox(
                'Assault-Rifle s2',
                ('Assault Rifle ', 'Suppressed Assualt Rifle', 'Burst Assualt Rifle', 'Tactical Assualt Rifle', 'Scoped Assualt Rifle'))
        elif slottwo == 'Snipers':
            slottwo1 = st.selectbox(
                'Snipers s2',
                ('Hunting Rifle ', 'Bolt-Action Sniper Rifle', 'Semi-Automatic Sniper Rifle'))
        elif slottwo == 'Explosives':
            slottwo1 = st.selectbox(
                'Explosives s2',
                ('Rocket Launcher ', 'Grenade Launcher'))
        elif slottwo == 'Other':
            slottwo1 = st.selectbox(
                'Other s2',
                ('Light Machine Gun ', 'Hand Cannon', 'Chug Jug', 'Shield Potion', 'Small Shield Potion', 'Medkit', 'Mushroom', 'Corn', 'Coconut', 'Cabbage', 'Banana', 'Apple'))
        # Slot three
        if slotthree == 'Shotgun':
            slotthree1 = st.selectbox(
                'Shotgun s3',
                ('Tactical Shotgun  ', 'Pump Shotgun', 'Heavy Shotgun'))
        elif slotthree == 'SMG':
            slotthree1 = st.selectbox(
                'SMG s3',
                ('Submachine Gun  ', 'Suppressed Submachine Gun', 'Pistol', 'Suppressed Pistol'))
        elif slotthree == 'Assault-Rifle':
            slotthree1 = st.selectbox(
                'Assault-Rifle s3',
                ('Assault Rifle  ', 'Suppressed Assualt Rifle', 'Burst Assualt Rifle', 'Tactical Assualt Rifle', 'Scoped Assualt Rifle'))
        elif slotthree == 'Snipers':
            slotthree1 = st.selectbox(
                'Snipers s3',
                ('Hunting Rifle  ', 'Bolt-Action Sniper Rifle', 'Semi-Automatic Sniper Rifle'))
        elif slotthree == 'Explosives':
            slotthree1 = st.selectbox(
                'Explosives s3',
                ('Rocket Launcher  ', 'Grenade Launcher'))
        elif slotthree == 'Other':
            slotthree1 = st.selectbox(
                'Other s3',
                ('Light Machine Gun  ', 'Hand Cannon', 'Chug Jug', 'Shield Potion', 'Small Shield Potion', 'Medkit', 'Mushroom', 'Corn', 'Coconut', 'Cabbage', 'Banana', 'Apple'))
        # Slot four
        if slotfour == 'Shotgun':
            slotfour1 = st.selectbox(
                'Shotgun s4',
                ('Tactical Shotgun   ', 'Pump Shotgun', 'Heavy Shotgun'))
        elif slotfour == 'SMG':
            slotfour1 = st.selectbox(
                'SMG s4',
                ('Submachine Gun   ', 'Suppressed Submachine Gun', 'Pistol', 'Suppressed Pistol'))
        elif slotfour == 'Assault-Rifle':
            slotfour1 = st.selectbox(
                'Assault-Rifle s4',
                ('Assault Rifle   ', 'Suppressed Assualt Rifle', 'Burst Assualt Rifle', 'Tactical Assualt Rifle', 'Scoped Assualt Rifle'))
        elif slotfour == 'Snipers':
            slotfour1 = st.selectbox(
                'Healing s4',
                ('Hunting Rifle   ', 'Bolt-Action Sniper Rifle', 'Semi-Automatic Sniper Rifle'))
        elif slotfour == 'Explosives':
            slotfour1 = st.selectbox(
                'Healing s4',
                ('Rocket Launcher   ', 'Grenade Launcher'))
        elif slotfour == 'Other':
            slotfour1 = st.selectbox(
                'Healing s4',
                ('Light Machine Gun   ', 'Hand Cannon', 'Chug Jug', 'Shield Potion', 'Small Shield Potion', 'Medkit', 'Mushroom', 'Corn', 'Coconut', 'Cabbage', 'Banana', 'Apple'))      
        # Slot five
        if slotfive == 'Shotgun':
            slotfive1 = st.selectbox(
                'Shotgun s5',
                ('Tactical Shotgun    ', 'Pump Shotgun', 'Heavy Shotgun'))
        elif slotfive == 'SMG':
            slotfive1 = st.selectbox(
                'SMG s5',
                ('Submachine Gun    ', 'Suppressed Submachine Gun', 'Pistol', 'Suppressed Pistol'))
        elif slotfive == 'Assault-Rifle':
            slotfive1 = st.selectbox(
                'Assault-Rifle s5',
                ('Assault Rifle    ', 'Suppressed Assualt Rifle', 'Burst Assualt Rifle', 'Tactical Assualt Rifle', 'Scoped Assualt Rifle'))
        elif slotfive == 'Snipers':
            slotfive1 = st.selectbox(
                'Snipers s5',
                ('Hunting Rifle    ', 'Bolt-Action Sniper Rifle', 'Semi-Automatic Sniper Rifle'))
        elif slotfive == 'Explosives':
            slotfive1 = st.selectbox(
                'Explosives s5',
                ('Rocket Launcher    ', 'Grenade Launcher'))
        elif slotfive == 'Other':
            slotfive1 = st.selectbox(
                'Other s5',
                ('Light Machine Gun    ', 'Hand Cannon', 'Chug Jug', 'Shield Potion', 'Small Shield Potion', 'Medkit', 'Mushroom', 'Corn', 'Coconut', 'Cabbage', 'Banana', 'Apple'))
    with col3:
        slotoner = 'None'
        slottwor = 'None'
        slotthreer = 'None'
        slotfourr = 'None'
        slotfiver = 'None'
        if slotone == 'None':
            pass
        elif slotone1 == 'Tactical Shotgun' or slotone1 == 'Pump Shotgun':
            slotoner = st.selectbox(
                'Shotgun rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Heavy Shotgun':
            slotoner = st.selectbox(
                'Shotgun rarity s1',
                ('Epic', 'Legendary'))
        elif slotone1 == 'Assault Rifle' or slotone1 == 'Burst Assualt Rifle':
            slotoner = st.selectbox(
                'AR rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Suppressed Assualt Rifle':
            slotoner = st.selectbox(
                'AR rarity s1',
                ('Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Tactical Assualt Rifle':
            slotoner = st.selectbox(
                'AR rarity s1',
                ('Legendary',))
        elif slotone1 == 'Scoped Assualt Rifle':
            slotoner = st.selectbox(
                'AR rarity s1',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Submachine Gun':
            slotoner = st.selectbox(
                'SMG rarity s1',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Suppressed Submachine Gun' or slotone1 == 'Pistol':
            slotoner = st.selectbox(
                'SMG Rarity s1',
                ('Common', 'Uncommon', 'Rare'))
        elif slotone1 == 'Suppressed Pistol':
            slotoner = st.selectbox(
                'SMG rarity s1',
                ('Rare', 'Epic'))
        elif slotone1 == 'Hunting Rifle':
            slotoner = st.selectbox(
                'Snipers rarity s1',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Bolt-Action Sniper Rifle':
            slotoner = st.selectbox(
                'Snipers rarity s1',
                ('Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Semi-Automatic Sniper Rifle':
            slotoner = st.selectbox(
                'Snipers rarity s1',
                ('Uncommon', 'Rare'))
        elif slotone1 == 'Rocket Launcher' or slotone1 == 'Grenade Launcher':
            slotoner = st.selectbox(
                'Explosives rarity s1',
                ('Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Light Machine Gun':
            slotoner = st.selectbox(
                'Other rarity s1',
                ('Rare', 'Epic'))
        elif slotone1 == 'Hand Cannon':
            slotoner = st.selectbox(
                'Other rarity s1',
                ('Epic', 'Legendary'))
        elif slotone1 == 'Chug Jug' or slotone1 == 'Shield Potion' or slotone1 == 'Small Shield Potion' or slotone1 == 'Medkit' or slotone1 == 'Mushroom' or slotone1 == 'Corn' or slotone1 == 'Coconut' or slotone1 == 'Cabbage' or slotone1 == 'Banana' or slotone1 == 'Apple':
            slotoner = st.selectbox(
                'Other rarity s1',
                ('None',))         

# SLOT TWO DOWN

        if slottwo == 'None':
            pass
        elif slottwo1 == 'Tactical Shotgun ' or slottwo1 == 'Pump Shotgun': # [SPACE]
            slottwor = st.selectbox(
                'Shotgun rarity s2',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Heavy Shotgun':
            slottwor = st.selectbox(
                'Shotgun rarity s2',
                ('Epic', 'Legendary'))
        elif slottwo1 == 'Assault Rifle ' or slottwo1 == 'Burst Assualt Rifle': # [SPACE]
            slottwor = st.selectbox(
                'AR rarity s2',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Suppressed Assualt Rifle':
            slottwor = st.selectbox(
                'AR rarity s2',
                ('Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Tactical Assualt Rifle':
            slottwor = st.selectbox(
                'AR rarity s2',
                ('Legendary',))
        elif slottwo1 == 'Scoped Assualt Rifle':
            slottwor = st.selectbox(
                'AR rarity s2',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Submachine Gun ':
            slottwor = st.selectbox(
                'SMG rarity s2',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Suppressed Submachine Gun' or slottwo1 == 'Pistol':
            slottwor = st.selectbox(
                'SMG Rarity s2',
                ('Common', 'Uncommon', 'Rare'))
        elif slottwo1 == 'Suppressed Pistol':
            slottwor = st.selectbox(
                'SMG rarity s2',
                ('Rare', 'Epic'))
        elif slottwo1 == 'Hunting Rifle ': # [SPACE]
            slottwor = st.selectbox(
                'Snipers rarity s2',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Bolt-Action Sniper Rifle':
            slottwor = st.selectbox(
                'Snipers rarity s2',
                ('Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Semi-Automatic Sniper Rifle':
            slottwor = st.selectbox(
                'Snipers rarity s2',
                ('Uncommon', 'Rare'))
        elif slottwo1 == 'Rocket Launcher ' or slottwo1 == 'Grenade Launcher': # [SPACE]
            slottwor = st.selectbox(
                'Explosives rarity s2',
                ('Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Light Machine Gun ': # [SPACE]
            slottwor = st.selectbox(
                'Other rarity s2',
                ('Rare', 'Epic'))
        elif slottwo1 == 'Hand Cannon':
            slottwor = st.selectbox(
                'Other rarity s2',
                ('Epic', 'Legendary'))
        elif slottwo1 == 'Chug Jug' or slottwo1 == 'Shield Potion' or slottwo1 == 'Small Shield Potion' or slottwo1 == 'Medkit' or slottwo1 == 'Mushroom' or slottwo1 == 'Corn' or slottwo1 == 'Coconut' or slottwo1 == 'Cabbage' or slottwo1 == 'Banana' or slottwo1 == 'Apple':
            slottwor = st.selectbox(
                'Other rarity s2',
                ('None',))

# SLOT THREE DOWN

        if slotthree == 'None':
            pass
        elif slotthree1 == 'Tactical Shotgun  ' or slotthree1 == 'Pump Shotgun': # [SPACE]
            slotthreer = st.selectbox(
                'Shotgun rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Heavy Shotgun':
            slotthreer = st.selectbox(
                'Shotgun rarity s3',
                ('Epic', 'Legendary'))
        elif slotthree1 == 'Assault Rifle  ' or slotthree1 == 'Burst Assualt Rifle': # [SPACE]
            slotthreer = st.selectbox(
                'AR rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Suppressed Assualt Rifle':
            slotthreer = st.selectbox(
                'AR rarity s3',
                ('Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Tactical Assualt Rifle':
            slotthreer = st.selectbox(
                'AR rarity s3',
                ('Legendary',))
        elif slotthree1 == 'Scoped Assualt Rifle':
            slotthreer = st.selectbox(
                'AR rarity s3',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Submachine Gun  ': # [SPACE]
            slotthreer = st.selectbox(
                'SMG rarity s3',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Suppressed Submachine Gun' or slotthree1 == 'Pistol':
            slotthreer = st.selectbox(
                'SMG Rarity s3',
                ('Common', 'Uncommon', 'Rare'))
        elif slotthree1 == 'Suppressed Pistol':
            slotthreer = st.selectbox(
                'SMG rarity s3',
                ('Rare', 'Epic'))
        elif slotthree1 == 'Hunting Rifle  ': # [SPACE]
            slotthreer = st.selectbox(
                'Snipers rarity s3',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Bolt-Action Sniper Rifle':
            slotthreer = st.selectbox(
                'Snipers rarity s3',
                ('Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Semi-Automatic Sniper Rifle':
            slotthreer = st.selectbox(
                'Snipers rarity s3',
                ('Uncommon', 'Rare'))
        elif slotthree1 == 'Rocket Launcher  ' or slotthree1 == 'Grenade Launcher': # [SPACE]
            slotthreer = st.selectbox(
                'Explosives rarity s3',
                ('Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Light Machine Gun  ': # [SPACE]
            slotthreer = st.selectbox(
                'Other rarity s3',
                ('Rare', 'Epic'))
        elif slotthree1 == 'Hand Cannon':
            slotthreer = st.selectbox(
                'Other rarity s3',
                ('Epic', 'Legendary'))
        elif slotthree1 == 'Chug Jug' or slotthree1 == 'Shield Potion' or slotthree1 == 'Small Shield Potion' or slotthree1 == 'Medkit' or slotthree1 == 'Mushroom' or slotthree1 == 'Corn' or slotthree1 == 'Coconut' or slotthree1 == 'Cabbage' or slotthree1 == 'Banana' or slotthree1 == 'Apple':
            slotthreer = st.selectbox(
                'Other rarity s3',
                ('None',))

# SLOT FOUR DOWN

        if slotfour == 'None':
            pass
        elif slotfour1 == 'Tactical Shotgun   ' or slotfour1 == 'Pump Shotgun': # [SPACE]
            slotfourr = st.selectbox(
                'Shotgun rarity s4',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Heavy Shotgun':
            slotfourr = st.selectbox(
                'Shotgun rarity s4',
                ('Epic', 'Legendary'))
        elif slotfour1 == 'Assault Rifle   ' or slotfour1 == 'Burst Assualt Rifle': # [SPACE]
            slotfourr = st.selectbox(
                'AR rarity s4',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Suppressed Assualt Rifle':
            slotfourr = st.selectbox(
                'AR rarity s4',
                ('Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Tactical Assualt Rifle':
            slotfourr = st.selectbox(
                'AR rarity s4',
                ('Legendary',))
        elif slotfour1 == 'Scoped Assualt Rifle':
            slotfourr = st.selectbox(
                'AR rarity s4',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Submachine Gun   ': # [SPACE]
            slotfourr = st.selectbox(
                'SMG rarity s4',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Suppressed Submachine Gun' or slotfour1 == 'Pistol':
            slotfourr = st.selectbox(
                'SMG Rarity s4',
                ('Common', 'Uncommon', 'Rare'))
        elif slotfour1 == 'Suppressed Pistol':
            slotfourr = st.selectbox(
                'SMG rarity s4',
                ('Rare', 'Epic'))
        elif slotfour1 == 'Hunting Rifle   ': # [SPACE]
            slotfourr = st.selectbox(
                'Snipers rarity s4',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Bolt-Action Sniper Rifle':
            slotfourr = st.selectbox(
                'Snipers rarity s4',
                ('Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Semi-Automatic Sniper Rifle':
            slotfourr = st.selectbox(
                'Snipers rarity s4',
                ('Uncommon', 'Rare'))
        elif slotfour1 == 'Rocket Launcher   ' or slotfour1 == 'Grenade Launcher': # [SPACE]
            slotfourr = st.selectbox(
                'Explosives rarity s4',
                ('Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Light Machine Gun   ': # [SPACE]
            slotfourr = st.selectbox(
                'Other rarity s4',
                ('Rare', 'Epic'))
        elif slotfour1 == 'Hand Cannon':
            slotfourr = st.selectbox(
                'Other rarity s4',
                ('Epic', 'Legendary'))
        elif slotfour1 == 'Chug Jug' or slotfour1 == 'Shield Potion' or slotfour1 == 'Small Shield Potion' or slotfour1 == 'Medkit' or slotfour1 == 'Mushroom' or slotfour1 == 'Corn' or slotfour1 == 'Coconut' or slotfour1 == 'Cabbage' or slotfour1 == 'Banana' or slotfour1 == 'Apple':
            slotfourr = st.selectbox(
                'Other rarity s4',
                ('None',))

# SLOT FIVE DOWN

        if slotfive == 'None':
            pass
        elif slotfive1 == 'Tactical Shotgun    ' or slotfive1 == 'Pump Shotgun': # [SPACE]
            slotfiver = st.selectbox(
                'Shotgun rarity s5',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Heavy Shotgun':
            slotfiver = st.selectbox(
                'Shotgun rarity s5',
                ('Epic', 'Legendary'))
        elif slotfive1 == 'Assault Rifle    ' or slotfive1 == 'Burst Assualt Rifle': # [SPACE]
            slotfiver = st.selectbox(
                'AR rarity s5',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Suppressed Assualt Rifle':
            slotfiver = st.selectbox(
                'AR rarity s5',
                ('Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Tactical Assualt Rifle':
            slotfiver = st.selectbox(
                'AR rarity s5',
                ('Legendary',))
        elif slotfive1 == 'Scoped Assualt Rifle':
            slotfiver = st.selectbox(
                'AR rarity s5',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Submachine Gun    ': # [SPACE]
            slotfiver = st.selectbox(
                'SMG rarity s5',
                ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Suppressed Submachine Gun' or slotfive1 == 'Pistol':
            slotfiver = st.selectbox(
                'SMG Rarity s5',
                ('Common', 'Uncommon', 'Rare'))
        elif slotfive1 == 'Suppressed Pistol':
            slotfiver = st.selectbox(
                'SMG rarity s5',
                ('Rare', 'Epic'))
        elif slotfive1 == 'Hunting Rifle    ': # [SPACE]
            slotfiver = st.selectbox(
                'Snipers rarity s5',
                ('Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Bolt-Action Sniper Rifle':
            slotfiver = st.selectbox(
                'Snipers rarity s5',
                ('Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Semi-Automatic Sniper Rifle':
            slotfiver = st.selectbox(
                'Snipers rarity s5',
                ('Uncommon', 'Rare'))
        elif slotfive1 == 'Rocket Launcher    ' or slotfive1 == 'Grenade Launcher': # [SPACE]
            slotfiver = st.selectbox(
                'Explosives rarity s5',
                ('Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Light Machine Gun    ': # [SPACE]
            slotfiver = st.selectbox(
                'Other rarity s5',
                ('Rare', 'Epic'))
        elif slotfive1 == 'Hand Cannon':
            slotfiver = st.selectbox(
                'Other rarity s5',
                ('Epic', 'Legendary'))
        elif slotfive1 == 'Chug Jug' or slotfive1 == 'Shield Potion' or slotfive1 == 'Small Shield Potion' or slotfive1 == 'Medkit' or slotfive1 == 'Mushroom' or slotfive1 == 'Corn' or slotfive1 == 'Coconut' or slotfive1 == 'Cabbage' or slotfive1 == 'Banana' or slotfive1 == 'Apple':
            slotfiver = st.selectbox(
                'Other rarity s5',
                ('None',))    

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
                t2.json({
                    'Custom loadout rarity': [
                        f'{slotone} : {slotoner}',
                        f'{slottwo} : {slottwor}',
                        f'{slotthree} : {slotthreer}',
                        f'{slotfour} : {slotfourr}',
                        f'{slotfive} : {slotfiver}'
                    ],
                })
        st.divider()

        def save():
            if os.path.exists(f"{File_Path}.txt"):
                os.remove(f"{File_Path}.txt")
                f = open(f"{File_Path}.txt", "a")           # here                             # here                                   # here                                # here
                f.write(f'{slotone}\n{slotone1}\n{slotoner}\n{slottwo}\n{slottwo1}\n{slottwor}\n{slotthree}\n{slotthree1}\n{slotthreer}\n{slotfour}\n{slotfour1}\n{slotfourr}\n{slotfive}\n{slotfive1}\n{slotfiver}')
                f.close()
            else:
                f = open(f"{File_Path}.txt", "a")           # here                             # here                                   # here                                # here
                f.write(f'{slotone}\n{slotone1}\n{slotoner}\n{slottwo}\n{slottwo1}\n{slottwor}\n{slotthree}\n{slotthree1}\n{slotthreer}\n{slotfour}\n{slotfour1}\n{slotfourr}\n{slotfive}\n{slotfive1}\n{slotfiver}')
                st.success(f'Saved config to file \'{File_Path}.txt\'', icon="✅")
                f.close()

        if st.button('Save Config'):
            if os.path.exists(f"{File_Path}.txt"):
                st.success(f'Saved config to file \'{File_Path}.txt\'', icon="✅")
            save()

        if st.button('Load Config'):
            if os.path.exists(f"{File_Path}.txt"):
                with open(f'{File_Path}.txt', "r") as file:
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

                    # These prints are just here if you want to get more info. Just remove the '#' from them and then check your CMD, they will show up there as well

                    # print("Loaded configuration with success:")
                    # print(f"Slot one : {slotone}, {slotoner}, {slotone1}\nSlot two : {slottwo}, {slottwor}, {slottwo1}\nSlot three : {slotthree}, {slotthreer}, {slotthree1}\nSlot four : {slotfour}, {slotfourr}, {slotfour1}\nSlot five : {slotfive}, {slotfiver}, {slotfive1}")

                    # RARITY

                    t.write(
                        f'# Custom loadout rarity\n    {slotone} : {slotoner}\n    {slottwo} : {slottwor}\n    {slotthree} : {slotthreer}\n    {slotfour} : {slotfourr}\n    {slotfive} : {slotfiver}')
                    t1.write(
                        f'# Custom loadout rarity  \n##### {slotone} : {slotoner}\n#####    {slottwo} : {slottwor}\n#####    {slotthree} : {slotthreer}\n#####    {slotfour} : {slotfourr}\n#####    {slotfive} : {slotfiver}')
                    t2.json({
                        'Custom loadout rarity': [
                            f'{slotone} : {slotoner}',
                            f'{slottwo} : {slottwor}',
                            f'{slotthree} : {slotthreer}',
                            f'{slotfour} : {slotfourr}',
                            f'{slotfive} : {slotfiver}'
                        ],
                    })

                    # WEAPONS

                    tt.write(
                        f'# Custom loadout\n    {slotone} : {slotone1}\n    {slottwo} : {slottwo1}\n    {slotthree} : {slotthree1}\n    {slotfour} : {slotfour1}\n    {slotfive} : {slotfive1}')
                    tt1.write(
                        f'# Custom loadout  \n##### {slotone} : {slotone1}\n#####    {slottwo} : {slottwo1}\n#####    {slotthree} : {slotthree1}\n#####    {slotfour} : {slotfour1}\n#####    {slotfive} : {slotfive1}')
                    tt2.json({
                        'Custom loadout': [
                            f'{slotone} : {slotone1}',
                            f'{slottwo} : {slottwo1}',
                            f'{slotthree} : {slotthree1}',
                            f'{slotfour} : {slotfour1}',
                            f'{slotfive} : {slotfive1}'
                        ],
                    })
                    st.success(f"Loaded configuration from \'{File_Path}.txt\'", icon="✅")
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
