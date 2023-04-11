
# * SECTION Local Imports
import modules.commands.term as term
import modules.commands.menus as menus

# * SECTION built-in Imports
#! NOTE used to run shell commands
import subprocess
from enum import Enum, StrEnum
# * SECTION Third Party Imports


#! NOTE used to print ascii art
import pyfiglet

#! NOTE used to create interactive menus
import inquirer

#! NOTE used to print colored text
from printy import printy

# * SECTION Application Strings
app_name: str = pyfiglet.figlet_format("gzmap", font="doh", width=200)
welcome_mesage: str = "Welcome to gzmap, Use the Arrow Keys to navigate and press Enter to select : "

# * SECTION Colors for printy
yellow: str = "y"
magenta: str = "m"

modes: StrEnum = menus.Menu.modes


def NmapMenu():
    nmap_menu_options = menus.MenuOptions(
        {"Nmap": {modes.COMMAND: "nmap"}, "Exit": {modes.FUNCTION: exit}}
    )
    return menus.Menu(nmap_menu_options, inquirer, subprocess)


# * SECTION Menu Options
#! NOTE
main_menu_options = menus.MenuOptions(
    {
        "Nmap": {modes.MENU: NmapMenu().show},
        "Nukem": {modes.COMMAND: "nmap"},
        "Exit": {modes.FUNCTION: exit},
    }
)


# * SECTION Menus
#! NOTE __name__ is the name of the current module, we pass this to the Menu class to prevent reimporting modules
main_menu_folder = menus.Menu(main_menu_options, inquirer, subprocess)


#! NOTE Application Entry Point
def run():
    term.clear()
    show_welcome_message()
    main_menu_folder.show()


def show_welcome_message():
    term.clear()
    printy(app_name, yellow)
    printy(welcome_mesage, magenta)
