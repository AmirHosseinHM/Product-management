import sys , os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3 as sql
# from PIL import Image



con = sql.connect('Products.db')
cur = con.cursor()



# default_img = 'Pics/box.png'


class AddMember(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Member')
        self.setWindowIcon(QIcon('Pics/company.png'))
        self.setGeometry(200,100,320,420)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
        
    def UI(self):
            
        self.widgets()
        self.layouts()
        
        
        
        
    def widgets(self):
        # widgets of top layout
        self.add_member_img = QLabel()
        self. img = QPixmap('Pics/icons8-add-male-user-group-100.png')
        self.add_member_img.setPixmap(self.img)
        self.add_member_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_text = QLabel('Add Member')
        self.title_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # widgets of bottom layout
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText('Enter name of member')
        
        self.surname_entry = QLineEdit()
        self.surname_entry.setPlaceholderText('Enter surname of member')
        
        self.phone_entry = QLineEdit()
        self.phone_entry.setPlaceholderText('Enter phone number')
       
        
        self.submit_btn = QPushButton('Submit')
        self.submit_btn.clicked.connect(self.addMember)
        
        self.title_text.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                
            }
        """)

        self.name_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                padding: 5px;
                border-radius: 5px;
            }
        """)

        self.surname_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                padding: 5px;
                border-radius: 5px;
            }
        """)
        
        self.phone_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                padding: 5px;
                border-radius: 5px;
            }
        """)
        
        

        self.submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #008CBA;
                color: white;
                padding: 8px 16px;
                border: none;
                cursor: pointer;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #007a9e;
            }
        """)
        
        
        
    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame() 
        
        
        ## add widgets
        # widgets of top layout
        self.top_layout.addWidget(self.title_text)
        self.top_layout.addWidget(self.add_member_img)
        self.top_frame.setLayout(self.top_layout)
        
        # widgets of form layout
        self.bottom_layout.addRow(QLabel('Name:'),self.name_entry)
        self.bottom_layout.addRow(QLabel('Surname:'),self.surname_entry)
        self.bottom_layout.addRow(QLabel('Phone:'),self.phone_entry)
        self.bottom_layout.addRow(QLabel(''),self.submit_btn)
        self.bottom_frame.setLayout(self.bottom_layout)
        
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)
        
        
        
    def addMember(self):

        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = self.phone_entry.text()
        
        if (name and surname and phone) != "":
            
            try:
                query = " INSERT INTO 'members' (member_name,member_surname,member_phone) VALUES(?,?,?) "
                cur.execute(query,(name,surname,phone))
                con.commit()
                QMessageBox.information(self,'Info' , 'Member has been added')
                # con.close()
                self.name_entry.setText('')
                self.surname_entry.setText('')
                self.phone_entry.setText('')
                
                
            except:
                QMessageBox.information(self,'Info' , 'Member has not been added')
        
        else: 
            QMessageBox.information(self,'Info' , 'Fields can not be empty')
                    