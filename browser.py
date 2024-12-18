import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web browser")
        self.setGeometry(100, 100, 1024, 768)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.navigate_button = QPushButton("Go to")
        self.navigate_button.clicked.connect(self.navigate_to_url)

        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.navigate_button)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def navigate_to_url(self):
        url = self.url_bar.text().strip()
        
        if "." not in url and " " not in url:
            url = f"https://www.google.com/search?q={url}"
        elif not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url
        
        self.browser.setUrl(QUrl(url))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec())

