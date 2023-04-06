import modules.commands.term as term
import pyfiglet
import subprocess
import inquirer
from printy import printy
  
# Application Strings
app_name =  pyfiglet.figlet_format("gzmap", font = "doh", width = 200)
welcome_mesage = "Welcome to gzmap, Use the Arrow Keys to navigate and press Enter to select : "

# Colors
yellow = "y"
magenta = "m"

def run():
    term.clear()
    printy(app_name, yellow)
    printy(welcome_mesage, magenta)
    questions = [
        inquirer.List(
            "action",
            message="What would you like to do?",
        choices=["nmap", "help", "exit"],
        ),
    ]

    answers = inquirer.prompt(questions)
    printy(answers, magenta)

