import streamlit as st, os, time
from datetime import datetime

st.set_page_config(page_title='Custom Loadout', page_icon="🤑", layout="wide", initial_sidebar_state="expanded", menu_items={'Get help': 'https://github.com/fuzzybuzzyboy/py', 'Report a bug': "https://github.com/fuzzybuzzyboy/py", 'About': "Random items generator for fortnite (no this doesn't inject into your game and do something blah blah blah)"})
slotoneattachment1 = slotoneattachment2 = slotoneattachment3 = slotoneattachment4 = slottwoattachment1 = slottwoattachment2 = slottwoattachment3 = slottwoattachment4 = slotthreeattachment1 = slotthreeattachment2 = slotthreeattachment3 = slotthreeattachment4 = slotfourattachment1 = slotfourattachment2 = slotfourattachment3 = slotfourattachment4 = slotfiveattachment1 = slotfiveattachment2 = slotfiveattachment3 = slotfiveattachment4 = None
slotone=slottwo=slotthree=slotfour=slotfive=None
slotone1=slottwo1=slotthree1=slotfour1=slotfive1=None
slotoner=slottwor=slotthreer=slotfourr=slotfiver=None
hammer_pump_options = (('None', 'Red Eye Sight', 'Holo-13 Optic'), ('None', 'Speed Mag',), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake'))
frenzy_auto_options = (('None', 'Red Eye Sight', 'Holo-13 Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake'))
assault_rifle_options = (('None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake'))
thunder_burst_options = (('None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake'))
ranger_pistol_options = (('None', 'Red Eye Sight', 'Holo-13 Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake'))
reaper_sniper_options = (('None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip'), ('None', 'Suppressor', 'Muzzle Brake'))
nothing_options=((), (), (), ())
rarity_options = {'Shotgun': ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'), 'SMG': ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'), 'Assault-Rifle': ('Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'), 'Sniper': ('Uncommon', 'Rare', 'Epic', 'Legendary'), 'Other': ('None',)}
weapon_options = {'Shotgun': ('Hammer Pump Shotgun', 'Peter Griffin\'s Hammer Pump Shotgun', 'Frenzy Auto Shotgun', 'Oscar\'s Frenzy Auto Shotgun'), 'SMG': ('Thunder Burst SMG', 'Hyper SMG', 'Valeria\'s Hyper SMG', 'Ranger Pistol'), 'Assault-Rifle': ('Striker AR', 'Nisha\'s Striker AR', 'Nemesis AR', 'Montague\'s Enforcer AR'), 'Sniper': ('Reaper Sniper Rifle',), 'Other': ('Grapple Blade', 'Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit')}
weapon_attachment_options = {'Hammer Pump Shotgun': hammer_pump_options, 'Frenzy Auto Shotgun': frenzy_auto_options, 'Striker AR': assault_rifle_options, 'Nemesis AR': assault_rifle_options, 'Enforcer AR': assault_rifle_options, 'Thunder Burst SMG': thunder_burst_options, 'Hyper SMG': thunder_burst_options, 'Ranger Pistol': ranger_pistol_options, 'Reaper Sniper Rifle': reaper_sniper_options}

