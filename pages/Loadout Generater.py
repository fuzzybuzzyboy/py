from datetime import datetime
import time, os, streamlit as st # type: ignore
from random import randint, sample, choice
st.set_page_config(page_title='Loadout Generater', page_icon="🤑", layout="wide", initial_sidebar_state="expanded", menu_items={'Get help': 'https://github.com/fuzzybuzzyboy/py', 'Report a bug': "https://github.com/fuzzybuzzyboy/py", 'About': "Random items generator for fortnite (no this doesn't inject into your game and do something blah blah blah)"})

medallions_amount, medallions_amount_text=0, '1-'
slotoneattachment1=slotoneattachment2=slotoneattachment3=slotoneattachment4=slottwoattachment1=slottwoattachment2=slottwoattachment3=slottwoattachment4=slotthreeattachment1=slotthreeattachment2=slotthreeattachment3=slotthreeattachment4=slotfourattachment1=slotfourattachment2=slotfourattachment3=slotfourattachment4=slotfiveattachment1=slotfiveattachment2=slotfiveattachment3=slotfiveattachment4=None
slotone=slotone_rarity=slotone_weapon=slottwo=slottwo_rarity=slottwo_weapon=slotthree=slotthree_rarity=slotthree_weapon=slotfour=slotfour_rarity=slotfour_weapon=slotfive=slotfive_rarity=slotfive_weapon='Disabled'

item_types=['Disabled', 'Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'DMR', 'Other', 'Health']
items = {'Shotgun': ['Hammer Pump Shotgun', 'Frenzy Auto Shotgun', 'Gatekeeper Shotgun', 'Cerberus\' Gatekeeper Shotgun'], 'SMG': ['Thunder Burst SMG', 'Harbinger SMG', 'Hades\' Harbinger SMG'], 'Pistol': ['Ranger Pistol',], 'Assault-Rifle': ['Warforged Assault Rifle', 'Ares\' Warforged Assault Rifle', 'Tactical Assault Rifle', 'Nemesis AR'], 'Sniper': ['Reaper Sniper Rifle'], 'DMR': ['Huntress DMR', 'Zeus\' Huntress DMR'], 'Other': ['Thunderbolt of Zeus', 'Cluster Clinger', 'Wings of Icarus', 'Shockwave Grenade'], 'Health': ['FlowBerry Fizz', 'FlowBerry', 'Shield Potion', 'Small Shield Potion', 'Medkit']}
item_raritys = {'Hammer Pump Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Frenzy Auto Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Gatekeeper Shotgun': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Cerberus\' Gatekeeper Shotgun': ['Mythic',], 'Thunder Burst SMG': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Harbinger SMG': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Hades\' Harbinger SMG': ['Mythic'], 'Ranger Pistol': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Warforged Assault Rifle': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Ares\' Warforged Assault Rifle': ['Mythic'], 'Tactical Assault Rifle': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Nemesis AR': ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'], 'Reaper Sniper Rifle': ['Uncommon', 'Rare', 'Epic', 'Legendary'], 'Huntress DMR': ['Uncommon', 'Rare', 'Epic', 'Legendary'], 'Zeus\' Huntress DMR': ['Mythic',], 'Cluster Clinger': ['Uncommon',], 'Thunderbolt of Zeus': ['Mythic',], 'Wings of Icarus': ['Epic',], 'Shockwave Grenade': ['Epic',], 'Shield Potion': ['Rare',], 'FlowBerry Fizz': ['Rare',], 'Small Shield Potion': ['Uncommon',], 'Medkit': ['Uncommon',], 'FlowBerry': ['Uncommmon',]}
weapon_attachments = {'Hammer Pump Shotgun': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Frenzy Auto Shotgun': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Gatekeeper Shotgun': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake']], 'Thunder Burst SMG': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Harbinger SMG': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Ranger Pistol': [['None', 'Red Eye Sight', 'Holo-13 Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Laser'], ['None', 'Muzzle Brake', 'Suppressor']], 'Warforged Assault Rifle': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Tactical Assault Rifle': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'Thermal Scope', 'Sniper Scope'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speedgrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Nemesis AR': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Reaper Sniper Rifle': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Laser', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Nemesis AR': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Speed Foregrip'], ['None', 'Muzzle Brake', 'Suppressor']], 'Huntress DMR': [['None', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Thermal Optic', 'Sniper Optic'], ['None', 'Drum Mag', 'Speed Mag'], ['None', 'Angled Foregrip', 'Vertical Foregrip', 'Speed Foregrip'], ['None', ]], 'Cerberus\' Gatekeeper Shotgun': [['None',], ['Speed Mag', ], ['Speed Foregrip', ], ['Muzzle Brake', ]], 'Hades\' Harbinger SMG': [['Red Eye Sight',], ['Speed Mag',], ['Vertical Foregrip',], ['Muzzle Brake']], 'Ares\' Warforged Assault Rifle': [['Red Eye Sight',], ['Drum Mag',], ['Speed Foregrip',], ['Muzzle Brake',]], 'Zeus\' Huntress DMR': [['Sniper Optic',], ['Speed Mag',], ['Angled Foregrip'], ['Muzzle Brake',]],'Cluster Clinger': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Thunderbolt of Zeus': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Wings of Icarus': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Shockwave Grenade': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Shield Potion': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'FlowBerry Fizz': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Small Shield Potion': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'Medkit': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]], 'FlowBerry': [['Disabled', ], ['Disabled', ], ['Disabled', ], ['Disabled', ]]}
Medallions=('Zeus\'s Medallion', 'Ares\'s Medallion', 'Cerberus\'s Medallion', 'Hades\'s Medallion')
images={'Hammer Pump Shotgun': os.path.join('item_images', 'HammerPumpShotgun.webp'), 'Frenzy Auto Shotgun': os.path.join('item_images', 'FrenzyAutoShotgun.webp'), 'Gatekeeper Shotgun': os.path.join('item_images', 'GatekeeperShotgun.webp'), 'Cerberus\' Gatekeeper Shotgun': os.path.join('item_images', 'GatekeeperShotgun.webp'), 'Thunder Burst SMG': os.path.join('item_images', 'ThunderBurstSMG.webp'), 'Harbinger SMG': os.path.join('item_images', 'HarbingerSMG.webp'), 'Hades\' Harbinger SMG': os.path.join('item_images', 'HarbingerSMG.webp'), 'Warforged Assault Rifle': os.path.join('item_images', 'WarforgedAssaultRifle.webp'), 'Ares\' Warforged Assault Rifle': os.path.join('item_images', 'WarforgedAssaultRifle.webp'), 'Tactical Assault Rifle': os.path.join('item_images', 'TacticalAssaultRifle.webp'), 'Nemesis AR': os.path.join('item_images', 'NemesisAR.webp'), 'Reaper Sniper Rifle': os.path.join('item_images', 'ReaperSniperRifle.webp'), 'Huntress DMR': os.path.join('item_images', 'HuntressDMR.webp'), 'Zeus\' Huntress DMR': os.path.join('item_images', 'HuntressDMR.webp'), 'Thunderbolt of Zeus': os.path.join('item_images', 'ThunderboltOfZeus.webp'), 'Cluster Clinger': os.path.join('item_images', 'ClusterClinger.webp'), 'Wings of Icarus': os.path.join('item_images', 'WingsOfIcarus.webp'), 'Shockwave Grenade': os.path.join('item_images', 'ShockwaveGrenade.webp'), 'FlowBerry Fizz': os.path.join('item_images', 'FlowBerryFizz.webp'), 'FlowBerry': os.path.join('item_images', 'FlowBerry.webp'), 'Shield Potion': os.path.join('item_images', 'ShieldPotion.webp'), 'Small Shield Potion': os.path.join('item_images', 'SmallShieldPotion.webp'), 'Medkit': os.path.join('item_images', 'Medkit.webp')}

