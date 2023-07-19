import sys , os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3 as sql
from PIL import Image



con = sql.connect('Products.db')
cur = con.cursor()

default_img = 'Pics/alarm.png'

class ConfirmWindow(QWidget):
    def __init__(self,product_name,product_id, member_name, member_id,quantity):
        super().__init__()
        self.setWindowTitle('Sell Product')
        self.setWindowIcon(QIcon('Pics/alarm.png'))
        self.setGeometry(200,100,320,420)
        self.setFixedSize(self.size())
        self.product_name_sell = product_name
        self.product_id_sell = product_id
        self.member_name_sell = member_name
        self.member_id_sell = member_id
        self.quantity_sell = quantity
        self.UI()
        self.show()
        
    def UI(self):
           
        self.widgets()
        self.layouts()
        
    
    def widgets(self):
        # widgets of top layout
        self.sell_product_img = QLabel()
        self.img = QPixmap('Pics/icons8-sell-100 (1).png')
        self.sell_product_img.setPixmap(self.img)
        self.sell_product_img.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_text = QLabel('Sell Product')
        self.title_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # widgets of botoom layout
        self.product_name = QLabel()
        self.product_name.setText(self.product_name_sell)
        self.member_name = QLabel()
        self.member_name.setText(self.member_name_sell)
        
        price = cur.execute("SELECT product_price FROM products WHERE product_id=?",(self.product_id_sell,)).fetchone()
        self.amount = self.quantity_sell * price[0]
        self.amount_label = QLabel()
        self.amount_label.setText(f'{price[0]} * {self.quantity_sell} = {self.amount}')
        
        
        self.confirm_btn = QPushButton('Confirm')
        self.confirm_btn.clicked.connect(self.funcConfirm)
        
        price = cur.execute("SELECT product_price FROM products WHERE product_id=?",(self.product_id_sell,)).fetchone()
        self.amount = self.quantity_sell * price[0]
        

        self.title_text.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                # border-radius: 5px;
            }
        """)

        self.member_name.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                padding: 5px;
                border-radius: 5px;
            }
        """)

        self.product_name.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                padding: 5px;
                border-radius: 5px;
            }
        """)
        
        

        # Add styles to the rest of the widgets

        # ...



        self.confirm_btn.setStyleSheet("""
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
        self.top_layout.addWidget(self.sell_product_img)
        self.top_frame.setLayout(self.top_layout)
        
        # widgets of form layout
        self.bottom_layout.addRow(QLabel('Product:'),self.product_name)
        self.bottom_layout.addRow(QLabel('Member:'),self.member_name)
        self.bottom_layout.addRow(QLabel('Amount:'),self.amount_label)
        self.bottom_layout.addRow(QLabel(''),self.confirm_btn)
        self.bottom_frame.setLayout(self.bottom_layout)
        
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)
        
    def funcConfirm(self):
        try:
                sell_query = " INSERT INTO 'sellings' (selling_member_id, selling_product_id, selling_quantity, selling_amount) VALUES (?,?,?,?) "
                cur.execute(sell_query,(self.member_id_sell,self.product_id_sell,self.quantity_sell,self.amount))
                self.qouta = cur.execute("SELECT product_qouta FROM products WHERE product_id=?",(self.product_id_sell,)).fetchone()
                con.commit()
                # QMessageBox.information(self,'Info' , 'Product has been sold')
                
                
                if self.quantity_sell == self.qouta[0]:
                    cur.execute("UPDATE products set product_qouta=?, product_availability=? WHERE product_id=?",(0,'Unavailable',self.product_id_sell))
                    con.commit()
                    self.close()
                else :
                    new_qouta = self.qouta[0] - self.quantity_sell
                    cur.execute("UPDATE products set product_qouta=? WHERE product_id=?",(new_qouta,self.product_id_sell))
                    con.commit()
                    self.close()
                    
                QMessageBox.information(self,'Info' , 'Success')
        except:
                QMessageBox.information(self,'Info' , 'Something went wrong !!')
        