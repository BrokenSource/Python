# Import Broken
from Broken import *

# Create main class
class PythonTemplate:
    def __init__(self):
        log.info("Project template alive")

    def cli(self):
        """Create and run a Command Line Interface"""
        self.typer = BrokenBase.typer_app()
        self.typer.command()(self.command1)
        self.typer.command()(self.command2)
        self.typer()

    def command1(self):
        """Description of Command 1"""
        log.info("command1")

    def command2(self):
        """Description of Command 2"""
        log.info("command2")
