import sys , os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3 as sql
from PIL import Image



con = sql.connect('Products.db')
cur = con.cursor()



default_img = 'Pics/box.png'


class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Product')
        self.setWindowIcon(QIcon('Pics/icons8-add-product-100.png'))
        self.setGeometry(200,100,320,420)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
        
    def UI(self):
            
        self.widgets()
        self.layouts()
        
        
    def widgets(self):
        # widgets of top layout
        self.add_product_img = QLabel()
        self. img = QPixmap('Pics/icons8-add-product-100.png')
        self.add_product_img.setPixmap(self.img)
        self.title_text = QLabel('Add Product')
        
        # widgets of botoom layout
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText('Enter name of product')
        
        self.manufact_entry = QLineEdit()
        self.manufact_entry.setPlaceholderText('Enter name of manufacturer')
        
        self.price_entry = QLineEdit()
        self.price_entry.setPlaceholderText('Enter price of product')
        
        self.qouta_entry = QLineEdit()
        self.qouta_entry.setPlaceholderText('Enter qouta of product')
        
        self.upload_btn = QPushButton('Upload')
        self.upload_btn.clicked.connect(self.uploadImg)
        
        self.submit_btn = QPushButton('Submit')
        self.submit_btn.clicked.connect(self.addProduct)
        
        # self.add_product_img.setStyleSheet("""
        #     QLabel {
        #         border: 1px solid gray;
        #     }
        # """)

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

        self.manufact_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                padding: 5px;
                border-radius: 5px;
            }
        """)
        
        self.qouta_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                padding: 5px;
                border-radius: 5px;
            }
        """)
        
        self.price_entry.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                padding: 5px;
                border-radius: 5px;
            }
        """)
        
        self.upload_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                border: none;
                cursor: pointer;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
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
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame() 
        
        ## add widgets
        # widgets of top layout
        self.top_layout.addWidget(self.add_product_img)
        self.top_layout.addWidget(self.title_text)
        self.top_frame.setLayout(self.top_layout)
        
        # widgets of form layout
        self.bottom_layout.addRow(QLabel('Name:'),self.name_entry)
        self.bottom_layout.addRow(QLabel('Manufacturer:'),self.manufact_entry)
        self.bottom_layout.addRow(QLabel('Price:'),self.price_entry)
        self.bottom_layout.addRow(QLabel('Qouta:'),self.qouta_entry)
        self.bottom_layout.addRow(QLabel('Upload:'),self.upload_btn)
        self.bottom_layout.addRow(QLabel(''),self.submit_btn)
        self.bottom_frame.setLayout(self.bottom_layout)
        
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)
        
        
        
    def uploadImg(self):
        
        global default_img
        size = (150,150)
        self.file_name,ok = QFileDialog.getOpenFileName(self,'Upload Image','','Image Files (*.jpg *.png)')
        if ok:
            # print(self.file_name)
            default_img = os.path.basename(self.file_name)
            img = Image.open(self.file_name)
            img = img.resize(size)
            img.save('imgs/{0}'.format(default_img))
    
    
    
    def addProduct(self):
        global default_img
        name = self.name_entry.text()
        manufact = self.manufact_entry.text()
        price = self.price_entry.text()
        qouta = self.qouta_entry.text()
        
        if (name and manufact and price and qouta) != "":
            
            try:
                query = " INSERT INTO 'products' (product_name,product_manufacture,product_price,product_qouta,product_img) VALUES(?,?,?,?,?) "
                cur.execute(query,(name,manufact,price,qouta,default_img))
                con.commit()
                QMessageBox.information(self,'Info' , 'Product has been added')
                # con.close()
                
            except:
                QMessageBox.information(self,'Info' , 'Product has not been added')
        
        else: 
            QMessageBox.information(self,'Info' , 'Fields can not be empty')
                    







                