The_app_py_script = """

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import time
import webbrowser
from .localhost import LocalHoat


# basedurlhere
class AppNameBabe(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        #? Get and setup the localhost
        dist_folder_path = str(__file__).replace("app.py", "assets/dist")
        LH = LocalHoat()
        LH.start()
        for i in range(15):
            if LH.started == True: break
            time.sleep(0.5)
        
        #! ---
        import shutil
        import os
        sandbox_documents_dir = os.path.expanduser('~/Documents')
        
        if os.path.isdir(f"{sandbox_documents_dir}/dist"):
            shutil.rmtree(f"{sandbox_documents_dir}/dist")
        shutil.copytree(dist_folder_path, f"{sandbox_documents_dir}/dist")

        the_file = open(f"{sandbox_documents_dir}/dist/index.html", encoding="utf-8").read()
        the_file = the_file.replace("/basedurlhere/", f"{sandbox_documents_dir}/dist/")
        open(f"{sandbox_documents_dir}/dist/index.html", "w+", encoding="utf-8").write(the_file)
        
        #! ---
        
        #? reWrite the index file.
        if 1 != 1:
            the_file = open(f"{dist_folder_path}/index.html", encoding="utf-8").read()
            the_file = the_file.replace("/basedurlhere/", f"{dist_folder_path}/")
            open(f"{dist_folder_path}/index.html", "w+", encoding="utf-8").write(the_file)

        #? create the webview
        webview = toga.WebView(style=Pack(flex=1))
        url = f'http://localhost:{LH.PORT}/{sandbox_documents_dir}/dist'
        webview.url = url
        main_box.add(webview)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content=main_box
        self.main_window.show()


def main():
    return AppNameBabe()


"""