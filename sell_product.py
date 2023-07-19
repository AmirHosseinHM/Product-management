import sys , os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3 as sql
from PIL import Image
from sell_product_update import ConfirmWindow



con = sql.connect('Products.db')
cur = con.cursor()

default_img = 'Pics/alarm.png'

class SellProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sell Product')
        self.setWindowIcon(QIcon('Pics/alarm.png'))
        self.setGeometry(200,100,320,420)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
        
    def UI(self):
            
        self.widgets()
        self.layouts()
        
        
    def widgets(self):
        # widgets of top layout
        self.sell_product_img = QLabel()
        self. img = QPixmap('Pics/icons8-sell-100 (1).png')
        self.sell_product_img.setPixmap(self.img)
        self.sell_product_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_text = QLabel('Add Product')
        self.title_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # widgets of botoom layout
        self.product_combo = QComboBox()
        self.product_combo.currentIndexChanged.connect(self.changeComboValue)
        self.member_combo = QComboBox()
        self.quantity_combo = QComboBox()
        
        self.submit_btn = QPushButton('Submit')
        self.submit_btn.clicked.connect(self.sellProductUpdate)
        
        products = cur.execute("SELECT * FROM products WHERE product_availability='Available'").fetchall()
        members = cur.execute("SELECT member_id,member_name FROM members").fetchall()
        quantity = products[0][4]
        
        for product in products:
            self.product_combo.addItem(product[1],product[0]) # product name and id(hiden)
            
        for member in members:
            self.member_combo.addItem(member[1],member[0]) # member name and id(hiden)
        
        # for i in range(1,quantity+1):
        #     self.quantity_combo.addItem(str(i)) 
        
        self.title_text.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                
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
        
        self.setStyleSheet("""
            QComboBox {
                background-color: #5b5b5b;
                color: white;
                padding: 8px 16px;
                border: none;
                cursor: pointer;
                border-radius: 5px;
            }
            QComboBox:hover {
                background-color: #007a9e;
            }
        """
            
        )
        
    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame() 
        
        ## add widgets
        # widgets of top layout
        self.top_layout.addWidget(self.title_text)
        self.top_layout.addWidget(self.sell_product_img)
        self.top_frame.setLayout(self.top_layout)
        
        # widgets of form layout
        self.bottom_layout.addRow(QLabel('Products:'),self.product_combo)
        self.bottom_layout.addRow(QLabel('Member:'),self.member_combo)
        self.bottom_layout.addRow(QLabel('Quantity:'),self.quantity_combo)
        self.bottom_layout.addRow(QLabel(''),self.submit_btn)
        self.bottom_frame.setLayout(self.bottom_layout)
        
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)
    
    
    def changeComboValue(self):
        self.quantity_combo.clear()
        product_id = self.product_combo.currentData()
        qouta = cur.execute("SELECT product_qouta FROM products WHERE product_id=?",(product_id,)).fetchone()
        
        for i in range(1,qouta[0]+1):
            self.quantity_combo.addItem(str(i))
            
            
    def sellProductUpdate(self):
        product_name = self.product_combo.currentText()
        product_id = self.product_combo.currentData()
        
        member_name = self.member_combo.currentText()
        member_id = self.member_combo.currentData()
              
        quantity = int(self.quantity_combo.currentText())    
        
        self.confirm = ConfirmWindow(product_name,product_id, member_name, member_id,quantity)
        self.close()   
            
            
            
            
            