def Weapon_Slot(slot_name):
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slot = st.selectbox('Weapon Type', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other'), help=f'Weapon type for {slot_name}') 
    with col3: slot1 = st.selectbox('Weapon', weapon_options.get(slot, ()), help=f'Weapon selection for {slot_name}')
    with col4:
        if slot1 in ('Peter Griffin\'s Hammer Pump Shotgun', 'Oscar\'s Frenzy Auto Shotgun', 'Valeria\'s Hyper SMG', 'Nisha\'s Striker AR', 'Montague\'s Enforcer AR'): slotr = st.selectbox('Rarity', ('Mythic',), help=f'Weapon rarity for {slot_name}')
        else: slotr = st.selectbox('Rarity', rarity_options.get(slot, ()), help=f'Weapon rarity for {slot_name}')
    st.divider()
    return slot, slot1, slotr

def AttachmentViewer(slot_name, weapon_name, optic_options, magazine_options, underbarrel_options, barrel_options, *attachments):
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current item: {weapon_name}', help=f"Shows current weapon for {slot_name}", divider='rainbow')
    with col2: attachment1 = st.selectbox('Optic', optic_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Increases hipfire accuracy. ({slot_name})")
    with col3: attachment2 = st.selectbox('Magazine', magazine_options, help=f"**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed. ({slot_name})")
    with col4: attachment3 = st.selectbox('Underbarrel', underbarrel_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Increases hipfire accuracy. ({slot_name})")
    with col5: attachment4 = st.selectbox('Barrel', barrel_options, help=f"**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil. ({slot_name})")
    st.divider()
    return attachment1, attachment2, attachment3, attachment4

selected_medallions = 'None'
Folder_Path = "configs"
File_Path = os.path.join(Folder_Path, "Config_loadout")

tab1, tab2, tab3, tab4 = st.tabs(["Customize", 'Weapon Mods', "Loadout", "Weapon Info"])
with tab1:
    slotone, slotone1, slotoner = Weapon_Slot("Slot 1")
    slottwo, slottwo1, slottwor = Weapon_Slot("Slot 2")
    slotthree, slotthree1, slotthreer = Weapon_Slot("Slot 3")
    slotfour, slotfour1, slotfourr = Weapon_Slot("Slot 4")
    slotfive, slotfive1, slotfiver = Weapon_Slot("Slot 5")
    col1,col2=st.columns(2)
    with col1: st.subheader(f'Medallion(s)', help=f"Medallion picker", divider='rainbow')
    with col2: slotsix = st.multiselect('Medallions', ('Valeria\'s Medallion', 'Montague\'s Medallion', 'Nisha\'s Medallion', 'Oscar\'s Medallion', 'Peter Griffin\'s Medallion'), placeholder="Choose a medallion(s).")
with tab2:
    if slotone1 and slotone!='Other' and slotoner!='Mythic': slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4 = AttachmentViewer('Slot 1', slotone1, *weapon_attachment_options[slotone1])
    else: slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4 = AttachmentViewer('Slot 1', slotone1, *nothing_options)
    if slottwo1 and slottwo!='Other' and slottwor!='Mythic': slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4 = AttachmentViewer('Slot 2', slottwo1, *weapon_attachment_options[slottwo1])
    else: slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4 = AttachmentViewer('Slot 2', slottwo1, *nothing_options)
    if slotthree1 and slotthree!='Other' and slotthreer!='Mythic': slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4 = AttachmentViewer('Slot 3', slotthree1, *weapon_attachment_options[slotthree1])
    else: slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4 = AttachmentViewer('Slot 3', slotthree1, *nothing_options)
    if slotfour1 and slotfour!='Other' and slotfourr!='Mythic': slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4 = AttachmentViewer('Slot 4', slotfour1, *weapon_attachment_options[slotfour1])
    else: slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4 = AttachmentViewer('Slot 4', slotfour1, *nothing_options)
    if slotfive1 and slotfive!='Other' and slotfiver!='Mythic': slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4 = AttachmentViewer('Slot 5', slotfive1, *weapon_attachment_options[slotfive1])
    else: slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4 = AttachmentViewer('Slot 5', slotfive1, *nothing_options)
with tab3:
    if slotsix: selected_medallions = ', '.join(slotsix)
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
            ttt.write(f'# Attachments\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
        with tabb2:
            ttt1 = st.empty()
            ttt1.write(f'# Attachments\n##### Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n##### Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n##### Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n##### Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n##### Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
        with tabb3:
            ttt2 = st.empty()
            ttt2.json({'Attachments': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}']})
    st.divider()
    if st.button('Save Config'):
        if os.path.exists(f"{File_Path}.txt"): os.remove(f"{File_Path}.txt")
        f = open(f"{File_Path}.txt", "a")           # here                             # here                                   # here                                # here
        f.write(f'{slotone}\n{slotone1}\n{slotoner}\n{slottwo}\n{slottwo1}\n{slottwor}\n{slotthree}\n{slotthree1}\n{slotthreer}\n{slotfour}\n{slotfour1}\n{slotfourr}\n{slotfive}\n{slotfive1}\n{slotfiver}\n{selected_medallions}\n{slotoneattachment1}\n{slotoneattachment2}\n{slotoneattachment3}\n{slotoneattachment4}\n{slottwoattachment1}\n{slottwoattachment2}\n{slottwoattachment3}\n{slottwoattachment4}\n{slotthreeattachment1}\n{slotthreeattachment2}\n{slotthreeattachment3}\n{slotthreeattachment4}\n{slotfourattachment1}\n{slotfourattachment2}\n{slotfourattachment3}\n{slotfourattachment4}\n{slotfiveattachment1}\n{slotfiveattachment2}\n{slotfiveattachment3}\n{slotfiveattachment4}')
        st.success(f'Saved config to file \'{File_Path}.txt\'', icon="✅")
        f.close()

    if st.button('Load Config'):
        if os.path.exists(f"{File_Path}.txt"):
            with open(f'{File_Path}.txt', "r") as file:
                lines = [line.strip() for line in file.readlines()]

            if len(lines) == 36:
                (slotone, slotone1, slotoner, slottwo, slottwo1, slottwor, slotthree, slotthree1, slotthreer, slotfour, slotfour1, slotfourr, slotfive, slotfive1, slotfiver, selected_medallions, slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4, slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4, slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4, slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4, slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4) = lines
                #print(f"Loaded configuration with success:\nSlot one : {slotone}, {slotoner}, {slotone1}, {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\nSlot two : {slottwo}, {slottwor}, {slottwo1}, {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\nSlot three : {slotthree}, {slotthreer}, {slotthree1}, {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\nSlot four : {slotfour}, {slotfourr}, {slotfour1}, {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\nSlot five : {slotfive}, {slotfiver}, {slotfive1}, {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}\n")
                t.write(f'# Weapons\n    {slotone} : {slotone1}\n    {slottwo} : {slottwo1}\n    {slotthree} : {slotthree1}\n    {slotfour} : {slotfour1}\n    {slotfive} : {slotfive1}\n    Medallion(s): {selected_medallions}')
                t1.write(f'# Weapons\n##### {slotone} : {slotone1}\n#####    {slottwo} : {slottwo1}\n#####    {slotthree} : {slotthree1}\n#####    {slotfour} : {slotfour1}\n#####    {slotfive} : {slotfive1}\n#####    Medallion(s): {selected_medallions}')
                t2.json({'Weapons': [f'{slotone} : {slotone1}', f'{slottwo} : {slottwo1}', f'{slotthree} : {slotthree1}', f'{slotfour} : {slotfour1}', f'{slotfive} : {slotfive1}', f'Medallion(s): {selected_medallions}'], })
                tt.write(f'# Rarity\n    {slotone} : {slotoner}\n    {slottwo} : {slottwor}\n    {slotthree} : {slotthreer}\n    {slotfour} : {slotfourr}\n    {slotfive} : {slotfiver}')
                tt1.write(f'# Rarity\n##### {slotone} : {slotoner}\n#####    {slottwo} : {slottwor}\n#####    {slotthree} : {slotthreer}\n#####    {slotfour} : {slotfourr}\n#####    {slotfive} : {slotfiver}')
                tt2.json({'Rarity': [f'{slotone} : {slotoner}', f'{slottwo} : {slottwor}', f'{slotthree} : {slotthreer}', f'{slotfour} : {slotfourr}', f'{slotfive} : {slotfiver}'], })
                ttt.write(f'# Attachments\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
                ttt1.write(f'# Attachments\n##### Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n##### Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n##### Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n##### Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n##### Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
                ttt2.json({'Attachments': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}']})
                st.success(f"Loaded configuration from \'{File_Path}.txt\'", icon="✅")
            else:
                st.error(f"Invalid configuration file. Expected 36 lines. Called back: {len(lines)} line(s)")
        else:
            st.error("File doesn't exist. Please save a config and try again.")

with st.sidebar:
    st.link_button("Github", "https://github.com/fuzzybuzzyboy/py")
    st.link_button("Discord", "https://discord.gg/HVEGufPNnF")
    if st.button('Clock'):
        with st.empty():
            while True:
                time_now1, time_now = datetime.now().strftime("%D"), datetime.now().strftime("%H:%M:%S")
                st.write(f'# Clock\n    Time : {time_now}\n    Date : {time_now1}')
                time.sleep(1)
