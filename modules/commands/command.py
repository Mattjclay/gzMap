class OpenMenu:
    def __init__(self, menu=None):
        self.menu = menu

    def run(self):
        self._menu = self.menu()
        self._menu.show()


class Function:
    def __init__(self, callback=None, args=None):
        self.callback = callback
        self.args = args

    def run(self):
        if self.args is not None and self.callback is not None:
            self.callback(self.args)
        elif self.callback is not None:
            self.callback()


class Command:
    def __init__(self, cmd=None):
        self.cmd = cmd

    def run(self):
        import subprocess

        subprocess.run(self.cmd.split())
