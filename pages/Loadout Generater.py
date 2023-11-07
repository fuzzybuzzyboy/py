from datetime import datetime
import random, time, os, platform, streamlit as st

st.set_page_config(
    page_title='Loadout Generater',
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help': 'https://github.com/fuzzybuzzyboy/py',
        'Report a bug': "https://github.com/fuzzybuzzyboy/py",
        'About': "Random items generator for fortnite (no this doesn't inject into your game and do something blah blah blah)"
    }
)

login = f'{platform.node()}_Gen'
Folder_Path = "configs"
File_Path = os.path.join(Folder_Path, login,)

code = '''https://github.com/fuzzybuzzyboy/py'''
Shotgun_Type = 'None'
Shotgun_Rarity = 'None'
Assualt_Rifle_Type = 'None'
Assualt_Rifle_Rarity = 'None'
SMG_Type = 'None'
SMG_Rarity = 'None'
Snipers_Type = 'None'
Snipers_Rarity = 'None'
Explosives_Type = 'None'
Explosives_Rarity = 'None'
Other_Type = 'None'
Other_Rarity = 'None'
button = 1

Shotgun_on = st.toggle('Shotguns')
Assualt_Rifle_on = st.toggle('Assault-Rifles')
SMG_on = st.toggle('SMG')
Snipers_on = st.toggle('Snipers')
Explosives_on = st.toggle('Explosives')
Other_on = st.toggle('Other')

