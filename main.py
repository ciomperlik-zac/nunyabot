import math
import pyperclip as clip
import keyboard
from os import system
from time import sleep

data = []

def print_logo():
    print(" ________   ___  ___  ________       ___    ___ ________  ________  ________  _________")
    print("|\\   ___  \\|\\  \\|\\  \\|\\   ___  \\    |\\  \\  /  /|\\   __  \\|\\   __  \\|\\   __  \\|\\___   ___\\")
    print("\\ \\  \\\\ \\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\   \\ \\  \\/  / | \\  \\|\\  \\ \\  \\|\\ /\\ \\  \\|\\  \\|___ \\  \\_|")
    print(" \\ \\  \\\\ \\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\   \\ \\    / / \\ \\   __  \\ \\   __  \\ \\  \\\\\\  \\   \\ \\  \\")
    print("  \\ \\  \\\\ \\  \\ \\  \\\\\\  \\ \\  \\\\ \\  \\   \\/  /  /   \\ \\  \\ \\  \\ \\  \\|\\  \\ \\  \\\\\\  \\   \\ \\  \\")
    print("   \\ \\__\\\\ \\__\\ \\_______\\ \\__\\\\ \\__\\__/  / /      \\ \\__\\ \\__\\ \\_______\\ \\_______\\   \\ \\__\\")
    print("    \\|__| \\|__|\\|_______|\\|__| \\|__|\\___/ /        \\|__|\\|__|\\|_______|\\|_______|    \\|__|")
    print("                                   \\|___|/                               by nunyabiz_\n")

print_logo()

def handle_f3c():
    add_throw()

    if len(data) == 2:
        locate_stronghold(data)

def add_throw():
    sleep(0.5)
    cmd_output = clip.paste()

    try:
        cmd_data = cmd_output.split("tp @s ")[1]
        cmd_data_list = [float(data) for data in cmd_data.split(" ")]
    except:
        return

    throw = (cmd_data_list[2], cmd_data_list[0], cmd_data_list[3])
    data.append(throw)

    print(f"Added eye throw: {cmd_data_list[0]}, {cmd_data_list[2]}, {cmd_data_list[3]}")

def locate_stronghold(data):
    x0, y0, angle0 = data[0]
    x1, y1, angle1 = data[1]

    m0 = math.tan(math.radians((angle0 % 360.0) * -1))
    m1 = math.tan(math.radians((angle1 % 360.0) * -1))

    soln_x = (-m1 * x1 + y1 + m0 * x0 - y0) / (m0 - m1)
    soln_y = m0 * (soln_x - x0) + y0

    dist = math.sqrt((data[-1][0] - soln_x) ** 2 + (data[-1][1] - soln_y) ** 2)
    
    print(f"\nEstimated stronghold distance:\n\nOverwold: {dist:.1f}\nNether: {(dist/8):.1f}")
    print(f"\nEstimated stronghold location:\n\nOverworld: {soln_y:.1f}, {soln_x:.1f}\nNether: {(soln_y/8):.1f}, {(soln_x/8):.1f}")

def clear_data():
    global data
    data = []

    system("cls")
    print_logo()

keyboard.add_hotkey("f3+c", handle_f3c)
keyboard.add_hotkey("shift+enter", lambda: locate_stronghold(data))
keyboard.add_hotkey("shift+backspace", clear_data)
keyboard.wait("shift+c")
