import sys
from PyQt5 import QtWidgets

class FenetreApp(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Task Manager - TEST")

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

        self.setFixedHeight(800)
        self.setFixedWidth(800)
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = FenetreApp()
    sys.exit(app.exec_())