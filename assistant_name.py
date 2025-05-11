import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

# File to store the assistant's name
NAME_FILE = "/home/preethi/SMART_LAP/assistant_name.txt"


class NamingPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Name Your Assistant")
        self.resize(400, 200)

        # Layout and widgets
        layout = QVBoxLayout()

        label = QLabel("Enter a name for your assistant:")
        layout.addWidget(label)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Type the name here...")
        layout.addWidget(self.name_input)

        save_button = QPushButton("Save Name")
        save_button.clicked.connect(self.save_name)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_name(self):
        name = self.name_input.text().strip()
        if name:
            with open(NAME_FILE, "w") as f:
                f.write(name)
            QMessageBox.information(self, "Success", f"Assistant named '{name}'!")
            self.close()  # Close the naming page
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a valid name.")

def main():
    # Check if the assistant name is already set
    if not os.path.exists(NAME_FILE):
        app = QApplication(sys.argv)
        naming_page = NamingPage()
        naming_page.show()
        sys.exit(app.exec_())
    else:
        print("Assistant name is already set. No naming page needed.")

if __name__ == "__main__":
    main()
