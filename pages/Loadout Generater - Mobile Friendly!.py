from datetime import datetime
import random, time, os, platform, streamlit as st

st.set_page_config(
    page_title='Loadout Generater',
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help': 'https://discord.gg/HVEGufPNnF',
        'Report a bug': "https://discord.gg/HVEGufPNnF",
        'About': "Random items generator for fortnite (no this doesn't inject into your game and do something blah blah blah)"
    }
)
login = f'{platform.node()}_Gen'
Folder_Path = "configs"
File_Path = os.path.join(Folder_Path, login,)

Slotone_weapon=Slottwo_weapon=Slotthree_weapon=Slotfour_weapon=Slotfive_weapon=None
slotoneattachment1 = slotoneattachment2 = slotoneattachment3 = slotoneattachment4 = slottwoattachment1 = slottwoattachment2 = slottwoattachment3 = slottwoattachment4 = slotthreeattachment1 = slotthreeattachment2 = slotthreeattachment3 = slotthreeattachment4 = slotfourattachment1 = slotfourattachment2 = slotfourattachment3 = slotfourattachment4 = slotfiveattachment1 = slotfiveattachment2 = slotfiveattachment3 = slotfiveattachment4 ='Disabled'
Slotone_Mythic_Mode=Slottwo_Mythic_Mode=Slotthree_Mythic_Mode=Slotfour_Mythic_Mode=Slotfive_Mythic_Mode=5
Slotone_weapon=Slotone_Rarity=Slotone_Attachment=Slottwo_weapon=Slottwo_Rarity=Slottwo_Attachment=Slotthree_Weapon=Slotthree_Rarity=Slotthree_Attachment=Slotfour_Weapon=Slotfour_Rarity=Slotfour_Attachment=Slotfive_weapon=Slotfive_Rarity=Slotfive_Attachment=Slotone_Rarity_Gen=Slottwo_Rarity_Gen=Slotthree_Rarity_Gen=Slotfour_Rarity_Gen=Slotfive_Rarity_Gen=Slotone_Mythic=Slottwo_Mythic=Slotthree_Mythic=Slotfour_Mythic=Slotfive_Mythic=Slottwo_weapon_selected=Slotthree_weapon_selected=Slotfour_weapon_selected=Slotfive_weapon_selected=Medallion=slotone_attachment=slottwo_attachment=slotthree_attachment=slotfour_attachment=slotfive_attachment=None
slotone_allowed=slottwo_allowed=slotthree_allowed=slotfour_allowed=slotfive_allowed='None', 'None'
hammer_pump_options = (('Red Eye Sight', 'Holo-13 Optic'), ('Speed Mag',), ('Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('Suppressor', 'Muzzle Brake'))
frenzy_auto_options = (('Red Eye Sight', 'Holo-13 Optic'), ('Speed Mag', 'Drum Mag'), ('Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('Suppressor', 'Muzzle Brake'))
assault_rifle_options = (('Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('Speed Mag', 'Drum Mag'), ('Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('Suppressor', 'Muzzle Brake'))
thunder_burst_options = (('Red Eye Sight', 'Holo-13 Optic', 'P2X Optic'), ('Speed Mag', 'Drum Mag'), ('Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('Suppressor', 'Muzzle Brake'))
ranger_pistol_options = (('Red Eye Sight', 'Holo-13 Optic'), ('Speed Mag', 'Drum Mag'), ('Laser'), ('Suppressor', 'Muzzle Brake'))
reaper_sniper_options = (('Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('Speed Mag', 'Drum Mag'), ('Vertical Foregrip', 'Angled Foregrip'), ('Suppressor', 'Muzzle Brake'))
rarity={'Hammer Pump Shotgun': 6, 'Frenzy Auto Shotgun': 6, 'Striker AR': 6, 'Enforcer AR':6, 'Nemesis AR':5, 'Hyper SMG':6, 'Thunder Burst SMG':5, 'Ranger Pistol':5, 'Reaper Sniper Rifle':5}
weapons = {'Shotgun': ['Hammer Pump Shotgun', 'Frenzy Auto Shotgun'], 'SMG': ['Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol'], 'Assault-Rifle': ['Striker AR', 'Nemesis AR', 'Enforcer AR'], 'Sniper': ['Reaper Sniper Rifle'], 'Other': ['Grapple Blade', 'Ballistic Shield'], 'Health': ['Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit']}
Medallions=['Valeria\'s Medallion', 'Montague\'s Medallion', 'Nisha\'s Medallion', 'Oscar\'s Medallion', 'Peter Griffin\'s Medallion']
def rarity_gen(Weapon, Slot_Mythic_Mode):
    global Slotone_Mythic_Mode, Slottwo_Mythic_Mode, Slotthree_Mythic_Mode, Slotfour_Mythic_Mode, Slotfive_Mythic_Mode
    if Weapon != 'None':
        SlotWeaponSelect = sorted(Weapon, key=lambda x: rarity.get(x, 0), reverse=True)
        Slot_Mythic_Mode=rarity.__getitem__(Weapon)

def Weapon_Slotone(slot_name):
    global slotone, slotone_allowed, slotone_attachment
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slotone = st.selectbox('Weapon Type', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other', 'Health'), help=f'Allowed weapons for {slot_name}')
    with col3: slotone_allowed = st.multiselect('Allowed Weapons', weapons.get(slotone, []), weapons.get(slotone, []), help=f'Allowed weapons for {slotone} ({slot_name}). You can disable and enable whatever you don\'t want in your loadout')
    with col4: 
        if slotone not in ['Disabled', 'Other', 'Health']: slotone_attachment = st.selectbox('Weapon attachments', ('Enabled', 'Disabled'), help=f'Weapon attachments for {slot_name}')
        else: slotone_attachment = st.selectbox('Weapon attachments', (), help=f'Weapon attachments for {slot_name}')
    st.divider()

def Weapon_Slottwo(slot_name):
    global slottwo, slottwo_allowed, slottwo_attachment
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slottwo = st.selectbox('Weapon Type', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other', 'Health'), help=f'Allowed Weapons for {slot_name}')
    with col3: slottwo_allowed = st.multiselect('Allowed Weapons', weapons.get(slottwo, []), weapons.get(slottwo, []), help=f'Allowed weapons for {slottwo} ({slot_name}). You can disable and enable whatever you don\'t want in your loadout')
    with col4: 
        if slottwo not in ['Disabled', 'Other', 'Health']: slottwo_attachment = st.selectbox('Weapon attachments', ('Enabled', 'Disabled'), help=f'Weapon attachments for {slot_name}')
        else: slottwo_attachment = st.selectbox('Weapon attachments', (), help=f'Weapon attachments for {slot_name}')
    st.divider()

def Weapon_Slotthree(slot_name):
    global slotthree, slotthree_allowed, slotthree_attachment
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slotthree = st.selectbox('Slot 3', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other', 'Health'))
    with col3: slotthree_allowed = st.multiselect('Allowed Weapons', weapons.get(slotthree, []), weapons.get(slotthree, []), help=f'Allowed weapons for {slotthree} ({slot_name}). You can disable and enable whatever you don\'t want in your loadout')
    with col4: 
        if slotthree not in ['Disabled', 'Other', 'Health']: slotthree_attachment = st.selectbox('Weapon attachments', ('Enabled', 'Disabled'), help=f'Weapon attachments for {slot_name}')
        else: slotthree_attachment = st.selectbox('Weapon attachments', (), help=f'Weapon attachments for {slot_name}')
    st.divider()

def Weapon_Slotfour(slot_name):
    global slotfour, slotfour_allowed, slotfour_attachment
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slotfour = st.selectbox('Slot 4', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other', 'Health'))
    with col3: slotfour_allowed = st.multiselect('Allowed Weapons', weapons.get(slotfour, []), weapons.get(slotfour, []), help=f'Allowed weapons for {slotfour} ({slot_name}). You can disable and enable whatever you don\'t want in your loadout')
    with col4: 
        if slotfour not in ['Disabled', 'Other', 'Health']: slotfour_attachment = st.selectbox('Weapon attachments', ('Enabled', 'Disabled'), help=f'Weapon attachments for {slot_name}')
        else: slotfour_attachment = st.selectbox('Weapon attachments', (), help=f'Weapon attachments for {slot_name}')
    st.divider()

def Weapon_Slotfive(slot_name):
    global slotfive, slotfive_allowed, slotfive_attachment
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slotfive = st.selectbox('Slot 5', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other', 'Health'))
    with col3: slotfive_allowed = st.multiselect('Allowed Weapons', weapons.get(slotfive, []), weapons.get(slotfive, []), help=f'Allowed weapons for {slotfive} ({slot_name}). You can disable and enable whatever you don\'t want in your loadout')
    with col4: 
        if slotfive not in ['Disabled', 'Other', 'Health']: slotfive_attachment = st.selectbox('Weapon attachments', ('Enabled', 'Disabled'), help=f'Weapon attachments for {slot_name}')
        else: slotfive_attachment = st.selectbox('Weapon attachments', (), help=f'Weapon attachments for {slot_name}')
    st.divider()

def Weapon_Attachments_Slotone(weapon_name, slot_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    global slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current weapon: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: slotoneattachment1_picker = st.multiselect('Optic', optic_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy. ({slot_name})")
    with col3: slotoneattachment2_picker = st.multiselect('Magazine', magazine_options, help=f"**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed. ({slot_name})")
    with col4: slotoneattachment3_picker = st.multiselect('Underbarrel', underbarrel_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy. ({slot_name})")
    with col5: slotoneattachment4_picker = st.multiselect('Barrel', barrel_options, help=f"**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil. ({slot_name})")
    st.divider()
    attachments_pickers = [slotoneattachment1_picker, slotoneattachment2_picker, slotoneattachment3_picker, slotoneattachment4_picker]
    for i in range(4): globals()[f'slotoneattachment{i + 1}'] = random.choice(attachments_pickers[i]) if attachments_pickers[i] else 'None'

def Weapon_Attachments_Slottwo(weapon_name, slot_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    global slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current weapon: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: slottwoattachment1_picker = st.multiselect('Optic', optic_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy. ({slot_name})")
    with col3: slottwoattachment2_picker = st.multiselect('Magazine', magazine_options, help=f"**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed. ({slot_name})")
    with col4: slottwoattachment3_picker = st.multiselect('Underbarrel', underbarrel_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy. ({slot_name})")
    with col5: slottwoattachment4_picker = st.multiselect('Barrel', barrel_options, help=f"**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil. ({slot_name})")
    st.divider()
    attachments_pickers = [slottwoattachment1_picker, slottwoattachment2_picker, slottwoattachment3_picker, slottwoattachment4_picker]
    for i in range(4): globals()[f'slottwoattachment{i + 1}'] = random.choice(attachments_pickers[i]) if attachments_pickers[i] else 'None'

def Weapon_Attachments_Slotthree(weapon_name, slot_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    global slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current weapon: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: slotthreeattachment1_picker = st.multiselect('Optic', optic_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy. ({slot_name})")
    with col3: slotthreeattachment2_picker = st.multiselect('Magazine', magazine_options, help=f"**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed. ({slot_name})")
    with col4: slotthreeattachment3_picker = st.multiselect('Underbarrel', underbarrel_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy. ({slot_name})")
    with col5: slotthreeattachment4_picker = st.multiselect('Barrel', barrel_options, help=f"**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil. ({slot_name})")
    st.divider()
    attachments_pickers = [slotthreeattachment1_picker, slotthreeattachment2_picker, slotthreeattachment3_picker, slotthreeattachment4_picker]
    for i in range(4): globals()[f'slotthreeattachment{i + 1}'] = random.choice(attachments_pickers[i]) if attachments_pickers[i] else 'None'

def Weapon_Attachments_Slotfour(weapon_name, slot_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    global slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current weapon: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: slotfourattachment1_picker = st.multiselect('Optic', optic_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy. ({slot_name})")
    with col3: slotfourattachment2_picker = st.multiselect('Magazine', magazine_options, help=f"**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed. ({slot_name})")
    with col4: slotfourattachment3_picker = st.multiselect('Underbarrel', underbarrel_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy. ({slot_name})")
    with col5: slotfourattachment4_picker = st.multiselect('Barrel', barrel_options, help=f"**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil. ({slot_name})")
    st.divider()
    attachments_pickers = [slotfourattachment1_picker, slotfourattachment2_picker, slotfourattachment3_picker, slotfourattachment4_picker]
    for i in range(4): globals()[f'slotfourattachment{i + 1}'] = random.choice(attachments_pickers[i]) if attachments_pickers[i] else 'None'

def Weapon_Attachments_Slotfive(weapon_name, slot_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    global slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current weapon: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: slotfiveattachment1_picker = st.multiselect('Optic', optic_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy. ({slot_name})")
    with col3: slotfiveattachment2_picker = st.multiselect('Magazine', magazine_options, help=f"**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed. ({slot_name})")
    with col4: slotfiveattachment3_picker = st.multiselect('Underbarrel', underbarrel_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Incresese hipfire accuracy. ({slot_name})")
    with col5: slotfiveattachment4_picker = st.multiselect('Barrel', barrel_options, help=f"**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil. ({slot_name})")
    st.divider()
    attachments_pickers = [slotfiveattachment1_picker, slotfiveattachment2_picker, slotfiveattachment3_picker, slotfiveattachment4_picker]
    for i in range(4): globals()[f'slotfiveattachment{i + 1}'] = random.choice(attachments_pickers[i]) if attachments_pickers[i] else 'None'
Customize, Weapon_mods, Loadout = st.tabs(["Customize", "Weapon Mods", "Loadout"])

with Customize:
    Weapon_Slotone("Slot 1")
    Weapon_Slottwo("Slot 2")
    Weapon_Slotthree("Slot 3")
    Weapon_Slotfour("Slot 4")
    Weapon_Slotfive("Slot 5")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Medallions', divider='rainbow')
    with col2: slotsix = st.selectbox('Medallions', ('Disabled', 'Enabled'))
    with col3:
        if slotsix == 'Enabled': medallions_amount = st.selectbox('Amount of medallions', [1, 2, 3, 4, 5], help='Example, if selected 5, it will select 1-5 medallions from a random list.')
    with col4: 
        if slotsix=='Enabled': slotsix_randomness = st.selectbox('Randomnmess', ['Enabled', 'Disabled'], help='If enabled it will randomly select from (lets say you selected 5) 1-5 medallions, else will pick 5 medallions')
    if slotone_allowed: Slotone_weapon = random.choice(slotone_allowed)
    if slottwo_allowed: Slottwo_weapon = random.choice(slottwo_allowed)
    if slotthree_allowed: Slotthree_weapon = random.choice(slotthree_allowed)
    if slotfour_allowed: Slotfour_weapon = random.choice(slotfour_allowed)
    if slotfive_allowed: Slotfive_weapon = random.choice(slotfive_allowed)
    if slotsix=='Enabled' and slotsix_randomness!='Disabled': 
        num_medallions_to_select = random.randint(1, medallions_amount)
        Selected_medallions = random.sample(Medallions, k=num_medallions_to_select)
        Medallion = ', '.join(Selected_medallions)
    elif slotsix=='Enabled' and slotsix_randomness=='Disabled':
        Selected_medallions = random.sample(Medallions, k=int(medallions_amount))
        Medallion = ', '.join(Selected_medallions)
with Weapon_mods:
    if slotone_attachment == 'Enabled':
        if Slotone_weapon == 'Hammer Pump Shotgun': Weapon_Attachments_Slotone(Slotone_weapon, "Slot 1",  *hammer_pump_options)
        elif Slotone_weapon == 'Frenzy Auto Shotgun': Weapon_Attachments_Slotone(Slotone_weapon, "Slot 1", *frenzy_auto_options)
        elif Slotone_weapon in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): Weapon_Attachments_Slotone(Slotone_weapon, "Slot 1", *assault_rifle_options)
        elif Slotone_weapon in ('Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol'): Weapon_Attachments_Slotone(Slotone_weapon, "Slot 1", *thunder_burst_options)
        elif Slotone_weapon == 'Reaper Sniper Rifle': Weapon_Attachments_Slotone(Slotone_weapon, "Slot 1", *reaper_sniper_options)
    else: slotoneattachment1=slotoneattachment2=slotoneattachment3=slotoneattachment4='Disabled'
    if slottwo_attachment == 'Enabled':
        if Slottwo_weapon == 'Hammer Pump Shotgun': Weapon_Attachments_Slottwo(Slottwo_weapon, "Slot 2",  *hammer_pump_options)
        elif Slottwo_weapon == 'Frenzy Auto Shotgun': Weapon_Attachments_Slottwo(Slottwo_weapon, "Slot 2", *frenzy_auto_options)
        elif Slottwo_weapon in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): Weapon_Attachments_Slottwo(Slottwo_weapon, "Slot 2", *assault_rifle_options)
        elif Slottwo_weapon in ('Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol'): Weapon_Attachments_Slottwo(Slottwo_weapon, "Slot 2", *thunder_burst_options)
        elif Slottwo_weapon == 'Reaper Sniper Rifle': Weapon_Attachments_Slottwo(Slottwo_weapon, "Slot 2", *reaper_sniper_options)
    else: slottwoattachment1=slottwoattachment2=slottwoattachment3=slottwoattachment4='Disabled'
    if slotthree_attachment == 'Enabled':
        if Slotthree_weapon == 'Hammer Pump Shotgun': Weapon_Attachments_Slotthree(Slotthree_weapon, "Slot 3",  *hammer_pump_options)
        elif Slotthree_weapon == 'Frenzy Auto Shotgun': Weapon_Attachments_Slotthree(Slotthree_weapon, "Slot 3", *frenzy_auto_options)
        elif Slotthree_weapon in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): Weapon_Attachments_Slotthree(Slotthree_weapon, "Slot 3", *assault_rifle_options)
        elif Slotthree_weapon in ('Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol'): Weapon_Attachments_Slotthree(Slotthree_weapon, "Slot 3", *thunder_burst_options)
        elif Slotthree_weapon == 'Reaper Sniper Rifle': Weapon_Attachments_Slotthree(Slotthree_weapon, "Slot 3", *reaper_sniper_options)
    else: slotthreeattachment1=slotthreeattachment2=slotthreeattachment3=slotthreeattachment4='Disabled'
    if slotfour_attachment == 'Enabled':
        if Slotfour_weapon == 'Hammer Pump Shotgun': Weapon_Attachments_Slotfour(Slotfour_weapon, "Slot 4",  *hammer_pump_options)
        elif Slotfour_weapon == 'Frenzy Auto Shotgun': Weapon_Attachments_Slotfour(Slotfour_weapon, "Slot 4", *frenzy_auto_options)
        elif Slotfour_weapon in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): Weapon_Attachments_Slotfour(Slotfour_weapon, "Slot 4", *assault_rifle_options)
        elif Slotfour_weapon in ('Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol'): Weapon_Attachments_Slotfour(Slotfour_weapon, "Slot 4", *thunder_burst_options)
        elif Slotfour_weapon == 'Reaper Sniper Rifle': Weapon_Attachments_Slotfour(Slotfour_weapon, "Slot 4", *reaper_sniper_options)
    else: slotfourattachment1=slotfourattachment2=slotfourattachment3=slotfourattachment4='Disabled'
    if slotfive_attachment == 'Enabled':
        if Slotfive_weapon == 'Hammer Pump Shotgun': Weapon_Attachments_Slotfive(Slotfive_weapon, "Slot 5",  *hammer_pump_options)
        elif Slotfive_weapon == 'Frenzy Auto Shotgun': Weapon_Attachments_Slotfive(Slotfive_weapon, "Slot 5", *frenzy_auto_options)
        elif Slotfive_weapon in ('Striker AR', 'Nemesis AR', 'Enforcer AR'): Weapon_Attachments_Slotfive(Slotfive_weapon, "Slot 5", *assault_rifle_options)
        elif Slotfive_weapon in ('Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol'): Weapon_Attachments_Slotfive(Slotfive_weapon, "Slot 5", *thunder_burst_options)
        elif Slotfive_weapon == 'Reaper Sniper Rifle': Weapon_Attachments_Slotfive(Slotfive_weapon, "Slot 5", *reaper_sniper_options)
    else: slotfiveattachment1=slotfiveattachment2=slotfiveattachment3=slotfiveattachment4='Disabled'
with Loadout: # absolutly amazing rarity gen. (why am i just not using a list with the raritys and calling the raritys based off of that or something stupid like that)
    if slotone!='Other' and slotone!='Disabled' and slotone!='Health':
        rarity_gen(Slotone_weapon, Slotone_Mythic_Mode)
        if slotone == 'Sniper': slotone_rarity_gen=random.randint(2, Slotone_Mythic_Mode)
        else: slotone_rarity_gen=random.randint(1, Slotone_Mythic_Mode)
        if slotone_rarity_gen==1: Slotone_Rarity='Common'
        elif slotone_rarity_gen==2: Slotone_Rarity='Uncommon'
        elif slotone_rarity_gen==3: Slotone_Rarity='Rare'
        elif slotone_rarity_gen==4: Slotone_Rarity='Epic'
        elif slotone_rarity_gen==5: Slotone_Rarity='Legendary'
        elif slotone_rarity_gen==6: Slotone_Rarity='Mythic'
    else: Slotone_Rarity=None

    if slottwo!='Other' and slottwo!='Disabled' and slottwo!='Health':
        rarity_gen(Slottwo_weapon, Slottwo_Mythic_Mode)
        if slottwo == 'Sniper': slottwo_rarity_gen=random.randint(2, Slottwo_Mythic_Mode)
        else: slottwo_rarity_gen=random.randint(1, Slottwo_Mythic_Mode)
        if slottwo_rarity_gen==1: Slottwo_Rarity='Common'
        elif slottwo_rarity_gen==2: Slottwo_Rarity='Uncommon'
        elif slottwo_rarity_gen==3: Slottwo_Rarity='Rare'
        elif slottwo_rarity_gen==4: Slottwo_Rarity='Epic'
        elif slottwo_rarity_gen==5: Slottwo_Rarity='Legendary'
        elif slottwo_rarity_gen==6: Slottwo_Rarity='Mythic'
    else: Slottwo_Rarity=None

    if slotthree!='Other' and slotthree!='Disabled' and slotthree!='Health':
        rarity_gen(Slotthree_weapon, Slotthree_Mythic_Mode)
        if slotthree == 'Sniper': slotthree_rarity_gen=random.randint(2, Slotthree_Mythic_Mode)
        else: slotthree_rarity_gen=random.randint(1, Slotthree_Mythic_Mode)
        if slotthree_rarity_gen==1: Slotthree_Rarity='Common'
        elif slotthree_rarity_gen==2: Slotthree_Rarity='Uncommon'
        elif slotthree_rarity_gen==3: Slotthree_Rarity='Rare'
        elif slotthree_rarity_gen==4: Slotthree_Rarity='Epic'
        elif slotthree_rarity_gen==5: Slotthree_Rarity='Legendary'
        elif slotthree_rarity_gen==6: Slotthree_Rarity='Mythic'
    else: Slotthree_Rarity=None

    if slotfour!='Other' and slotfour!='Disabled' and slotfour!='Health':
        rarity_gen(Slotfour_weapon, Slotfour_Mythic_Mode)
        if slotfour == 'Sniper': slotfour_rarity_gen=random.randint(2, Slotfour_Mythic_Mode)
        else: slotfour_rarity_gen=random.randint(1, Slotfour_Mythic_Mode)
        if slotfour_rarity_gen==1: Slotfour_Rarity='Common'
        elif slotfour_rarity_gen==2: Slotfour_Rarity='Uncommon'
        elif slotfour_rarity_gen==3: Slotfour_Rarity='Rare'
        elif slotfour_rarity_gen==4: Slotfour_Rarity='Epic'
        elif slotfour_rarity_gen==5: Slotfour_Rarity='Legendary'
        elif slotfour_rarity_gen==6: Slotfour_Rarity='Mythic'
    else: Slotfour_Rarity=None

    if slotfive!='Other' and slotfive!='Disabled' and slotfive!='Health':
        rarity_gen(Slotfive_weapon, Slotfive_Mythic_Mode)
        if slotfive == 'Sniper': slotfive_rarity_gen=random.randint(2, Slotfive_Mythic_Mode)
        else: slotfive_rarity_gen=random.randint(1, Slotfive_Mythic_Mode)
        if slotfive_rarity_gen==1: Slotfive_Rarity='Common'
        elif slotfive_rarity_gen==2: Slotfive_Rarity='Uncommon'
        elif slotfive_rarity_gen==3: Slotfive_Rarity='Rare'
        elif slotfive_rarity_gen==4: Slotfive_Rarity='Epic'
        elif slotfive_rarity_gen==5: Slotfive_Rarity='Legendary'
        elif slotfive_rarity_gen==6: Slotfive_Rarity='Mythic'
    else: Slotfive_Rarity=None # yay we passed the shitty code and now we can see how you see your generated loadout (why am I making these comments, its already 1am and i should probably go to sleep)

    col1, col2, col3 = st.columns(3)
    with col1:
        tab1b, tab2b, tab3b = st.tabs(["Base", "Regular", "Json"])
        with tab1b:
            t1 = st.empty() # ah dont we love streamlit and its stupid st.empty thing (this code could be so much shorter if streamlit wasnt sooooo shitty sometimes :D)
            t1.write(f'# Weapons\n    Slot 1 : {Slotone_weapon}\n    Slot 2 : {Slottwo_weapon}\n    Slot 3 : {Slotthree_weapon}\n    Slot 4 : {Slotfour_weapon}\n    Slot 5 : {Slotfive_weapon}\n    Medallions : {Medallion}')
        with tab2b:
            t2 = st.empty()
            t2.write(f'# Weapons  \n##### Slot 1 : {Slotone_weapon}\n#####    Slot 2 : {Slottwo_weapon}\n#####    Slot 3 : {Slotthree_weapon}\n#####    Slot 4 : {Slotfour_weapon}\n#####    Slot 5 : {Slotfive_weapon}')
        with tab3b:
            t3 = st.empty()
            t3.json({'Weapons': [f'Slot 1 : {Slotone_weapon}', f'Slot 2 : {Slottwo_weapon}', f'Slot 3 : {Slotthree_weapon}', f'Slot 4 : {Slotfour_weapon}', f'Slot 5 : {Slotfive_weapon}'], })
    with col2:
            taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])
            with taba1:
                tt1 = st.empty()
                tt1.write(f'# Rarity\n    Slot 1 : {Slotone_Rarity}\n    Slot 2 : {Slottwo_Rarity}\n    Slot 3 : {Slotthree_Rarity}\n    Slot 4 : {Slotfour_Rarity}\n    Slot 5 : {Slotfive_Rarity}')
            with taba2:
                tt2 = st.empty()
                tt2.write(f'# Rarity  \n##### Slot 1 : {Slotone_Rarity}\n#####    Slot 2 : {Slottwo_Rarity}\n#####    Slot 3 : {Slotthree_Rarity}\n#####    Slot 4 : {Slotfour_Rarity}\n#####    Slot 5 : {Slotfive_Rarity}')
            with taba3:
                tt3 = st.empty()
                tt3.json({'Rarity': [f'Slot 1 : {Slotone_Rarity}', f'Slot 2 : {Slottwo_Rarity}', f'Slot 3 : {Slotthree_Rarity}', f'Slot 4 : {Slotfour_Rarity}', f'Slot 5 : {Slotfive_Rarity}'], })
    with col3:
            taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])
            with taba1:
                ttt1 = st.empty()
                ttt1.write(f'# Attachments\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
            with taba2:
                ttt2 = st.empty()
                ttt2.write(f'# Attachments  \n##### Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n#####    Slot 2 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n#####    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n#####    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n#####    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
            with taba3:
                ttt3 = st.empty()
                ttt3.json({'Attachments': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}'], })

    st.divider()
    st.button('Randomize loadout') # why the hell is this written like this :skull:. I guess it work's so :shrug:
    st.divider()

    def save():
        f = open(f"{File_Path}.txt", "a")           # here                             # here                                   # here                                # here
        f.write(f'{Slotone_weapon}\n{Slottwo_weapon}\n{Slotthree_weapon}\n{Slotfour_weapon}\n{Slotfive_weapon}\n{Slotone_Rarity}\n{Slottwo_Rarity}\n{Slotthree_Rarity}\n{Slotfour_Rarity}\n{Slotfive_Rarity}\n{slotoneattachment1}\n{slotoneattachment2}\n{slotoneattachment3}\n{slotoneattachment4}\n{slottwoattachment1}\n{slottwoattachment2}\n{slottwoattachment3}\n{slottwoattachment4}\n{slotthreeattachment1}\n{slotthreeattachment2}\n{slotthreeattachment3}\n{slotthreeattachment4}\n{slotfourattachment1}\n{slotfourattachment2}\n{slotfourattachment3}\n{slotfourattachment4}\n{slotfiveattachment1}\n{slotfiveattachment2}\n{slotfiveattachment3}\n{slotfiveattachment4}\n{Medallion}')
        f.close()

    if st.button('Save Config'):
        if os.path.exists(f"{File_Path}.txt"): os.remove(f"{File_Path}.txt")
        save()
        if os.path.exists(f"{File_Path}.txt"):
            st.success(f'Saved config to file \'{File_Path}.txt\'', icon="✅")


    if st.button('Load Config'): # chatgpt code lmao
        if os.path.exists(f"{File_Path}.txt"): 
            with open(f'{File_Path}.txt', "r") as file: lines = [line.strip() for line in file.readlines()]

            if len(lines) == 31:
                Slotone_weapon = lines[0]
                Slottwo_weapon = lines[1]
                Slotthree_weapon = lines[2]
                Slotfour_weapon = lines[3]
                Slotfive_weapon = lines[4]
                Slotone_Rarity = lines[5]
                Slottwo_Rarity = lines[6]
                Slotthree_Rarity = lines[7]
                Slotfour_Rarity = lines[8]
                Slotfive_Rarity = lines[9]
                slotoneattachment1 = lines[10]
                slotoneattachment2 = lines[11]
                slotoneattachment3 = lines[12]
                slotoneattachment4 = lines[13]
                slottwoattachment1 = lines[14]
                slottwoattachment2 = lines[15]
                slottwoattachment3 = lines[16]
                slottwoattachment4 = lines[17]
                slotthreeattachment1 = lines[18]
                slotthreeattachment2 = lines[19]
                slotthreeattachment3 = lines[20]
                slotthreeattachment4 = lines[21]
                slotfourattachment1 = lines[22]
                slotfourattachment2 = lines[23]
                slotfourattachment3 = lines[24]
                slotfourattachment4 = lines[25]
                slotfiveattachment1 = lines[26]
                slotfiveattachment2 = lines[27]
                slotfiveattachment3 = lines[28]
                slotfiveattachment4 = lines[29]
                Medallion = lines[30]

                t1.write(f'# Weapons\n    Slot 1 : {Slotone_weapon}\n    Slot 2 : {Slottwo_weapon}\n    Slot 3 : {Slotthree_weapon}\n    Slot 4 : {Slotfour_weapon}\n    Slot 5 : {Slotfive_weapon}\n    Medallions : {Medallion}')
                t2.write(f'# Weapons  \n##### Slot 1 : {Slotone_weapon}\n#####    Slot 2 : {Slottwo_weapon}\n#####    Slot 3 : {Slotthree_weapon}\n#####    Slot 4 : {Slotfour_weapon}\n#####    Slot 5 : {Slotfive_weapon}')
                t3.json({'Weapons': [f'Slot 1 : {Slotone_weapon}', f'Slot 2 : {Slottwo_weapon}', f'Slot 3 : {Slotthree_weapon}', f'Slot 4 : {Slotfour_weapon}', f'Slot 5 : {Slotfive_weapon}'], })

                tt1.write(f'# Rarity\n    Slot 1 : {Slotone_Rarity}\n    Slot 2 : {Slottwo_Rarity}\n    Slot 3 : {Slotthree_Rarity}\n    Slot 4 : {Slotfour_Rarity}\n    Slot 5 : {Slotfive_Rarity}')
                tt2.write(f'# Rarity  \n##### Slot 1 : {Slotone_Rarity}\n#####    Slot 2 : {Slottwo_Rarity}\n#####    Slot 3 : {Slotthree_Rarity}\n#####    Slot 4 : {Slotfour_Rarity}\n#####    Slot 5 : {Slotfive_Rarity}')
                tt3.json({'Rarity': [f'Slot 1 : {Slotone_Rarity}', f'Slot 2 : {Slottwo_Rarity}', f'Slot 3 : {Slotthree_Rarity}', f'Slot 4 : {Slotfour_Rarity}', f'Slot 5 : {Slotfive_Rarity}'], })

                ttt1.write(f'# Attachments\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
                ttt2.write(f'# Attachments  \n##### Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n#####    Slot 2 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n#####    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n#####    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n#####    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
                ttt3.json({'Attachments': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}'], })
                st.success(f"Loaded configuration from \'{File_Path}.txt\'", icon="✅")
            else: st.error(f"Invalid configuration file. Expected 31 lines. Called back: {len(lines)} line(s)")
        else: st.error("File doesn't exist. Please save a config and try again.")
with st.sidebar:
    st.link_button("Github", "https://github.com/fuzzybuzzyboy/py")
    st.link_button("Discord", "https://discord.gg/HVEGufPNnF")
    with st.empty():
        if st.button('Clock'):
                while True:
                    time_now1 = datetime.now().strftime("%D")
                    time_now = datetime.now().strftime("%H:%M:%S")
                    st.write(f'# Clock\n    Time : {time_now}\n    Date : {time_now1}')
                    time_later = datetime.now().strftime("%S")
                    time.sleep(1) # fucking kill me with this clock code god damn it, this code was written like 9 months ago or some shit and just now im realizing how bad this code is (go check old commits for old clock code because im too lazy to show u)
