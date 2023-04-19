from pypresence import Presence
import PySimpleGUI as sg
import time

layout = [[sg.Text("GLC-DRP is active!")], [sg.Button("close")]]
window = sg.Window("GLC-DRP", layout)

client_id = ""  # Enter your Application ID here.
RPC = Presence(client_id=client_id)
RPC.connect()


# Make sure you are using the same name that you used when uploading the image
start_time=time.time() # Using the time that we imported at the start. start_time equals time.
RPC.update(large_image="large", state="Playing Minecraft 1.8.8", start=start_time) # We want to apply start time when you run the presence.

while 1:
    event, values = window.read()
    if event == "close" or event == sg.WIN_CLOSED:
        break
RPC.clear()
window.close()
