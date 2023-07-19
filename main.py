import sys , os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3 
import hashlib
from app import Main

class LoginRegisterPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login and Registration')
        self.setWindowIcon(QIcon('Pics/null.png'))
        self.setGeometry(400, 100, 400, 300)
        
        self.pages_widget = QStackedWidget()

        self.login_page = LoginPage(parent=self)
        self.register_page = RegisterPage(parent=self)
        
        self.pages_widget.addWidget(self.login_page)
        self.pages_widget.addWidget(self.register_page)

        self.setCentralWidget(self.pages_widget)

        # Create users table in the database if it doesn't exist
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users 
                        (username TEXT PRIMARY KEY,
                         password TEXT)''')
        conn.commit()
        conn.close()
        
    def switch_page(self, index):
        self.pages_widget.setCurrentIndex(index)



class LoginPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        image_label = QLabel()
        pixmap = QPixmap("imgs/20945760.jpg")  # Replace "path/to/your/image.jpg" with the actual image path
        image_label.setPixmap(pixmap.scaledToWidth(300))  # Adjust the width as needed
        layout.addWidget(image_label, alignment=Qt.AlignCenter)

        # Title label
        title_label = QLabel('Login')
        title_label.setStyleSheet('font-size: 24px; font-weight: bold; margin-bottom: 20px; color: #333;')
        layout.addWidget(title_label, alignment=Qt.AlignCenter)  # Center align the login label

        
        
        
        
        
        
        self.username_label = QLabel('Username')
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet('padding: 5px; border-radius: 3px; border: 1px solid #ccc;')
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel('Password')
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet('padding: 5px; border-radius: 3px; border: 1px solid #ccc;')
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_btn = QPushButton('Login')
        self.login_btn.setStyleSheet('padding: 7px 15px; border-radius: 3px; background-color: #4CAF50; color: white;')
        self.login_btn.clicked.connect(self.login)
        layout.addWidget(self.login_btn)

        self.register_label = QLabel('Don\'t have an account?')
        self.register_label.setAlignment(Qt.AlignCenter)
        self.register_label.setStyleSheet('font-size: 16px; color: #333; margin-top: 20px;')
        self.register_btn = QPushButton('Register Now')
        self.register_btn.setStyleSheet('padding: 10px 20px; border-radius: 5px; background-color: #555; color: white; font-size: 16px;')
        self.register_btn.clicked.connect(lambda: parent.switch_page(1))
        layout.addWidget(self.register_label)
        layout.addWidget(self.register_btn)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Connect to the database
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()

        # Check if user exists
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()

        if user is None:
            QMessageBox.warning(self, 'Login Failed', 'Invalid username or password.')
        else:
            # Hash the password and compare it with the stored hash
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            if user[1] == password_hash:
                QMessageBox.information(self, 'Login Successful', 'You are logged in.')
                self.main = Main()
                self.parent.close()
                
            else:
                QMessageBox.warning(self, 'Login Failed', 'Invalid username or password.')

        conn.close()


class RegisterPage(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        layout = QVBoxLayout()

        image_label = QLabel()
        pixmap = QPixmap("imgs/20945760.jpg")  # Replace "path/to/your/image.jpg" with the actual image path
        image_label.setPixmap(pixmap.scaledToWidth(300))  # Adjust the width as needed
        layout.addWidget(image_label, alignment=Qt.AlignCenter)

        title_label = QLabel('Register')
        title_label.setStyleSheet('font-size: 24px; font-weight: bold; margin-bottom: 20px; color:#333')
        layout.addWidget(title_label, alignment=Qt.AlignCenter)
        
        

        self.username_label = QLabel('Username')
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet('padding: 5px; border-radius: 3px; border: 1px solid #ccc;')
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel('Password')
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet('padding: 5px; border-radius: 3px; border: 1px solid #ccc;')
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.confirm_password_label = QLabel('Confirm Password')
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setStyleSheet('padding: 5px; border-radius: 3px; border: 1px solid #ccc;')
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)

        self.register_btn = QPushButton('Register')
        self.register_btn.setStyleSheet('padding: 7px 15px; border-radius: 3px; background-color: #4CAF50; color: white;')
        self.register_btn.clicked.connect(self.register)
        layout.addWidget(self.register_btn)

        self.login_label = QLabel('Already have an account?')
        self.login_btn = QPushButton('Login')
        self.login_btn.setStyleSheet('padding: 7px 15px; border-radius: 3px; background-color: transparent; border: 1px solid #4CAF50; color: #4CAF50;')
        self.login_btn.clicked.connect(lambda: parent.switch_page(0))
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_btn)

        self.setLayout(layout)
        


    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        # Validate form fields
        if not username:
            QMessageBox.warning(self, 'Registration Failed', 'Please enter a username.')
            return

        if not password:
            QMessageBox.warning(self, 'Registration Failed', 'Please enter a password.')
            return

        if password != confirm_password:
            QMessageBox.warning(self, 'Registration Failed', 'Passwords do not match.')
            return

        # # Hash the password
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        # Connect to the database
        conn = sqlite3.connect('user_database.db')
        c = conn.cursor()

        # Check if username already exists
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()

        if user is not None:
            QMessageBox.warning(self, 'Registration Failed', 'Username already exists.')
        else:
            # Insert the new user into the database
            c.execute("INSERT INTO users VALUES (?, ?)", (username, password_hash))
            conn.commit()
            QMessageBox.information(self, 'Registration Successful', 'Registration was successful.')
            

        conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_register_page = LoginRegisterPage()
    login_register_page.show()
    sys.exit(app.exec_())

