# * SECTION Local Imports
import modules.commands.term as term
import modules.commands.menus as menus

# * SECTION built-in Imports
#! NOTE used to run shell commands
import subprocess
from enum import Enum, StrEnum
import os, os.path


# * SECTION Third Party Imports
#! NOTE used to create loading spinners
from yaspin import yaspin

#! NOTE used to print ascii art
import pyfiglet

#! NOTE used to create interactive menus
import inquirer

#! NOTE used to print colored text
from printy import printy, inputy











# * SECTION Application Strings
app_name = pyfiglet.figlet_format("gzmap", font="doh", width=200)
welcome_mesage = (
    "Welcome to gzmap, Use the Arrow Keys to navigate and press Enter to select : "
)

# * SECTION Colors for printy
colors = {
    "red": "r",
    "green": "g",
    "yellow": "y",
    "blue": "b",
    "magenta": "m",
    "cyan": "c",
    "white": "w",
    "black": "k",
    "grey": "g",
    "orange": "o",
    "purple": "p",
}




def get_active_project():
    with open(get_active_project_file_path(), "r") as file:
        return file.read()

def set_active_project():
    project_name = NmapMenu().readInput("Enter Project Name: ")
    project_name = project_name.replace(" ", "_")
    project_name = project_name.replace("/", "_")
    project_name = project_name.replace("\\", "_")
    project_name = project_name.replace(":", "_")
    project_name = project_name.replace("*", "_")
    project_name = project_name.replace("?", "_")
    project_name = project_name.replace('"', "_")
    project_name = project_name.lower()
    try:
        with open(get_active_project_file_path(), "w") as file:
            file.write(project_name)
            
    except:
        with open(get_active_project_file_path(), "x") as file:
            file.write(project_name)
    setupProject()
        


# * SECTION File Paths
def get_active_project_file_path():
    return f"./projects/active_project.txt"


def get_help_file_path():
    return f"./help/help.txt"


def get_nmap_ip_file_path():
    return f"./projects/{get_active_project()}/nmap/ip.txt"


def get_nmap_ports_file_path():
    return f"./projects/{get_active_project()}/nmap/ports.txt"


# * SECTION Output File Names
def get_nmap_scan_all_ports_output_file_name():
    finished = False
    sequence_number = 0
    nmap_scan_all_ports_output_file_name = f"scan_all_ports_{sequence_number}.txt"
    while not finished:
        if os.path.exists(
            f"{get_nmap_port_scan_output_file_path()}{nmap_scan_all_ports_output_file_name}"
        ):
            sequence_number += 1
            nmap_scan_all_ports_output_file_name = (
                f"scan_all_ports_{sequence_number}.txt"
            )
        else:
            finished = True

    return nmap_scan_all_ports_output_file_name


# * SECTION Output File Paths
def get_nmap_port_scan_output_file_path():
    return f"./projects/{get_active_project()}/nmap/port_scans/"


# * SECTION Menu Options
#! NOTE
modes = menus.Menu.modes


def show_welcome_message():
    term.clear()
    printy(app_name, colors.get("yellow"))
    printy(welcome_mesage, colors.get("magenta"))


def get_target_info():
    return {"ip": getIP(), "ports": getPorts(), "project": get_active_project()}


def NmapMenu():
    def get_menu_options():
        return menus.MenuOptions(
            {
                "Setup": {modes.FUNCTION: setupNMAP},
                "Scan All Ports": {
                    modes.COMMAND: f"nmap -sV -sC -A -p- -oN {get_nmap_port_scan_output_file_path()}{get_nmap_scan_all_ports_output_file_name()}  {getIP()}"
                },
                "Help": {modes.HELP: showHelp},
                "Back": {modes.MENU: {"showMenu": MainMenu}},
            }
        )

    return menus.Menu(
        get_menu_options,
        inquirer,
        subprocess,
        printy,
        target=get_target_info,
        name="Nmap Menu",
        colors=colors,
        activeMenu=set_active_menu,
        welcomeMessage=show_welcome_message,
    )


def MainMenu():
    def get_menu_options():
        return menus.MenuOptions(
            {
                "Set Active Project": {modes.FUNCTION: set_active_project},
                "Nmap": {modes.MENU: {"showMenu": NmapMenu}},
                "Exit": {modes.FUNCTION: exit},
            }
        )

    return menus.Menu(
        get_menu_options,
        inquirer,
        subprocess,
        printy,
        target=get_target_info,
        name="Main Menu",
        colors=colors,
        activeMenu=set_active_menu,
        welcomeMessage=show_welcome_message,
    )


def set_active_menu(menu):
    global active_menu
    active_menu = menu


active_menu = MainMenu()


#! NOTE Application Entry Point
def run():
    setupProject()
    while True:
        show_welcome_message()
        active_menu.show()


def showHelp(lastMenu):
    with open(get_help_file_path(), "r") as file:
        printy(file.read(), colors.get("yellow"))
    inputy("Press Enter to continue...", colors.get("magenta"))
    term.clear()
    show_welcome_message()
    lastMenu.show()


def set_IP():
    ip = NmapMenu().readInput("Enter IP Address ")
    with open(get_nmap_ip_file_path(),"w") as file:
        file.write(ip)


def set_ports():
    ports = NmapMenu().readInput(
        "Enter Port range, separated by a hyphen, EX. 69-6969  "
    )
    with open(get_nmap_ports_file_path(),"w") as file:
        file.write(ports)


def getIP():
    with open(get_nmap_ip_file_path(), "r") as file:
        return file.read()


def getPorts():
    with open(get_nmap_ports_file_path(), "r") as file:
        return file.read()

def setupProject():
    project_path = f"./projects/{get_active_project()}/nmap/port_scans"
    ip_file = f"./projects/{get_active_project()}/nmap/ip.txt"
    port_file = f"./projects/{get_active_project()}/nmap/ports.txt"
    if os.path.exists(f"./projects/{get_active_project()}"):
        return
    else :
        os.makedirs(project_path, exist_ok=True)
        file = open(ip_file, "x")
        file.close()
        file = open (port_file, "x")
        file.close()
        

def setupNMAP():
    set_active_project()
    set_IP()
    set_ports()
    with yaspin(
        text="Setup Finished Successfully! Press Enter to continue...", color="yellow"
    ).white.bold.fistBump.on_blue as spinner:
        input()
        spinner.ok("✔")
        term.clear()
    show_welcome_message()
    NmapMenu().show()
