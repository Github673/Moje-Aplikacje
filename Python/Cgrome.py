from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ustawienie tytułu okna
        self.setWindowTitle("Aplikacja typu Chrome")

        # Ustawienie rozmiaru okna
        self.setGeometry(100, 100, 800, 600)

        # Utworzenie paska menu i paska narzędzi
        menu_bar = self.menuBar()
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Dodanie przycisków do paska narzędzi
        new_tab_action = QAction(QIcon("icons/new_tab.png"), "Nowa karta", self)
        new_tab_action.triggered.connect(self.new_tab)
        toolbar.addAction(new_tab_action)

        # Utworzenie panelu bocznego
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(150)
        self.sidebar.itemClicked.connect(self.sidebar_clicked)
        self.addDockWidget(Qt.LeftDockWidgetArea, QDockWidget("Karty", self).setWidget(self.sidebar))

        # Utworzenie widżetu wyświetlającego stronę internetową
        self.webview = QWebEngineView()
        self.setCentralWidget(self.webview)

        # Utworzenie listy kart
        self.tabs = []

        # Otwarcie pierwszej karty
        self.new_tab()

    def new_tab(self):
        # Utworzenie nowej karty
        tab = QWebEngineView()
        self.tabs.append(tab)

        # Dodanie nowej karty do menu i panelu bocznego
        title = f"Karta {len(self.tabs)}"
        self.sidebar.addItem(title)
        self.sidebar.setCurrentRow(len(self.tabs) - 1)

        # Wyświetlenie nowej karty w panelu głównym
        self.webview.setUrl(QUrl("about:blank"))
        self.webview.page().layout().addWidget(tab)

    def sidebar_clicked(self, item):
        # Przełączenie na wybraną kartę
        index = self.sidebar.row(item)
        self.webview.page().layout().setCurrentWidget(self.tabs[index])

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()