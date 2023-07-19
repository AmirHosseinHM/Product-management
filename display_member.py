import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3 as sql
from PIL import Image

con = sql.connect('Products.db')
cur = con.cursor()

class DisplayMember(QWidget):
    def __init__(self , member_id):
        super().__init__()
        self.setWindowTitle("Members Details")
        self.setWindowIcon(QIcon('Pics/login.png'))
        self.setGeometry(200,100,350,480)
        self.setFixedSize(self.size())
        self.member_id = member_id
        self.UI()
        self.show()
    
    
    
    def UI(self):
        
        self.memeberDetails()
        self.widgets()
        self.layouts()
        
        
    
    def memeberDetails(self):
        
        query = ("SELECT * FROM members WHERE member_id =?")
        member = cur.execute(query,(self.member_id,)).fetchone() # single item tuple -> (1,)
        self.member_name = member[1]
        self.memeber_surname = member[2]
        self.phone = member[3]

        
    def widgets(self):
        # widgets of top layout
        self.member_img_widget = QLabel()
        self. img = QPixmap('Pics/icons8-member-100.png')
        self.member_img_widget.setPixmap(self.img)
        # self.member_img_widget.setStyleSheet("width:100pt")
        self.member_img_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_text = QLabel('member Page')
        self.title_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # widgets of bottom layout
        self.name_entry = QLineEdit()
        self.name_entry.setText(self.member_name)
        
        self.surname_entry = QLineEdit()
        self.surname_entry.setText(self.memeber_surname)
        
        self.phone_entry = QLineEdit()
        self.phone_entry.setText(str(self.phone))
        
        self.del_btn = QPushButton('Delete')
        self.del_btn.clicked.connect(self.delMember)
        
        self.update_btn = QPushButton('Update')
        self.update_btn.clicked.connect(self.updateMember)
        
         # Add stylesheets to the desired widgets

        self.title_text.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                # border-radius: 5px;
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
        
        

        # Add styles to the rest of the widgets

        # ...


        self.del_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 8px 16px;
                border: none;
                cursor: pointer;
                border-radius: 5px;
                
            }
            QPushButton:hover {
                background-color: #d6372a;
                
            }
        """)

        self.update_btn.setStyleSheet("""
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
        self.top_layout.addWidget(self.member_img_widget)
        self.top_frame.setLayout(self.top_layout)
        
        # widgets of form layout
        self.bottom_layout.addRow(QLabel('Name:'),self.name_entry)
        self.bottom_layout.addRow(QLabel('Surname:'),self.surname_entry)
        self.bottom_layout.addRow(QLabel('Phone:'),self.phone_entry)
        self.bottom_layout.addRow(QLabel(''),self.del_btn)
        self.bottom_layout.addRow(QLabel(''),self.update_btn)
        self.bottom_frame.setLayout(self.bottom_layout)
        
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)
        
    
    def delMember(self):
        
        massage_box = QMessageBox.information(self,'Warning' , 'Are you sure to delete this member',QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if massage_box == QMessageBox.Yes:
            try:
                cur.execute("DELETE FROM 'members' WHERE member_id=?",(self.member_id,))
                con.commit()
                QMessageBox.information(self,'Info' , 'Member has been deleted !')
                self.close()
            except:
              QMessageBox.information(self,'Info' , 'Member has not been deleted')
        
    def updateMember(self):
        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = int(self.phone_entry.text())


        
        if (name and surname and phone) != "":
            try:
                query = " UPDATE 'members' set member_name=?,member_surname=?,member_phone=? WHERE member_id=? "
                cur.execute(query,(name,surname,phone,self.member_id))
                con.commit()
                QMessageBox.information(self,'Info' , 'Member has been updated')
                # con.close()
                
            except:
                QMessageBox.information(self,'Info' , 'Member has not been updated')
        
        else: 
          QMessageBox.information(self,'Info' , 'Fields can not be empty')