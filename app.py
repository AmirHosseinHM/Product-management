import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import sqlite3 as sql
from add_product import AddProduct
from add_member import AddMember
from sell_product import SellProduct
from display_product import DisplayProduct
from display_member import DisplayMember
from style import *


con = sql.connect('Products.db')
cur = con.cursor()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shop")
        self.setWindowIcon(QIcon('Pics/truck.png'))
        self.setGeometry(150,50,1000,650)
        self.setFixedSize(self.size())
        self.UI()
        self.show()
        
    def UI(self):
        
        self.toolBar()
        self.tabeWigdet()
        self.widgets()
        self.layouts()
        self.displayProducts()
        self.diplayMembers()
        self.getStatistics()
        
            
    def toolBar(self):
        self.tool_bar = self.addToolBar('tool bar')
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        
        self.add_product = QAction(QIcon('Pics/icons8-add-product-100 (2).png'),'Add Product' , self)
        self.tool_bar.addAction(self.add_product)
        self.add_product.triggered.connect(self.funcAddProduct)
        self.tool_bar.addSeparator()
        
        self.add_member = QAction(QIcon('Pics/icons8-add-male-user-group-100 (1).png'),'Add Member' , self)
        self.tool_bar.addAction(self.add_member)
        self.add_member.triggered.connect(self.funcAddMember)
        self.tool_bar.addSeparator()
        
        self.sell_product = QAction(QIcon('Pics/icons8-sell-100.png'),'Sell Product' , self)
        self.tool_bar.addAction(self.sell_product)
        self.sell_product.triggered.connect(self.funcSellProduct)
        self.tool_bar.addSeparator()
        
        self.exit = QAction(QIcon('Pics/icons8-exit-100.png'),'Close' , self)
        self.tool_bar.addAction(self.exit)
        self.exit.triggered.connect(self.Quit)
        self.tool_bar.addSeparator()
        
        
    
    def tabeWigdet(self):
        self.tabs= QTabWidget()
        self.tabs.blockSignals(True)
        self.tabs.currentChanged.connect(self.tabChanges)
        self.setCentralWidget(self.tabs)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1,'Products')
        self.tabs.addTab(self.tab2,'Members')
        self.tabs.addTab(self.tab3,'Statastics')
        
        
        
    def widgets(self):
        ## tab1 -> products widgets
        # main left layout widgets
        self.products_table = QTableWidget()  
        self.products_table.setColumnCount(6)
        self.products_table.setColumnHidden(0,True)
        self.products_table.setHorizontalHeaderItem(0,QTableWidgetItem('Product Id'))
        self.products_table.setHorizontalHeaderItem(1,QTableWidgetItem('Product Name'))
        self.products_table.setHorizontalHeaderItem(2,QTableWidgetItem('Manufacturer'))
        self.products_table.setHorizontalHeaderItem(3,QTableWidgetItem('Price'))
        self.products_table.setHorizontalHeaderItem(4,QTableWidgetItem('Qouta'))
        self.products_table.setHorizontalHeaderItem(5,QTableWidgetItem('Availbility'))
        self.products_table.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.products_table.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.products_table.doubleClicked.connect(self.detailSelectedProduct)
        
        
        # right top layout widgets
        self.search_text = QLabel('Search')
        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText('Search for products')
        self.search_entry.setStyleSheet(ser_ent_style())
        self.search_botton = QPushButton('Search')
        self.search_botton.clicked.connect(self.searchProducts)
        self.search_botton.setStyleSheet(bot_styles())
        
        
        
        # right middle layout widgets
        self.all_products = QRadioButton('All Products')
        self.available = QRadioButton('Available')
        self.not_available = QRadioButton('Not Available') 
        self.list_botton     = QPushButton('List')
        self.list_botton.clicked.connect(self.listProducts)
        self.list_botton.setStyleSheet(bot_styles())
        
        
        ## tab2 -> members widgets
        self.members_table = QTableWidget()
        self.members_table.setColumnCount(4)
        self.members_table.setHorizontalHeaderItem(0,QTableWidgetItem('Member Id'))
        self.members_table.setHorizontalHeaderItem(1,QTableWidgetItem('Member Name'))
        self.members_table.setHorizontalHeaderItem(2,QTableWidgetItem('Member Surname'))
        self.members_table.setHorizontalHeaderItem(3,QTableWidgetItem('Phone'))
        self.members_table.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.members_table.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.members_table.horizontalHeader().setSectionResizeMode(3,QHeaderView.Stretch)
        self.members_table.doubleClicked.connect(self.detailSelectedMember)
        
        self.member_search_text = QLabel('Search members')
        self.member_search_entry = QLineEdit()
        self.member_search_entry.setPlaceholderText('Search')
        self.member_search_entry.setStyleSheet(ser_ent_style())
        self.member_search_botton = QPushButton('Search')
        self.member_search_botton.clicked.connect(self.searchMembers)
        self.member_search_botton.setStyleSheet(bot_styles())
        
        
        ## tab3 -> statistics widgets
        self.total_products_lable = QLabel()
        self.total_member_lable = QLabel()
        self.sold_products_lable = QLabel()
        self.total_amount_lable = QLabel()
        

        self.total_products_lable.setStyleSheet('''
        font-weight: bold;
        color: #333333;
        font-size: 16px; /* Increase font size to increase label size */
        ''')
        self.total_member_lable.setStyleSheet('''
            font-weight: bold;
            color: #333333;
            font-size: 16px; /* Increase font size to increase label size */
        ''')
        self.sold_products_lable.setStyleSheet('''
            font-weight: bold;
            color: #333333;
            font-size: 16px; /* Increase font size to increase label size */
        ''')
        self.total_amount_lable.setStyleSheet('''
            font-weight: bold;
            color: #333333;
            font-size: 16px; /* Increase font size to increase label size */
        ''')

        
        
        
        
        
        
        
        
    def layouts(self):
        ## tab 1 -> Products layouts
        self.main_layout = QHBoxLayout()
        self.main_left_layout = QVBoxLayout()
        self.main_right_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_middle_layout = QHBoxLayout()
        self.top_group_box = QGroupBox('Search Box')
        self.top_group_box.setStyleSheet(searchBoxStyle())
        self.middle_group_box = QGroupBox('List Box')
        self.middle_group_box.setStyleSheet(listBoxStyle())
        self.bottom_group_box = QGroupBox()
        
        # add widgets
        # left main layout widget
        self.main_left_layout.addWidget(self.products_table)
        
        # right top layout widget
        self.right_top_layout.addWidget(self.search_text)
        self.right_top_layout.addWidget(self.search_entry)
        self.right_top_layout.addWidget(self.search_botton)
        self.top_group_box.setLayout(self.right_top_layout)
        
        # right middle layout widgets
        self.right_middle_layout.addWidget(self.all_products)
        self.right_middle_layout.addWidget(self.available)
        self.right_middle_layout.addWidget(self.not_available)
        self.right_middle_layout.addWidget(self.list_botton)
        self.middle_group_box.setLayout(self.right_middle_layout)
        
        self.main_right_layout.addWidget(self.top_group_box,25)
        self.main_right_layout.addWidget(self.middle_group_box,25)
        self.main_right_layout.addWidget(self.bottom_group_box,50)
        self.main_layout.addLayout(self.main_left_layout , 70)
        self.main_layout.addLayout(self.main_right_layout , 30)
        self.tab1.setLayout(self.main_layout)
        
        

        
        ## tab2 -> members layouts
        self.member_main_layout = QHBoxLayout()
        self.member_left_layout = QHBoxLayout()
        self.member_right_layout = QHBoxLayout()
        self.member_right_group_box = QGroupBox('Search for members')
        self.member_right_group_box.setContentsMargins(10,10,10,500)
        
        self.member_right_layout.addWidget(self.member_search_text)
        self.member_right_layout.addWidget(self.member_search_entry)
        self.member_right_layout.addWidget(self.member_search_botton)
        self.member_right_group_box.setLayout(self.member_right_layout)
        # self.member_right_group_box.setStyleSheet(searchBoxStyle())
            
        self.member_left_layout.addWidget(self.members_table)
        self.member_main_layout.addLayout(self.member_left_layout,70)
        self.member_main_layout.addWidget(self.member_right_group_box,30)
        self.tab2.setLayout(self.member_main_layout)
        
        
        ## tab3 -> statistics layout
        self.statistics_main_layout = QVBoxLayout()
        self.statistics_layout = QFormLayout()
        self.statistics_group_box = QGroupBox('Statistics')
        self.statistics_layout.addRow('Total Products:',self.total_products_lable)
        self.statistics_layout.addRow('Total Member:',self.total_member_lable)
        self.statistics_layout.addRow('Sold Products:',self.sold_products_lable)
        self.statistics_layout.addRow('Total Amount:',self.total_amount_lable)
        self.statistics_group_box.setLayout(self.statistics_layout)
        self.statistics_group_box.setFont(QFont('Arial',16))
        self.statistics_main_layout.addWidget(self.statistics_group_box)
        # Apply stylesheet to the statistics group box
        self.statistics_group_box.setStyleSheet('''
        QGroupBox {
            background-color: #E0E0E0;
            border: 1px solid #C0C0C0;
            border-radius: 4px;
            padding: 100px; /* Increase padding to increase the size of the group box */
            
        }
    ''')
        # Center align the statistics group box
        self.statistics_main_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.tab3.setLayout(self.statistics_main_layout)
        
        
        
        self.tabs.blockSignals(False)
        
        
    def funcAddProduct(self):
        self.new_product = AddProduct()
    
    
    def funcAddMember(self):
        self.new_member = AddMember()   
    
    
    def displayProducts(self):
        self.products_table.setFont(QFont('Times',10))
        for i in reversed(range(self.products_table.rowCount())):
            self.products_table.removeRow(i)

        query = cur.execute("SELECT product_id,product_name,product_manufacture,product_price,product_qouta,product_availability FROM products")
        for row_data in query:
            row_number = self.products_table.rowCount()
            self.products_table.insertRow(row_number)
            for col_number,data in enumerate(row_data):
                self.products_table.setItem(row_number ,col_number , QTableWidgetItem(str(data)))

        self.products_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  
    
        
    def diplayMembers(self):
        self.members_table.setFont(QFont('Times',10))
        for i in reversed(range(self.members_table.rowCount())):
            self.members_table.removeRow(i)

        query = cur.execute("SELECT member_id,member_name,member_surname,member_phone FROM members")
        for row_data in query:
            row_number = self.members_table.rowCount()
            self.members_table.insertRow(row_number)
            for col_number,data in enumerate(row_data):
                self.members_table.setItem(row_number ,col_number , QTableWidgetItem(str(data)))

        self.members_table.setEditTriggers(QAbstractItemView.NoEditTriggers)  
        
    
    def detailSelectedProduct(self):
        # global product_id
        list_product = []
        for i in range(6):
            list_product.append(self.products_table.item(self.products_table.currentRow(),i).text())
        product_id = list_product[0]  
        
        self.det_product_display = DisplayProduct(product_id)
        
        
    def detailSelectedMember(self):
        
        list_product = []
        for i in range(4):
            list_product.append(self.members_table.item(self.members_table.currentRow(),i).text())
        member_id = list_product[0]  
        
        self.det_member_display = DisplayMember(member_id)
        
     
    def searchMembers(self):
        value = self.member_search_entry.text()
        if value == '':
            QMessageBox.information(self,'Warning','Search query cant be empty !!')   
        
        else :
            
            self.search_entry.setText('')
            query = ("SELECT * FROM members WHERE member_name LIKE ? or member_surname LIKE ? or member_phone LIKE ?")
            results = cur.execute(query,('%' + value + '%','%' + value + '%','%' + value + '%')).fetchall()
            
            if results == []:
                QMessageBox.information(self,'Warning','There is no such a member or surname')
            else:
                for i in reversed(range(self.members_table.rowCount())):
                    self.members_table.removeRow(i)
                
                for row_data in results:
                    row_num = self.members_table.rowCount()
                    self.members_table.insertRow(row_num)
                    for col_num , data in enumerate(row_data):
                        self.members_table.setItem(row_num,col_num,QTableWidgetItem(str(data)))


    def searchProducts(self):
        value = self.search_entry.text()
        if value == '':
            QMessageBox.information(self,'Warning','Search query cant be empty !!')   
        
        else :
            
            self.search_entry.setText('')
            query = ("SELECT product_id,product_name,product_manufacture,product_price,product_qouta,product_availability FROM products WHERE product_name LIKE ? or product_manufacture LIKE ?")
            results = cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall()
            
            if results == []:
                QMessageBox.information(self,'Warning','There is no such a product or manufacture')
            else:
                for i in reversed(range(self.products_table.rowCount())):
                    self.products_table.removeRow(i)
                
                for row_data in results:
                    row_num = self.products_table.rowCount()
                    self.products_table.insertRow(row_num)
                    for col_num , data in enumerate(row_data):
                        self.products_table.setItem(row_num,col_num,QTableWidgetItem(str(data)))


    def listProducts(self):
        if self.all_products.isChecked():
            self.displayProducts()
        else:
            
            if self.available.isChecked():
                products_list = cur.execute("SELECT product_id,product_name,product_manufacture,product_price,product_qouta,product_availability FROM products WHERE product_availability='Available'")
            elif self.not_available.isChecked():
                products_list = cur.execute("SELECT product_id,product_name,product_manufacture,product_price,product_qouta,product_availability FROM products WHERE product_availability='Unavailable'")
            for i in reversed(range(self.products_table.rowCount())):
                    self.products_table.removeRow(i)
                    for row_data in products_list:
                        row_num = self.products_table.rowCount()
                        self.products_table.insertRow(row_num)
                        for col_num , data in enumerate(row_data):
                            self.products_table.setItem(row_num,col_num,QTableWidgetItem(str(data)))


    def funcSellProduct(self):
        
        self.sell_product_widget = SellProduct()


    def getStatistics(self):
        
        count_products = cur.execute(" SELECT count(product_id) FROM products ").fetchall()[0][0]
        count_members = cur.execute(" SELECT count(member_id) FROM members ").fetchall()[0][0]
        sold_products = cur.execute(" SELECT SUM(selling_quantity) FROM sellings ").fetchall()[0][0]
        total_amount = cur.execute(" SELECT SUM(selling_amount) FROM sellings ").fetchall()[0][0]

        self.total_products_lable.setText(str(count_products))
        self.total_member_lable.setText(str(count_members))
        self.sold_products_lable.setText(str(sold_products))
        self.total_amount_lable.setText(str(total_amount) + ' $ ')


    def tabChanges(self):
        self.getStatistics()
        self.displayProducts()
        self.diplayMembers()


    def Quit(self):
        sys.exit()












# def main():
#     app = QApplication(sys.argv)
#     win = Main()
#     sys.exit(app.exec_())
    

# if __name__ == '__main__':
#     main()