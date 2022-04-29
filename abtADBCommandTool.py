import os
import subprocess


class send_adb_command:

    def __init__(self, command):

        self.command=command

    
    def open_adb_shell(self):