st.divider()
for i in range(button):
    Shotgun_Type_Weapon = random.randint(1, 2)
    Shotgun_Type_Weapon_2 = random.randint(1, 2)
    Assualt_Type_Weapon = random.randint(1, 4)
    Assualt_Type_Weapon_2 = random.randint(1, 2)
    SMG_Type_Weapon = random.randint(1, 4)
    SMG_Type_Weapon_2 = random.randint(1, 2)
    Snipers_Type_Weapon = random.randint(1, 3)
    Other_Type_Weapon = random.randint(1, 2)
    button = 0
    if Shotgun_on:
        if Shotgun_Type_Weapon == 1:
            Shotgun_Type_Rarity = random.randint(1, 5)
            if Shotgun_Type_Weapon_2 == 1:
                Shotgun_Type = 'Tactical Shotgun'
            elif Shotgun_Type_Weapon_2 == 2:
                Shotgun_Type = 'Pump Shotgun'
            if Shotgun_Type_Rarity == 1:
                Shotgun_Rarity = 'Common'
            elif Shotgun_Type_Rarity == 2:
                Shotgun_Rarity = 'Uncommon'
            elif Shotgun_Type_Rarity == 3:
                Shotgun_Rarity = 'Rare'
            elif Shotgun_Type_Rarity == 4:
                Shotgun_Rarity = 'Epic'
            elif Shotgun_Type_Rarity == 5:
                Shotgun_Rarity = 'Legendary'
        if Shotgun_Type_Weapon == 2:
            Shotgun_Type = 'Heavy Shotgun'
            Shotgun_Type_Rarity = random.randint(1, 2)
            if Shotgun_Type_Rarity == 1:
                Shotgun_Rarity = 'Epic'
            elif Shotgun_Type_Rarity == 2:
                Shotgun_Rarity = 'Legendary'
    if Assualt_Rifle_on:
        if Assualt_Type_Weapon == 1:
            Assualt_Rifle_Type_Rarity = random.randint(1, 3)
            Assualt_Rifle_Type = 'Suppressed Assualt Rifle'
            if Assualt_Rifle_Type_Rarity == 1:
                Assualt_Rifle_Rarity = 'Rare'
            elif Assualt_Rifle_Type_Rarity == 2:
                Assualt_Rifle_Rarity = 'Epic'
            elif Assualt_Rifle_Type_Rarity == 3:
                Assualt_Rifle_Rarity = 'Legendary'
        elif Assualt_Type_Weapon == 2:
            Assualt_Rifle_Type_Rarity = random.randint(1, 5)
            if Assualt_Type_Weapon_2 == 1:
                Assualt_Rifle_Type = 'Assault Rifle'
            elif Assualt_Type_Weapon_2 == 2:
                Assualt_Rifle_Type = 'Burst Assualt Rifle'
            if Assualt_Type_Weapon == 1:
                Assualt_Rifle_Rarity = 'Common'
            elif Assualt_Type_Weapon == 2:
                Assualt_Rifle_Rarity = 'Uncommon'
            elif Assualt_Type_Weapon == 3:
                Assualt_Rifle_Rarity = 'Rare'
            elif Assualt_Type_Weapon == 4:
                Assualt_Rifle_Rarity = 'Epic'
            elif Assualt_Type_Weapon == 5:
                Assualt_Rifle_Rarity = 'Legendary'
        elif Assualt_Type_Weapon == 3:
            Assualt_Rifle_Type_Rarity = 1
            Assualt_Rifle_Type = 'Tactical Assualt Rifle'
            Assualt_Rifle_Rarity = 'Legendary'
        elif Assualt_Type_Weapon == 4:
            Assualt_Rifle_Type_Rarity = random.randint(1, 4)
            Assualt_Rifle_Type = 'Scoped Assualt Rifle'
            if Assualt_Rifle_Type_Rarity == 1:
                Assualt_Rifle_Rarity = 'Uncommon'
            elif Assualt_Rifle_Type_Rarity == 2:
                Assualt_Rifle_Rarity = 'Rare'
            elif Assualt_Rifle_Type_Rarity == 3:
                Assualt_Rifle_Rarity = 'Epic'
            elif Assualt_Rifle_Type_Rarity == 4:
                Assualt_Rifle_Rarity = 'Legendary'
    if SMG_on:
        if SMG_Type_Weapon == 1:
            SMG_Type_Rarity = random.randint(1, 5)
            SMG_Type = 'Submachine Gun'
            if SMG_Type_Rarity == 1:
                SMG_Rarity = 'Common'
            elif SMG_Type_Rarity == 2:
                SMG_Rarity = 'Uncommon'
            elif SMG_Type_Rarity == 3:
                SMG_Rarity = 'Rare'
            elif SMG_Type_Rarity == 4:
                SMG_Rarity = 'Epic'
            elif SMG_Type_Rarity == 5:
                SMG_Rarity = 'Legendary'
        elif SMG_Type_Weapon == 2 or SMG_Type_Weapon == 3:
            SMG_Type_Rarity = random.randint(1, 3)
            if SMG_Type_Weapon_2 == 1:
                SMG_Type = 'Suppressed Submachine Gun'
            elif SMG_Type_Weapon_2 == 2:
                SMG_Type = 'Pistol'
            if SMG_Type_Rarity == 1:
                SMG_Rarity = 'Common'
            elif SMG_Type_Rarity == 2:
                SMG_Rarity = 'Uncommon'
            elif SMG_Type_Rarity == 3:
                SMG_Rarity = 'Rare'
        elif SMG_Type_Weapon == 4:
            SMG_Type_Rarity = random.randint(1, 2)
            SMG_Type = 'Suppressed Pistol'
            if SMG_Type_Rarity == 1:
                SMG_Rarity = 'Rare'
            elif SMG_Type_Rarity == 2:
                SMG_Rarity = 'Epic'
    if Snipers_on:
        if Snipers_Type_Weapon == 1:
            Snipers_Type = 'Hunting Rifle'
            Snipers_Type_Rarity = random.randint(1, 4)
            if Snipers_Type_Rarity == 1:
                Snipers_Rarity = 'Uncommon'
            elif Snipers_Type_Rarity == 2:
                Snipers_Rarity = 'Rare'
            elif Snipers_Type_Rarity == 3:
                Snipers_Rarity = 'Epic'
            elif Snipers_Type_Rarity == 4:
                Snipers_Rarity = 'Legendary'
        elif Snipers_Type_Weapon == 2:
            Snipers_Type = 'Bolt-Action Sniper Rifle'
            Snipers_Type_Rarity = random.randint(1, 3)
            if Snipers_Type_Rarity == 1:
                Snipers_Rarity = 'Rare'
            elif Snipers_Type_Rarity == 2:
                Snipers_Rarity = 'Epic'
            elif Snipers_Type_Rarity == 3:
                Snipers_Rarity = 'Legendary'
        elif Snipers_Type_Weapon == 3:
            Snipers_Type = 'Semi-Automatic Sniper Rifle'
            Snipers_Type_Rarity = random.randint(1, 2)
            if Snipers_Type_Rarity == 1:
                Snipers_Rarity = 'Uncommon'
            elif Snipers_Type_Rarity == 2:
                Snipers_Rarity = 'Rare'
    if Explosives_on:
        Explosives_Type_Weapon = random.randint(1, 2)
        Explosives_Type_Rarity = random.randint(1, 3)
        if Explosives_Type_Weapon == 1:
            Explosives_Type = 'Rocket Launcher'
        elif Explosives_Type_Weapon == 2:
            Explosives_Type = 'Grenade Launcher'
        if Explosives_Type_Rarity == 1:
            Explosives_Rarity = 'Rare'
        elif Explosives_Type_Rarity == 2:
            Explosives_Rarity = 'Epic'
        elif Explosives_Type_Rarity == 3:
            Explosives_Rarity = 'Legendary'
    if Other_on:
        Other_Type_Rarity = random.randint(1, 2)
        if Other_Type_Weapon == 1:
            Other_Type = 'Light Machine Gun'
            if Other_Type_Rarity == 1:
                Other_Rarity = 'Rare'
            elif Other_Type_Rarity == 2:
                Other_Rarity = 'Epic'
        elif Other_Type_Weapon == 2:
            Other_Type = 'Hand Cannon'
            if Other_Type_Rarity == 1:
                Other_Rarity = 'Epic'
            elif Other_Type_Rarity == 2:
                Other_Rarity = 'Legendary'

