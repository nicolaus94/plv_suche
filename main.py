import time
import sys
import os
import pathlib
import requests
from bs4 import BeautifulSoup
import simpleaudio as sa

###### Einstellungen: ###########################################################

# Name der Sounddatei, die beim Fund gespielt werden soll:
sound_file = 'clap.wav'  # Muss im gleichen Verzeichnis liegen, Format: WAV

# So oft soll nach neuen Seminaren geschaut werden (nicht zu niedrig wählen!):
refresh_time = 60  # Zeit in Sekunden, mindestens 60!

#################################################################################
i = refresh_time;
last_search = None

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


if os.name == 'posix':
    path = str(pathlib.Path(__file__).parent.absolute()) + '/' + sound_file
else:
    path = str(pathlib.Path(__file__).parent.absolute()) + '\\' + sound_file
wave_obj = sa.WaveObject.from_wave_file(path)


# Saving actual amount of available seminars:
r = requests.get('https://pmit-ext.th-deg.de/seminare/')
soup = BeautifulSoup(r.text, 'html.parser')

badge = soup.find('span', class_='badge')
amount = int(badge.string)


# Welcome-Screen
clear_screen()
print(" /$$$$$$$  /$$    /$$    /$$         /$$$$$$                      /$$\n| $$__  $$| $$   | $$   | $$        /$$__  $$                    | $$\n| $$  \ $$| $$   | $$   | $$       | $$  \__/ /$$   /$$  /$$$$$$$| $$$$$$$   /$$$$$$\n| $$$$$$$/| $$   |  $$ / $$//$$$$$$|  $$$$$$ | $$  | $$ /$$_____/| $$__  $$ /$$__  $$\n| $$____/ | $$    \  $$ $$/|______/ \____  $$| $$  | $$| $$      | $$  \ $$| $$$$$$$$\n| $$      | $$     \  $$$/          /$$  \ $$| $$  | $$| $$      | $$  | $$| $$_____/\n| $$      | $$$$$$$$\  $/          |  $$$$$$/|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$\n|__/      |________/ \_/            \______/  \______/  \_______/|__/  |__/ \_______/\n                                                                             by Nico\n")
print("Willkommen.")
if refresh_time < 60:
    print("Die Refreshrate ist relativ niedrig eingestellt. Um keine Probleme mit der THD zu bekommen,\n "
          "stelle sie besser auf über 60 Sekunden ein. Benutzen niedriger Raten auf eigene Gefahr.")
    sys.exit()
print("So hört es sich an, wenn Kurse gefunden wurden....")
play_obj = wave_obj.play()
play_obj.wait_done()
print("Die Suche startet jetzt!")
time.sleep(1)

# Search-Routine:
while True:
    time.sleep(1)
    if i > 0:
        clear_screen()
        print(" /$$$$$$$  /$$    /$$    /$$         /$$$$$$                      /$$\n| $$__  $$| $$   | $$   | $$        /$$__  $$                    | $$\n| $$  \ $$| $$   | $$   | $$       | $$  \__/ /$$   /$$  /$$$$$$$| $$$$$$$   /$$$$$$\n| $$$$$$$/| $$   |  $$ / $$//$$$$$$|  $$$$$$ | $$  | $$ /$$_____/| $$__  $$ /$$__  $$\n| $$____/ | $$    \  $$ $$/|______/ \____  $$| $$  | $$| $$      | $$  \ $$| $$$$$$$$\n| $$      | $$     \  $$$/          /$$  \ $$| $$  | $$| $$      | $$  | $$| $$_____/\n| $$      | $$$$$$$$\  $/          |  $$$$$$/|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$\n|__/      |________/ \_/            \______/  \______/  \_______/|__/  |__/ \_______/\n                                                                             by Nico\n")
        if last_search:
            print("Zuletzt überprüft um " + last_search + " ohne neue Ergebnisse.")
        print("Neuer Versuch in", i, "Sekunden.")
    else:
        r = requests.get('https://pmit-ext.th-deg.de/seminare/')
        soup = BeautifulSoup(r.text, 'html.parser')

        badge = soup.find('span', class_='badge')
        number = int(badge.string)

        if number > 3:
            clear_screen()
            print(" /$$$$$$$  /$$    /$$    /$$         /$$$$$$                      /$$\n| $$__  $$| $$   | $$   | $$        /$$__  $$                    | $$\n| $$  \ $$| $$   | $$   | $$       | $$  \__/ /$$   /$$  /$$$$$$$| $$$$$$$   /$$$$$$\n| $$$$$$$/| $$   |  $$ / $$//$$$$$$|  $$$$$$ | $$  | $$ /$$_____/| $$__  $$ /$$__  $$\n| $$____/ | $$    \  $$ $$/|______/ \____  $$| $$  | $$| $$      | $$  \ $$| $$$$$$$$\n| $$      | $$     \  $$$/          /$$  \ $$| $$  | $$| $$      | $$  | $$| $$_____/\n| $$      | $$$$$$$$\  $/          |  $$$$$$/|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$\n|__/      |________/ \_/            \______/  \______/  \_______/|__/  |__/ \_______/\n                                                                             by Nico\n")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!!!!!!!!!!!!! NEUE KURSE !!!!!!!!!!!!!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("\n Beenden mit STRG + C.")
            try:
                while True:
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
            except KeyboardInterrupt:
                print("Viel Erfolg bei der Kurswahl!")
            break
        else:
            last_search = time.strftime('%H:%M:%S', time.localtime())
            clear_screen()
            print("/$$$$$$$  /$$    /$$    /$$         /$$$$$$                      /$$\n| $$__  $$| $$   | $$   | $$        /$$__  $$                    | $$\n| $$  \ $$| $$   | $$   | $$       | $$  \__/ /$$   /$$  /$$$$$$$| $$$$$$$   /$$$$$$\n| $$$$$$$/| $$   |  $$ / $$//$$$$$$|  $$$$$$ | $$  | $$ /$$_____/| $$__  $$ /$$__  $$\n| $$____/ | $$    \  $$ $$/|______/ \____  $$| $$  | $$| $$      | $$  \ $$| $$$$$$$$\n| $$      | $$     \  $$$/          /$$  \ $$| $$  | $$| $$      | $$  | $$| $$_____/\n| $$      | $$$$$$$$\  $/          |  $$$$$$/|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$\n|__/      |________/ \_/            \______/  \______/  \_______/|__/  |__/ \_______/\n                                                                             by Nico\n")
            print("Nichts Neues....")
            time.sleep(1)
            i = refresh_time
    i -= 1
