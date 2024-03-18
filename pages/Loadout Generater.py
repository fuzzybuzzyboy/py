from datetime import datetime
import random, time, os, streamlit as st

st.set_page_config(page_title='Loadout Generater', page_icon="🤑", layout="wide", initial_sidebar_state="expanded", menu_items={'Get help': 'https://github.com/fuzzybuzzyboy/py', 'Report a bug': "https://github.com/fuzzybuzzyboy/py", 'About': "Random items generator for fortnite (no this doesn't inject into your game and do something blah blah blah)"})

File_Path = os.path.join('configs', 'Loadout_generator_config')
medallions_amount=0
medallions_amount_text='1-'
slotoneattachment1=slotoneattachment2=slotoneattachment3=slotoneattachment4=slottwoattachment1=slottwoattachment2=slottwoattachment3=slottwoattachment4=slotthreeattachment1=slotthreeattachment2=slotthreeattachment3=slotthreeattachment4=slotfourattachment1=slotfourattachment2=slotfourattachment3=slotfourattachment4=slotfiveattachment1=slotfiveattachment2=slotfiveattachment3=slotfiveattachment4=None
slottwo=slottwo_rarity=slottwo_weapon=slotthree=slotthree_rarity=slotthree_weapon=slotfour=slotfour_rarity=slotfour_weapon=slotfive=slotfive_rarity=slotfive_weapon='Disabled'

item_types=['Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'DMR', 'Other', 'Health']
items = {'Shotgun': ['Hammer Pump Shotgun', 'Frenzy Auto Shotgun', 'Gatekeeper Shotgun', 'Cerberus\' Gatekeeper Shotgun'], 'SMG': ['Thunder Burst SMG', 'Harbinger SMG', 'Hades\' Harbinger SMG'], 'Pistol': ['Ranger Pistol',], 'Assault-Rifle': ['Warforged Assault Rifle', 'Ares\' Warforged Assault Rifle', 'Nemesis AR'], 'Sniper': ['Reaper Sniper Rifle'], 'DMR': ['Huntress DMR', 'Zeus\' Huntress DMR'], 'Other': ['Thunderbolt of Zeus', 'Cluster Clinger', 'Wings Of Icarus', 'Shockwave Grenade'], 'Health': ['Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit']}
item_raritys = {'Hammer Pump Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Frenzy Auto Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Gatekeeper Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Cerberus\' Gatekeeper Shotgun': ['Mythic',], 'Thunder Burst SMG': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Harbinger SMG': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Hades\' Harbinger SMG': ['Mythic'], 'Ranger Pistol': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Warforged Assault Rifle': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Ares\' Warforged Assault Rifle': ['Mythic'], 'Nemesis AR': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Reaper Sniper Rifle': ['Uncommon', 'Rare', 'Epic', 'Legendary'], 'Huntress DMR': ['Uncommon', 'Rare', 'Epic', 'Legendary'], 'Zeus\' Huntress DMR': ['Mythic',], 'Cluster Clinger': ['Uncommon',], 'Thunderbolt of Zeus': ['Mythic',], 'Wings Of Icarus': ['Epic',], 'Shockwave Grenade': ['Epic',], 'Shield Potion': ['Rare',], 'Flowberry Fizz': ['Rare',], 'Small Shield Potion': ['Uncommon',], 'Medkit': ['Uncommon',], 'Flowberry': ['Uncommmon',]}
weapon_attachments = {'Hammer Pump Shotgun': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Frenzy Auto Shotgun': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Gatekeeper Shotgun': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake']], 'Thunder Burst SMG': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Harbinger SMG': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Ranger Pistol': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Laser'], ['None', 'Muzzle Brake', 'Suppressor']], 'Warforged Assault Rifle': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Nemesis AR': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Reaper Sniper Rifle': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Nemesis AR': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Huntress DMR': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Speed Foregrip'], ['None', ]], 'Cerberus\' Gatekeeper Shotgun': [['None', ], ['Speed Mag', ], ['Speed Foregrip', ], ['Muzzle Brake', ]], 'Hades\' Harbinger SMG': [['Red Eye Sight',], ['Speed Mag',], ['Vertical Foregrip',], ['Muzzle Brake']], 'Ares\' Warforged Assault Rifle': [['Red Eye Sight',], ['Drum Mag',], ['Speed Foregrip',], ['Muzzle Brake',]], 'Zeus\' Huntress DMR': [['Sniper Optic',], ['Speed Mag',], ['Angled Foregrip'], ['Muzzle Brake',]],'Cluster Clinger': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Thunderbolt of Zeus': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Wings Of Icarus': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Shockwave Grenade': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Shield Potion': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Flowberry Fizz': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Small Shield Potion': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Medkit': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Flowberry': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]]}