col1, col2 = st.columns(2)
with col1:
    tab1b, tab2b, tab3b = st.tabs(["Base", "Regular", "Json"])
    with tab1b:
        t1 = st.empty()
        t1.write(f'# Load-Out\n    Shotgun : {Shotgun_Type}\n    Assault Rifle : {Assualt_Rifle_Type}\n    SMG : {SMG_Type}\n    Sniper : {Snipers_Type}\n    Explosives : {Explosives_Type}\n    Other : {Other_Type}')
    with tab2b:
        t2 = st.empty()
        t2.write(f'# Load-Out  \n##### Shotgun : {Shotgun_Type}\n#####    Assault Rifle : {Assualt_Rifle_Type}\n#####    Smg : {SMG_Type}\n#####    Sniper : {Snipers_Type}\n#####    Explosives : {Explosives_Type}\n#####    Other : {Other_Type}')
    with tab3b:
        t3 = st.empty()
        t3.json({
            'Load-Out': [
                f'Shotgun : {Shotgun_Type}',
                f'Assault Rifle : {Assualt_Rifle_Type}',
                f'SMG : {SMG_Type}',
                f'Sniper : {Snipers_Type}',
                f'Explosives : {Explosives_Type}',
                f'Other : {Other_Type}'
            ],
        })
with col2:
        taba1, taba2, taba3 = st.tabs(["Base", "Regular", "Json"])
        with taba1:
            tt1 = st.empty()
            tt1.write(f'# Rarity\n    Shotgun : {Shotgun_Rarity}\n    Assault Rifle : {Assualt_Rifle_Rarity}\n    SMG : {SMG_Rarity}\n    Sniper : {Snipers_Rarity}\n    Explosives : {Explosives_Rarity}\n    Other : {Other_Rarity}')
        with taba2:
            tt2 = st.empty()
            tt2.write(f'# Rarity  \n##### Shotgun : {Shotgun_Rarity}\n#####    Assault Rifle : {Assualt_Rifle_Rarity}\n#####    SMG : {SMG_Rarity}\n#####    Sniper : {Snipers_Rarity}\n#####    Explosives : {Explosives_Rarity}\n#####    Other : {Other_Rarity}')
        with taba3:
            tt3 = st.empty()
            tt3.json({
                'Rarity': [
                    f'Shotgun : {Shotgun_Rarity}',
                    f'Assault Rifle : {Assualt_Rifle_Rarity}',
                    f'SMG : {SMG_Rarity}',
                    f'Sniper : {Snipers_Rarity}'
                    f'Explosives : {Explosives_Rarity}',
                    f'Other : {Other_Rarity}'
                ],
            })
