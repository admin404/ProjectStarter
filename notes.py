class django_start_server(QWidget):
    def __init__(self):
        super().__init__()
        self.start_server()
        self.resize(250, 100)
        self.setWindowTitle("Start Server")

    def start_server(self):
        self.setWindowTitle("Django Starter")
        self.resize(250, 100)
        path = os.getcwd()
        resources = os.path.join(path, "django.txt")
        proc = subprocess.Popen(
            ["start", "cmd", "/c", f"python -m pip install -r {resources}"], shell=True
        )
        proc.wait()

        # data text
        self.text = QLabel()

        # path select
        self.path = QLineEdit()
        self.path.setPlaceholderText("Path")

        # browse path
        self.browse = QPushButton()
        self.browse.setText("...")
        self.browse.clicked.connect(self.set_path)

        # start server btn
        self.start = QPushButton()
        self.start.setText("Start Server")
        self.start.clicked.connect(self.serv)

        # self.migrate = QPushButton()
        # self.migrate.setText("Make Migrations")
        # self.migrate.clicked.connect(self.mmg)

        self.back = QPushButton()
        self.back.setText("Back")
        self.back.clicked.connect(self.back_handler)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.text, 0, 0, 1, 0)
        self.layout.addWidget(self.path, 1, 0, 1, 1)
        self.layout.addWidget(self.browse, 1, 1, 1, 1)
        self.layout.addWidget(self.start, 2, 0, 1, 0)
        # self.layout.addWidget(self.migrate, 3, 0, 1, 0)
        self.layout.addWidget(self.back, 4, 0, 1, 0)

    def set_path(self):
        path_link = QFileDialog.getOpenFileName(
            self, "Open File", "C:\\", "Python Script (*.py)"
        )[0]
        self.path.setText(path_link)

    def serv(self):
        self.text.setText("Starting Server ...")
        path = self.path.text()
        proc = subprocess.Popen(
            ["start", "cmd", "/k", f"python {path} runserver"], shell=True
        )
        proc.wait()

    def mmg(self):
        self.text.setText("migrating ...")
        path = self.path.text()
        proc = subprocess.Popen(
            ["start", "cmd", "/c", f"python {path} makemigrations"], shell=True
        )
        proc = subprocess.Popen(
            ["start", "cmd", "/c", f"python {path} migrate"], shell=True
        )
        proc.wait()

    def back_handler(self):
        self.close()
        self.django_back = django_action_chose()
        self.django_back.show()