Medallions=('Zeus\'s Medallion', 'Ares\'s Medallion', 'Cerberus\'s Medallion', 'Hades\'s Medallion')
def Weapon_Slot(slot_name, slot_number):
    selected_weapon=None
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: {slot_name}', divider='rainbow')
    with col2: slot = st.selectbox(f'Item type', (item_types), help=f'Weapon type for slot {slot_number}')
    with col3: slot_allowed = st.multiselect('Allowed Weapons', items.get(slot, []), items.get(slot, []), help=f'Allowed items for item type ({slot_name}).')
    if slot_allowed: selected_weapon=random.choice(slot_allowed)
    with col4:
        if slot not in ['Disabled', 'Other', 'Health'] and selected_weapon!=None: slot_rarity_allowed = st.multiselect('Allowed rarity', item_raritys.get(selected_weapon, []), item_raritys.get(selected_weapon, []), help=f'Allowed raritys for slot {slot_number}')
        else: slot_rarity_allowed = st.multiselect('Allowed rarity', (), help=f'Allowed raritys for slot {slot_number}')
        if slot_rarity_allowed and slot !='Disabled' and slot_allowed: Slot_Rarity = random.choice(slot_rarity_allowed)
        else: Slot_Rarity=None
        selected_weapon = {'Hammer Pump Shotgun': 'Peter Griffin\'s Hammer Pump Shotgun', 'Frenzy Auto Shotgun': 'Oscar\'s Frenzy Auto Shotgun', 'Warforged Assault Rifle': 'Ares\' Warforged Assault Rifle', 'Nemesis AR': 'Montague\'s Nemesis AR', 'Harbinger SMG': 'Valeria\'s Harbinger SMG'}.get(selected_weapon, selected_weapon) if Slot_Rarity == 'Mythic' else selected_weapon
    st.divider()
    return slot, Slot_Rarity, selected_weapon

