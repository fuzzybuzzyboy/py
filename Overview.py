
)
Folder_Path = "configs"
File_Path = os.path.join(Folder_Path, "DeleteThisFile.txt")

if os.path.exists(f"{File_Path}.txt"):
    print('Deleted file.')
    os.remove(f"{File_Path}.txt")

st.title('Hi')
st.divider()
st.title('UPDATE INFO :')
st.write('### [:] Changed weapons to chapter 5 season 1 weapons. (Loadout generator, Custom loadout)')
st.write("### [+] Added weapon mods (Loadout generator, Custom loadout)")
st.write("### [+] Added medallions. (Loadout generator, Custom loadout)")
st.write("### [:] Shorter code (Loadout generator, Custom loadout)")
st.write('### [:] Nice ui now (Loadout generator, Custom loadout)')
st.write("### [+] Loadout generator loadout now shows medallions amount and other.")
col1,col2=st.columns(2)
with col1: st.image(os.path.join("Pictures", "Example1.png"), caption='Example 1 (Loadout generator)', use_column_width=True)
with col2: st.image(os.path.join("Pictures", "Example2.png"), caption='Example 2 (Loadout generator)', use_column_width=True)
st.write('# \n ##### [/] = Fixed\n ##### [:] = Changed something\n ##### [+] = Added\n ##### [-] = Removed\n\n\n ##### also pls tell me about bugs and other things so i can fix them (on discord) :)')

with st.sidebar:
    st.link_button("Github", "https://github.com/fuzzybuzzyboy/py")
    st.link_button("Discord", "https://discord.gg/HVEGufPNnF")
    if st.button('Clock'):
        with st.empty():
            while True:
                time_now1, time_now = datetime.now().strftime("%D"), datetime.now().strftime("%H:%M:%S")
                st.write(f'# Clock\n    Time : {time_now}\n    Date : {time_now1}', format="markdown")
                time.sleep(1)
