import os
import sys
import time
import platform
import subprocess

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

# main function


class main(QWidget):
    def __init__(self):
        super().__init__()
        self.set_ui()
        self.setWindowTitle("Project Starter")
        self.resize(242, 100)

    # ui
    def set_ui(self):
        types = ["Django", "PySide", "PyQt6"]

        self.project_type = QComboBox()
        for projectType in types:
            self.project_type.addItem(projectType)

        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_handler)

        self.exit = QPushButton()
        self.exit.setText("Exit")
        self.exit.clicked.connect(self.exit_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.project_type)
        self.layout.addWidget(self.submit)
        self.layout.addWidget(self.exit)

    # submit
    def submit_handler(self):
        project_type_id = self.project_type.currentIndex()
        self.project_type.setHidden(1)
        self.submit.setHidden(1)
        if project_type_id == 0:
            self.close()
            self.django_choose_action = django_action_chose()
            self.django_choose_action.show()
        if project_type_id == 1 or project_type_id == 2:
            self.close()
            self.pyside_choose_action = pyside_action_choose()
            self.pyside_choose_action.show()

    # exit
    def exit_handler(self):
        self.close()


# django choose action
class django_action_chose(QWidget):
    def __init__(self):
        super().__init__()
        self.django_ui()
        self.resize(250, 100)
        self.setWindowTitle("Choose action")

    # ui
    def django_ui(self):
        actions = [
            "Install requirements",
            "Start project",
            "Start App",
            "Start Server",
            "Make migrations",
        ]

        self.action = QComboBox()
        for action in actions:
            self.action.addItem(action)

        self.submit_action = QPushButton()
        self.submit_action.setText("Submit")
        self.submit_action.clicked.connect(self.submit_handler)

        self.back = QPushButton()
        self.back.setText("Back")
        self.back.clicked.connect(self.back_action)

        self.layout = QGridLayout(self)

        self.layout.addWidget(self.action)
        self.layout.addWidget(self.submit_action)
        self.layout.addWidget(self.back)

    # submit
    def submit_handler(self):
        action_id = self.action.currentIndex()
        if platform.system() == "Windows":
            if action_id == 0:
                path = os.getcwd()
                txt = os.path.join(path, "\\requirements\\django.txt")
                proc = subprocess.Popen(
                    ["start", "cmd", "/c", f"python -m pip install -r {txt}"],
                    shell=True,
                )
                proc.wait()
            if action_id == 1:
                self.close()
                self.django_start_project = django_start_project()
                self.django_start_project.show()
            if action_id == 2:
                self.close()
                self.django_start_app = django_start_app()
                self.django_start_app.show()
            if action_id == 3:
                self.close()
                self.django_start_server = django_start_server()
                self.django_start_server.show()
            if action_id == 4:
                self.close()
                self.django_make_migrations = django_make_migrations()
                self.django_make_migrations.show()
        if platform.system() == "Linux" or platform.system == "Darwin":
            if action_id == 0:
                path = os.getcwd()
                requirements_folder = os.path.join(path, "requirements")
                txt = os.path.join(requirements_folder, "django.txt")
                proc = subprocess.Popen(
                    [f"pip3 install -r {txt}"],
                    shell=True,
                )
                proc.wait()
            if action_id == 1:
                self.close()
                self.django_start_project = django_start_project()
                self.django_start_project.show()
            if action_id == 2:
                self.close()
                self.django_start_app = django_start_app()
                self.django_start_app.show()
            if action_id == 3:
                self.close()
                self.django_start_server = django_start_server()
                self.django_start_server.show()
            if action_id == 4:
                self.close()
                self.django_make_migrations = django_make_migrations()
                self.django_make_migrations.show()

    # back
    def back_action(self):
        self.close()
        self.main_ui = main()
        self.main_ui.show()


