from .the_app_py import The_app_py_script
from .the_localhost_py import The_localhost_py_script
from ..Tools.unzip_assets import Unzip_asset
import os
import shutil
import subprocess
import sys

def edit_an_exist_project():
    print("Create a briefcase project..")
    Unzip_asset()

    
    project_name = "fpyo2apkdist"
    if not os.path.isdir(project_name):
        raise FileNotFoundError(f"There is no folder with path '{project_name}'.")
    
    if not os.path.isdir(f"{project_name}/src"):
        raise FileNotFoundError(f"There is no folder with path '{project_name}/src'.")
    
    if not os.path.isdir(f"{project_name}/src/fpyo2apk/assets"):
        os.mkdir(f"{project_name}/src/fpyo2apk/assets")
    
    if not os.path.isdir("dist"):
        raise FileNotFoundError("There must be a flet-pyodide folder called `dist` to start.")
    
    print("editing the dist..")
    if '  <base href="/basedurlhere/">' in open("dist/index.html", encoding="utf-8").read():
        pass
    elif '  <base href="/">' not in open("dist/index.html", encoding="utf-8").read():
        sys.exit("Exit with Error: The base/href url of the dist must be '/'.")
    
    the_index_file = open("dist/index.html", encoding="utf-8").read()
    the_index_file = str(the_index_file).replace('  <base href="/">', '  <base href="/basedurlhere/">')
    open("dist/index.html", "w+", encoding="utf-8").write(the_index_file)

    print("copy the dist..")
    if os.path.isdir(f"{project_name}/src/fpyo2apk/assets/dist"):
        shutil.rmtree(f"{project_name}/src/fpyo2apk/assets/dist")
    shutil.copytree("dist", f"{project_name}/src/fpyo2apk/assets/dist")

    print("start edit the 'app.py' file")
    open(f"{project_name}/src/fpyo2apk/app.py", "w+", encoding="utf-8").write(The_app_py_script)

    print("start creating/editing the 'localhost.py' file")
    open(f"{project_name}/src/fpyo2apk/localhost.py", "w+", encoding="utf-8").write(The_localhost_py_script)

    print("Your app is being built and then opened on the iOS simulator..\nThis Usually take two minutes to finish, please wait..")
    process = subprocess.Popen(["cd fpyo2apkdist\nbriefcase create Android\nbriefcase build Android\n"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error != None:
        sys.exit(f"\nExit with Error: {error}")
    
    print("""

All work done!
Your app is in the `fpyo2apkdist/build/fpyo2apkdist/Android/`!
To run a simulator, use:
$ cd pyo2ipadist
$ briefcase run Android

    """)