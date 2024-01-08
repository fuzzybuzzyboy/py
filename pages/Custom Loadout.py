import streamlit as st, os, time, platform, requests
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

slotoneattachment1 = slotoneattachment2 = slotoneattachment3 = slotoneattachment4 = slottwoattachment1 = slottwoattachment2 = slottwoattachment3 = slottwoattachment4 = slotthreeattachment1 = slotthreeattachment2 = slotthreeattachment3 = slotthreeattachment4 = slotfourattachment1 = slotfourattachment2 = slotfourattachment3 = slotfourattachment4 = slotfiveattachment1 = slotfiveattachment2 = slotfiveattachment3 = slotfiveattachment4 = None
slotone1=slottwo1=slotthree1=slotfour1=slotfive1=None
slotoner=slottwor=slotthreer=slotfourr=slotfiver=None

def SlotOneAttachmentViewer(slot_name, weapon_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    global slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current weapon: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: slotoneattachment1 = st.selectbox('Optic', optic_options, help="**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy", index=None)
    with col3: slotoneattachment2 = st.selectbox('Magazine', magazine_options, help="**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed.", index=None)
    with col4: slotoneattachment3 = st.selectbox('Underbarrel', underbarrel_options, help="**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy", index=None)
    with col5: slotoneattachment4 = st.selectbox('Barrel', barrel_options, help="**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil.", index=None)
    st.divider()

def SlotTwoAttachmentViewer(slot_name, weapon_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    global slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current weapon: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: slottwoattachment1 = st.selectbox('Optic ', optic_options, help="**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy", index=None)
    with col3: slottwoattachment2 = st.selectbox('Magazine ', magazine_options, help="**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed.", index=None)
    with col4: slottwoattachment3 = st.selectbox('Underbarrel ', underbarrel_options, help="**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy", index=None)
    with col5: slottwoattachment4 = st.selectbox('Barrel ', barrel_options, help="**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil.", index=None)
    st.divider()

def SlotThreeAttachmentViewer(slot_name, weapon_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    global slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current weapon: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: slotthreeattachment1 = st.selectbox('Optic  ', optic_options, help="**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy", index=None)
    with col3: slotthreeattachment2 = st.selectbox('Magazine  ', magazine_options, help="**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed.", index=None)
    with col4: slotthreeattachment3 = st.selectbox('Underbarrel  ', underbarrel_options, help="**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy", index=None)
    with col5: slotthreeattachment4 = st.selectbox('Barrel  ', barrel_options, help="**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil.", index=None)
    st.divider()

def SlotFourAttachmentViewer(slot_name, weapon_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    global slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current weapon: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: slotfourattachment1 = st.selectbox('Optic   ', optic_options, help="**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy", index=None)
    with col3: slotfourattachment2 = st.selectbox('Magazine   ', magazine_options, help="**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed.", index=None)
    with col4: slotfourattachment3 = st.selectbox('Underbarrel   ', underbarrel_options, help="**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy", index=None)
    with col5: slotfourattachment4 = st.selectbox('Barrel   ', barrel_options, help="**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil.", index=None)
    st.divider()

def SlotFiveAttachmentViewer(slot_name, weapon_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    global slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current weapon: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: slotfiveattachment1 = st.selectbox('Optic    ', optic_options, help="**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy", index=None)
    with col3: slotfiveattachment2 = st.selectbox('Magazine    ', magazine_options, help="**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed.", index=None)
    with col4: slotfiveattachment3 = st.selectbox('Underbarrel    ', underbarrel_options, help="**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy", index=None)
    with col5: slotfiveattachment4 = st.selectbox('Barrel    ', barrel_options, help="**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil.", index=None)
    st.divider()

hammer_pump_options = (('Red Eye Sight', 'Holo-13 Optic'), ('Speed Mag',), ('Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('Suppressor', 'Muzzle Brake'))
frenzy_auto_options = (('Red Eye Sight', 'Holo-13 Optic'), ('Speed Mag', 'Drum Mag'), ('Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('Suppressor', 'Muzzle Brake'))
assault_rifle_options = (('Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('Speed Mag', 'Drum Mag'), ('Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('Suppressor', 'Muzzle Brake'))
thunder_burst_options = (('Red Eye Sight', 'Holo-13 Optic', 'P2X Optic'), ('Speed Mag', 'Drum Mag'), ('Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('Suppressor', 'Muzzle Brake'))
hyper_smg_options = thunder_burst_options
ranger_pistol_options = (('Red Eye Sight', 'Holo-13 Optic'), ('Speed Mag', 'Drum Mag'), ('Laser'), ('Suppressor', 'Muzzle Brake'))
reaper_sniper_options = (('Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('Speed Mag', 'Drum Mag'), ('Vertical Foregrip', 'Angled Foregrip'), ('Suppressor', 'Muzzle Brake'))

selected_medallions = 'None'
login = platform.node()
Folder_Path = "configs"
File_Path = os.path.join(Folder_Path, login)

tab1, tab2, tab3 = st.tabs(["Customize", 'Weapon Mods', "Loadout"])
with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        slotone = st.selectbox('Slot 1', ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Snipers', 'Explosives', 'Other'))
        slottwo = st.selectbox('Slot 2', ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Snipers', 'Explosives', 'Other'))
        slotthree = st.selectbox('Slot 3', ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Snipers', 'Explosives', 'Other'))
        slotfour = st.selectbox('Slot 4', ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Snipers', 'Explosives', 'Other'))
        slotfive = st.selectbox('Slot 5', ('None', 'Shotgun', 'SMG', 'Assault-Rifle', 'Snipers', 'Explosives', 'Other'))
        slotsix = st.multiselect('Medallions', ('Valeria\'s Medallion', 'Montague\'s Medallion', 'Nisha\'s Medallion', 'Oscar\'s Medallion', 'Peter Griffin\'s Medallion'), placeholder="Choose a medallion(s).")
    with col2:
        if slotone == 'Shotgun': slotone1 = st.selectbox('Slot 1', ('Hammer Pump Shotgun', 'Peter Griffin\'s Hammer Pump Shotgun', 'Frenzy Auto Shotgun', 'Oscar\'s Frenzy Auto Shotgun'))
        elif slotone == 'SMG': slotone1 = st.selectbox('SMG Slot 1', ('Thunder Burst SMG', 'Hyper SMG', 'Valeria\'s Hyper SMG', 'Ranger Pistol'))
        elif slotone == 'Assault-Rifle': slotone1 = st.selectbox('Assault-Rifle Slot 1', ('Striker AR', 'Nisha\'s Striker AR', 'Nemesis AR', 'Montague\'s Enforcer AR'))
        elif slotone == 'Snipers': slotone1 = st.selectbox('Snipers Slot 1',  ('Reaper Sniper Rifle',))
        elif slotone == 'Explosives': slotone1 = st.selectbox('Explosives Slot 1', ('Snowball Launcher',))
        elif slotone == 'Other': slotone1 = st.selectbox('Other Slot 1', ('Grapple Blade', 'Grappler', 'Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit'))
        
        
        if slottwo == 'Shotgun': slottwo1 = st.selectbox('Slot 2', ('Hammer Pump Shotgun ', 'Peter Griffin\'s Hammer Pump Shotgun', 'Frenzy Auto Shotgun', 'Oscar\'s Frenzy Auto Shotgun'))
        elif slottwo == 'SMG': slottwo1 = st.selectbox('Slot 2', ('Thunder Burst SMG ', 'Hyper SMG', 'Valeria\'s Hyper SMG', 'Ranger Pistol'))
        elif slottwo == 'Assault-Rifle': slottwo1 = st.selectbox('Slot 2', ('Striker AR ', 'Nisha\'s Striker AR', 'Nemesis AR', 'Montague\'s Enforcer AR'))
        elif slottwo == 'Snipers': slottwo1 = st.selectbox('Slot 2', ('Reaper Sniper Rifle ',))
        elif slottwo == 'Explosives': slottwo1 = st.selectbox('Slot 2', ('Snowball Launcher ',))
        elif slottwo == 'Other': slottwo1 = st.selectbox('Slot 2', ('Grapple Blade ', 'Grappler', 'Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit'))
        
        
        if slotthree == 'Shotgun': slotthree1 = st.selectbox('Slot 3', ('Hammer Pump Shotgun  ', 'Peter Griffin\'s Hammer Pump Shotgun', 'Frenzy Auto Shotgun', 'Oscar\'s Frenzy Auto Shotgun'))
        elif slotthree == 'SMG': slotthree1 = st.selectbox('Slot 3', ('Thunder Burst SMG  ', 'Hyper SMG', 'Valeria\'s Hyper SMG', 'Ranger Pistol'))
        elif slotthree == 'Assault-Rifle': slotthree1 = st.selectbox('Slot 3', ('Striker AR  ', 'Nisha\'s Striker AR', 'Nemesis AR', 'Montague\'s Enforcer AR'))
        elif slotthree == 'Snipers': slotthree1 = st.selectbox('Slot 3', ('Reaper Sniper Rifle  ',))
        elif slotthree == 'Explosives': slotthree1 = st.selectbox('Slot 3', ('Snowball Launcher',))
        elif slotthree == 'Other': slotthree1 = st.selectbox('Slot 3', ('Grapple Blade  ', 'Grappler', 'Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit'))


        if slotfour == 'Shotgun': slotfour1 = st.selectbox('Slot 4', ('Hammer Pump Shotgun   ', 'Peter Griffin\'s Hammer Pump Shotgun', 'Frenzy Auto Shotgun', 'Oscar\'s Frenzy Auto Shotgun'))
        elif slotfour == 'SMG': slotfour1 = st.selectbox('Slot 4', ('Thunder Burst SMG   ', 'Hyper SMG', 'Valeria\'s Hyper SMG', 'Ranger Pistol'))
        elif slotfour == 'Assault-Rifle': slotfour1 = st.selectbox( 'Slot 4', ('Striker AR   ', 'Nisha\'s Striker AR', 'Nemesis AR', 'Montague\'s Enforcer AR'))
        elif slotfour == 'Snipers':slotfour1 = st.selectbox('Slot 4', ('Reaper Sniper Rifle   ',))
        elif slotfour == 'Explosives': slotfour1 = st.selectbox('Slot 4', ('Snowball Launcher',))
        elif slotfour == 'Other': slotfour1 = st.selectbox('Slot 4', ('Grapple Blade   ', 'Grappler', 'Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit'))     
        

        if slotfive == 'Shotgun': slotfive1 = st.selectbox('Slot 5', ('Hammer Pump Shotgun    ', 'Peter Griffin\'s Hammer Pump Shotgun', 'Frenzy Auto Shotgun', 'Oscar\'s Frenzy Auto Shotgun'))
        elif slotfive == 'SMG': slotfive1 = st.selectbox('Slot 5', ('Thunder Burst SMG    ', 'Hyper SMG', 'Valeria\'s Hyper SMG', 'Ranger Pistol'))
        elif slotfive == 'Assault-Rifle': slotfive1 = st.selectbox('Slot 5', ('Striker AR    ', 'Nisha\'s Striker AR', 'Nemesis AR', 'Montague\'s Enforcer AR'))
        elif slotfive == 'Snipers': slotfive1 = st.selectbox('Slot 5', ('Reaper Sniper Rifle    ',))
        elif slotfive == 'Explosives': slotfive1 = st.selectbox('Slot 5', ('Snowball Launcher',))
        elif slotfive == 'Other': slotfive1 = st.selectbox('Slot 5', ('Grapple Blade    ', 'Grappler', 'Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit'))
    
    
    
    with col3:
        if slotone == 'None': pass 
        elif slotone1 == 'Hammer Pump Shotgun' or slotone1=='Frenzy Auto Shotgun': slotoner = st.selectbox('Slot 1', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Peter Griffin\'s Hammer Pump Shotgun' or slotone1=='Oscar\'s Frenzy Auto Shotgun' or slotone1=='Montague\'s Enforcer AR' or slotone1=='Nisha\'s Striker AR' or slotone1=='Valeria\'s Hyper SMG': slotoner = st.selectbox('Slot 1', ('Mythic',))
        elif slotone1 == 'Striker AR' or slotone1 == 'Nemesis AR' or slotone1 == 'Enforcer AR': slotoner = st.selectbox('Slot 1', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Thunder Burst SMG' or slotone1 == 'Ranger Pistol' or slotone1 == 'Hyper SMG': slotoner = st.selectbox('Slot 1', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Reaper Sniper Rifle': slotoner = st.selectbox('Slot 1', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotone1 == 'Grapple Blade' or slotone1 == 'Grappler' or slotone1 == 'Flowberry Fizz' or slotone1 == 'Flowberry' or slotone1 == 'Shield Potion' or slotone1 == 'Small Shield Potion' or slotone1 == 'Medkit':slotoner = st.selectbox('Slot 1', ('None',))         

        if slottwo == 'None': pass 
        elif slottwo1 == 'Hammer Pump Shotgun ' or slottwo1=='Frenzy Auto Shotgun': slottwor = st.selectbox('Slot 2', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Peter Griffin\'s Hammer Pump Shotgun' or slottwo1=='Oscar\'s Frenzy Auto Shotgun' or slottwo1=='Montague\'s Enforcer AR' or slottwo1=='Nisha\'s Striker AR' or slottwo1=='Valeria\'s Hyper SMG': slottwor = st.selectbox('Slot 2', ('Mythic',))
        elif slottwo1 == 'Striker AR ' or slottwo1 == 'Nemesis AR' or slottwo1 == 'Enforcer AR': slottwor = st.selectbox('Slot 2', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Thunder Burst SMG ' or slottwo1 == 'Ranger Pistol' or slottwo1 == 'Hyper SMG': slottwor = st.selectbox('Slot 2', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Reaper Sniper Rifle ': slottwor = st.selectbox('Slot 2', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slottwo1 == 'Grapple Blade ' or slottwo1 == 'Grappler' or slottwo1 == 'Flowberry Fizz' or slottwo1 == 'Flowberry' or slottwo1 == 'Shield Potion' or slottwo1 == 'Small Shield Potion' or slottwo1 == 'Medkit':slottwor = st.selectbox('Slot 2', ('None',))         

        if slotthree == 'None': pass 
        elif slotthree1 == 'Hammer Pump Shotgun  ' or slotthree1=='Frenzy Auto Shotgun': slotthreer = st.selectbox('Slot 3', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Peter Griffin\'s Hammer Pump Shotgun' or slotthree1=='Oscar\'s Frenzy Auto Shotgun' or slotthree1=='Montague\'s Enforcer AR' or slotthree1=='Nisha\'s Striker AR' or slotthree1=='Valeria\'s Hyper SMG': slotthreer = st.selectbox('Slot 3', ('Mythic',))
        elif slotthree1 == 'Striker AR  ' or slotthree1 == 'Nemesis AR' or slotthree1 == 'Enforcer AR': slotthreer = st.selectbox('Slot 3', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Thunder Burst SMG  ' or slotthree1 == 'Ranger Pistol' or slotthree1 == 'Hyper SMG': slotthreer = st.selectbox('Slot 3', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Reaper Sniper Rifle  ': slotthreer = st.selectbox('Slot 3', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotthree1 == 'Grapple Blade  ' or slotthree1 == 'Grappler' or slotthree1 == 'Flowberry Fizz' or slotthree1 == 'Flowberry' or slotthree1 == 'Shield Potion' or slotthree1 == 'Small Shield Potion' or slotthree1 == 'Medkit':slotthreer = st.selectbox('Slot 3', ('None',))         

        if slotfour == 'None': pass 
        elif slotfour1 == 'Hammer Pump Shotgun   ' or slotfour1=='Frenzy Auto Shotgun': slotfourr = st.selectbox('Slot 4', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Peter Griffin\'s Hammer Pump Shotgun' or slotfour1=='Oscar\'s Frenzy Auto Shotgun' or slotfour1=='Montague\'s Enforcer AR' or slotfour1=='Nisha\'s Striker AR' or slotfour1=='Valeria\'s Hyper SMG': slotfourr = st.selectbox('Slot 4', ('Mythic',))
        elif slotfour1 == 'Striker AR   ' or slotfour1 == 'Nemesis AR' or slotfour1 == 'Enforcer AR': slotfourr = st.selectbox('Slot 4', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Thunder Burst SMG   ' or slotfour1 == 'Ranger Pistol' or slotfour1 == 'Hyper SMG': slotfourr = st.selectbox('Slot 4', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Reaper Sniper Rifle   ': slotfourr = st.selectbox('Slot 4', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfour1 == 'Grapple Blade   ' or slotfour1 == 'Grappler' or slotfour1 == 'Flowberry Fizz' or slotfour1 == 'Flowberry' or slotfour1 == 'Shield Potion' or slotfour1 == 'Small Shield Potion' or slotfour1 == 'Medkit':slotfourr = st.selectbox('Slot 4', ('None',))         

        if slottwo == 'None': pass 
        elif slotfive1 == 'Hammer Pump Shotgun    ' or slottwo1=='Frenzy Auto Shotgun': slotfiver = st.selectbox('Slot 5', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Peter Griffin\'s Hammer Pump Shotgun' or slotfive1=='Oscar\'s Frenzy Auto Shotgun' or slotfive1=='Montague\'s Enforcer AR' or slotfive1=='Nisha\'s Striker AR' or slotfive1=='Valeria\'s Hyper SMG': slotfiver = st.selectbox('Slot 5', ('Mythic',))
        elif slotfive1 == 'Striker AR    ' or slotfive1 == 'Nemesis AR' or slotfive1 == 'Enforcer AR': slotfiver = st.selectbox('Slot 5', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Thunder Burst SMG    ' or slotfive1 == 'Ranger Pistol' or slotfive1 == 'Hyper SMG': slotfiver = st.selectbox('Slot 5', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Reaper Sniper Rifle    ': slotfiver = st.selectbox('Slot 5', ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'))
        elif slotfive1 == 'Grapple Blade    ' or slotfive1 == 'Grappler' or slotfive1 == 'Flowberry Fizz' or slotfive1 == 'Flowberry' or slotfive1 == 'Shield Potion' or slotfive1 == 'Small Shield Potion' or slotfive1 == 'Medkit':slotfiver = st.selectbox('Slot 5', ('None',))         

with tab2:
    if slotone1 and slotone!='Other' and slotoner!='Mythic':
        if slotone1 == 'Hammer Pump Shotgun': SlotOneAttachmentViewer('Slot 1', slotone1, *hammer_pump_options)
        elif slotone1 == 'Frenzy Auto Shotgun': SlotOneAttachmentViewer('Slot 1', slotone1, *frenzy_auto_options)
        elif slotone1 in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): SlotOneAttachmentViewer('Slot 1', slotone1, *assault_rifle_options)
        elif slotone1 in ('Thunder Burst SMG', 'Hyper SMG'): SlotOneAttachmentViewer('Slot 1', slotone1, *thunder_burst_options)
        elif slotone1 == 'Ranger Pistol': SlotOneAttachmentViewer('Slot 1', slotone1, *ranger_pistol_options)
        elif slotone1 == 'Reaper Sniper Rifle': SlotOneAttachmentViewer('Slot 1', slotone1, *reaper_sniper_options)

    if slottwo1 and slottwo!='Other' and slottwor!='Mythic':
        if slottwo1 == 'Hammer Pump Shotgun ': SlotTwoAttachmentViewer('Slot 2', slottwo1, *hammer_pump_options)
        elif slottwo1 == 'Frenzy Auto Shotgun': SlotTwoAttachmentViewer('Slot 2', slottwo1, *frenzy_auto_options)
        elif slottwo1 in ('Striker AR ', 'Nemesis AR', 'Enforcer AR'): SlotTwoAttachmentViewer('Slot 2', slottwo1, *assault_rifle_options)
        elif slottwo1 in ('Thunder Burst SMG ', 'Hyper SMG'): SlotTwoAttachmentViewer('Slot 2', slottwo1, *thunder_burst_options)
        elif slottwo1 == 'Ranger Pistol': SlotTwoAttachmentViewer('Slot 2', slottwo1, *ranger_pistol_options)
        elif slottwo1 == 'Reaper Sniper Rifle ': SlotTwoAttachmentViewer('Slot 2', slottwo1, *reaper_sniper_options)
    if slotthree1 and slotthree!='Other' and slotthreer!='Mythic':
        if slotthree1 == 'Hammer Pump Shotgun  ': SlotThreeAttachmentViewer('Slot 3', slotthree1, *hammer_pump_options)
        elif slotthree1 == 'Frenzy Auto Shotgun': SlotThreeAttachmentViewer('Slot 3', slotthree1, *frenzy_auto_options)
        elif slotthree1 in ('Striker AR  ', 'Nemesis AR', 'Enforcer AR'): SlotThreeAttachmentViewer('Slot 3', slotthree1, *assault_rifle_options)
        elif slotthree1 in ('Thunder Burst SMG  ', 'Hyper SMG', 'Ranger Pistol'): SlotThreeAttachmentViewer('Slot 3', slotthree1, *thunder_burst_options)
        elif slotthree1 == 'Reaper Sniper Rifle  ': SlotThreeAttachmentViewer('Slot 3', slotthree1, *reaper_sniper_options)
    if slotfour1 and slotfour!='Other' and slotfourr!='Mythic':
        if slotfour1 == 'Hammer Pump Shotgun   ': SlotFourAttachmentViewer('Slot 4', slotfour1, *hammer_pump_options)
        elif slotfour1 == 'Frenzy Auto Shotgun': SlotFourAttachmentViewer('Slot 4', slotfour1, *frenzy_auto_options)
        elif slotfour1 in ('Striker AR   ', 'Nemesis AR', 'Enforcer AR'): SlotFourAttachmentViewer('Slot 4', slotfour1, *assault_rifle_options)
        elif slotfour1 in ('Thunder Burst SMG   ', 'Hyper SMG', 'Ranger Pistol'): SlotFourAttachmentViewer('Slot 4', slotfour1, *thunder_burst_options)
        elif slotfour1 == 'Reaper Sniper Rifle   ': SlotFourAttachmentViewer('Slot 4', slotfour1, *reaper_sniper_options)
    if slotfive1 and slotfive!='Other' and slotfiver!='Mythic':
        if slotfive1 == 'Hammer Pump Shotgun    ': SlotFiveAttachmentViewer('Slot 5', slotfive1, *hammer_pump_options)
        elif slotfive1 == 'Frenzy Auto Shotgun': SlotFiveAttachmentViewer('Slot 5', slotfive1, *frenzy_auto_options)
        elif slotfive1 in ('Striker AR    ', 'Nemesis AR', 'Enforcer AR'): SlotFiveAttachmentViewer('Slot 5', slotfive1, *assault_rifle_options)
        elif slotfive1 in ('Thunder Burst SMG    ', 'Hyper SMG', 'Ranger Pistol'): SlotFiveAttachmentViewer('Slot 5', slotfive1, *thunder_burst_options)
        elif slotfive1 == 'Reaper Sniper Rifle    ': SlotFiveAttachmentViewer('Slot 5', slotfive1, *reaper_sniper_options)
    #if slotone1=='Peter Griffin\'s Hammer Pump Shotgun' or slotone1=='Peter Griffin\'s Hammer Pump Shotgun 'or slotone1=='Peter Griffin\'s Hammer Pump Shotgun  'or slotone1=='Peter Griffin\'s Hammer Pump Shotgun   'or slotone1=='Peter Griffin\'s Hammer Pump Shotgun    ':slotoneattachment1 = slotoneattachment2 = slotoneattachment3 = slotoneattachment4 = None
with tab3:
    if slotsix:
        selected_medallions = ', '.join(slotsix)
    if slotone == 'None' or slottwo == 'None' or slotthree == 'None' or slotfour == 'None' or slotfive == 'None':
        st.error('Create/complete your loadout before checking this tab.')
    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])

            with taba1:
                tt = st.empty()
                tt.write(
                    f'# Custom loadout\n    {slotone} : {slotone1}\n    {slottwo} : {slottwo1}\n    {slotthree} : {slotthree1}\n    {slotfour} : {slotfour1}\n    {slotfive} : {slotfive1}\n    Medallion(s): {selected_medallions}')
            with taba2:
                tt1 = st.empty()
                tt1.write(
                    f'# Custom loadout  \n##### {slotone} : {slotone1}\n#####    {slottwo} : {slottwo1}\n#####    {slotthree} : {slotthree1}\n#####    {slotfour} : {slotfour1}\n#####    {slotfive} : {slotfive1}\n#####    Medallion(s): {selected_medallions}')

            with taba3:
                tt2 = st.empty()
                tt2.json({
                    'Custom loadout': [
                        f'{slotone} : {slotone1}',
                        f'{slottwo} : {slottwo1}',
                        f'{slotthree} : {slotthree1}',
                        f'{slotfour} : {slotfour1}',
                        f'{slotfive} : {slotfive1}',
                        f'Medallion(s) : {selected_medallions}'
                    ],
                })
        with col2:
            taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])

            with taba1:
                t = st.empty()
                t.write(f'# loadout rarity\n    {slotone} : {slotoner}\n    {slottwo} : {slottwor}\n    {slotthree} : {slotthreer}\n    {slotfour} : {slotfourr}\n    {slotfive} : {slotfiver}')

            with taba2:
                t1 = st.empty()
                t1.write(f'# loadout rarity  \n##### {slotone} : {slotoner}\n#####    {slottwo} : {slottwor}\n#####    {slotthree} : {slotthreer}\n#####    {slotfour} : {slotfourr}\n#####    {slotfive} : {slotfiver}')

            with taba3:
                t2 = st.empty()
                t2.json({'loadout rarity': [f'{slotone} : {slotoner}', f'{slottwo} : {slottwor}', f'{slotthree} : {slotthreer}', f'{slotfour} : {slotfourr}', f'{slotfive} : {slotfiver}'],})
        with col3:
            tabb1, tabb2, tabb3 = st.tabs(['Base', 'Regular', 'Json'])
            with tabb1:
                ttt = st.empty()
                ttt.write(
                    f'# loadout Mod\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')

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
                        f'# Custom loadout\n    {slotone} : {slotone1}\n    {slottwo} : {slottwo1}\n    {slotthree} : {slotthree1}\n    {slotfour} : {slotfour1}\n    {slotfive} : {slotfive1}\n    Medallion(s): {selected_medallions}')
                    tt1.write(
                        f'# Custom loadout  \n##### {slotone} : {slotone1}\n#####    {slottwo} : {slottwo1}\n#####    {slotthree} : {slotthree1}\n#####    {slotfour} : {slotfour1}\n#####    {slotfive} : {slotfive1}\n#####    Medallion(s): {selected_medallions}')
                    tt2.json({
                        'Custom loadout': [
                            f'{slotone} : {slotone1}',
                            f'{slottwo} : {slottwo1}',
                            f'{slotthree} : {slotthree1}',
                            f'{slotfour} : {slotfour1}',
                            f'{slotfive} : {slotfive1}',
                            f'Medallion(s): {selected_medallions}'
                        ],
                    })
                    st.success(f"Loaded configuration from \'{File_Path}.txt\'", icon="✅")
                else:
                    st.error("Invalid configuration file. Expected 15 lines.")
            else:
                st.error("File doesn't exist. Please create/save a configuration.")
        if st.button('Send saved config to webhook'):
            if os.path.exists(f"{File_Path}.txt"):
                with open(f'{File_Path}.txt', "r") as file:
                    lines = [line.strip() for line in file.readlines()]

                if len(lines) == 15:
                    pass
                else:
                    st.error("Invalid configuration file. Expected 15 lines.")
            else:
                st.error("File doesn't exist. Please create/save a configuration.")
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
                    st.write(
                        f'# Clock\n    Current time : {time_now}\n    Date : {time_now1}\n##### Reminder, the clock will vanish when creating a new load-out. The clock button will show up.')
                    time_later = datetime.now().strftime("%S")
                    t += 1
                    time.sleep(1)
