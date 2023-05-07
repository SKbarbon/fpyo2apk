import os
import zipfile
import shutil

def Unzip_asset ():
    asset_path = str(__file__).replace("Tools/unzip_assets.py", "assets/fpyo2apkdist.zip")
    if not os.path.isfile(asset_path):
        raise FileNotFoundError("Cannot found the assets.")
    
    if os.path.isdir("fpyo2apkdist"):
        shutil.rmtree("fpyo2apkdist")

    with zipfile.ZipFile(asset_path, "r") as zip_ref:
        zip_ref.extractall("fpyo2apkdist")
    
    shutil.copytree("fpyo2apkdist/fpyo2apkdist", "_fpyo2apkdist")
    shutil.rmtree("fpyo2apkdist")
    shutil.move("_fpyo2apkdist", "fpyo2apkdist")

    #? Edit the pyproject.toml file.
    AppName = input("Write the name of your app: ")
    Describe = input("Write a small descibe of your app:")
    if str(AppName).replace(" ", "") == "": AppName = "fpyo2apk"
    if '"' in str(AppName): AppName = "fpyo2apk"
    if '"' in str(Describe): Describe = "fpyo2apk"

    print("setting your appname and describe..")
    read_file = open("fpyo2apkdist/pyproject.toml", encoding="utf-8").read()
    read_file = str(read_file).replace("_here_the_app_name_", AppName)
    read_file = str(read_file).replace("_here_the_describe_of_app_", Describe)

    open("fpyo2apkdist/pyproject.toml", "w+", encoding="utf-8").write(read_file)

    print("unzip is done..")