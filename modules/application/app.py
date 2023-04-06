import modules.commands.term as term
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
    term.clear()
    printy(app_name, yellow)
    printy(welcome_mesage, magenta)
    
    menu_main()
    
    
def menu_main():
    questions = [
        inquirer.List(
            "action",
            message="What would you like to do?",
        choices=["Nmap", "Help", "Exit"],
        ),
    ]
    action = inquirer.prompt(questions)
    
    match (action.get("action")):
        case "Nmap":
            printy("Nmap Selected", yellow)
            menu_nmap()
        case "Help":
            printy("Help Selected", yellow)
        case "Exit":
            printy("Exiting", yellow)
            subprocess.run("clear")
            exit()
        case _: 
            printy("Invalid Option", yellow)
            run()

def menu_nmap():
    questions = [
        inquirer.List(
            "action",
            message="What would you like to do?",
        choices=["Banners", "Port Scan", "Exit"],
        ),
    ]
    action = inquirer.prompt(questions)
    
    match (action.get("action")):
        case "Banners":
            printy("Banners Selected", yellow)
            
        case "Port Scan":
            printy("Port Scan Selected", yellow)
        case "Exit":
            printy("Exiting", yellow)
            subprocess.run("clear")
            exit()
        case _: 
            printy("Invalid Option", yellow)
            menu_nmap()
