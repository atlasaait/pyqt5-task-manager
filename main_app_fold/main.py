import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidget, QMainWindow, QVBoxLayout, QWidget
import json


class FenetreApp(QtWidgets.QWidget, QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Gestionnaire de tâches")
        self.resize(800, 800)

        contain = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(contain)

        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(contain)
        scroll.setWidgetResizable(True)

        layout_scroll = QtWidgets.QVBoxLayout(self)
        layout_scroll.addWidget(scroll)

    ## -----------------------------------------------------------------------------------------------------------------------
        
        ## SETTINGS
        settings = QtWidgets.QLabel("Paramètres du task manager")
        settings.setStyleSheet("font-weight: bold; font-size: 17px;")
        layout.addRow(settings)

        settings_list = QtWidgets.QComboBox()
        settings_list.addItems(["Language", "Elements", "Other"])
        layout.addRow(settings_list)

        ## PROPERTIES
        property = QtWidgets.QLabel("Propriétés du task manager")
        property.setStyleSheet("font-weight: bold; font-size: 17px;")
        layout.addRow(property)

        property_list = QtWidgets.QComboBox()
        property_list.addItems(["Size", "Theme", "Add stats"])  
        layout.addRow(property_list)

    def charger_taches(chemin="tasks.json"):
        try:
            with open(chemin, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = FenetreApp()
    sys.exit(app.exec_())