def AttachmentViewer(rarity, slot_name, slot_number, weapon_name, optic_options, magazine_options, underbarrel_options, barrel_options, *attachments):
    st.title(slot_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current item: {weapon_name}', help=f"Shows current weapon for slot {slot_number} (Auto selects attachments for mythic rarity weapons, doesn't keep old settings.)", divider='rainbow')
    with col2: attachment1 = st.multiselect('Optic', optic_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Increases hipfire accuracy. ({slot_name})")
    with col3: attachment2 = st.multiselect('Magazine', magazine_options, help=f"**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed. ({slot_name})")
    with col4: attachment3 = st.multiselect('Underbarrel', underbarrel_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Increases hipfire accuracy. ({slot_name})")
    with col5: attachment4 = st.multiselect('Barrel', barrel_options, help=f"**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil. ({slot_name})")
    st.divider() 
    if rarity == 'Mythic': pass
    else: attachment1, attachment2, attachment3, attachment4=random.choice(attachment1) if attachment1 else None, random.choice(attachment2) if attachment2 else None, random.choice(attachment3) if attachment3 else None, random.choice(attachment4) if attachment4 else None
    return attachment1, attachment2, attachment3, attachment4

Customize, Weapon_mods, Loadout, Weapon_Info = st.tabs(["Customize", "Weapon Mods", "Loadout", "Weapon Info"])
with Customize:
    slotone, slotone_rarity, slotone_weapon = Weapon_Slot("Slot 1", "1")
    slottwo, slottwo_rarity, slottwo_weapon = Weapon_Slot("Slot 2", "2")
    slotthree, slotthree_rarity, slotthree_weapon = Weapon_Slot("Slot 3", "3")
    slotfour, slotfour_rarity, slotfour_weapon = Weapon_Slot("Slot 4", "4")
    slotfive, slotfive_rarity, slotfive_weapon = Weapon_Slot("Slot 5", "5")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Medallions', divider='rainbow')
    with col2: slotsix = st.selectbox('Medallions', ('Disabled', 'Enabled'))
    with col3: medallions_amount = st.selectbox('Amount of medallions', [1, 2, 3, 4], help=f'Example, if selected {len(Medallions)}, it will select 1-{len(Medallions)} medallions from a random list.') if slotsix == 'Enabled' else st.selectbox('Amount of medallions', [], help='Example, if selected 5, it will select 1-5 medallions from a random list.')
    with col4: slotsix_randomness = st.selectbox('Randomness', ['Enabled', 'Disabled'], help=f'If enabled it will randomly select from (lets say you selected {len(Medallions)}) 1-{len(Medallions)} medallions, else will pick {len(Medallions)} medallions') if slotsix == 'Enabled' else st.selectbox('Randomness', [], help='If enabled it will randomly select from (lets say you selected 5) 1-5 medallions, else will pick 5 medallions')
    Medallion = ', '.join(random.sample(Medallions, k=random.randint(1, medallions_amount))) if slotsix == 'Enabled' and slotsix_randomness != 'Disabled' else ', '.join(random.sample(Medallions, k=int(medallions_amount))) if slotsix == 'Enabled' and slotsix_randomness == 'Disabled' else 'Disabled'
    if not medallions_amount: medallions_amount_text='0'
    elif slotsix_randomness=='Disabled' and medallions_amount: medallions_amount_text=medallions_amount
    else: medallions_amount_text=f'1-{medallions_amount}'
    if slotsix == 'Enabled' and medallions_amount: selected_meddalions_amount = len(Medallion.split(', '))
    else: selected_meddalions_amount='0'
with Weapon_mods:
    if slotone_weapon: slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4 = AttachmentViewer(slotone_rarity, "Slot 1", "1", slotone_weapon, *weapon_attachments.get(slotone_weapon, []))
    elif slotone in ('Disabled', 'Other', 'Health') or slotone_rarity=='Mythic': slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4 = AttachmentViewer(slotone_rarity, "Slot 1", "1", slotone_weapon, *[[], [], [], []])
    if slottwo_weapon: slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4 = AttachmentViewer(slottwo_rarity, "Slot 2", "2", slottwo_weapon, *weapon_attachments.get(slotone_weapon, []))
    elif slottwo in ('Disabled', 'Other', 'Health') or slottwo_rarity=='Mythic': slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4 = AttachmentViewer(slottwo_rarity, "Slot 2", "2", slottwo_weapon, *[[], [], [], []])
    if slotthree_weapon: slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4 = AttachmentViewer(slotthree_rarity, "Slot 3", "3", slotthree_weapon, *weapon_attachments.get(slotone_weapon, []))
    elif slotthree in ('Disabled', 'Other', 'Health') or slotthree_rarity=='Mythic': slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4 = AttachmentViewer(slotthree_rarity, "Slot 3", "3", slotthree_weapon, *[[], [], [], []])
    if slotfour_weapon: slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4 = AttachmentViewer(slotfour_rarity, "Slot 4", "4", slotfour_weapon, *weapon_attachments.get(slotone_weapon, []))
    elif slotfour in ('Disabled', 'Other', 'Health') or slotfour_rarity=='Mythic': slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4 = AttachmentViewer(slotfour_rarity, "Slot 4", "4", slotfour_weapon, *[[], [], [], []])
    if slotfive_weapon: slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4 = AttachmentViewer(slotfive_rarity, "Slot 5", "5", slotfive_weapon, *weapon_attachments.get(slotone_weapon, []))
    elif slotfive in ('Disabled', 'Other', 'Health') or slotfive_rarity=='Mythic': slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4 = AttachmentViewer(slotfive_rarity, "Slot 5", "5", slotfive_weapon, *[[], [], [], []])
with Loadout:
    col1, col2, col3 = st.columns(3)
    with col1:
        tab1b, tab2b, tab3b = st.tabs(["Base", "Regular", "Json"])
        with tab1b:
            t1 = st.empty()
            t1.write(f'# Items\n    Slot 1 : {slotone_weapon}\n    Slot 2 : {slottwo_weapon}\n    Slot 3 : {slotthree_weapon}\n    Slot 4 : {slotfour_weapon}\n    Slot 5 : {slotfive_weapon}\n    Medallions : {Medallion}')
        with tab2b:
            t2 = st.empty()
            t2.write(f'# Items  \n##### Slot 1 : {slotone_weapon}\n#####    Slot 2 : {slottwo_weapon}\n#####    Slot 3 : {slotthree_weapon}\n#####    Slot 4 : {slotfour_weapon}\n#####    Slot 5 : {slotfive_weapon}')
        with tab3b:
            t3 = st.empty()
            t3.json({'Items': [f'Slot 1 : {slotone_weapon}', f'Slot 2 : {slottwo_weapon}', f'Slot 3 : {slotthree_weapon}', f'Slot 4 : {slotfour_weapon}', f'Slot 5 : {slotfive_weapon}'], })
    with col2:
        taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])
        with taba1:
            tt1 = st.empty()
            tt1.write(f'# Rarity\n    Slot 1 : {slotone_rarity}\n    Slot 2 : {slottwo_rarity}\n    Slot 3 : {slotthree_rarity}\n    Slot 4 : {slotfour_rarity}\n    Slot 5 : {slotfive_rarity}\n    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})')
        with taba2:
            tt2 = st.empty()
            tt2.write(f'# Rarity  \n##### Slot 1 : {slotone_rarity}\n#####    Slot 2 : {slottwo_rarity}\n#####    Slot 3 : {slotthree_rarity}\n#####    Slot 4 : {slotfour_rarity}\n#####    Slot 5 : {slotfive_rarity}\n#####    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})')
        with taba3:
            tt3 = st.empty()
            tt3.json({'Rarity': [f'Slot 1 : {slotone_rarity}', f'Slot 2 : {slottwo_rarity}', f'Slot 3 : {slotthree_rarity}', f'Slot 4 : {slotfour_rarity}', f'Slot 5 : {slotfive_rarity}', f'Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount}'], })
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
        f.write(f'{slotone_weapon}\n{slottwo_weapon}\n{slotthree_weapon}\n{slotfour_weapon}\n{slotfive_weapon}\n{slotone_rarity}\n{slottwo_rarity}\n{slotthree_rarity}\n{slotfour_rarity}\n{slotfive_rarity}\n{slotoneattachment1}\n{slotoneattachment2}\n{slotoneattachment3}\n{slotoneattachment4}\n{slottwoattachment1}\n{slottwoattachment2}\n{slottwoattachment3}\n{slottwoattachment4}\n{slotthreeattachment1}\n{slotthreeattachment2}\n{slotthreeattachment3}\n{slotthreeattachment4}\n{slotfourattachment1}\n{slotfourattachment2}\n{slotfourattachment3}\n{slotfourattachment4}\n{slotfiveattachment1}\n{slotfiveattachment2}\n{slotfiveattachment3}\n{slotfiveattachment4}\n{Medallion}\n{medallions_amount_text}\n{selected_meddalions_amount}')
        st.success(f'Saved config to file \'{File_Path}.txt\'', icon="✅")
        f.close()

    if st.button('Load Config'):
        if os.path.exists(f"{File_Path}.txt"): 
            with open(f'{File_Path}.txt', "r") as file: lines = [line.strip() for line in file.readlines()]
            if len(lines) == 33: 
                (slotone_weapon, slottwo_weapon, slotthree_weapon, slotfour_weapon, slotfive_weapon, slotone_rarity, slottwo_rarity, slotthree_rarity, slotfour_rarity, slotfive_rarity, slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4, slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4, slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4, slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4, slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4, Medallion, medallions_amount_text, selected_meddalions_amount) = lines
                t1.write(f'# Items\n    Slot 1 : {slotone_weapon}\n    Slot 2 : {slottwo_weapon}\n    Slot 3 : {slotthree_weapon}\n    Slot 4 : {slotfour_weapon}\n    Slot 5 : {slotfive_weapon}\n    Medallions : {Medallion}')
                t2.write(f'# Items  \n##### Slot 1 : {slotone_weapon}\n#####    Slot 2 : {slottwo_weapon}\n#####    Slot 3 : {slotthree_weapon}\n#####    Slot 4 : {slotfour_weapon}\n#####    Slot 5 : {slotfive_weapon}')
                t3.json({'Items': [f'Slot 1 : {slotone_weapon}', f'Slot 2 : {slottwo_weapon}', f'Slot 3 : {slotthree_weapon}', f'Slot 4 : {slotfour_weapon}', f'Slot 5 : {slotfive_weapon}'], })
                tt1.write(f'# Rarity\n    Slot 1 : {slotone_rarity}\n    Slot 2 : {slottwo_rarity}\n    Slot 3 : {slotthree_rarity}\n    Slot 4 : {slotfour_rarity}\n    Slot 5 : {slotfive_rarity}\n    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})')
                tt2.write(f'# Rarity  \n##### Slot 1 : {slotone_rarity}\n#####    Slot 2 : {slottwo_rarity}\n#####    Slot 3 : {slotthree_rarity}\n#####    Slot 4 : {slotfour_rarity}\n#####    Slot 5 : {slotfive_rarity}\n#####    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})')
                tt3.json({'Rarity': [f'Slot 1 : {slotone_rarity}', f'Slot 2 : {slottwo_rarity}', f'Slot 3 : {slotthree_rarity}', f'Slot 4 : {slotfour_rarity}', f'Slot 5 : {slotfive_rarity}', f'Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount}'], })
                ttt1.write(f'# Attachments\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
                ttt2.write(f'# Attachments  \n##### Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n#####    Slot 2 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n#####    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n#####    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n#####    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
                ttt3.json({'Attachments': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}'], })
                st.success(f"Loaded configuration from \'{File_Path}.txt\'", icon="✅")
            else: st.error(f"Invalid configuration file. Expected 33 lines. Called back: {len(lines)} line(s)")
        else: st.error("File doesn't exist. Please save a config and try again.")
with Weapon_Info:
    col1, col2 = st.columns(2)
    with col1: st.expander("Hammer Pump Shotgun", expanded=True).write("#\n    Common: 59.5 DPS, 85 Damage, 0.7 Firerate, 5.78S reload speed\n    Uncommon: 62.3 DPS, 89 Damage, 0.7 Firerate, 5.51S reload speed\n    Rare: 65.8 DPS, 94 Damage, 0.7 Firerate, 5.25S reload speed\n    Epic: 69.3 DPS, 99 Damage, 0.7 Firerate, 4.99S reload speed\n    Legendary: 72.1 DPS, 103 Damage, 0.7 Firerate, 4.73S reload speed\n    Mythic: 75.6 DPS, 108 Damage, 0.7 Firerate, 4.46S reload speed")
    with col2: st.expander('Frenzy Auto Shotgun', expanded=True).write("#\n    Common: 152.5 DPS, 61 Damage, 2.5 Firerate, 5.17S reload speed\n    Uncommon: 162.5 DPS, 65 Damage, 2.5 Firerate, 4.94S reload speed\n    Rare: 170 DPS, 68 Damage, 2.5 Firerate, 4.7S reload speed\n    Epic: 177.5 DPS, 71 Damage, 2.5 Firerate, 4.47S reload speed\n    Legendary: 187.5 DPS, 75 Damage, 2.5 Firerate, 4.23S reload speed\n    Mythic: 195 DPS, 78 Damage, 2.5 Firerate, 4S reload speed")
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1: st.expander("Warforged Assault Rifle", expanded=True).write(f'#\n    Common: 194.4 DPS, 24 Damage, 8.1 Firerate, 3.52S reload speed\n    Uncommon: 210.6 DPS, 26 Damage, 8.1 Firerate, 3.36S reload speed\n    Rare: 218.7 DPS, 27 Damage, 8.1 Firerate, 3.2S reload speed\n    Epic: 226.8 DPS, 28 Damage, 8.1 Firerate, 3.04S reload speed\n    Legendary: 243 DPS, 30 Damage, 8.1 Firerate, 2.88S reload speed\n    Mythic: 251.1 DPS, 31 Damage, 8.1 Firerate, 2.72S reload speed')
    with col2: st.expander("Nemesis AR", expanded=True).write(f'#\n    Common: 145 DPS, 29 Damage, 2.5 Firerate, 5.17S reload speed\n    Uncommon: 150 DPS, 30 Damage, 2.5 Firerate, 4.94S reload speed\n    Rare: 160 DPS, 32 Damage, 2.5 Firerate, 4.7S reload speed\n    Epic: 170 DPS, 34 Damage, 2.5 Firerate, 4.47S reload speed\n    Legendary: 175 DPS, 35 Damage, 2.5 Firerate, 4.23S reload speed')
    with col3: st.expander("Enforcer AR", expanded=True).write(f'#\n    Common: 126.4 DPS, 32 Damage, 2.5 Firerate, 5.17S reload speed\n    Uncommon: 162.5 DPS, 65 Damage, 2.5 Firerate, 4.94S reload speed\n    Rare: 170 DPS, 68 Damage, 2.5 Firerate, 4.7S reload speed\n    Epic: 177.5 DPS, 71 Damage, 2.5 Firerate, 4.47S reload speed\n    Legendary: 187.5 DPS, 75 Damage, 2.5 Firerate, 4.23S reload speed\n    Mythic: 185 DPS, 78 Damage, 2.5 Firerate, 4S reload speed')
    st.divider()
    col1, col2 = st.columns(2)
    with col1: st.expander('Thunder Burst SMG', expanded=True).write('#\n    Common: 84 DPS, 24 Damage, 3.5 Firerate, 2.48 Reload speed\n    Uncommon: 87.5 DPS, 25 Damage, 3.5 Firerate 2.36 Reload speed\n    Rare: 91 DPS, 26 Damage, 3.5 Firerate, 2.25 Reload speed\n    Epic: 98 DPS, 28 Damage, 3.5 Firerate, 2.14 Reload speed\n    Legendary: 101.5 DPS, 29 Damage, 3.5 Firerate, 2.03 Reload speed')
    with col2: st.expander('Harbinger SMG', expanded=True).write('#\n    Common: \n    Uncommon: \n    Rare: \n    Epic: \n    Legendary: \n    Mythic: ')
    st.divider()
    col1, col2 = st.columns(2)
    with col1: st.expander('Ranger Pistol', expanded=True).write('#\n    Common: \n    Uncommon: \n    Rare: \n    Epic: \n    Legendary: ')
    with col2: st.expander('Lock On Pistol', expanded=True).write('#\n    Common: \n    Uncommon: \n    Rare: \n    Epic: \n    Legendary: ')
with st.sidebar:
    st.page_link("http://www.Github.com/fuzzybuzzyboy/py", label="Github", icon="🛢️")
    st.page_link("https://discord.gg/HVEGufPNnF", label='Discord', icon='💻')
    if st.button('Clock'):
        with st.empty():
            while True:
                time_now1, time_now = datetime.now().strftime("%D"), datetime.now().strftime("%H:%M:%S")
                st.write(f'# Clock\n    Time : {time_now}\n    Date : {time_now1}')
                time.sleep(1)
