from datetime import datetime
import random, time, os, streamlit as st

st.set_page_config(page_title='Loadout Generater', page_icon="🤑", layout="wide", initial_sidebar_state="expanded", menu_items={'Get help': 'https://github.com/fuzzybuzzyboy/py', 'Report a bug': "https://github.com/fuzzybuzzyboy/py", 'About': "Random items generator for fortnite (no this doesn't inject into your game and do something blah blah blah)"})

login = 'Config_generator'
Folder_Path = "configs"
File_Path = os.path.join(Folder_Path, login)

medallions_amount=0
medallions_amount_text='1-'
Slotone_weapon=Slottwo_weapon=Slotthree_weapon=Slotfour_weapon=Slotfive_weapon=Slotone_weapon=Slotone_Rarity=Slotone_Attachment=Slottwo_weapon=Slottwo_Rarity=Slottwo_Attachment=Slotthree_Weapon=Slotthree_Rarity=Slotthree_Attachment=Slotfour_Weapon=Slotfour_Rarity=Slotfour_Attachment=Slotfive_weapon=Slotfive_Rarity=Slotfive_Attachment=Slotone_Rarity_Gen=Slottwo_Rarity_Gen=Slotthree_Rarity_Gen=Slotfour_Rarity_Gen=Slotfive_Rarity_Gen=Slotone_Mythic=Slottwo_Mythic=Slotthree_Mythic=Slotfour_Mythic=Slotfive_Mythic=Slottwo_weapon_selected=Slotthree_weapon_selected=Slotfour_weapon_selected=Slotfive_weapon_selected=Medallion=slotone_attachment=slottwo_attachment=slotthree_attachment=slotfour_attachment=slotfive_attachment=None
slotoneattachment1 = slotoneattachment2 = slotoneattachment3 = slotoneattachment4 = slottwoattachment1 = slottwoattachment2 = slottwoattachment3 = slottwoattachment4 = slotthreeattachment1 = slotthreeattachment2 = slotthreeattachment3 = slotthreeattachment4 = slotfourattachment1 = slotfourattachment2 = slotfourattachment3 = slotfourattachment4 = slotfiveattachment1 = slotfiveattachment2 = slotfiveattachment3 = slotfiveattachment4 ='Disabled'
slotone_allowed=slottwo_allowed=slotthree_allowed=slotfour_allowed=slotfive_allowed='None', 'None'
hammer_pump_options = (('None', 'Red Eye Sight', 'Holo-13 Optic'), ('None', 'Speed Mag',), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake'))
frenzy_auto_options = (('None', 'Red Eye Sight', 'Holo-13 Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake'))
assault_rifle_options = (('None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake'))
thunder_burst_options = (('None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake'))
ranger_pistol_options = (('None', 'Red Eye Sight', 'Holo-13 Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Laser'), ('None', 'Suppressor', 'Muzzle Brake'))
reaper_sniper_options = (('None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Optic'), ('None', 'Speed Mag', 'Drum Mag'), ('None', 'Vertical Foregrip', 'Angled Foregrip'), ('None', 'Suppressor', 'Muzzle Brake'))
nothing_options=((), (), (), ())
rarity_picker=['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary']
rarity_picker_mythic=['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic']
rarity_picker_sniper=['Uncommon', 'Rare', 'Epic', 'Legendary']
weapons = {'Shotgun': ['Hammer Pump Shotgun', 'Frenzy Auto Shotgun'], 'SMG': ['Thunder Burst SMG', 'Hyper SMG', 'Ranger Pistol'], 'Assault-Rifle': ['Striker AR', 'Nemesis AR', 'Enforcer AR'], 'Sniper': ['Reaper Sniper Rifle'], 'Other': ['Grapple Blade', 'Ballistic Shield'], 'Health': ['Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit']}
weapon_options = {'Hammer Pump Shotgun': hammer_pump_options, 'Frenzy Auto Shotgun': frenzy_auto_options, 'Striker AR': assault_rifle_options, 'Nemesis AR': assault_rifle_options, 'Enforcer AR': assault_rifle_options, 'Thunder Burst SMG': thunder_burst_options, 'Hyper SMG': thunder_burst_options, 'Ranger Pistol': ranger_pistol_options, 'Reaper Sniper Rifle': reaper_sniper_options}
weapon_rarity_options = {'Hammer Pump Shotgun': rarity_picker_mythic, 'Frenzy Auto Shotgun': rarity_picker_mythic, 'Striker AR': rarity_picker_mythic, 'Nemesis AR': rarity_picker_mythic, 'Enforcer AR': rarity_picker, 'Thunder Burst SMG': rarity_picker, 'Hyper SMG': rarity_picker_mythic, 'Ranger Pistol': rarity_picker, 'Reaper Sniper Rifle': rarity_picker_sniper}
Medallions=['Valeria\'s Medallion', 'Montague\'s Medallion', 'Nisha\'s Medallion', 'Oscar\'s Medallion', 'Peter Griffin\'s Medallion']

def Weapon_Slot(slot_name, slot_number):
    selected_weapon=None
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current slot: {slot_name}', help=f"Shows current slot for {slot_name}", divider='rainbow')
    with col2: slot = st.selectbox(f'Item type', ('Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'Other', 'Health'), help=f'Weapon type for slot {slot_number}')
    with col3: slot_allowed = st.multiselect('Allowed Weapons', weapons.get(slot, []), weapons.get(slot, []), help=f'Allowed items for item type ({slot_name}).')
    if slot_allowed: selected_weapon=random.choice(slot_allowed)
    with col4:
        if slot not in ['Disabled', 'Other', 'Health'] and selected_weapon!=None: slot_rarity_allowed = st.multiselect('Allowed rarity', weapon_rarity_options.get(selected_weapon, []), weapon_rarity_options.get(selected_weapon, []), help=f'Allowed raritys for slot {slot_number}')
        else: slot_rarity_allowed = st.multiselect('Allowed rarity', (), help=f'Allowed raritys for slot {slot_number}')
        if slot_rarity_allowed and slot !='Disabled' and slot_allowed: Slot_Rarity = random.choice(slot_rarity_allowed)
        else: Slot_Rarity=None
        selected_weapon = {'Hammer Pump Shotgun': 'Peter Griffin\'s Hammer Pump Shotgun', 'Frenzy Auto Shotgun': 'Oscar\'s Frenzy Auto Shotgun', 'Striker AR': 'Nisha\'s Striker AR', 'Nemesis AR': 'Montague\'s Nemesis AR', 'Hyper SMG': 'Valeria\'s Hyper SMG'}.get(selected_weapon, selected_weapon) if Slot_Rarity == 'Mythic' else selected_weapon
    with col5:
        if slot not in ['Disabled', 'Other', 'Health'] and slot_allowed!=None: slot_attachment = st.selectbox('Weapon attachments', ('Enabled', 'Disabled'), help=f'Weapon attachments for slot {slot_number}')
        elif slot_allowed=='[]': slot_attachment = st.selectbox('Weapon attachments', (), help=f'Weapon attachments for slot {slot_number}')
        else: slot_attachment = st.selectbox('Weapon attachments', (), help=f'Weapon attachments for slot {slot_number}')
    st.divider()
    return slot, slot_allowed, Slot_Rarity, slot_attachment, selected_weapon

def AttachmentViewer(slot_name, slot_number, weapon_name, optic_options, magazine_options, underbarrel_options, barrel_options, *attachments):
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current item: {weapon_name}', help=f"Shows current weapon for slot {slot_number}", divider='rainbow')
    with col2: attachment1 = st.multiselect('Optic', optic_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Increases hipfire accuracy. ({slot_name})")
    with col3: attachment2 = st.multiselect('Magazine', magazine_options, help=f"**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed. ({slot_name})")
    with col4: attachment3 = st.multiselect('Underbarrel', underbarrel_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Increases hipfire accuracy. ({slot_name})")
    with col5: attachment4 = st.multiselect('Barrel', barrel_options, help=f"**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil. ({slot_name})")
    st.divider() 
    attachment1=random.choice(attachment1) if attachment1 else 'None'
    attachment2=random.choice(attachment2) if attachment2 else 'None'
    attachment3=random.choice(attachment3) if attachment3 else 'None'
    attachment4=random.choice(attachment4) if attachment4 else 'None'
    return attachment1, attachment2, attachment3, attachment4

Customize, Weapon_mods, Loadout, Weapon_Info = st.tabs(["Customize", "Weapon Mods", "Loadout", "Weapon Info"])

with Customize:
    slotone, slotone_allowed, Slotone_Rarity, slotone_attachment, Slotone_weapon = Weapon_Slot("Slot 1", "1")
    slottwo, slottwo_allowed, Slottwo_Rarity, slottwo_attachment, Slottwo_weapon = Weapon_Slot("Slot 2", "2")
    slotthree, slotthree_allowed, Slotthree_Rarity, slotthree_attachment, Slotthree_weapon = Weapon_Slot("Slot 3", "3")
    slotfour, slotfour_allowed, Slotfour_Rarity, slotfour_attachment, Slotfour_weapon = Weapon_Slot("Slot 4", "4")
    slotfive, slotfive_allowed, Slotfive_Rarity, slotfive_attachment, Slotfive_weapon = Weapon_Slot("Slot 5", "5")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Medallions', divider='rainbow')
    with col2: slotsix = st.selectbox('Medallions', ('Disabled', 'Enabled'))
    if slotsix == 'Enabled':
        with col3: medallions_amount = st.selectbox('Amount of medallions', [1, 2, 3, 4, 5], help='Example, if selected 5, it will select 1-5 medallions from a random list.')
        with col4: slotsix_randomness = st.selectbox('Randomnmess', ['Enabled', 'Disabled'], help='If enabled it will randomly select from (lets say you selected 5) 1-5 medallions, else will pick 5 medallions')
    else:
        with col3: medallions_amount = st.selectbox('Amount of medallions', [], help='Example, if selected 5, it will select 1-5 medallions from a random list.')
        with col4: slotsix_randomness = st.selectbox('Randomnmess', [], help='If enabled it will randomly select from (lets say you selected 5) 1-5 medallions, else will pick 5 medallions')
    Medallion = ', '.join(random.sample(Medallions, k=random.randint(1, medallions_amount))) if slotsix == 'Enabled' and slotsix_randomness != 'Disabled' else ', '.join(random.sample(Medallions, k=int(medallions_amount))) if slotsix == 'Enabled' and slotsix_randomness == 'Disabled' else None
    if not medallions_amount: medallions_amount_text='0'
    elif slotsix_randomness=='Disabled' and medallions_amount: medallions_amount_text=medallions_amount
    else: medallions_amount_text=f'1-{medallions_amount}'
    if slotsix == 'Enabled' and medallions_amount: selected_meddalions_amount = len(Medallion.split(', '))
    else: selected_meddalions_amount='0'
    #print(f'Slotone: {slotone}\n    {slotone_allowed}\n    {slotone_attachment}\n    {Slotone_weapon}\n Slottwo: {slottwo}\n    {slottwo_allowed}\n    {slottwo_attachment}\n    {Slottwo_weapon}\n Slotthree: {slotthree}\n    {slotthree_allowed}\n    {slotthree_attachment}\n    {Slotthree_weapon}\n Slotfour: {slotfour}\n    {slotfour_allowed}\n    {slotfour_attachment}\n    {Slotfour_weapon}\n Slotfive: {slotfive}\n    {slotfive_allowed}\n    {slotfive_attachment}\n    {Slotfive_weapon}')
with Weapon_mods:
    if Slotone_weapon in weapon_options and slotone_attachment!='Disabled': slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4 = AttachmentViewer("Slot 1", "1", Slotone_weapon, *weapon_options[Slotone_weapon])
    elif slotone in ('Disabled', 'Other', 'Health') or slotone_attachment=='Disabled': slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4 = AttachmentViewer("Slot 1", "1", Slotone_weapon, *nothing_options)
    else: slotoneattachment1 = slotoneattachment2 = slotoneattachment3 = slotoneattachment4 = 'Disabled'
    if Slottwo_weapon in weapon_options and slottwo_attachment!='Disabled': slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4 = AttachmentViewer("Slot 2", "2", Slottwo_weapon, *weapon_options[Slottwo_weapon])
    elif slottwo in ('Disabled', 'Other', 'Health') or slottwo_attachment=='Disabled': slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4 = AttachmentViewer("Slot 2", "2", Slottwo_weapon, *nothing_options)
    else: slottwoattachment1 = slottwoattachment2 = slottwoattachment3 = slottwoattachment4 = 'Disabled'
    if Slotthree_weapon in weapon_options and slotthree_attachment!='Disabled': slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4 = AttachmentViewer("Slot 3", "3", Slotthree_weapon, *weapon_options[Slotthree_weapon])
    elif slotthree in ('Disabled', 'Other', 'Health') or slotthree_attachment=='Disabled': slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4 = AttachmentViewer("Slot 3", "3", Slotthree_weapon, *nothing_options)
    else: slotthreeattachment1 = slotthreeattachment2 = slotthreeattachment3 = slotthreeattachment4 = 'Disabled'
    if Slotfour_weapon in weapon_options and slotfour_attachment!='Disabled': slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4 = AttachmentViewer("Slot 4", "4", Slotfour_weapon, *weapon_options[Slotfour_weapon])
    elif slotfour in ('Disabled', 'Other', 'Health') or slotfour_attachment=='Disabled': slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4 = AttachmentViewer("Slot 4", "4", Slotfour_weapon, *nothing_options)
    else: slotfourattachment1 = slotfourattachment2 = slotfourattachment3 = slotfourattachment4 = 'Disabled'
    if Slotfive_weapon in weapon_options and slotfive_attachment!='Disabled': slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4 = AttachmentViewer("Slot 5", "5", Slotfive_weapon, *weapon_options[Slotfive_weapon])
    elif slotfive in ('Disabled', 'Other', 'Health') or slotfive_attachment=='Disabled': slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4 = AttachmentViewer("Slot 5", "5", Slotfive_weapon, *nothing_options)
    else: slotfiveattachment1 = slotfiveattachment2 = slotfiveattachment3 = slotfiveattachment4 = 'Disabled'
with Loadout:
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
            tt1.write(f'# Rarity\n    Slot 1 : {Slotone_Rarity}\n    Slot 2 : {Slottwo_Rarity}\n    Slot 3 : {Slotthree_Rarity}\n    Slot 4 : {Slotfour_Rarity}\n    Slot 5 : {Slotfive_Rarity}\n    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})')
        with taba2:
            tt2 = st.empty()
            tt2.write(f'# Rarity  \n##### Slot 1 : {Slotone_Rarity}\n#####    Slot 2 : {Slottwo_Rarity}\n#####    Slot 3 : {Slotthree_Rarity}\n#####    Slot 4 : {Slotfour_Rarity}\n#####    Slot 5 : {Slotfive_Rarity}\n#####    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})')
        with taba3:
            tt3 = st.empty()
            tt3.json({'Rarity': [f'Slot 1 : {Slotone_Rarity}', f'Slot 2 : {Slottwo_Rarity}', f'Slot 3 : {Slotthree_Rarity}', f'Slot 4 : {Slotfour_Rarity}', f'Slot 5 : {Slotfive_Rarity}', f'Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount}'], })
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
    st.button('Randomize loadout')
    st.divider()

    if st.button('Save Config'):
        if os.path.exists(f"{File_Path}.txt"): os.remove(f"{File_Path}.txt")
        f = open(f"{File_Path}.txt", "a")
        f.write(f'{Slotone_weapon}\n{Slottwo_weapon}\n{Slotthree_weapon}\n{Slotfour_weapon}\n{Slotfive_weapon}\n{Slotone_Rarity}\n{Slottwo_Rarity}\n{Slotthree_Rarity}\n{Slotfour_Rarity}\n{Slotfive_Rarity}\n{slotoneattachment1}\n{slotoneattachment2}\n{slotoneattachment3}\n{slotoneattachment4}\n{slottwoattachment1}\n{slottwoattachment2}\n{slottwoattachment3}\n{slottwoattachment4}\n{slotthreeattachment1}\n{slotthreeattachment2}\n{slotthreeattachment3}\n{slotthreeattachment4}\n{slotfourattachment1}\n{slotfourattachment2}\n{slotfourattachment3}\n{slotfourattachment4}\n{slotfiveattachment1}\n{slotfiveattachment2}\n{slotfiveattachment3}\n{slotfiveattachment4}\n{Medallion}\n{medallions_amount_text}\n{selected_meddalions_amount}')
        st.success(f'Saved config to file \'{File_Path}.txt\'', icon="✅")
        f.close()

    if st.button('Load Config'):
        if os.path.exists(f"{File_Path}.txt"): 
            with open(f'{File_Path}.txt', "r") as file: lines = [line.strip() for line in file.readlines()]
            if len(lines) == 33: 
                (Slotone_weapon, Slottwo_weapon, Slotthree_weapon, Slotfour_weapon, Slotfive_weapon, Slotone_Rarity, Slottwo_Rarity, Slotthree_Rarity, Slotfour_Rarity, Slotfive_Rarity, slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4, slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4, slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4, slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4, slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4, Medallion, medallions_amount_text, selected_meddalions_amount) = lines
                t1.write(f'# Weapons\n    Slot 1 : {Slotone_weapon}\n    Slot 2 : {Slottwo_weapon}\n    Slot 3 : {Slotthree_weapon}\n    Slot 4 : {Slotfour_weapon}\n    Slot 5 : {Slotfive_weapon}\n    Medallions : {Medallion}')
                t2.write(f'# Weapons  \n##### Slot 1 : {Slotone_weapon}\n#####    Slot 2 : {Slottwo_weapon}\n#####    Slot 3 : {Slotthree_weapon}\n#####    Slot 4 : {Slotfour_weapon}\n#####    Slot 5 : {Slotfive_weapon}')
                t3.json({'Weapons': [f'Slot 1 : {Slotone_weapon}', f'Slot 2 : {Slottwo_weapon}', f'Slot 3 : {Slotthree_weapon}', f'Slot 4 : {Slotfour_weapon}', f'Slot 5 : {Slotfive_weapon}'], })
                tt1.write(f'# Rarity\n    Slot 1 : {Slotone_Rarity}\n    Slot 2 : {Slottwo_Rarity}\n    Slot 3 : {Slotthree_Rarity}\n    Slot 4 : {Slotfour_Rarity}\n    Slot 5 : {Slotfive_Rarity}\n    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})')
                tt2.write(f'# Rarity  \n##### Slot 1 : {Slotone_Rarity}\n#####    Slot 2 : {Slottwo_Rarity}\n#####    Slot 3 : {Slotthree_Rarity}\n#####    Slot 4 : {Slotfour_Rarity}\n#####    Slot 5 : {Slotfive_Rarity}\n#####    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})')
                tt3.json({'Rarity': [f'Slot 1 : {Slotone_Rarity}', f'Slot 2 : {Slottwo_Rarity}', f'Slot 3 : {Slotthree_Rarity}', f'Slot 4 : {Slotfour_Rarity}', f'Slot 5 : {Slotfive_Rarity}', f'Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount}'], })
                ttt1.write(f'# Attachments\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
                ttt2.write(f'# Attachments  \n##### Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n#####    Slot 2 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n#####    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n#####    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n#####    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
                ttt3.json({'Attachments': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}'], })
                st.success(f"Loaded configuration from \'{File_Path}.txt\'", icon="✅")
            else: st.error(f"Invalid configuration file. Expected 33 lines. Called back: {len(lines)} line(s)")
        else: st.error("File doesn't exist. Please save a config and try again.")
with Weapon_Info:
    col1, col2 = st.columns(2)
    with col1: st.write(f'# The Hammer Pump Shotgun\n    Common: 59.5 DPS, 85 Damage, 0.7 Firerate, 5.78S reload speed\n    Uncommon: 62.3 DPS, 89 Damage, 0.7 Firerate, 5.51S reload speed\n    Rare: 65.8 DPS, 94 Damage, 0.7 Firerate, 5.25S reload speed\n    Epic: 69.3 DPS, 99 Damage, 0.7 Firerate, 4.99S reload speed\n    Legendary: 72.1 DPS, 103 Damage, 0.7 Firerate, 4.73S reload speed\n    Mythic: 75.6 DPS, 108 Damage, 0.7 Firerate, 4.46S reload speed')
    with col2: st.write(f'# The Frenzy Auto Shotgun\n    Common: 152.5 DPS, 61 Damage, 2.5 Firerate, 5.17S reload speed\n    Uncommon: 162.5 DPS, 65 Damage, 2.5 Firerate, 4.94S reload speed\n    Rare: 170 DPS, 68 Damage, 2.5 Firerate, 4.7S reload speed\n    Epic: 177.5 DPS, 71 Damage, 2.5 Firerate, 4.47S reload speed\n    Legendary: 187.5 DPS, 75 Damage, 2.5 Firerate, 4.23S reload speed\n    Mythic: 195 DPS, 78 Damage, 2.5 Firerate, 4S reload speed')
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1: st.write(f'# The Striker AR\n    Common: 194.4 DPS, 24 Damage, 8.1 Firerate, 3.52S reload speed\n    Uncommon: 210.6 DPS, 26 Damage, 8.1 Firerate, 3.36S reload speed\n    Rare: 218.7 DPS, 27 Damage, 8.1 Firerate, 3.2S reload speed\n    Epic: 226.8 DPS, 28 Damage, 8.1 Firerate, 3.04S reload speed\n    Legendary: 243 DPS, 30 Damage, 8.1 Firerate, 2.88S reload speed\n    Mythic: 251.1 DPS, 31 Damage, 8.1 Firerate, 2.72S reload speed')
    with col2: st.write(f'# The Nemesis AR\n    Common: 145 DPS, 29 Damage, 2.5 Firerate, 5.17S reload speed\n    Uncommon: 150 DPS, 30 Damage, 2.5 Firerate, 4.94S reload speed\n    Rare: 160 DPS, 32 Damage, 2.5 Firerate, 4.7S reload speed\n    Epic: 170 DPS, 34 Damage, 2.5 Firerate, 4.47S reload speed\n    Legendary: 175 DPS, 35 Damage, 2.5 Firerate, 4.23S reload speed')
    with col3: st.write(f'# The Enforcer AR\n    Common: 126.4 DPS, 32 Damage, 2.5 Firerate, 5.17S reload speed\n    Uncommon: 162.5 DPS, 65 Damage, 2.5 Firerate, 4.94S reload speed\n    Rare: 170 DPS, 68 Damage, 2.5 Firerate, 4.7S reload speed\n    Epic: 177.5 DPS, 71 Damage, 2.5 Firerate, 4.47S reload speed\n    Legendary: 187.5 DPS, 75 Damage, 2.5 Firerate, 4.23S reload speed\n    Mythic: 185 DPS, 78 Damage, 2.5 Firerate, 4S reload speed')
with st.sidebar:
    st.link_button("Github", "https://github.com/fuzzybuzzyboy/py")
    st.link_button("Discord", "https://discord.gg/HVEGufPNnF")
    if st.button('Clock'):
        with st.empty():
            while True:
                time_now1, time_now = datetime.now().strftime("%D"), datetime.now().strftime("%H:%M:%S")
                st.write(f'# Clock\n    Time : {time_now}\n    Date : {time_now1}')
                time.sleep(1)
