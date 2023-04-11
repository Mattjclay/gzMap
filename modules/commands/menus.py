from enum import StrEnum


class MenuOptions:
    def __init__(self, options: dict):
        self.options = options


class Menu:
    modes: StrEnum = StrEnum("modes", ["COMMAND", "MENU", "FUNCTION"])

    def __init__(self, menu: MenuOptions, inquirer, subprocess, args: list[str]=None):
        self.menu = menu
        self.inquirer = inquirer
        self.subprocess = subprocess
        self.args = args

    def show(self):
        self.questions = [
            self.inquirer.List(
                "action",
                message="What would you like to do?",
                choices=self.menu.options.keys(),
            ),
        ]
        self.action = self.inquirer.prompt(self.questions)
        self.action = self.action["action"]

        if Menu.modes.MENU in self.menu.options[self.action]:
            self.menu.options[self.action][Menu.modes.MENU]()
        if Menu.modes.COMMAND in self.menu.options[self.action]:
            self.subprocess.run(
                self.menu.options[self.action][Menu.modes.COMMAND].split()
            )
        if Menu.modes.FUNCTION in self.menu.options[self.action]:
            self.menu.options[self.action][Menu.modes.FUNCTION]()
