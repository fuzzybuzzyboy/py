import streamlit as st, os, time, platform
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
slotone=slottwo=slotthree=slotfour=slotfive=None
slotone1=slottwo1=slotthree1=slotfour1=slotfive1=None
slotoner=slottwor=slotthreer=slotfourr=slotfiver=None
rarity_options = {'Shotgun': ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'), 'SMG': ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'), 'Assault-Rifle': ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'), 'Sniper': ('Uncommon', 'Rare', 'Epic', 'Legendary'), 'Other': ('None',)}
weapon_options = {'Shotgun': ('Hammer Pump Shotgun', 'Peter Griffin\'s Hammer Pump Shotgun', 'Frenzy Auto Shotgun', 'Oscar\'s Frenzy Auto Shotgun'), 'SMG': ('Thunder Burst SMG', 'Hyper SMG', 'Valeria\'s Hyper SMG', 'Ranger Pistol'), 'Assault-Rifle': ('Striker AR', 'Nisha\'s Striker AR', 'Nemesis AR', 'Montague\'s Enforcer AR'), 'Sniper': ('Reaper Sniper Rifle',), 'Other': ('Grapple Blade', 'Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit')}

def Weapon_Slotone(slot_name):
    global slotone, slotone1, slotoner
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slotone = st.selectbox('Weapon Type', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other'), help=f'Weapon type for {slot_name}') 
    with col3: slotone1 = st.selectbox('Weapon', weapon_options.get(slotone, ()), help=f'Weapon selection for {slot_name}')
    with col4: 
        if slotone1 in ('Peter Griffin\'s Hammer Pump Shotgun', 'Oscar\'s Frenzy Auto Shotgun', 'Valeria\'s Hyper SMG', 'Nisha\'s Striker AR', 'Montague\'s Enforcer AR'): slotoner = st.selectbox('Rarity', ('Mythic',), help=f'Weapon rarity for {slot_name}')
        else: slotoner = st.selectbox('Rarity', rarity_options.get(slotone, ()), help=f'Weapon rarity for {slot_name}')
    st.divider()

def Weapon_Slottwo(slot_name):
    global slottwo, slottwo1, slottwor
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slottwo = st.selectbox('Weapon Type', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other'), help=f'Weapon type for {slot_name}') 
    with col3: slottwo1 = st.selectbox('Weapon', weapon_options.get(slottwo, ()), help=f'Weapon selection for {slot_name}')
    with col4: 
        if slottwo1 in ('Peter Griffin\'s Hammer Pump Shotgun', 'Oscar\'s Frenzy Auto Shotgun', 'Valeria\'s Hyper SMG', 'Nisha\'s Striker AR', 'Montague\'s Enforcer AR'): slottwor = st.selectbox('Rarity', ('Mythic',), help=f'Weapon rarity for {slot_name}')
        else: slottwor = st.selectbox('Rarity', rarity_options.get(slottwo, ()), help=f'Weapon rarity for {slot_name}')
    st.divider()

def Weapon_Slotthree(slot_name):
    global slotthree, slotthree1, slotthreer
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slotthree = st.selectbox('Weapon Type', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other'), help=f'Weapon type for {slot_name}') 
    with col3: slotthree1 = st.selectbox('Weapon', weapon_options.get(slotthree, ()), help=f'Weapon selection for {slot_name}')
    with col4: 
        if slotthree1 in ('Peter Griffin\'s Hammer Pump Shotgun', 'Oscar\'s Frenzy Auto Shotgun', 'Valeria\'s Hyper SMG', 'Nisha\'s Striker AR', 'Montague\'s Enforcer AR'): slotthreer = st.selectbox('Rarity', ('Mythic',), help=f'Weapon rarity for {slot_name}')
        else: slotthreer = st.selectbox('Rarity', rarity_options.get(slotthree, ()), help=f'Weapon rarity for {slot_name}')
    st.divider()

def Weapon_Slotfour(slot_name):
    global slotfour, slotfour1, slotfourr
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slotfour = st.selectbox('Weapon Type', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other'), help=f'Weapon type for {slot_name}') 
    with col3: slotfour1 = st.selectbox('Weapon', weapon_options.get(slotfour, ()), help=f'Weapon selection for {slot_name}')
    with col4: 
        if slotfour1 in ('Peter Griffin\'s Hammer Pump Shotgun', 'Oscar\'s Frenzy Auto Shotgun', 'Valeria\'s Hyper SMG', 'Nisha\'s Striker AR', 'Montague\'s Enforcer AR'): slotfourr = st.selectbox('Rarity', ('Mythic',), help=f'Weapon rarity for {slot_name}')
        else: slotfourr = st.selectbox('Rarity', rarity_options.get(slotfour, ()), help=f'Weapon rarity for {slot_name}')
    st.divider()

def Weapon_Slotfive(slot_name):
    global slotfive, slotfive1, slotfiver
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slotfive = st.selectbox('Weapon Type', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other'), help=f'Weapon type for {slot_name}') 
    with col3: slotfive1 = st.selectbox('Weapon', weapon_options.get(slotfive, ()), help=f'Weapon selection for {slot_name}')
    with col4:
        if slotfive1 in ('Peter Griffin\'s Hammer Pump Shotgun', 'Oscar\'s Frenzy Auto Shotgun', 'Valeria\'s Hyper SMG', 'Nisha\'s Striker AR', 'Montague\'s Enforcer AR'): slotfiver = st.selectbox('Rarity', ('Mythic',), help=f'Weapon rarity for {slot_name}')
        else: slotfiver = st.selectbox('Rarity', rarity_options.get(slotfive, ()), help=f'Weapon rarity for {slot_name}')
    st.divider()

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
ranger_pistol_options = (('Red Eye Sight', 'Holo-13 Optic'), ('Speed Mag', 'Drum Mag'), ('Laser'), ('Suppressor', 'Muzzle Brake'))
reaper_sniper_options = (('Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('Speed Mag', 'Drum Mag'), ('Vertical Foregrip', 'Angled Foregrip'), ('Suppressor', 'Muzzle Brake'))

selected_medallions = 'None'
login = platform.node()
Folder_Path = "configs"
File_Path = os.path.join(Folder_Path, login)

tab1, tab2, tab3 = st.tabs(["Customize", 'Weapon Mods', "Loadout"])
with tab1:
    Weapon_Slotone("Slot 1")
    Weapon_Slottwo("Slot 2")
    Weapon_Slotthree("Slot 3")
    Weapon_Slotfour("Slot 4")
    Weapon_Slotfive("Slot 5")
    slotsix = st.multiselect('Medallions', ('Valeria\'s Medallion', 'Montague\'s Medallion', 'Nisha\'s Medallion', 'Oscar\'s Medallion', 'Peter Griffin\'s Medallion'), placeholder="Choose a medallion(s).")

with tab2:
    if slotone1 and slotone!='Other' and slotoner!='Mythic':
        if slotone1 == 'Hammer Pump Shotgun': SlotOneAttachmentViewer('Slot 1', slotone1, *hammer_pump_options)
        elif slotone1 == 'Frenzy Auto Shotgun': SlotOneAttachmentViewer('Slot 1', slotone1, *frenzy_auto_options)
        elif slotone1 in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): SlotOneAttachmentViewer('Slot 1', slotone1, *assault_rifle_options)
        elif slotone1 in ('Thunder Burst SMG', 'Hyper SMG'): SlotOneAttachmentViewer('Slot 1', slotone1, *thunder_burst_options)
        elif slotone1 == 'Ranger Pistol': SlotOneAttachmentViewer('Slot 1', slotone1, *ranger_pistol_options)
        elif slotone1 == 'Reaper Sniper Rifle': SlotOneAttachmentViewer('Slot 1', slotone1, *reaper_sniper_options)
    if slottwo1 and slottwo!='Other' and slottwor!='Mythic':
        if slottwo1 == 'Hammer Pump Shotgun': SlotTwoAttachmentViewer('Slot 2', slottwo1, *hammer_pump_options)
        elif slottwo1 == 'Frenzy Auto Shotgun': SlotTwoAttachmentViewer('Slot 2', slottwo1, *frenzy_auto_options)
        elif slottwo1 in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): SlotTwoAttachmentViewer('Slot 2', slottwo1, *assault_rifle_options)
        elif slottwo1 in ('Thunder Burst SMG', 'Hyper SMG'): SlotTwoAttachmentViewer('Slot 2', slottwo1, *thunder_burst_options)
        elif slottwo1 == 'Ranger Pistol': SlotTwoAttachmentViewer('Slot 2', slottwo1, *ranger_pistol_options)
        elif slottwo1 == 'Reaper Sniper Rifle': SlotTwoAttachmentViewer('Slot 2', slottwo1, *reaper_sniper_options)
    if slotthree1 and slotthree!='Other' and slotthreer!='Mythic':
        if slotthree1 == 'Hammer Pump Shotgun': SlotThreeAttachmentViewer('Slot 3', slotthree1, *hammer_pump_options)
        elif slotthree1 == 'Frenzy Auto Shotgun': SlotThreeAttachmentViewer('Slot 3', slotthree1, *frenzy_auto_options)
        elif slotthree1 in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): SlotThreeAttachmentViewer('Slot 3', slotthree1, *assault_rifle_options)
        elif slotthree1 in ('Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol'): SlotThreeAttachmentViewer('Slot 3', slotthree1, *thunder_burst_options)
        elif slotthree1 == 'Reaper Sniper Rifle': SlotThreeAttachmentViewer('Slot 3', slotthree1, *reaper_sniper_options)
    if slotfour1 and slotfour!='Other' and slotfourr!='Mythic':
        if slotfour1 == 'Hammer Pump Shotgun': SlotFourAttachmentViewer('Slot 4', slotfour1, *hammer_pump_options)
        elif slotfour1 == 'Frenzy Auto Shotgun': SlotFourAttachmentViewer('Slot 4', slotfour1, *frenzy_auto_options)
        elif slotfour1 in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): SlotFourAttachmentViewer('Slot 4', slotfour1, *assault_rifle_options)
        elif slotfour1 in ('Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol'): SlotFourAttachmentViewer('Slot 4', slotfour1, *thunder_burst_options)
        elif slotfour1 == 'Reaper Sniper Rifle': SlotFourAttachmentViewer('Slot 4', slotfour1, *reaper_sniper_options)
    if slotfive1 and slotfive!='Other' and slotfiver!='Mythic':
        if slotfive1 == 'Hammer Pump Shotgun': SlotFiveAttachmentViewer('Slot 5', slotfive1, *hammer_pump_options)
        elif slotfive1 == 'Frenzy Auto Shotgun': SlotFiveAttachmentViewer('Slot 5', slotfive1, *frenzy_auto_options)
        elif slotfive1 in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): SlotFiveAttachmentViewer('Slot 5', slotfive1, *assault_rifle_options)
        elif slotfive1 in ('Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol'): SlotFiveAttachmentViewer('Slot 5', slotfive1, *thunder_burst_options)
        elif slotfive1 == 'Reaper Sniper Rifle': SlotFiveAttachmentViewer('Slot 5', slotfive1, *reaper_sniper_options)
with tab3:
    if slotsix:
        selected_medallions = ', '.join(slotsix)
    col1, col2, col3 = st.columns(3)
    with col1:
        taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])

        with taba1:
            t = st.empty()
            t.write(f'# Weapons\n    Slot 1 : {slotone1}\n    Slot 2 : {slottwo1}\n    Slot 3 : {slotthree1}\n    Slot 4 : {slotfour1}\n    Slot 5 : {slotfive1}\n    Medallion(s): {selected_medallions}')
        with taba2:
            t1 = st.empty()
            t1.write(f'# Weapons  \n##### Slot 1 : {slotone1}\n#####    Slot 2 : {slottwo1}\n#####    Slot 3 : {slotthree1}\n#####    Slot 4 : {slotfour1}\n#####    Slot 5 : {slotfive1}\n#####    Medallion(s): {selected_medallions}')

        with taba3:
            t2 = st.empty()
            t2.json({'Weapons': [f'Slot 1 : {slotone1}', f'Slot 2 : {slottwo1}', f'Slot 3 : {slotthree1}', f'Slot 4 : {slotfour1}', f'Slot 5 : {slotfive1}', f'Medallion(s) : {selected_medallions}'], })
    with col2:
        taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])

        with taba1:
            tt = st.empty()
            tt.write(f'# Rarity\n    Slot 1 : {slotoner}\n    Slot 2 : {slottwor}\n    Slot 3 : {slotthreer}\n    Slot 4 : {slotfourr}\n    Slot 5 : {slotfiver}')

        with taba2:
            tt1 = st.empty()
            tt1.write(f'# Rarity  \n##### Slot 1 : {slotoner}\n#####    Slot 2 : {slottwor}\n#####    Slot 3 : {slotthreer}\n#####    Slot 4 : {slotfourr}\n#####    Slot 5 : {slotfiver}')

        with taba3:
            tt2 = st.empty()
            tt2.json({'Rarity': [f'Slot 1 : {slotoner}', f'Slot 2 : {slottwor}', f'Slot 3 : {slotthreer}', f'Slot 4 : {slotfourr}', f'Slot 5 : {slotfiver}'],})
    with col3:
        tabb1, tabb2, tabb3 = st.tabs(['Base', 'Regular', 'Json'])
        with tabb1:
            ttt = st.empty()
            ttt.write(
                f'# Attachments\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
        with tabb2:
            ttt1 = st.empty()
            ttt1.write(f'# Attachments\n##### Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n##### Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n##### Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n##### Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n##### Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
        with tabb3:
            ttt2 = st.empty()
            ttt2.json({'Attachments': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}']})
    st.divider()

    def save():
        f = open(f"{File_Path}.txt", "a")           # here                             # here                                   # here                                # here
        f.write(f'{slotone}\n{slotone1}\n{slotoner}\n{slottwo}\n{slottwo1}\n{slottwor}\n{slotthree}\n{slotthree1}\n{slotthreer}\n{slotfour}\n{slotfour1}\n{slotfourr}\n{slotfive}\n{slotfive1}\n{slotfiver}\n{selected_medallions}\n{slotoneattachment1}\n{slotoneattachment2}\n{slotoneattachment3}\n{slotoneattachment4}\n{slottwoattachment1}\n{slottwoattachment2}\n{slottwoattachment3}\n{slottwoattachment4}\n{slotthreeattachment1}\n{slotthreeattachment2}\n{slotthreeattachment3}\n{slotthreeattachment4}\n{slotfourattachment1}\n{slotfourattachment2}\n{slotfourattachment3}\n{slotfourattachment4}\n{slotfiveattachment1}\n{slotfiveattachment2}\n{slotfiveattachment3}\n{slotfiveattachment4}')
        f.close()

    if st.button('Save Config'):
        if os.path.exists(f"{File_Path}.txt"): os.remove(f"{File_Path}.txt")
        save()
        if os.path.exists(f"{File_Path}.txt"):
            st.success(f'Saved config to file \'{File_Path}.txt\'', icon="✅")
    if st.button('Load Config'):
        if os.path.exists(f"{File_Path}.txt"):
            with open(f'{File_Path}.txt', "r") as file:
                lines = [line.strip() for line in file.readlines()]

            if len(lines) == 36:
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
                selected_medallions = lines[15]
                slotoneattachment1 = lines[16]
                slotoneattachment2 = lines[17]
                slotoneattachment3 = lines[18]
                slotoneattachment4 = lines[19]
                slottwoattachment1 = lines[20]
                slottwoattachment2 = lines[21]
                slottwoattachment3 = lines[22]
                slottwoattachment4 = lines[23]
                slotthreeattachment1 = lines[24]
                slotthreeattachment2 = lines[25]
                slotthreeattachment3 = lines[26]
                slotthreeattachment4 = lines[27]
                slotfourattachment1 = lines[28]
                slotfourattachment2 = lines[29]
                slotfourattachment3 = lines[30]
                slotfourattachment4 = lines[31]
                slotfiveattachment1 = lines[32]
                slotfiveattachment2 = lines[33]
                slotfiveattachment3 = lines[34]
                slotfiveattachment4 = lines[35]
                # These prints are just here if you want to get more info. Just remove the '#' from them and then check your CMD, they will show up there as well

                # print("Loaded configuration with success:")
                # print(f"Slot one : {slotone}, {slotoner}, {slotone1}\nSlot two : {slottwo}, {slottwor}, {slottwo1}\nSlot three : {slotthree}, {slotthreer}, {slotthree1}\nSlot four : {slotfour}, {slotfourr}, {slotfour1}\nSlot five : {slotfive}, {slotfiver}, {slotfive1}")

                
                t.write(f'# Custom loadout\n    {slotone} : {slotone1}\n    {slottwo} : {slottwo1}\n    {slotthree} : {slotthree1}\n    {slotfour} : {slotfour1}\n    {slotfive} : {slotfive1}\n    Medallion(s): {selected_medallions}')
                t1.write(f'# Custom loadout  \n##### {slotone} : {slotone1}\n#####    {slottwo} : {slottwo1}\n#####    {slotthree} : {slotthree1}\n#####    {slotfour} : {slotfour1}\n#####    {slotfive} : {slotfive1}\n#####    Medallion(s): {selected_medallions}')
                t2.json({'Custom loadout': [f'{slotone} : {slotone1}', f'{slottwo} : {slottwo1}', f'{slotthree} : {slotthree1}', f'{slotfour} : {slotfour1}', f'{slotfive} : {slotfive1}', f'Medallion(s): {selected_medallions}'], })

                tt.write(f'# Custom loadout rarity\n    {slotone} : {slotoner}\n    {slottwo} : {slottwor}\n    {slotthree} : {slotthreer}\n    {slotfour} : {slotfourr}\n    {slotfive} : {slotfiver}')
                tt1.write(f'# Custom loadout rarity  \n##### {slotone} : {slotoner}\n#####    {slottwo} : {slottwor}\n#####    {slotthree} : {slotthreer}\n#####    {slotfour} : {slotfourr}\n#####    {slotfive} : {slotfiver}')
                tt2.json({'Custom loadout rarity': [f'{slotone} : {slotoner}', f'{slottwo} : {slottwor}', f'{slotthree} : {slotthreer}', f'{slotfour} : {slotfourr}', f'{slotfive} : {slotfiver}'], })

                ttt.write(f'# loadout Mod\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
                ttt1.write(f'# loadout Mod\n##### Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n##### Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n##### Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n##### Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n##### Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
                ttt2.json({'Loadout Mod': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}']})
                st.success(f"Loaded configuration from \'{File_Path}.txt\'", icon="✅")
            else:
                st.error(f"Invalid configuration file. Expected 32 lines. Called back: {len(lines)} line(s)")
        else:
            st.error("File doesn't exist. Please save a config and try again.")

with st.sidebar:
    st.link_button("Github", "https://github.com/fuzzybuzzyboy/py")
    st.link_button("Discord", "https://discord.gg/HVEGufPNnF")
with st.sidebar:
    st.divider()
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
