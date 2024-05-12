from datetime import datetime
import time, os, streamlit as st # type: ignore
from random import randint, sample, choice
st.set_page_config(page_title='Loadout Generater', page_icon="🤑", layout="wide", initial_sidebar_state="expanded", menu_items={'Get help': 'https://github.com/fuzzybuzzyboy/py', 'Report a bug': "https://github.com/fuzzybuzzyboy/py", 'About': "Random items generator for fortnite (no this doesn't inject into your game and do something blah blah blah)"})

medallions_amount, medallions_amount_text=0, '1-'
slotoneattachment1=slotoneattachment2=slotoneattachment3=slotoneattachment4=slottwoattachment1=slottwoattachment2=slottwoattachment3=slottwoattachment4=slotthreeattachment1=slotthreeattachment2=slotthreeattachment3=slotthreeattachment4=slotfourattachment1=slotfourattachment2=slotfourattachment3=slotfourattachment4=slotfiveattachment1=slotfiveattachment2=slotfiveattachment3=slotfiveattachment4=None
slottwo=slottwo_rarity=slottwo_weapon=slotthree=slotthree_rarity=slotthree_weapon=slotfour=slotfour_rarity=slotfour_weapon=slotfive=slotfive_rarity=slotfive_weapon='Disabled'

item_types=['Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'DMR', 'Other', 'Health']
items = {'Shotgun': ['Hammer Pump Shotgun', 'Frenzy Auto Shotgun', 'Gatekeeper Shotgun', 'Cerberus\' Gatekeeper Shotgun'], 'SMG': ['Thunder Burst SMG', 'Harbinger SMG', 'Hades\' Harbinger SMG'], 'Pistol': ['Ranger Pistol',], 'Assault-Rifle': ['Warforged Assault Rifle', 'Ares\' Warforged Assault Rifle', 'Nemesis AR'], 'Sniper': ['Reaper Sniper Rifle'], 'DMR': ['Huntress DMR', 'Zeus\' Huntress DMR'], 'Other': ['Thunderbolt of Zeus', 'Cluster Clinger', 'Wings Of Icarus', 'Shockwave Grenade'], 'Health': ['Flowberry Fizz', 'Flowberry', 'Shield Potion', 'Small Shield Potion', 'Medkit']}
item_raritys = {'Hammer Pump Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Frenzy Auto Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Gatekeeper Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Cerberus\' Gatekeeper Shotgun': ['Mythic',], 'Thunder Burst SMG': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Harbinger SMG': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Hades\' Harbinger SMG': ['Mythic'], 'Ranger Pistol': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Warforged Assault Rifle': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Ares\' Warforged Assault Rifle': ['Mythic'], 'Nemesis AR': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Reaper Sniper Rifle': ['Uncommon', 'Rare', 'Epic', 'Legendary'], 'Huntress DMR': ['Uncommon', 'Rare', 'Epic', 'Legendary'], 'Zeus\' Huntress DMR': ['Mythic',], 'Cluster Clinger': ['Uncommon',], 'Thunderbolt of Zeus': ['Mythic',], 'Wings Of Icarus': ['Epic',], 'Shockwave Grenade': ['Epic',], 'Shield Potion': ['Rare',], 'Flowberry Fizz': ['Rare',], 'Small Shield Potion': ['Uncommon',], 'Medkit': ['Uncommon',], 'Flowberry': ['Uncommmon',]}
weapon_attachments = {'Hammer Pump Shotgun': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Frenzy Auto Shotgun': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Gatekeeper Shotgun': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake']], 'Thunder Burst SMG': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Harbinger SMG': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Ranger Pistol': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Laser'], ['None', 'Muzzle Brake', 'Suppressor']], 'Warforged Assault Rifle': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Nemesis AR': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Reaper Sniper Rifle': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Nemesis AR': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Huntress DMR': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Speed Foregrip'], ['None', ]], 'Cerberus\' Gatekeeper Shotgun': [['None',], ['Speed Mag', ], ['Speed Foregrip', ], ['Muzzle Brake', ]], 'Hades\' Harbinger SMG': [['Red Eye Sight',], ['Speed Mag',], ['Vertical Foregrip',], ['Muzzle Brake']], 'Ares\' Warforged Assault Rifle': [['Red Eye Sight',], ['Drum Mag',], ['Speed Foregrip',], ['Muzzle Brake',]], 'Zeus\' Huntress DMR': [['Sniper Optic',], ['Speed Mag',], ['Angled Foregrip'], ['Muzzle Brake',]],'Cluster Clinger': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Thunderbolt of Zeus': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Wings Of Icarus': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Shockwave Grenade': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Shield Potion': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Flowberry Fizz': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Small Shield Potion': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Medkit': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Flowberry': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]]}
Medallions=('Zeus\'s Medallion', 'Ares\'s Medallion', 'Cerberus\'s Medallion', 'Hades\'s Medallion')
def Weapon_Slot(slot_name, slot_number):
    selected_weapon=None
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Current slot: :red[{slot_name}]', divider='rainbow')
    with col2: slot = st.selectbox(f'Item type', (item_types), help=f'Weapon type for :rainbow[slot {slot_number}]')
    with col3: slot_allowed = st.multiselect('Allowed items', items.get(slot, []), items.get(slot, []), help=f'Allowed items for item type (:rainbow[{slot_name}]).')
    if slot_allowed: selected_weapon=choice(slot_allowed)
    with col4: slot_rarity_allowed = st.multiselect('Allowed rarity', ["Common", 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'], help=f'If the weapon randomly selected doesn\'t have a valid rarity selected for it, it will randomly pick a rarity for the item, this will also happen if no rarity is selected. (Allowed raritys for :rainbow[slot {slot_number}].)') if slot not in ['Disabled', 'Other', 'Health'] and selected_weapon!=None else st.multiselect('Allowed rarity', (), help=f'If the weapon randomly selected doesn\'t have a valid rarity selected for it, it will randomly pick a rarity for the item, this will also happen if no rarity is selected. (Allowed raritys for :rainbow[slot {slot_number}].)'); Slot_Rarity = choice([r if r in item_raritys.get(selected_weapon, []) else choice(item_raritys.get(selected_weapon, [])) for r in slot_rarity_allowed]) if slot_rarity_allowed and slot != 'Disabled' and slot_allowed else None; Slot_Rarity = 'No rarity selected' if slot!='Disabled' and slot_allowed and not slot_rarity_allowed else Slot_Rarity if slot_rarity_allowed else 'None'; Slot_Rarity = choice(item_raritys.get(selected_weapon)) if Slot_Rarity == 'No rarity selected' else Slot_Rarity

    st.divider(); return slot, Slot_Rarity, selected_weapon

def AttachmentViewer(rarity, slot_name, slot_number, slot, weapon_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    st.title(f':red[{slot_name}]')
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: st.subheader(f'Current item:\n ## :green[{weapon_name}]', help=f"Shows current weapon for :red[slot {slot_number}] (Auto selects attachments for mythic rarity weapons, doesn't keep old settings.)", divider='rainbow')
    with col2: attachment1 = st.multiselect('Optic', optic_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Increases hipfire accuracy. (:red[{slot_name}])", disabled=True if rarity == "Mythic" or slot in ('Disabled', 'Other', 'Health') else False)
    with col3: attachment2 = st.multiselect('Magazine', magazine_options, help=f"**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed. (:red[{slot_name}])", disabled=True if rarity == "Mythic" or slot in ('Disabled', 'Other', 'Health') else False)
    with col4: attachment3 = st.multiselect('Underbarrel', underbarrel_options, help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Increases hipfire accuracy. (:red[{slot_name}])", disabled=True if rarity == "Mythic" or slot in ('Disabled', 'Other', 'Health') else False)
    with col5: attachment4 = st.multiselect('Barrel', barrel_options, help=f"**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil. (:red[{slot_name}])", disabled=True if rarity == "Mythic" or slot in ('Disabled', 'Other', 'Health') else False)
    st.divider() 
    if rarity == 'Mythic': return map(lambda x: x[0], weapon_attachments.get(weapon_name))
    else: attachment1, attachment2, attachment3, attachment4=choice(attachment1) if attachment1 else None, choice(attachment2) if attachment2 else None, choice(attachment3) if attachment3 else None, choice(attachment4) if attachment4 else None; return attachment1, attachment2, attachment3, attachment4

Customize, Weapon_mods, Loadout, Weapon_Info = st.tabs(["Customize", "Weapon Mods", "Loadout", "Weapon Info"])
with Customize:
    slotone, slotone_rarity, slotone_weapon = Weapon_Slot("Slot 1", "1")
    slottwo, slottwo_rarity, slottwo_weapon = Weapon_Slot("Slot 2", "2")
    slotthree, slotthree_rarity, slotthree_weapon = Weapon_Slot("Slot 3", "3")
    slotfour, slotfour_rarity, slotfour_weapon = Weapon_Slot("Slot 4", "4")
    slotfive, slotfive_rarity, slotfive_weapon = Weapon_Slot("Slot 5", "5")
    # st.toast(f'Your loadout was :rainbow[saved!]', icon='✅')
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.subheader(f'Medallions', divider='rainbow')
    with col2: slotsix = st.selectbox('Medallions', ('Disabled', 'Enabled'))
    with col3: medallions_amount = st.selectbox('Amount of medallions', [1, 2, 3, 4], help=f'Example, if selected {len(Medallions)}, it will select 1-{len(Medallions)} medallions from a random list.') if slotsix == 'Enabled' else st.selectbox('Amount of medallions', [], help='Example, if selected 5, it will select 1-5 medallions from a random list.')
    with col4: slotsix_randomness = st.selectbox('Randomness', ['Enabled', 'Disabled'], help=f'If enabled it will randomly select from (lets say you selected {len(Medallions)}) 1-{len(Medallions)} medallions, else will pick {len(Medallions)} medallions') if slotsix == 'Enabled' else st.selectbox('Randomness', [], help='If enabled it will randomly select from (lets say you selected 5) 1-5 medallions, else will pick 5 medallions')
    Medallion = ', '.join(sample(Medallions, k=randint(1, medallions_amount))) if slotsix == 'Enabled' and slotsix_randomness != 'Disabled' else ', '.join(sample(Medallions, k=int(medallions_amount))) if slotsix == 'Enabled' and slotsix_randomness == 'Disabled' else 'Disabled'
    if not medallions_amount: medallions_amount_text='0'
    elif slotsix_randomness=='Disabled' and medallions_amount: medallions_amount_text=medallions_amount
    else: medallions_amount_text=f'1-{medallions_amount}'
    if slotsix == 'Enabled' and medallions_amount: selected_meddalions_amount = len(Medallion.split(', '))
    else: selected_meddalions_amount='0'
with Weapon_mods:
    slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4 = AttachmentViewer(slotone_rarity, "Slot 1", "1", slotone, slotone_weapon, *weapon_attachments.get(slotone_weapon, [[],[],[],[]]) if slotone!='Disabled' else [[] for _ in range(4)])
    slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4 = AttachmentViewer(slottwo_rarity, "Slot 2", "2", slottwo, slottwo_weapon, *weapon_attachments.get(slottwo_weapon, [[],[],[],[]]) if slottwo!='Disabled' else [[] for _ in range(4)])
    slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4 = AttachmentViewer(slotthree_rarity, "Slot 3", "3", slotthree, slotthree_weapon, *weapon_attachments.get(slotthree_weapon, [[],[],[],[]]) if slotthree!='Disabled' else [[] for _ in range(4)])
    slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4 = AttachmentViewer(slotfour_rarity, "Slot 4", "4", slotfour, slotfour_weapon, *weapon_attachments.get(slotfour_weapon, [[],[],[],[]]) if slotfour!='Disabled' else [[] for _ in range(4)])
    slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4 = AttachmentViewer(slotfive_rarity, "Slot 5", "5", slotfive, slotfive_weapon, *weapon_attachments.get(slotfive_weapon, [[],[],[],[]]) if slotfive!='Disabled' else [[] for _ in range(4)])
with Loadout:
    col1, col2, col3 = st.columns(3)
    with col1:
        tab1b, tab2b, tab3b = st.tabs(["Regular", "Base", "Json"])
        with tab1b: t1 = st.empty(); t1.write(f'# :violet[Items]  \n##### Slot 1 : :green[{slotone_weapon}]\n#####    Slot 2 : :green[{slottwo_weapon}]\n#####    Slot 3 : :green[{slotthree_weapon}]\n#####    Slot 4 : :green[{slotfour_weapon}]\n#####    Slot 5 : :green[{slotfive_weapon}]')
        with tab2b: t2 = st.empty(); t2.write(f'# Items\n    Slot 1 : {slotone_weapon}\n    Slot 2 : {slottwo_weapon}\n    Slot 3 : {slotthree_weapon}\n    Slot 4 : {slotfour_weapon}\n    Slot 5 : {slotfive_weapon}\n    Medallions : {Medallion}')
        with tab3b: t3 = st.empty(); t3.json({'Items': [f'Slot 1 : {slotone_weapon}', f'Slot 2 : {slottwo_weapon}', f'Slot 3 : {slotthree_weapon}', f'Slot 4 : {slotfour_weapon}', f'Slot 5 : {slotfive_weapon}'], })
    with col2:
        taba1, taba2, taba3 = st.tabs(["Regular", "Base", "Json"])
        with taba1: tt1 = st.empty(); tt1.write(f'# :violet[Rarity]  \n##### Slot 1 : :orange[{slotone_rarity}]\n#####    Slot 2 : :orange[{slottwo_rarity}]\n#####    Slot 3 : :orange[{slotthree_rarity}]\n#####    Slot 4 : :orange[{slotfour_rarity}]\n#####    Slot 5 : :orange[{slotfive_rarity}]\n#####    Medallions amount : :blue[{medallions_amount_text}] (current: :blue[{selected_meddalions_amount}])')
        with taba2: tt2 = st.empty(); tt2.write(f'# Rarity\n    Slot 1 : {slotone_rarity}\n    Slot 2 : {slottwo_rarity}\n    Slot 3 : {slotthree_rarity}\n    Slot 4 : {slotfour_rarity}\n    Slot 5 : {slotfive_rarity}\n    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})')
        with taba3: tt3 = st.empty(); tt3.json({'Rarity': [f'Slot 1 : {slotone_rarity}', f'Slot 2 : {slottwo_rarity}', f'Slot 3 : {slotthree_rarity}', f'Slot 4 : {slotfour_rarity}', f'Slot 5 : {slotfive_rarity}', f'Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount}'], })
    with col3:
        taba1, taba2, taba3 = st.tabs(["Regular", "Base", "Json"])
        with taba1: ttt1 = st.empty(); ttt1.write(f'# :violet[Attachments]  \n##### Slot 1 : :red[{slotoneattachment1}], :red[{slotoneattachment2}], :red[{slotoneattachment3}], :red[{slottwoattachment4}]\n#####    Slot 2 : :red[{slottwoattachment1}], :red[{slottwoattachment2}], :red[{slottwoattachment3}], :red[{slottwoattachment4}]\n#####    Slot 3 : :red[{slotthreeattachment1}], :red[{slotthreeattachment2}], :red[{slotthreeattachment3}], :red[{slotthreeattachment4}]\n#####    Slot 4 : :red[{slotfourattachment1}], :red[{slotfourattachment2}], :red[{slotfourattachment3}], :red[{slotfourattachment4}]\n#####    Slot 5 : :red[{slotfiveattachment1}], :red[{slotfiveattachment2}], :red[{slotfiveattachment3}], :red[{slotfiveattachment4}]')
        with taba2: ttt2 = st.empty(); ttt2.write(f'# Attachments\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
        with taba3: ttt3 = st.empty(); ttt3.json({'Attachments': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}'], })
    st.divider()
    if st.button('Randomize loadout'):
        #WriteToFile()
        st.toast(f'Your loadout was :rainbow[generated!]', icon='✅')
    st.divider()
    
    if st.button('Save Config'):
        if os.path.exists(f"{os.path.join('configs', 'Loadout_generator_config')}.txt"): os.remove(f"{os.path.join('configs', 'Loadout_generator_config')}.txt"); f = open(f"{os.path.join('configs', 'Loadout_generator_config')}.txt", "a"); f.write(f'{slotone_weapon}\n{slottwo_weapon}\n{slotthree_weapon}\n{slotfour_weapon}\n{slotfive_weapon}\n{slotone_rarity}\n{slottwo_rarity}\n{slotthree_rarity}\n{slotfour_rarity}\n{slotfive_rarity}\n{slotoneattachment1}\n{slotoneattachment2}\n{slotoneattachment3}\n{slotoneattachment4}\n{slottwoattachment1}\n{slottwoattachment2}\n{slottwoattachment3}\n{slottwoattachment4}\n{slotthreeattachment1}\n{slotthreeattachment2}\n{slotthreeattachment3}\n{slotthreeattachment4}\n{slotfourattachment1}\n{slotfourattachment2}\n{slotfourattachment3}\n{slotfourattachment4}\n{slotfiveattachment1}\n{slotfiveattachment2}\n{slotfiveattachment3}\n{slotfiveattachment4}\n{Medallion}\n{medallions_amount_text}\n{selected_meddalions_amount}'); st.toast(f'Saved configuration to file :red[configs\\Loadout_generator_config.txt]', icon="✅"); f.close()

    if st.button('Load Config'):
        if os.path.exists(f"{os.path.join('configs', 'Loadout_generator_config')}.txt"): 
            with open(f"{os.path.join('configs', 'Loadout_generator_config')}.txt", "r") as file: lines = [line.strip() for line in file.readlines()]
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
                st.toast(f'Loaded configuration from file :red[configs\\Loadout_generator_config.txt]', icon="✅")
            else: st.error(f"Invalid configuration file. Expected 33 lines. Called back: {len(lines)} line(s)")
        else: st.error("File doesn't exist. Please save a config and try again.")
with Weapon_Info:
    #with st.sidebar: st.info('Weapon Info tab:\n Some DPS (Damage per second) Data of some weapons may be inacurate.', icon='❗')
    st.warning('Most of the data/info here is inacurate (thank you fortnite wiki and fortnite.gg/weapons for being amazing), everything works correctly though.', icon='❗')
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander('Frenzy Auto Shotgun'):
            col1_,_,col2_ = st.columns(3)
            with col1_: st.caption('Hover over the raritys for more info', help='Hovering over the raritys will say what rarity it is coresponding to each letter (Rarity).')
            with col2_: button=st.checkbox('Show image', help='Enabling this will show you an image of the Frenzy Auto Shotgun.')
            if button and os.path.exists(os.path.join('images', 'FrenzyAutoShotgun.jpg')): st.image(os.path.join('images', 'FrenzyAutoShotgun.jpg'), use_column_width=True)
            elif button and not os.path.exists(os.path.join('images', 'FrenzyAutoShotgun.jpg')): st.write(':green[images\\FrenzyAutoShotgun.jpg] wasn\'t found.')
            st.subheader("Weapon info", divider='rainbow')
            col1expanded,col2expanded,col3expanded,col4expanded,col5expanded = st.columns(5)
            with col1expanded:
                with st.popover(':gray[C]', help='Rarity: Common', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 152.5 DPS'); tab21.write('# 61 Damage'); tab31.write('# 2.2 Firerate'); tab41.write('# 8 Mag size'); tab51.write('# 5.17S reload speed')
            with col2expanded:
                with st.popover(':green[U]', help='Rarity: Uncommon', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 62.3 DPS'); tab21.write('# 89 Damage'); tab31.write('# 2.2 Firerate'); tab41.write('# 8 Mag size'); tab51.write('# 4.94S reload speed')
            with col3expanded:
                with st.popover(':blue[R]', help='Rarity: Rare', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 65.8 DPS'); tab21.write('# 94 Damage'); tab31.write('# 2.2 Firerate'); tab41.write('# 8 Mag size'); tab51.write('# 4.7S reload speed')
            with col4expanded:
                with st.popover(':violet[E]', help='Rarity: Epic', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 69.3 DPS'); tab21.write('# 99 Damage'); tab31.write('# 2.2 Firerate'); tab41.write('# 8 Mag size'); tab51.write('# 4.47S reload speed')
            with col5expanded:
                with st.popover(':orange[L]', help='Rarity: Legendary', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 72.1 DPS'); tab21.write('# 103 Damage'); tab31.write('# 2.2 Firerate'); tab41.write('# 8 Mag size'); tab51.write('# 4.23S reload speed')
            st.subheader("Weapon attachments info", divider='rainbow')
            with st.container(border=True):
                col1info,col2info,col3info,col4info = st.columns(4)
                with col1info: 
                    with st.popover('Optic', use_container_width=True): st.write('Red Eye Sight: ✅'); st.write('Holo-13 Optic: ✅'); st.write('P2X Optic: ❌'); st.write('Thermal Optic: ❌'); st.write('Sniper Optic: ❌')#tab11,tab21,tab31,tab41 = st.tabs(['ye','ye1','ye2','ye3']); tab11.write('haha')
                with col2info:
                    with st.popover('Magazine', use_container_width=True): st.write('Drum Mag: ✅'); st.write('Speed Mag: ✅')
                with col3info:
                    with st.popover('Underbarrel', use_container_width=True): st.write('Angled Foregrip: ✅'); st.write('Vertical Foregrip: ✅'); st.write('Laser: ✅'); st.write('Speed Foregrip: ✅')
                with col4info:
                    with st.popover('Barrel', use_container_width=True): st.write('Muzzle Brake: ✅'); st.write('Suppressor: ✅')
    with col2:
        with st.expander('Hammer Pump Shotgun'):
            col1_,_,col2_ = st.columns(3)
            with col1_: st.caption('Hover over the raritys for more info', help='Hovering over the raritys will say what rarity it is coresponding to each letter (Rarity).')
            with col2_: button=st.checkbox('Show image', help='Enabling this will show you an image of the Hammer Pump Shotgun.')
            if button and os.path.exists(os.path.join('images', 'HammerPumpShotgun.jpg')): st.image(os.path.join('images', 'HammerPumpShotgun.jpg'), use_column_width=True)
            elif button and not os.path.exists(os.path.join('images', 'HammerPumpShotgun.jpg')): st.write(':green[images\\HammerPumpShotgun.jpg] wasn\'t found.')
            st.subheader("Weapon info", divider='rainbow')
            col1expanded,col2expanded,col3expanded,col4expanded,col5expanded = st.columns(5)
            with col1expanded:
                with st.popover(':gray[C]', help='Rarity: Common', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 152.5 DPS'); tab21.write('# 61 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 5.17S reload speed')
            with col2expanded:
                with st.popover(':green[U]', help='Rarity: Uncommon', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 162.5 DPS'); tab21.write('# 65 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 4.94S reload speed')
            with col3expanded:
                with st.popover(':blue[R]', help='Rarity: Rare', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 170 DPS'); tab21.write('# 68 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 4.7S reload speed')
            with col4expanded:
                with st.popover(':violet[E]', help='Rarity: Epic', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 177.5 DPS'); tab21.write('# 71 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 4.47S reload speed')
            with col5expanded:
                with st.popover(':orange[L]', help='Rarity: Legendary', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 187.5 DPS'); tab21.write('# 75 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 4.23S reload speed')
            st.subheader("Weapon attachments info", divider='rainbow')
            with st.container(border=True):
                col1info,col2info,col3info,col4info = st.columns(4)
                with col1info: 
                    with st.popover('Optic', use_container_width=True): st.write('Red Eye Sight: ✅'); st.write('Holo-13 Optic: ✅'); st.write('P2X Optic: ❌'); st.write('Thermal Optic: ❌'); st.write('Sniper Optic: ❌')
                with col2info:
                    with st.popover('Magazine', use_container_width=True): st.write('Drum Mag: ❌'); st.write('Speed Mag: ✅')
                with col3info:
                    with st.popover('Underbarrel', use_container_width=True): st.write('Angled Foregrip: ✅'); st.write('Vertical Foregrip: ✅'); st.write('Laser: ✅'); st.write('Speed Foregrip: ✅')
                with col4info:
                    with st.popover('Barrel', use_container_width=True): st.write('Muzzle Brake: ✅'); st.write('Suppressor: ✅')
    with col3:
        with st.expander('Gatekeeper Shotgun'):
            col1_,_,col2_ = st.columns(3)
            with col1_: st.caption('Hover over the raritys for more info', help='Hovering over the raritys will say what rarity it is coresponding to each letter (Rarity).')
            with col2_: button=st.checkbox('Show image', help='Enabling this will show you an image of the Gatekeeper Shotgun.')
            if button and os.path.exists(os.path.join('images', 'GatekeeperShotgun.jpg')): st.image(os.path.join('images', 'GatekeeperShotgun.jpg'), use_column_width=True)
            elif button and not os.path.exists(os.path.join('images', 'GatekeeperShotgun.jpg')): st.write(':green[images\\GatekeeperShotgun.jpg] wasn\'t found.')
            st.subheader("Weapon info", divider='rainbow')
            col1expanded,col2expanded,col3expanded,col4expanded,col5expanded,col6expanded = st.columns(6)
            with col1expanded:
                with st.popover(':gray[C]', help='Rarity: Common', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 152.5 DPS'); tab21.write('# 61 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 5.17S reload speed')
            with col2expanded:
                with st.popover(':green[U]', help='Rarity: Uncommon', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 162.5 DPS'); tab21.write('# 65 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 4.94S reload speed')
            with col3expanded:
                with st.popover(':blue[R]', help='Rarity: Rare', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 170 DPS'); tab21.write('# 68 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 4.7S reload speed')
            with col4expanded:
                with st.popover(':violet[E]', help='Rarity: Epic', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 177.5 DPS'); tab21.write('# 71 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 4.47S reload speed')
            with col5expanded:
                with st.popover(':orange[L]', help='Rarity: Legendary', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 187.5 DPS'); tab21.write('# 75 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 4.23S reload speed')
            with col6expanded:
                with st.popover(':red[M]', help='Rarity: Mythic', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 187.5 DPS'); tab21.write('# 75 Damage'); tab31.write('# 2.5 Firerate'); tab41.write('# 4.23S reload speed')  
            st.subheader("Weapon attachments info", divider='rainbow')
            with st.container(border=True):
                col1info,col2info,col3info,col4info = st.columns(4)
                with col1info: 
                    with st.popover('Optic', use_container_width=True): st.write('Red Eye Sight: ✅'); st.write('Holo-13 Optic: ✅'); st.write('P2X Optic: ❌'); st.write('Thermal Optic: ❌'); st.write('Sniper Optic: ❌')
                with col2info:
                    with st.popover('Magazine', use_container_width=True): st.write('Drum Mag: ✅'); st.write('Speed Mag: ✅')
                with col3info:
                    with st.popover('Underbarrel', use_container_width=True): st.write('Angled Foregrip: ✅'); st.write('Vertical Foregrip: ✅'); st.write('Laser: ✅'); st.write('Speed Foregrip: ✅')
                with col4info:
                    with st.popover('Barrel', use_container_width=True): st.write('Muzzle Brake: ✅'); st.write('Suppressor: ❌')
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        with st.expander('Warforged Assault Rifle'):
            col1_,_,col2_ = st.columns(3)
            with col1_: st.caption('Hover over the raritys for more info', help='Hovering over the raritys will say what rarity it is coresponding to each letter (Rarity).')
            with col2_: button=st.checkbox('Show image', help='Enabling this will show you an image of the Warforged Assualt Rifle.')
            if button and os.path.exists(os.path.join('images', 'WarforgedAR.jpg')): st.image(os.path.join('images', 'WarforgedAR.jpg'), use_column_width=True)
            elif button and not os.path.exists(os.path.join('images', 'WarforgedAR.jpg')): st.write(':green[images\\WarforgedAR.jpg] wasn\'t found.')
            st.subheader("Weapon info", divider='rainbow')
            col1expanded,col2expanded,col3expanded,col4expanded,col5expanded,col6expanded = st.columns(6)
            with col1expanded:
                with st.popover(':gray[C]', help='Rarity: Common', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag size', 'Reload speed']); tab11.write('# 172.8 DPS'); tab21.write('# 24 Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Mag size'); tab51.write('# 3.85S reload speed')
            with col2expanded:
                with st.popover(':green[U]', help='Rarity: Uncommon', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag size', 'Reload speed']); tab11.write('# 187.2 DPS'); tab21.write('# 26 Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Mag size') ; tab51.write('# 3.68S reload speed')
            with col3expanded:
                with st.popover(':blue[R]', help='Rarity: Rare', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag size', 'Reload speed']); tab11.write('# 194.4 DPS'); tab21.write('# 27 Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Mag size') ; tab51.write('# 3.5S reload speed')
            with col4expanded:
                with st.popover(':violet[E]', help='Rarity: Epic', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag size', 'Reload speed']); tab11.write('# 201.6 DPS'); tab21.write('# 28 Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Mag size') ; tab51.write('# 3.33S reload speed')
            with col5expanded:
                with st.popover(':orange[L]', help='Rarity: Legendary', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag size', 'Reload speed']); tab11.write('# 216 DPS'); tab21.write('# 30 Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Mag size') ; tab51.write('# 3.15S reload speed')
            with col6expanded:
                with st.popover(':red[M]', help='Rarity: Mythic', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag size', 'Reload speed']); tab11.write('# 223.2 DPS'); tab21.write('# 31 Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Mag size') ; tab51.write('# 2.98S reload speed')  
            st.subheader("Weapon attachments info", divider='rainbow')
            with st.container(border=True):
                col1info,col2info,col3info,col4info = st.columns(4)
                with col1info: 
                    with st.popover('Optic', use_container_width=True): st.write('Red Eye Sight: ✅'); st.write('Holo-13 Optic: ✅'); st.write('P2X Optic: ✅'); st.write('Thermal Optic: ✅'); st.write('Sniper Optic: ✅')#tab11,tab21,tab31,tab41 = st.tabs(['ye','ye1','ye2','ye3']); tab11.write('haha')
                with col2info:
                    with st.popover('Magazine', use_container_width=True): st.write('Drum Mag: ✅'); st.write('Speed Mag: ✅')
                with col3info:
                    with st.popover('Underbarrel', use_container_width=True): st.write('Angled Foregrip: ✅'); st.write('Vertical Foregrip: ✅'); st.write('Laser: ✅'); st.write('Speed Foregrip: ✅')
                with col4info:
                    with st.popover('Barrel', use_container_width=True): st.write('Muzzle Brake: ✅'); st.write('Suppressor: ✅')
    with col2:
        with st.expander('Nemesis AR'):
            col1_,_,col2_ = st.columns(3)
            with col1_: st.caption('Hover over the raritys for more info', help='Hovering over the raritys will say what rarity it is coresponding to each letter (Rarity).')
            with col2_: button=st.checkbox('Show image', help='Enabling this will show you an image of the Nemesis AR.')
            if button and os.path.exists(os.path.join('images', 'NemesisAR.jpg')): st.image(os.path.join('images', 'NemesisAR.jpg'), use_column_width=True)
            elif button and not os.path.exists(os.path.join('images', 'NemesisAR.jpg')): st.write(':green[images\\NemesisAR.jpg] wasn\'t found.')
            st.subheader("Weapon info", divider='rainbow')
            col1expanded,col2expanded,col3expanded,col4expanded,col5expanded = st.columns(5)
            with col1expanded:
                with st.popover(':gray[C]', help='Rarity: Common', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 145 DPS'); tab21.write('# 29 Damage'); tab31.write('# 5 Firerate'); tab41.write('test'); tab51.write('# 2.75S reload speed')
            with col2expanded:
                with st.popover(':green[U]', help='Rarity: Uncommon', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 150 DPS'); tab21.write('# 30 Damage'); tab31.write('# 5 Firerate'); tab41.write('test'); tab51.write('# 2.63S reload speed')
            with col3expanded:
                with st.popover(':blue[R]', help='Rarity: Rare', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 160 DPS'); tab21.write('# 32 Damage'); tab31.write('# 5 Firerate'); tab41.write('test'); tab51.write('# 2.5S reload speed')
            with col4expanded:
                with st.popover(':violet[E]', help='Rarity: Epic', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 170 DPS'); tab21.write('# 34 Damage'); tab31.write('# 5 Firerate'); tab41.write('test'); tab51.write('# 2.38S reload speed')
            with col5expanded:
                with st.popover(':orange[L]', help='Rarity: Legendary', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['DPS', 'Damage', 'Firerate', 'Mag Size', 'Reload speed']); tab11.write('# 175 DPS'); tab21.write('# 35 Damage'); tab31.write('# 5 Firerate'); tab41.write('test'); tab51.write('# 2.35S reload speed')
            st.subheader("Weapon attachments info", divider='rainbow')
            with st.container(border=True):
                col1info,col2info,col3info,col4info = st.columns(4)
                with col1info: 
                    with st.popover('Optic', use_container_width=True): st.write('Red Eye Sight: ✅'); st.write('Holo-13 Optic: ✅'); st.write('P2X Optic: ✅'); st.write('Thermal Optic: ✅'); st.write('Sniper Optic: ✅')#tab11,tab21,tab31,tab41 = st.tabs(['ye','ye1','ye2','ye3']); tab11.write('haha')
                with col2info:
                    with st.popover('Magazine', use_container_width=True): st.write('Drum Mag: ✅'); st.write('Speed Mag: ✅')
                with col3info:
                    with st.popover('Underbarrel', use_container_width=True): st.write('Angled Foregrip: ✅'); st.write('Vertical Foregrip: ✅'); st.write('Laser: ✅'); st.write('Speed Foregrip: ✅')
                with col4info:
                    with st.popover('Barrel', use_container_width=True): st.write('Muzzle Brake: ✅'); st.write('Suppressor: ✅')
    st.divider()
with st.sidebar:
    st.page_link("http://www.Github.com/fuzzybuzzyboy/py", label="Github", icon="🛢️")
    if st.button('Clock'):
        with st.empty():
            while True:
                time_now1, time_now = datetime.now().strftime("%D"), datetime.now().strftime("%H:%M:%S")
                st.write(f'# Clock\n    Time : {time_now}\n    Date : {time_now1}')
                time.sleep(1)
