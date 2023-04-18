from enum import StrEnum


class MenuOptions:
    def __init__(self, options: dict):
        self.options = options


class Menu:
    modes = StrEnum("modes", ["COMMAND", "MENU", "FUNCTION", "HELP"])

    def __init__(
        self,
        menu,
        inquirer,
        subprocess,
        printy,
        name=None,
        colors=None,
        target=None,
        args=None,
        activeMenu=None,
        welcomeMessage=None,
    ):
        self.name = name
        self.menu = menu()
        self.inquirer = inquirer
        self.subprocess = subprocess
        self.printy = printy
        self.args = args
        self.colors = colors
        self.target = target
        self.activeMenu = activeMenu
        self.welcomeMessage = welcomeMessage

    def show(self):
        self.activeMenu(self)
        self.welcomeMessage()
        self.printy(f"Showing {self.name} ", self.colors.get("magenta"))
        self.printy(
            f"Active Project: {self.target()['project']}", self.colors.get("red")
        )
        self.printy(f"Target IP: {self.target()['ip']}", self.colors.get("red"))
        self.printy(f"Target Ports: {self.target()['ports']}", self.colors.get("red"))
        self.questions = [
            self.inquirer.List(
                "action",
                message="What would you like to do?",
                choices=self.menu.options.keys(),
            ),
        ]
        self.action = self.inquirer.prompt(self.questions)
        self.action = self.action["action"]
        
        self.menu.options[self.action]()
        
        
        
       

    def readInput(self, _message="Enter a prompt "):
        self.questions = [
            self.inquirer.Text("result", message=_message),
        ]
        self.answers = self.inquirer.prompt(self.questions)
        return self.answers["result"]