# start project
class django_start_project(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()
        self.resize(250, 100)
        self.setWindowTitle("Start Project")

    def ui(self):
        self.path = QLineEdit()
        self.path.setPlaceholderText("Path")
        self.path.returnPressed.connect(self.start_app)

        self.browse = QPushButton()
        self.browse.setText("...")
        self.browse.clicked.connect(self.set_path)

        self.project_name = QLineEdit()
        self.project_name.setPlaceholderText("Project Name")

        self.start = QPushButton()
        self.start.setText("Start App")
        self.start.clicked.connect(self.start_app)

        self.back = QPushButton()
        self.back.setText("Back")
        self.back.clicked.connect(self.back_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.project_name, 0, 0, 1, 0)
        self.layout.addWidget(self.path, 1, 0, 1, 1)
        self.layout.addWidget(self.browse, 1, 1, 1, 1)
        self.layout.addWidget(self.start, 2, 0, 1, 0)
        self.layout.addWidget(self.back, 3, 0, 1, 0)

    def set_path(self):
        path_link = QFileDialog.getExistingDirectory(self, "Choose Directory", "C:\\")
        self.path.setText(path_link)

    def start_app(self):
        path = self.path.text()
        name = self.project_name.text()

        if path == "":
            self.setWindowTitle("ERROR")
            time.sleep(0.5)
            self.setWindowTitle("Start Project")
        else:
            self.create_project(path, name)

    def create_project(self, path, name):
        path_converted = path.replace("/", "\\")
        proc = subprocess.Popen(
            [
                "start",
                "cmd",
                "/c",
                f"cd {path_converted} && django-admin startproject {name}",
            ],
            shell=True,
        )
        proc.wait()

    def back_handler(self):
        self.close()
        self.django_back = django_action_chose()
        self.django_back.show()


# start app
class django_start_app(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()
        self.resize(250, 100)
        self.setWindowTitle("Start Server")

    def ui(self):
        self.app_name = QLineEdit()
        self.app_name.setPlaceholderText("App Name")

        self.project_path = QLineEdit()
        self.project_path.setPlaceholderText("Project Directory")

        self.browse = QPushButton()
        self.browse.setText("...")
        self.browse.clicked.connect(self.browse_handler)

        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_handler)

        self.back = QPushButton()
        self.back.setText("Back")
        self.back.clicked.connect(self.back_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.project_path, 0, 0, 1, 1)
        self.layout.addWidget(self.browse, 0, 1, 1, 1)
        self.layout.addWidget(self.app_name, 2, 0, 1, 0)
        self.layout.addWidget(self.submit, 3, 0, 1, 0)
        self.layout.addWidget(self.back, 4, 0, 1, 0)

    def browse_handler(self):
        path_link = QFileDialog.getExistingDirectory(
            self, "Choose Project Directory", "C:\\"
        )
        self.project_path.setText(path_link)

    def submit_handler(self):
        path = self.project_path.text()
        app_name = self.app_name.text()

        if path == "" or app_name == "":
            self.setWindowTitle("ERROR")
            time.sleep(0.5)
            self.setWindowTitle("Start Project")
        else:
            self.django_create_app(path, app_name)

    def django_create_app(self, path, name):
        print(path)
        proc = subprocess.Popen(
            ["start", "cmd", "/k", f"cd {path} && python manage.py startapp {name}"],
            shell=True,
        )

    def back_handler(self):
        self.close()
        self.django_back = django_action_chose()
        self.django_back.show()


# start server
class django_start_server(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()
        self.resize(250, 100)
        self.setWindowTitle("Start Server")

    def ui(self):
        self.path = QLineEdit()
        self.path.setPlaceholderText("Path")

        self.browse = QPushButton()
        self.browse.setText("...")
        self.browse.clicked.connect(self.set_path)

        self.start = QPushButton()
        self.start.setText("Start Server")
        self.start.clicked.connect(self.serv)

        self.back = QPushButton()
        self.back.setText("Back")
        self.back.clicked.connect(self.back_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.path, 0, 0, 1, 1)
        self.layout.addWidget(self.browse, 0, 1, 1, 1)
        self.layout.addWidget(self.start, 1, 0, 1, 0)
        self.layout.addWidget(self.back, 2, 0, 1, 0)

    def set_path(self):
        path_link = QFileDialog.getOpenFileName(
            self, "Open File", "C:\\", "Python Script (*.py)"
        )[0]
        self.path.setText(path_link)

    def serv(self):
        path = self.path.text()
        contains = "manage.py" in path
        if not contains or path == "":
            self.setWindowTitle("ERROR")
            time.sleep(0.5)
            self.setWindowTitle("Start Server")
        if contains:
            self.setWindowTitle("Starting")
            proc = subprocess.Popen(
                ["start", "cmd", "/k", f"python {path} runserver"], shell=True
            )
            proc.wait()

    def back_handler(self):
        self.close()
        self.django_back = django_action_chose()
        self.django_back.show()


# make migration
class django_make_migrations(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Make Migrations")
        self.resize(258, 60)
        self.ui()

    def ui(self):
        self.path = QLineEdit()
        self.path.setPlaceholderText("Path")

        self.browse = QPushButton()
        self.browse.setText("...")
        self.browse.clicked.connect(self.set_path)

        self.start = QPushButton()
        self.start.setText("Make Migrations")
        self.start.clicked.connect(self.make_migration)

        self.back = QPushButton()
        self.back.setText("Back")
        self.back.clicked.connect(self.back_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.path, 0, 0, 1, 1)
        self.layout.addWidget(self.browse, 0, 1, 1, 1)
        self.layout.addWidget(self.start, 1, 0, 1, 0)
        self.layout.addWidget(self.back, 2, 0, 1, 0)

    def set_path(self):
        path_link = QFileDialog.getOpenFileName(
            self, "Open File", "C:\\", "Python Script (*.py)"
        )[0]
        self.path.setText(path_link)

    def make_migration(self):
        path = self.path.text()
        contains = "manage.py" in path
        if not contains or path == "":
            self.setWindowTitle("ERROR")
            time.sleep(0.5)
            self.setWindowTitle("Make Migrations")
        if contains:
            self.setWindowTitle("migrating")
            proc = subprocess.Popen(
                ["start", "cmd", "/c", f"python {path} makemigrations"], shell=True
            )
            proc = subprocess.Popen(
                ["start", "cmd", "/c", f"python {path} migrate"], shell=True
            )
            proc.wait()

    def back_handler(self):
        self.close()
        self.django_action_chose = django_action_chose()
        self.django_action_chose.show()


# pyside choose
class pyside_action_choose(QWidget):
    def __init__(self):
        super().__init__()
        self.pyside_ui()
        self.resize(250, 100)
        self.setWindowTitle("Choose action")

    def pyside_ui(self):
        actions = [
            "Install PySide2",
            "Install PySide6",
            "Create PySide2 app",
            "Create PySide6 app",
            "Start Pyside2 app",
            "Start Pyside6 app",
        ]

        self.action = QComboBox()
        for action in actions:
            self.action.addItem(action)

        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_handler)

        self.back = QPushButton()
        self.back.setText("Back")
        self.back.clicked.connect(self.back_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.action)
        self.layout.addWidget(self.submit)
        self.layout.addWidget(self.back)

    def submit_handler(self):
        action_id = self.action.currentIndex()
        system = platform.system()
        if system == "Windows":
            # install pyside2
            if action_id == 0:
                path = os.getcwd()
                txt = os.path.join(path, "\\requirements\\pyside2.txt")
                proc = subprocess.Popen(
                    ["start", "cmd", "/c", f"python -m pip install -r {txt}"],
                    shell=True,
                )
                proc.wait()
            # install pyside 6
            if action_id == 1:
                path = os.getcwd()
                txt = os.path.join(path, "\\requirements\\pyside6.txt")
                proc = subprocess.Popen(
                    ["start", "cmd", "/c", f"python -m pip install -r {txt}"],
                    shell=True,
                )
                proc.wait()
            # create pyside2 app
            if action_id == 2:
                self.close()
                self.wps2pc = pyside2_project_creation()
                self.wps2pc.show()
            # create pyside6 app
            if action_id == 3:
                self.close()
                self.wps6pc = pyside6_project_creation()
                self.wps6pc.show()
            # start pyside2 app
            if action_id == 4:
                self.close()
                self.wps2ps = pyside2_project_start()
                self.wps2ps.show()
            # start pyside6 app
            if action_id == 5:
                self.close()
                self.wps6ps = pyside6_project_start()
                self.wps6ps.show()
        if system == "Linux" or system == "Darwin":
            action_id = self.action.currentIndex()
            system = platform.system()
            # install pyside2
            if action_id == 0:
                path = os.getcwd()
                requirements_folder = os.path.join(path, "requirements")
                txt = os.path.join(requirements_folder, "pyside2.txt")
                proc = subprocess.Popen(
                    [f"pip3 install -r {txt}"],
                    shell=True,
                )
                proc.wait()
            # install pyside 6
            if action_id == 1:
                path = os.getcwd()
                requirements_folder = os.path.join(path, "requirements")
                txt = os.path.join(requirements_folder, "pyside6.txt")
                proc = subprocess.Popen(
                    [f"pip3 install -r {txt}"],
                    shell=True,
                )
                proc.wait()
                # create pyside2 app
            if action_id == 2:
                self.close()
                self.ups2pc = pyside2_project_creation()
                self.ups2pc.show()
            # create pyside6 app
            if action_id == 3:
                self.close()
                self.ups6pc = pyside6_project_creation()
                self.ups6pc.show()
            # start pyside2 app
            if action_id == 4:
                self.close()
                self.ups2ps = pyside2_project_start()
                self.ups2ps.show()
            # start pyside6 app
            if action_id == 5:
                self.close()
                self.ps6ps = _pyside6_project_start()
                self.ups6ps.show()

    def back_handler(self):
        self.close()
        self.main_ui = main()
        self.main_ui.show()


class pyside2_project_creation(QWidget):
    def __init__(self):
        super().__init__()
        self.pyside2_project_creation_ui()
        self.resize(250, 100)
        self.setWindowTitle("Choose action")

    def pyside2_project_creation_ui(self):
        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.submit)

    def submit_handler(self):
        print("Hello")


class pyside6_project_creation(QWidget):
    def __init__(self):
        super().__init__()
        self.pyside6_project_creation_ui()
        self.resize(250, 100)
        self.setWindowTitle("Choose action")

    def pyside6_project_creation_ui(self):
        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.submit)

    def submit_handler(self):
        print("Hello")


class pyside2_project_start(QWidget):
    def __init__(self):
        super().__init__()
        self.pyside2_project_start_ui()
        self.resize(250, 100)
        self.setWindowTitle("Choose action")

    def pyside2_project_start_ui(self):
        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.submit)

    def submit_handler(self):
        print("Hello")


class pyside6_project_start(QWidget):
    def __init__(self):
        super().__init__()
        self.pyside6_project_start_ui()
        self.resize(250, 100)
        self.setWindowTitle("Choose action")

    def pyside6_project_start_ui(self):
        self.submit = QPushButton()
        self.submit.setText("Submit")
        self.submit.clicked.connect(self.submit_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.submit)

    def submit_handler(self, os):
        print("Hello")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    sys.exit(app.exec_())