st.divider()
def save():
    if os.path.exists(f"{File_Path}.txt"):
        os.remove(f"{File_Path}.txt")
        f = open(f"{File_Path}.txt", "a")          # here                                        # here                    # here                            # here                                  # here
        f.write(f'{Shotgun_Type}\n{Shotgun_Rarity}\n{Assualt_Rifle_Type}\n{Assualt_Rifle_Rarity}\n{SMG_Type}\n{SMG_Rarity}\n{Snipers_Type}\n{Snipers_Rarity}\n{Explosives_Type}\n{Explosives_Rarity}\n{Other_Type}\n{Other_Rarity}')
        f.close()
    else:
        f = open(f"{File_Path}.txt", "a")          # here                                        # here                    # here                            # here                                  # here
        f.write(f'{Shotgun_Type}\n{Shotgun_Rarity}\n{Assualt_Rifle_Type}\n{Assualt_Rifle_Rarity}\n{SMG_Type}\n{SMG_Rarity}\n{Snipers_Type}\n{Snipers_Rarity}\n{Explosives_Type}\n{Explosives_Rarity}\n{Other_Type}\n{Other_Rarity}')
        f.close()
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

        if len(lines) == 12:
            Shotgun_Type = lines[0]
            Shotgun_Rarity = lines[1]
            Assualt_Rifle_Type = lines[2]
            Assualt_Rifle_Rarity = lines[3]
            SMG_Type = lines[4]
            SMG_Rarity = lines[5]
            Snipers_Type = lines[6]
            Snipers_Rarity = lines[7]
            Explosives_Type = lines[8]
            Explosives_Rarity = lines[9]
            Other_Type = lines[10]
            Other_Rarity = lines[11]

            # These prints are just here if you want to get more info. Just remove the '#' from them and then check your CMD, they will show up there as well

            # print("Loaded configuration with success:")
            # print(f"Slot one : {slotone}, {slotoner}, {slotone1}\nSlot two : {slottwo}, {slottwor}, {slottwo1}\nSlot three : {slotthree}, {slotthreer}, {slotthree1}\nSlot four : {slotfour}, {slotfourr}, {slotfour1}\nSlot five : {slotfive}, {slotfiver}, {slotfive1}")

            # RARITY

            t1.write(
                f'# Custom loadout rarity\n    Shotgun : {Shotgun_Type}\n    Assault Rifle : {Assualt_Rifle_Type}\n    SMG : {SMG_Type}\n    Sniper : {Snipers_Type}\n    Explosives : {Explosives_Type}\n    Other : {Other_Type}')
            t2.write(
                f'# Custom loadout rarity  \n##### Shotgun : {Shotgun_Type}\n#####    Assault Rifle : {Assualt_Rifle_Type}\n#####    SMG : {SMG_Type}\n#####    Sniper : {Snipers_Type}\n#####    Explosives : {Explosives_Type}\n#####    Other : {Other_Type}')
            t3.json({
                'Custom loadout rarity': [
                    f'Shotgun : {Shotgun_Type}',
                    f'Assault Rifle : {Assualt_Rifle_Type}',
                    f'SMG : {SMG_Type}',
                    f'Sniper : {Snipers_Type}',
                    f'Explosives : {Explosives_Type}',
                    f'Other : {Other_Type}'
                ],
            })

            # WEAPONS

            tt1.write(
                f'# Custom loadout\n    Shotgun : {Shotgun_Rarity}\n    Assault Rifle : {Assualt_Rifle_Rarity}\n    SMG : {SMG_Rarity}\n    Sniper : {Snipers_Rarity}\n    Explosives : {Explosives_Rarity}\n    Other : {Other_Rarity}')
            tt2.write(
                f'# Custom loadout  \n##### Shotgun : {Shotgun_Rarity}\n#####    Assault Rifle : {Assualt_Rifle_Rarity}\n#####    SMG : {SMG_Rarity}\n#####    Sniper : {Snipers_Rarity}\n#####    Explosives : {Explosives_Rarity}\n#####    Other : {Other_Rarity}')
            tt3.json({
                'Custom loadout': [
                    f'Shotgun : {Shotgun_Rarity}',
                    f'Assault Rifle : {Assualt_Rifle_Rarity}',
                    f'SMG : {SMG_Rarity}',
                    f'Sniper : {Snipers_Rarity}',
                    f'Explosives : {Explosives_Rarity}',
                    f'Other : {Other_Rarity}'
                ],
            })
            st.success(f"Loaded configuration from \'{File_Path}.txt\'", icon="✅")
        else:
            st.error("Invalid configuration file. Expected 12 lines.")
    else:
        st.error("File doesn't exist. Please create/save a configuration.")
st.divider()
if st.button('Randomize Load-Out'):
    button = + 1
else:
    pass
with st.sidebar:
    st.code(f'Code at : \n{code}', language='Text')
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
                    time.sleep(1)
