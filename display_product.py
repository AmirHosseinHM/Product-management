import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3 as sql
from PIL import Image


con = sql.connect('Products.db')
cur = con.cursor()

class DisplayProduct(QWidget):
    def __init__(self , product_id):
        super().__init__()
        self.setWindowTitle("Products Details")
        self.setWindowIcon(QIcon('Pics/exam.png'))
        self.setGeometry(200,100,450,580)
        self.setFixedSize(self.size())
        self.product_id = product_id
        self.UI()
        self.show()
    
    
    
    def UI(self):
        
        self.productDetails()
        self.widgets()
        self.layouts()
    
    
    def productDetails(self):
        
        query = ("SELECT * FROM products WHERE product_id =?")
        product = cur.execute(query,(self.product_id,)).fetchone() # single item tuple -> (1,)
        self.product_name = product[1]
        self.manufact_product = product[2]
        self.product_price = product[3]
        self.product_quota = product[4]
        self.product_img = product[5]
        self.product_status = product[6]
        
    
    def widgets(self):
        # widgets of top layout
        self.product_img_widget = QLabel()
        self. img = QPixmap(f'imgs/{self.product_img}')
        self.product_img_widget.setPixmap(self.img)
        self.product_img_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_text = QLabel('Product Page')
        self.title_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # widgets of bottom layout
        self.name_entry = QLineEdit()
        self.name_entry.setText(self.product_name)
        
        self.manufact_entry = QLineEdit()
        self.manufact_entry.setText(self.manufact_product)
        
        self.price_entry = QLineEdit()
        self.price_entry.setText(str(self.product_price))
        
        self.qouta_entry = QLineEdit()
        self.qouta_entry.setText(str(self.product_quota))
        
        self.availability_combo = QComboBox()
        self.availability_combo.addItems(['Available' , 'Unavailable'])
        
        self.upload_btn = QPushButton('Upload')
        self.upload_btn.clicked.connect(self.uploadImg)
        
        self.del_btn = QPushButton('Delete')
        self.del_btn.clicked.connect(self.delProduct)
        
        self.update_btn = QPushButton('Update')
        self.update_btn.clicked.connect(self.updateProduct)
        
         # Add stylesheets to the desired widgets

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

        # Add styles to the rest of the widgets

        # ...

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
        # self.setStyleSheet(
        #     '''
        #     QLabel#product_img_widget {
        #         border: 2px solid #555;
        #         background-color: #eee;
        #         padding: 10px;
        #     }
        #     QLabel#product_img_widget:hover {
        #         border-color: #aaa;
        #     }
            
        #     QLabel#title_text {
        #         font-size: 24px;
        #         font-weight: bold;
        #         margin-bottom: 20px;
        #     }
            
        #     QLineEdit {
        #         padding: 10px;
        #         border-radius: 5px;
        #         border: 1px solid #ccc;
        #     }
            
        #     QComboBox {
        #         padding: 10px;
        #         border-radius: 5px;
        #         border: 1px solid #ccc;
        #     }
            
        #     QPushButton {
        #         padding: 10px 20px;
        #         border-radius: 5px;
        #         background-color: #4CAF50;
        #         color: white;
        #         font-size: 16px;
        #     }
            
        #     QPushButton:hover {
        #         background-color: #45a049;
        #     }
        #     '''
        # ) 
        
        
        ## add widgets
        # widgets of top layout
        self.top_layout.addWidget(self.title_text)
        self.top_layout.addWidget(self.product_img_widget)
        self.top_frame.setLayout(self.top_layout)
        
        # widgets of form layout
        self.bottom_layout.addRow(QLabel('Name:'),self.name_entry)
        self.bottom_layout.addRow(QLabel('Manufacturer:'),self.manufact_entry)
        self.bottom_layout.addRow(QLabel('Price:'),self.price_entry)
        self.bottom_layout.addRow(QLabel('Qouta:'),self.qouta_entry)
        self.bottom_layout.addRow(QLabel('Status:'),self.availability_combo)
        self.bottom_layout.addRow(QLabel('Image:'),self.upload_btn)
        self.bottom_layout.addRow(QLabel(''),self.del_btn)
        self.bottom_layout.addRow(QLabel(''),self.update_btn)
        self.bottom_frame.setLayout(self.bottom_layout)
        
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)
        
    
    def uploadImg(self):
        
        size = (150,150)
        self.file_name,ok = QFileDialog.getOpenFileName(self,'Upload Image','','Image Files (*.jpg *.png)')
        if ok:
            # print(self.file_name)
            self.product_img = os.path.basename(self.file_name)
            img = Image.open(self.file_name)
            img = img.resize(size)
            img.save('imgs/{0}'.format(self.product_img))
            
    
    def updateProduct(self):
        name = self.name_entry.text()
        manufact = self.manufact_entry.text()
        price = int(self.price_entry.text())
        qouta = int(self.qouta_entry.text())
        status = self.availability_combo.currentText()
        curr_img = self.product_img
        
        if (name and manufact and price and qouta) != "":
            try:
                query = " UPDATE 'products' set product_name=?,product_manufacture=?,product_price=?,product_qouta=?,product_img=?,product_availability=? WHERE product_id=? "
                cur.execute(query,(name,manufact,price,qouta,curr_img,status,self.product_id))
                con.commit()
                QMessageBox.information(self,'Info' , 'Product has been updated')
                # con.close()
                
            except:
                QMessageBox.information(self,'Info' , 'Product has not been updated')
        
        else: 
            QMessageBox.information(self,'Info' , 'Fields can not be empty')
                    
    def delProduct(self):
        
        massage_box = QMessageBox.information(self,'Warning' , 'Are you sure to delete this product',QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if massage_box == QMessageBox.Yes:
            try:
              cur.execute("DELETE FROM 'products' WHERE product_id=?",(self.product_id,))
              con.commit()
              QMessageBox.information(self,'Info' , 'Product has been deleted !')
              self.close()
            except:
              QMessageBox.information(self,'Info' , 'Product has not been deleted')
        
        
        
        
        
        
        
        
        
        
        
        
        