def Weapon_Slot(slot_name, slot_number):
    selected_weapon=None
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        container_thing = st.container(border=True)
        container_thing.write(f'##### Current slot: :red[{slot_name}]')
    with col2: slot = st.selectbox(f'Item type', (item_types), help=f'Weapon type for :rainbow[slot {slot_number}]')
    with col3: slot_allowed = st.multiselect('Allowed items', items.get(slot, []), items.get(slot, []), help=f'Allowed items for item type (:rainbow[{slot_name}]).')
    if slot_allowed: selected_weapon=choice(slot_allowed)
    if selected_weapon: 
        with container_thing.expander('Image', expanded=True): 
            st.image(images.get(selected_weapon))
    with col4: slot_rarity_allowed = st.multiselect('Allowed rarity', ["Common", 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic'], help=f'If the weapon randomly selected doesn\'t have a valid rarity selected for it, it will randomly pick a rarity for the item, this will also happen if no rarity is selected. (Allowed raritys for :rainbow[slot {slot_number}].)') if slot not in ['Disabled', 'Other', 'Health'] and selected_weapon!=None else st.multiselect('Allowed rarity', (), help=f'If the weapon randomly selected doesn\'t have a valid rarity selected for it, it will randomly pick a rarity for the item, this will also happen if no rarity is selected. (Allowed raritys for :rainbow[slot {slot_number}].)'); Slot_Rarity = choice([r if r in item_raritys.get(selected_weapon, []) else choice(item_raritys.get(selected_weapon, [])) for r in slot_rarity_allowed]) if slot_rarity_allowed and slot != 'Disabled' and slot_allowed else None; Slot_Rarity = 'No rarity selected' if slot!='Disabled' and slot_allowed and not slot_rarity_allowed else Slot_Rarity if slot_rarity_allowed else 'None'; Slot_Rarity = choice(item_raritys.get(selected_weapon)) if Slot_Rarity == 'No rarity selected' else Slot_Rarity
    st.divider(); return slot, Slot_Rarity, selected_weapon
def Random_Weapon():
    Slot = choice(['Shotgun', 'SMG', 'Assault-Rifle', 'Sniper', 'DMR', 'Other', 'Health']); Selected_weapon = choice(items.get(Slot)); Slot_Rarity = choice(item_raritys.get(Selected_weapon)); Attachments = weapon_attachments.get(Selected_weapon); Attachment1, Attachment2, Attachment3, Attachment4 = choice(Attachments[0]), choice(Attachments[1]), choice(Attachments[2]), choice(Attachments[3])
    return Slot, Selected_weapon, Slot_Rarity, Attachment1, Attachment2, Attachment3, Attachment4
def AttachmentViewer(rarity, slot_name, slot_number, slot, weapon_name, optic_options, magazine_options, underbarrel_options, barrel_options):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: 
        with st.container(border=True):
            with st.expander('Slot | Item', expanded=True if weapon_name is not None else False):
                st.write(f'##### Current slot: :red[{slot_name}]')
                st.write(f'##### Current item: :green[{weapon_name}]')#, help=f"Shows current weapon for :red[slot {slot_number}] (Auto selects attachments for mythic rarity weapons, doesn't keep old settings.)")
            with st.expander('image', expanded=False):
                if weapon_name != 'None' and images.get(weapon_name) is not None:  st.image(images.get(weapon_name))
    attachment1, attachment2, attachment3, attachment4 = col2.multiselect('Optic', ['Default (None)', 'Red Eye Sight', 'Holo-13 Optic', 'P2X Optic', 'Sniper Scope', 'Thermal Optic'], help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Increases hipfire accuracy. (:red[{slot_name}])", disabled=True if rarity == "Mythic" or slot in ('Disabled', 'Other', 'Health') else False), col3.multiselect('Magazine', ['Default (None)', 'Drum Mag', 'Speed Mag'], help=f"**Speed Mag** - Increases reload speed, **Drum Mag** - Larger magazine size. Decreases reload speed. (:red[{slot_name}])", disabled=True if rarity == "Mythic" or slot in ('Disabled', 'Other', 'Health') else False), col4.multiselect('Underbarrel', ['Default (None)', 'Angled Foregrip', 'Vertical Foregrip', 'Speed Foregrip'], help=f"**Vertical Foregrip** - Improves ADS recoil and spread, **Angled Foregrip** - Reduces ADS time, **Laser** - Increases hipfire accuracy. (:red[{slot_name}])", disabled=True if rarity == "Mythic" or slot in ('Disabled', 'Other', 'Health') else False), col5.multiselect('Barrel', ['Default (None)', 'Muzzle Brake', 'Suppressor'], help=f"**Suppressor** - Reduces muzzle flash and dampens audio, **Muzzle Brake** - Reduces recoil. (:red[{slot_name}])", disabled=True if rarity == "Mythic" or slot in ('Disabled', 'Other', 'Health') else False)
    st.divider() 
    if rarity == 'Mythic': return map(lambda x: x[0], weapon_attachments.get(weapon_name))
    else: attachment1, attachment2, attachment3, attachment4=choice(attachment1) if attachment1 else None, choice(attachment2) if attachment2 else None, choice(attachment3) if attachment3 else None, choice(attachment4) if attachment4 else None; return attachment1, attachment2, attachment3, attachment4

Customize, Weapon_mods, Loadout, Weapon_Info = st.tabs(["Customize", "Weapon Mods", "Loadout", "Weapon Info"])
with Customize:
    slotone, slotone_rarity, slotone_weapon = Weapon_Slot("Slot 1", 1)
    slottwo, slottwo_rarity, slottwo_weapon = Weapon_Slot("Slot 2", 2)
    slotthree, slotthree_rarity, slotthree_weapon = Weapon_Slot("Slot 3", 3)
    slotfour, slotfour_rarity, slotfour_weapon = Weapon_Slot("Slot 4", 4)
    slotfive, slotfive_rarity, slotfive_weapon = Weapon_Slot("Slot 5", 5)
    # st.toast(f'Your loadout was :rainbow[saved!]', icon='✅')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        with st.container(border=True): st.write(f':red-background[:red[Medallions]]')
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
    with st.sidebar:
        if st.button('Suprise me with a random loadout'):
            slotone, slotone_weapon, slotone_rarity, slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4 = Random_Weapon(); slottwo, slottwo_weapon, slottwo_rarity, slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4 = Random_Weapon(); slotthree, slotthree_weapon, slotthree_rarity, slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4 = Random_Weapon(); slotfour, slotfour_weapon, slotfour_rarity, slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4= Random_Weapon(); slotfive, slotfive_weapon, slotfive_rarity, slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4 = Random_Weapon(); Medallion = ', '.join(sample(Medallions, k=randint(1, 4))); medallions_amount_text=f'1-4'; selected_meddalions_amount = len(Medallion.split(', ')); st.toast('Go to the :blue-background[loadout page] to see your :orange[loadout]:violet-background[!]')
            st.session_state['slot1'] = [f'Item: :green[{slotone_weapon}]'  , f'Rarity: :orange[{slotone_rarity}]'  , f'Attachment 1: :red[{slotoneattachment1}]'  , f'Attachment 2: :red[{slotoneattachment2}]'  , f'Attachment 3: :red[{slotoneattachment4}]'  , f'Attachment 4: :red[{slotoneattachment4}]']
            st.session_state['slot2'] = [f'Item: :green[{slottwo_weapon}]'  , f'Rarity: :orange[{slottwo_rarity}]'  , f'Attachment 1: :red[{slottwoattachment1}]'  , f'Attachment 2: :red[{slottwoattachment2}]'  , f'Attachment 3: :red[{slottwoattachment4}]'  , f'Attachment 4: :red[{slottwoattachment4}]']
            st.session_state['slot3'] = [f'Item: :green[{slotthree_weapon}]', f'Rarity: :orange[{slotthree_rarity}]', f'Attachment 1: :red[{slotthreeattachment1}]', f'Attachment 2: :red[{slotthreeattachment2}]', f'Attachment 3: :red[{slotthreeattachment4}]', f'Attachment 4: :red[{slotthreeattachment4}]']
            st.session_state['slot4'] = [f'Item: :green[{slotfour_weapon}]' , f'Rarity: :orange[{slotfour_rarity}]' , f'Attachment 1: :red[{slotfourattachment1}]' , f'Attachment 2: :red[{slotfourattachment2}]' , f'Attachment 3: :red[{slotfourattachment4}]' , f'Attachment 4: :red[{slotfourattachment4}]']
            st.session_state['slot5'] = [f'Item: :green[{slotfive_weapon}]' , f'Rarity: :orange[{slotfive_rarity}]' , f'Attachment 1: :red[{slotfiveattachment1}]' , f'Attachment 2: :red[{slotfiveattachment2}]' , f'Attachment 3: :red[{slotfiveattachment4}]' , f'Attachment 4: :red[{slotfiveattachment4}]']
            st.session_state['other'] = [f':blue[{Medallion}]', f'Amount of medallions: :blue[{medallions_amount_text}]', f'Currently selected amount: :blue[{selected_meddalions_amount}]']
            if not os.path.exists(os.path.join('configs', 'AutoConfig_Generator.txt')): st.toast(':red[AutoConfig]\n\nCreated file :orange[Configs\\AutoConfig_Generator.txt]\n\nReason: File missing.')
            with open(os.path.join('configs', 'AutoConfig_Generator.txt'), 'a') as f: f.write(f'{str(st.session_state)}\n'); f.close()
    col1, col2, col3 = st.columns(3)
    with col1:
        tab1b, tab2b, tab3b = st.tabs(["Regular", "Base", "Json"])
        with tab1b: t1 = st.empty(); t1.write(f'# :violet[Items]  \n##### Slot 1 : :green[{slotone_weapon}]\n#####    Slot 2 : :green[{slottwo_weapon}]\n#####    Slot 3 : :green[{slotthree_weapon}]\n#####    Slot 4 : :green[{slotfour_weapon}]\n#####    Slot 5 : :green[{slotfive_weapon}]\n##### Medallions : :blue[{Medallion}]')
        with tab2b: t2 = st.empty(); t2.write(f'# Items\n    Slot 1 : {slotone_weapon}\n    Slot 2 : {slottwo_weapon}\n    Slot 3 : {slotthree_weapon}\n    Slot 4 : {slotfour_weapon}\n    Slot 5 : {slotfive_weapon}\n    Medallions : {Medallion}')
        with tab3b: t3 = st.empty(); t3.json({'Items': [f'Slot 1 : {slotone_weapon}', f'Slot 2 : {slottwo_weapon}', f'Slot 3 : {slotthree_weapon}', f'Slot 4 : {slotfour_weapon}', f'Slot 5 : {slotfive_weapon}', f'Medallions : {Medallion}']})
    with col2:
        taba1, taba2, taba3 = st.tabs(["Regular", "Base", "Json"])
        with taba1: tt1 = st.empty(); tt1.write(f'# :violet[Rarity]  \n##### Slot 1 : :orange[{slotone_rarity}]\n#####    Slot 2 : :orange[{slottwo_rarity}]\n#####    Slot 3 : :orange[{slotthree_rarity}]\n#####    Slot 4 : :orange[{slotfour_rarity}]\n#####    Slot 5 : :orange[{slotfive_rarity}]\n#####    Medallions amount : :blue[{medallions_amount_text}] (current: :blue[{selected_meddalions_amount}])')
        with taba2: tt2 = st.empty(); tt2.write(f'# Rarity\n    Slot 1 : {slotone_rarity}\n    Slot 2 : {slottwo_rarity}\n    Slot 3 : {slotthree_rarity}\n    Slot 4 : {slotfour_rarity}\n    Slot 5 : {slotfive_rarity}\n    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})')
        with taba3: tt3 = st.empty(); tt3.json({'Rarity': [f'Slot 1 : {slotone_rarity}', f'Slot 2 : {slottwo_rarity}', f'Slot 3 : {slotthree_rarity}', f'Slot 4 : {slotfour_rarity}', f'Slot 5 : {slotfive_rarity}', f'Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount}'], })
    with col3:
        taba1, taba2, taba3 = st.tabs(["Regular", "Base", "Json"])
        with taba1: ttt1 = st.empty(); ttt1.write(f'# :violet[Attachments]  \n##### Slot 1 : :red[{slotoneattachment1}], :red[{slotoneattachment2}], :red[{slotoneattachment3}], :red[{slotoneattachment4}]\n#####    Slot 2 : :red[{slottwoattachment1}], :red[{slottwoattachment2}], :red[{slottwoattachment3}], :red[{slottwoattachment4}]\n#####    Slot 3 : :red[{slotthreeattachment1}], :red[{slotthreeattachment2}], :red[{slotthreeattachment3}], :red[{slotthreeattachment4}]\n#####    Slot 4 : :red[{slotfourattachment1}], :red[{slotfourattachment2}], :red[{slotfourattachment3}], :red[{slotfourattachment4}]\n#####    Slot 5 : :red[{slotfiveattachment1}], :red[{slotfiveattachment2}], :red[{slotfiveattachment3}], :red[{slotfiveattachment4}]')
        with taba2: ttt2 = st.empty(); ttt2.write(f'# Attachments\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}')
        with taba3: ttt3 = st.empty(); ttt3.json({'Attachments': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}'], })
    st.divider()
    if st.button('Randomize loadout'):
        st.session_state['slot1'] = [f'Item: :green[{slotone_weapon}]'  , f'Rarity: :orange[{slotone_rarity}]'  , f'Attachment 1: :red[{slotoneattachment1}]'  , f'Attachment 2: :red[{slotoneattachment2}]'  , f'Attachment 3: :red[{slotoneattachment4}]'  , f'Attachment 4: :red[{slotoneattachment4}]']
        st.session_state['slot2'] = [f'Item: :green[{slottwo_weapon}]'  , f'Rarity: :orange[{slottwo_rarity}]'  , f'Attachment 1: :red[{slottwoattachment1}]'  , f'Attachment 2: :red[{slottwoattachment2}]'  , f'Attachment 3: :red[{slottwoattachment4}]'  , f'Attachment 4: :red[{slottwoattachment4}]']
        st.session_state['slot3'] = [f'Item: :green[{slotthree_weapon}]', f'Rarity: :orange[{slotthree_rarity}]', f'Attachment 1: :red[{slotthreeattachment1}]', f'Attachment 2: :red[{slotthreeattachment2}]', f'Attachment 3: :red[{slotthreeattachment4}]', f'Attachment 4: :red[{slotthreeattachment4}]']
        st.session_state['slot4'] = [f'Item: :green[{slotfour_weapon}]' , f'Rarity: :orange[{slotfour_rarity}]' , f'Attachment 1: :red[{slotfourattachment1}]' , f'Attachment 2: :red[{slotfourattachment2}]' , f'Attachment 3: :red[{slotfourattachment4}]' , f'Attachment 4: :red[{slotfourattachment4}]']
        st.session_state['slot5'] = [f'Item: :green[{slotfive_weapon}]' , f'Rarity: :orange[{slotfive_rarity}]' , f'Attachment 1: :red[{slotfiveattachment1}]' , f'Attachment 2: :red[{slotfiveattachment2}]' , f'Attachment 3: :red[{slotfiveattachment4}]' , f'Attachment 4: :red[{slotfiveattachment4}]']
        st.session_state['other'] = [f':blue[{Medallion}]', f'Amount of medallions: :blue[{medallions_amount_text}]', f'Currently selected amount: :blue[{selected_meddalions_amount}]']
        if not os.path.exists(os.path.join('configs', 'AutoConfig_Generator.txt')): st.toast(':red[AutoConfig]\n\nCreated file :orange[Configs\\AutoConfig_Generator.txt]\n\nReason: File missing.')
        with open(os.path.join('configs', 'AutoConfig_Generator.txt'), 'a') as f: f.write(f'{str(st.session_state)}\n'); f.close()
        st.toast(f'Your loadout was :rainbow[generated!]', icon='✅')
    with st.popover('Load :red[AutoConfig]', help=':red[AutoConfig] will automatically save your config after every time you generate a new one (by pressing Randomize loadout), this means you\'ll never lose out on of your loadouts\n\n:red[AutoConfig] will stay disabled when you have no past config history', disabled=False if os.path.exists(os.path.join('configs', 'AutoConfig_Generator.txt')) else True):
        @st.experimental_dialog("Loadout preview")
        def preview(text):
            slot1,slot2,slot3,slot4,slot5,slot6 = st.tabs(['Slot 1', 'Slot 2', 'Slot 3', 'Slot 4', 'Slot 5', 'Medallions'])
            with slot1: st.write(text.split('\n\n\n')[0])
            with slot2: st.write(text.split('\n\n\n')[1])
            with slot3: st.write(text.split('\n\n\n')[2])
            with slot4: st.write(text.split('\n\n\n')[3])
            with slot5: st.write(text.split('\n\n\n')[4])
            with slot6: st.write(text.split('\n\n\n')[5])
            if st.button("Exit"): st.rerun()
        if os.path.exists(os.path.join('configs', 'AutoConfig_Generator.txt')):
            with open(os.path.join('configs', 'AutoConfig_Generator.txt'), 'r') as f: g = f.readlines()
            for i in range(len(g)):
                line_data = eval(g[i])
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button(f'Loadout {i+1}', help=f'Load config {i+1}', use_container_width=True): slotone_weapon, slotone_rarity, slotoneattachment1, slotoneattachment2, slotoneattachment3, slotoneattachment4 = (line_data.get('slot1'))[0].split('[')[1].split(']')[0], (line_data.get('slot1'))[1].split('[')[1].split(']')[0], (line_data.get('slot1'))[2].split('[')[1].split(']')[0], (line_data.get('slot1'))[3].split('[')[1].split(']')[0], (line_data.get('slot1'))[4].split('[')[1].split(']')[0], (line_data.get('slot1'))[5].split('[')[1].split(']')[0]; slottwo_weapon, slottwo_rarity, slottwoattachment1, slottwoattachment2, slottwoattachment3, slottwoattachment4 = (line_data.get('slot2'))[0].split('[')[1].split(']')[0], (line_data.get('slot2'))[1].split('[')[1].split(']')[0], (line_data.get('slot2'))[2].split('[')[1].split(']')[0], (line_data.get('slot2'))[3].split('[')[1].split(']')[0], (line_data.get('slot2'))[4].split('[')[1].split(']')[0], (line_data.get('slot2'))[5].split('[')[1].split(']')[0]; slotthree_weapon, slotthree_rarity, slotthreeattachment1, slotthreeattachment2, slotthreeattachment3, slotthreeattachment4 = (line_data.get('slot3'))[0].split('[')[1].split(']')[0], (line_data.get('slot3'))[1].split('[')[1].split(']')[0], (line_data.get('slot3'))[2].split('[')[1].split(']')[0], (line_data.get('slot3'))[3].split('[')[1].split(']')[0], (line_data.get('slot3'))[4].split('[')[1].split(']')[0], (line_data.get('slot3'))[5].split('[')[1].split(']')[0]; slotfour_weapon, slotfour_rarity, slotfourattachment1, slotfourattachment2, slotfourattachment3, slotfourattachment4 = (line_data.get('slot4'))[0].split('[')[1].split(']')[0], (line_data.get('slot4'))[1].split('[')[1].split(']')[0], (line_data.get('slot4'))[2].split('[')[1].split(']')[0], (line_data.get('slot4'))[3].split('[')[1].split(']')[0], (line_data.get('slot4'))[4].split('[')[1].split(']')[0], (line_data.get('slot4'))[5].split('[')[1].split(']')[0]; slotfive_weapon, slotfive_rarity, slotfiveattachment1, slotfiveattachment2, slotfiveattachment3, slotfiveattachment4 = (line_data.get('slot5'))[0].split('[')[1].split(']')[0], (line_data.get('slot5'))[1].split('[')[1].split(']')[0], (line_data.get('slot5'))[2].split('[')[1].split(']')[0], (line_data.get('slot5'))[3].split('[')[1].split(']')[0], (line_data.get('slot5'))[4].split('[')[1].split(']')[0], (line_data.get('slot5'))[5].split('[')[1].split(']')[0]; Medallion=(line_data.get("other"))[0]; medallions_amount_text=(line_data.get("other"))[1].split(": ")[1]; selected_meddalions_amount=(line_data.get("other"))[2].split(': ')[1]; t1.write(f'# :violet[Items]  \n##### Slot 1 : :green[{slotone_weapon}]\n#####    Slot 2 : :green[{slottwo_weapon}]\n#####    Slot 3 : :green[{slotthree_weapon}]\n#####    Slot 4 : :green[{slotfour_weapon}]\n#####    Slot 5 : :green[{slotfive_weapon}]\n#####    Medallions : :blue[{Medallion}]');  t2.write(f'# Items\n    Slot 1 : {slotone_weapon}\n    Slot 2 : {slottwo_weapon}\n    Slot 3 : {slotthree_weapon}\n    Slot 4 : {slotfour_weapon}\n    Slot 5 : {slotfive_weapon}\n    Medallions : {Medallion}');  t3.json({'Items': [f'Slot 1 : {slotone_weapon}', f'Slot 2 : {slottwo_weapon}', f'Slot 3 : {slotthree_weapon}', f'Slot 4 : {slotfour_weapon}', f'Slot 5 : {slotfive_weapon}', f'Medallions : {Medallion}'],});  tt1.write(f'# :violet[Rarity]  \n##### Slot 1 : :orange[{slotone_rarity}]\n#####    Slot 2 : :orange[{slottwo_rarity}]\n#####    Slot 3 : :orange[{slotthree_rarity}]\n#####    Slot 4 : :orange[{slotfour_rarity}]\n#####    Slot 5 : :orange[{slotfive_rarity}]\n#####    Medallions amount : :blue[{medallions_amount_text}] (current: :blue[{selected_meddalions_amount}])');  tt2.write(f'# Rarity\n    Slot 1 : {slotone_rarity}\n    Slot 2 : {slottwo_rarity}\n    Slot 3 : {slotthree_rarity}\n    Slot 4 : {slotfour_rarity}\n    Slot 5 : {slotfive_rarity}\n    Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount})');  tt3.json({'Rarity': [f'Slot 1 : {slotone_rarity}', f'Slot 2 : {slottwo_rarity}', f'Slot 3 : {slotthree_rarity}', f'Slot 4 : {slotfour_rarity}', f'Slot 5 : {slotfive_rarity}', f'Medallions amount : {medallions_amount_text} (current: {selected_meddalions_amount}'], });  ttt1.write(f'# :violet[Attachments]  \n##### Slot 1 : :red[{slotoneattachment1}], :red[{slotoneattachment2}], :red[{slotoneattachment3}], :red[{slotoneattachment4}]\n#####    Slot 2 : :red[{slottwoattachment1}], :red[{slottwoattachment2}], :red[{slottwoattachment3}], :red[{slottwoattachment4}]\n#####    Slot 3 : :red[{slotthreeattachment1}], :red[{slotthreeattachment2}], :red[{slotthreeattachment3}], :red[{slotthreeattachment4}]\n#####    Slot 4 : :red[{slotfourattachment1}], :red[{slotfourattachment2}], :red[{slotfourattachment3}], :red[{slotfourattachment4}]\n#####    Slot 5 : :red[{slotfiveattachment1}], :red[{slotfiveattachment2}], :red[{slotfiveattachment3}], :red[{slotfiveattachment4}]');  ttt2.write(f'# Attachments\n    Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}\n    Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}\n    Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}\n    Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}\n    Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}'); ttt3.json({'Attachments': [f'Slot 1 : {slotoneattachment1}, {slotoneattachment2}, {slotoneattachment3}, {slotoneattachment4}', f'Slot 2 : {slottwoattachment1}, {slottwoattachment2}, {slottwoattachment3}, {slottwoattachment4}', f'Slot 3 : {slotthreeattachment1}, {slotthreeattachment2}, {slotthreeattachment3}, {slotthreeattachment4}', f'Slot 4 : {slotfourattachment1}, {slotfourattachment2}, {slotfourattachment3}, {slotfourattachment4}', f'Slot 5 : {slotfiveattachment1}, {slotfiveattachment2}, {slotfiveattachment3}, {slotfiveattachment4}'], }); st.toast(f':red[AutoConfig]\n\n:blue[Loaded configuration] from file: :orange[configs\\AutoConfig_Generator.txt]', icon="✨")
                with col2:
                    if st.button('Loadout preview', help=f'Preview the loadout for slot {i+1}', use_container_width=True): preview(f'Item: :green[{(line_data.get("slot1"))[0].split("[")[1].split("]")[0]}]\n\nRarity: :orange[{(line_data.get("slot1"))[1].split("[")[1].split("]")[0]}]\n\nAttachments: :red[{(line_data.get("slot1"))[2].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot1"))[3].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot1"))[4].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot1"))[5].split("[")[1].split("]")[0]}]\n\n\nItem: :green[{(line_data.get("slot2"))[0].split("[")[1].split("]")[0]}]\n\nRarity: :orange[{(line_data.get("slot2"))[1].split("[")[1].split("]")[0]}]\n\nAttachments: :red[{(line_data.get("slot2"))[2].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot2"))[3].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot2"))[4].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot2"))[5].split("[")[1].split("]")[0]}]\n\n\nItem: :green[{(line_data.get("slot3"))[0].split("[")[1].split("]")[0]}]\n\nRarity: :orange[{(line_data.get("slot3"))[1].split("[")[1].split("]")[0]}]\n\nAttachments: :red[{(line_data.get("slot3"))[2].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot3"))[3].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot3"))[4].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot3"))[5].split("[")[1].split("]")[0]}]\n\n\nItem: :green[{(line_data.get("slot4"))[0].split("[")[1].split("]")[0]}]\n\nRarity: :orange[{(line_data.get("slot4"))[1].split("[")[1].split("]")[0]}]\n\nAttachments: :red[{(line_data.get("slot4"))[2].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot4"))[3].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot4"))[4].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot4"))[5].split("[")[1].split("]")[0]}]\n\n\nItem: :green[{(line_data.get("slot5"))[0].split("[")[1].split("]")[0]}]\n\nRarity: :orange[{(line_data.get("slot5"))[1].split("[")[1].split("]")[0]}]\n\nAttachments: :red[{(line_data.get("slot5"))[2].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot5"))[3].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot5"))[4].split("[")[1].split("]")[0]}], :red[{(line_data.get("slot5"))[5].split("[")[1].split("]")[0]}]\n\n\n:blue[{(line_data.get("other"))[0]}]\n\n:blue[{(line_data.get("other"))[1]}]\n\n:blue[{(line_data.get("other"))[2]}]')
                with col3:
                    if st.button(':red[Remove loadout]', help=f'Remove loadout {i+1}', use_container_width=True):
                        st.session_state.deleted_loadout_index = i
                        if st.session_state.deleted_loadout_index is not None:
                            i = st.session_state.deleted_loadout_index
                            with open(os.path.join('configs', 'AutoConfig_Generator.txt'), 'r') as f: lines = f.readlines()
                            with open(os.path.join('configs', 'AutoConfig_Generator.txt'), 'w') as f:
                                for index, line in enumerate(lines):
                                    if index != i: f.write(line)
                            st.toast('Loadout deleted.'); st.session_state.deleted_loadout_index = None; st.rerun()
                if i+1 != len(g): st.divider()

                        
        else: st.toast(':red[AutoConfig]\n\nCreated file :orange[Configs\\AutoConfig_Generator.txt]\n\nReason: File missing.'); f = open(os.path.join('configs', 'AutoConfig_Generator.txt'), 'a'); f.close()
with Weapon_Info:
    st.caption('Thank you Osirion for actually having good data about weapons')
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander('Frenzy Auto Shotgun'):
            col1_,_,col2_ = st.columns(3)
            with col1_: st.caption('Hover over the raritys for more info', help='Hovering over the raritys will say what rarity it is coresponding to each letter (Rarity).')
            with col2_: button=st.checkbox('Show image', help='Enabling this will show you an image of the Frenzy Auto Shotgun.')
            if button: st.image(images.get('Frenzy Auto Shotgun'), use_column_width=True)
            st.subheader("Weapon info", divider='rainbow')
            col1expanded,col2expanded,col3expanded,col4expanded,col5expanded = st.columns(5)
            with col1expanded:
                with st.popover(':gray[C]', help='Rarity: Common', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 61 Damage'); tab21.write('# 100.65 Headshot Damage'); tab31.write('# 2.2S Firerate'); tab41.write('# 8 Clip Size'); tab51.write('# 5.17S Reload Time')
            with col2expanded:
                with st.popover(':green[U]', help='Rarity: Uncommon', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 65 Damage'); tab21.write('# 107.25 Headshot Damage'); tab31.write('# 2.2S Firerate'); tab41.write('# 8 Clip Size'); tab51.write('# 4.93S Reload Time')
            with col3expanded:
                with st.popover(':blue[R]', help='Rarity: Rare', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 68 Damage'); tab21.write('# 112.2 Headshot Damage'); tab31.write('# 2.2 Firerate'); tab41.write('# 8 Clip Size'); tab51.write('# 4.7S Reload Time')
            with col4expanded:
                with st.popover(':violet[E]', help='Rarity: Epic', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 71 Damage'); tab21.write('# 117.15 Headshot Damage'); tab31.write('# 2.2 Firerate'); tab41.write('# 8 Clip Size'); tab51.write('# 4.46S Reload Time')
            with col5expanded:
                with st.popover(':orange[L]', help='Rarity: Legendary', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 75 Damage'); tab21.write('# 123.75 Headshot Damage'); tab31.write('# 2.2 Firerate'); tab41.write('# 8 Clip Size'); tab51.write('# 4.23S Reload Time')
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
                    with st.popover('Barrel', use_container_width=True): st.write('Muzzle Brake: ✅'); st.write('Suppressor: ✅')
    with col2:
        with st.expander('Hammer Pump Shotgun'):
            col1_,_,col2_ = st.columns(3)
            with col1_: st.caption('Hover over the raritys for more info', help='Hovering over the raritys will say what rarity it is coresponding to each letter (Rarity).')
            with col2_: button=st.checkbox('Show image', help='Enabling this will show you an image of the Hammer Pump Shotgun.')
            if button: st.image(images.get('Hammer Pump Shotgun'), use_column_width=True)
            st.subheader("Weapon info", divider='rainbow')
            col1expanded,col2expanded,col3expanded,col4expanded,col5expanded = st.columns(5)
            with col1expanded:
                with st.popover(':gray[C]', help='Rarity: Common', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 85 Damage'); tab21.write('# 157.25 Headshot Damage'); tab31.write('# 0.7 Firerate'); tab41.write('# 6 Clip Size'); tab51.write('# 5.78S Reload Time')
            with col2expanded:
                with st.popover(':green[U]', help='Rarity: Uncommon', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 89 Damage'); tab21.write('# 164.65 Headshot Damage'); tab31.write('# 0.7 Firerate'); tab41.write('# 6 Clip Size'); tab51.write('# 5.51S Reload Time')
            with col3expanded:
                with st.popover(':blue[R]', help='Rarity: Rare', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 94 Damage'); tab21.write('# 173.9 Headshot Damage'); tab31.write('# 0.7 Firerate'); tab41.write('# 6 Clip Size'); tab51.write('# 5.25S Reload Time')
            with col4expanded:
                with st.popover(':violet[E]', help='Rarity: Epic', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 99 Damage'); tab21.write('# 183.15 Headshot Damage'); tab31.write('# 0.7 Firerate'); tab41.write('# 6 Clip Size'); tab51.write('# 4.99S Reload Time')
            with col5expanded:
                with st.popover(':orange[L]', help='Rarity: Legendary', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 103 Damage'); tab21.write('# 190.55 Headshot Damage'); tab31.write('# 0.7 Firerate'); tab41.write('# 6 Clip Size'); tab51.write('# 4.72S Reload Time')
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
            if button: st.image(images.get('Gatekeeper Shotgun'), use_column_width=True)
            st.subheader("Weapon info", divider='rainbow')
            col1expanded,col2expanded,col3expanded,col4expanded,col5expanded,col6expanded = st.columns(6)
            with col1expanded:
                with st.popover(':gray[C]', help='Rarity: :gray[Common]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 76 Damage'); tab21.write('# 114 Headshot Damage'); tab31.write('# 1.7 Firerate'); tab41.write('# 3 Clip Size'); tab51.write('# 2.75S reload Time')
            with col2expanded:
                with st.popover(':green[U]', help='Rarity: :green[Uncommon]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 80 Damage'); tab21.write('# 120 Headshot Damage'); tab31.write('# 1.7 Firerate'); tab41.write('# 3 Clip Size') ; tab51.write('# 2.63S Reload Time')
            with col3expanded:
                with st.popover(':blue[R]', help='Rarity: :blue[Rare]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 84 Damage'); tab21.write('# 126 Headshot Damage'); tab31.write('# 1.7 Firerate'); tab41.write('# 3 Clip Size') ; tab51.write('# 2.5S Reload Time')
            with col4expanded:
                with st.popover(':violet[E]', help='Rarity: :violet[Epic]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 88 Damage'); tab21.write('# 132 Headshot Damage'); tab31.write('# 1.7 Firerate'); tab41.write('# 3 Clip Size') ; tab51.write('# 2.38S Reload Time')
            with col5expanded:
                with st.popover(':orange[L]', help='Rarity: :orange[Legendary]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 92 Damage'); tab21.write('# 138 Headshot Damage'); tab31.write('# 1.7 Firerate'); tab41.write('# 3 Clip Size') ; tab51.write('# 2.25S Reload Time')
            with col6expanded:
                with st.popover(':red[M]', help='Rarity: :red[Mythic]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 97 Damage'); tab21.write('# 145.5 Headshot Damage'); tab31.write('# 1.7 Firerate'); tab41.write('# 3 Clip Size') ; tab51.write('# 2.13S Reload Time')  
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
            if button: st.image(images.get('Warforged Assault Rifle'), use_column_width=True)
            st.subheader("Weapon info", divider='rainbow')
            col1expanded,col2expanded,col3expanded,col4expanded,col5expanded,col6expanded = st.columns(6)
            with col1expanded:
                with st.popover(':gray[C]', help='Rarity: :gray[Common]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 24 Damage'); tab21.write('# 36 Headshot Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Clip Size'); tab51.write('# 3.85S Reload Time')
            with col2expanded:
                with st.popover(':green[U]', help='Rarity: :green[Uncommon]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 26 Damage'); tab21.write('# 39 Headshot Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Clip Size') ; tab51.write('# 3.68S Reload Time')
            with col3expanded:
                with st.popover(':blue[R]', help='Rarity: :blue[Rare]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 27 Damage'); tab21.write('# 40.5 Headshot Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Clip Size') ; tab51.write('# 3.5S Reload Time')
            with col4expanded:
                with st.popover(':violet[E]', help='Rarity: :violet[Epic]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 28 Damage'); tab21.write('# 42 Headshot Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Clip Size') ; tab51.write('# 3.33S Reload Time')
            with col5expanded:
                with st.popover(':orange[L]', help='Rarity: :orange[Legendary]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 30 Damage'); tab21.write('# 45 Headshot Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Clip Size') ; tab51.write('# 3.15S Reload Time')
            with col6expanded:
                with st.popover(':red[M]', help='Rarity: :red[Mythic]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 31 Damage'); tab21.write('# 46.5 Headshot Damage'); tab31.write('# 7.2 Firerate'); tab41.write('# 35 Clip Size') ; tab51.write('# 2.98S Reload Time')  
            st.subheader("Weapon attachments info", divider='rainbow')
            with st.container(border=True):
                col1info,col2info,col3info,col4info = st.columns(4)
                with col1info: 
                    with st.popover('Optic', use_container_width=True): st.write('Red Eye Sight: ✅'); st.write('Holo-13 Optic: ✅'); st.write('P2X Optic: ✅'); st.write('Thermal Optic: ✅'); st.write('Sniper Optic: ✅')
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
            if button: st.image(images.get('Nemesis AR'), use_column_width=True)
            st.subheader("Weapon info", divider='rainbow')
            col1expanded,col2expanded,col3expanded,col4expanded,col5expanded = st.columns(5)
            with col1expanded:
                with st.popover(':gray[C]', help='Rarity: :gray[Common]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 29 Damage'); tab21.write('# 43.5 Headshot Damage'); tab31.write('# 5 Firerate'); tab41.write('28 Clip Size'); tab51.write('# 2.75S Reload Time')
            with col2expanded:
                with st.popover(':green[U]', help='Rarity: :green[Uncommon]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 30 Damage'); tab21.write('# 45 Headshot Damage'); tab31.write('# 5 Firerate'); tab41.write('28 Clip Size'); tab51.write('# 2.63S Reload Time')
            with col3expanded:
                with st.popover(':blue[R]', help='Rarity: :blue[Rare]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 32 Damage'); tab21.write('# 48 Headshot Damage'); tab31.write('# 5 Firerate'); tab41.write('28 Clip Size'); tab51.write('# 2.5S Reload Time')
            with col4expanded:
                with st.popover(':violet[E]', help='Rarity: :violet[Epic]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 34 Damage'); tab21.write('# 51 Headshot Damage'); tab31.write('# 5 Firerate'); tab41.write('28 Clip Size'); tab51.write('# 2.38S Reload Time')
            with col5expanded:
                with st.popover(':orange[L]', help='Rarity: :orange[Legendary]', use_container_width=True): tab11,tab21,tab31,tab41,tab51 = st.tabs(['Damage', 'Headshot Damage', 'Firerate', 'Clip Size', 'Reload Time']); tab11.write('# 35 Damage'); tab21.write('# 52.5 Headshot Damage'); tab31.write('# 5 Firerate'); tab41.write('28 Clip Size'); tab51.write('# 2.35S Reload Time')
            st.subheader("Weapon attachments info", divider='rainbow')
            with st.container(border=True):
                col1info,col2info,col3info,col4info = st.columns(4)
                with col1info: 
                    with st.popover('Optic', use_container_width=True): st.write('Red Eye Sight: ✅'); st.write('Holo-13 Optic: ✅'); st.write('P2X Optic: ✅'); st.write('Thermal Optic: ✅'); st.write('Sniper Optic: ✅')
                with col2info:
                    with st.popover('Magazine', use_container_width=True): st.write('Drum Mag: ✅'); st.write('Speed Mag: ✅')
                with col3info:
                    with st.popover('Underbarrel', use_container_width=True): st.write('Angled Foregrip: ✅'); st.write('Vertical Foregrip: ✅'); st.write('Laser: ✅'); st.write('Speed Foregrip: ✅')
                with col4info:
                    with st.popover('Barrel', use_container_width=True): st.write('Muzzle Brake: ✅'); st.write('Suppressor: ✅')
    st.divider()
with st.sidebar: st.page_link("http://www.Github.com/fuzzybuzzyboy/py", label="Github", icon="🛢️")
#with st.sidebar:
#    st.page_link("http://www.Github.com/fuzzybuzzyboy/py", label="Github", icon="🛢️")
#    if st.button('Clock'):
#        with st.empty():
#            while True:
#                time_now1, time_now = datetime.now().strftime("%D"), datetime.now().strftime("%H:%M:%S")
#                st.write(f'# Clock\n    Time : {time_now}\n    Date : {time_now1}')
#                time.sleep(1)
