from .Tools.check_system import is_it_mac
from .Tools.check_venv import is_on_venv
from .beeware_tools.edit_beeware_project import edit_an_exist_project
import sys
import sys

# python -m fpyo2ipa.build
args = str(sys.argv)

if is_on_venv() == False:
    #? exit if not in venv.
    sys.exit("Exit: Please run this on a virtual environment. Run this command to create one: `python3 -m venv venv`")


#! important informations
print("""
This is `fpyo2apk`. A flet-pyodide dist to apk converter.
Be sure that Android Studio is installed and setuped.
Starting..

""")

#! Step1: Create the project
edit_an_exist_project()