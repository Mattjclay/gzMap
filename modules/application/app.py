import modules.commands.term as term
import modules.commands.menus as menus   
import pyfiglet
import subprocess
import inquirer
from printy import printy
  
# Application Strings
app_name =  pyfiglet.figlet_format("gzmap", font = "doh", width = 200)
welcome_mesage = "Welcome to gzmap, Use the Arrow Keys to navigate and press Enter to select : "

# Colors for printy
yellow = "y"
magenta = "m"

# Application Entry Point
def run():
    # Menus
    main_menu = {
        "Nmap": show_run_menu,
        "Directory Enumeration": show_run_menu,
        "Help": "",
        "Exit": "exit",
    }
    
    term.clear()
    printy(app_name, yellow)
    printy(welcome_mesage, magenta)
    show_folder_menu(main_menu)
    
def show_folder_menu(menu, ):
    questions = [
        inquirer.List(
            "action",
            message="What would you like to do?",
        choices=menu.keys(),
        ),
    ]
    action = inquirer.prompt(questions)
    
    if action["action"] == "Exit":
        exit()
    elif action["action"] == "Help":
        show_help()
    else:
        menu.get(action["action"])(menus.get_options(action["action"]))
    
def show_run_menu(menu_options):
    questions = [
        inquirer.List(
            "action",
            message="What would you like to do?",
        choices=menu_options.keys(),
        ),
    ]
    action = inquirer.prompt(questions)
    action = action.get("action")
    subprocess.run(menu_options.get(action).split())
    
def show_help():
    printy("Help", yellow)
    printy("This is the help menu", magenta)
    printy("Press any key to continue", magenta)
    input()
    run()