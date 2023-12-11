from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys, os
from functools import partial
from fetch import uisetup

class cartUI(QWidget):
    food_items = [
        {'name': 'Pizza','price': 100, 'path':'./resources/images/item1'},
        {'name': 'Ice Tea','price': 20, 'path':'./resources/images/item2'},
        {'name': 'Spaghetti','price': 70, 'path':'./resources/images/item3'},
        {'name': 'MilkShake','price': 65, 'path':'./resources/images/item4'},
        {'name': 'Cheese Burger','price': 45, 'path':'./resources/images/item5'},
        {'name': 'Taco','price': 30, 'path':'./resources/images/item6'},
        {'name': 'Hotdog Sandwich','price': 32, 'path':'./resources/images/item7'},
        {'name': 'Veggie Salad','price': 25, 'path':'./resources/images/item8'},
        {'name': 'Halo Halo','price':50, 'path':'./resources/images/item9'},
        {'name': 'Tapsilog','price': 55, 'path':'./resources/images/item10'}
    ]

    receipt_items = []
    
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self):
        uisetup.setup_ui(self, 'Food Cart - Cart', 850, 650)
        #manually adjusted since i cant add background to the layout
        grid_bg = QFrame(self)
        grid_bg.setStyleSheet('background-color: white; border: 1.5px solid black')
        grid_bg.setGeometry(5,10,565,640)
        
        self.total_label = QLabel(self)
        self.total_label.setText('ORDER DETAILS')
        self.total_label.setStyleSheet('color:black; font-size:25px; font-weight:bold;')
        self.Foodlist = QLabel(self)
        self.Foodlist.setText('                                     Food List                           ')
        self.Foodlist.setStyleSheet('color:black; font-size:25px; font-weight:bold; text-decoration: underline')

        separator = QFrame(self)
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("QFrame { background-color: black; height: 2px; }")

        self.pay_but = QPushButton(self)
        self.pay_but.setText('PLACE ORDER')
        self.pay_but.setFixedSize(200,50)
        self.pay_but.clicked.connect(self.confirm)
        self.pay_but.setStyleSheet('''
        QPushButton{
            background-color: #557C55;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border: none;
            border-radius: 25px;
            margin-left: 50px;}       
        QPushButton:hover{
            background-color: green;
            color: white;
            border: 1px solid green;
        }
''')

        grid_layout = QGridLayout()
        # Add widgets(ffod in the layout)
        for i, item in enumerate(self.food_items):
            food_label = QLabel(self)
            pixmap = QPixmap(item["path"])
            resized_pixmap = pixmap.scaled(130, 130, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            food_label.setPixmap(resized_pixmap)
            food_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            food_label.setStyleSheet('border: 2px solid gray; background-color: #eaaf7b')

            food_label.setScaledContents(True)
            food_label.mousePressEvent = partial(self.showinfo, item["name"], item['price'])
            grid_layout.addWidget(food_label, i // 4, i % 4)

        content_layout = QVBoxLayout()
        receipt_layout = QVBoxLayout()

        self.order_summary_layout = QVBoxLayout()
        
        content_layout.addWidget(self.Foodlist) 
        content_layout.addLayout(grid_layout,1)
        receipt_layout.addWidget(self.total_label)
        receipt_layout.addWidget(separator)
        receipt_layout.addLayout(self.order_summary_layout)
        receipt_layout.addStretch(1)
        receipt_layout.addWidget(self.pay_but, Qt.AlignmentFlag.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        contents = QHBoxLayout()
        contents.setAlignment(Qt.AlignmentFlag.AlignCenter)
        contents.addLayout(content_layout)
        contents.addSpacing(15)
        contents.addLayout(receipt_layout)

        main_layout.addLayout(contents)
        self.setLayout(main_layout)
    
    def goback(self):
        from landingUI import landingUI
        self.switchabout = landingUI()
        self.switchabout.show()
        self.close()
    
    def showinfo(self, name,price, event):
        add_dialog = QDialog(self)
        uisetup.setup_ui(add_dialog,'Add Food Dialog',200,200)

        layout = QVBoxLayout()

        label = QLabel(f'item: <span style="font-weight: bold;">{name}</span>')
        item_price = QLabel(f'price: $<span style="font-weight: bold;">{price}</span>')
        item_price.setStyleSheet('''color: white; font-size: 15px;''')
        label.setStyleSheet('''color: white; font-size: 15px;''')
        layout.addWidget(label)
        layout.addWidget(item_price)

        label_quantity = QLabel('Enter the quantity:')
        label_quantity.setStyleSheet('''color: white; font-size: 15px;''')
        layout.addWidget(label_quantity)

        self.quantity_input = QLineEdit(self)
        layout.addWidget(self.quantity_input)
        self.value = self.quantity_input

        button = QPushButton('Add Item', self)
        button.clicked.connect(lambda: self.add_to_receipt(name, self.value.text()))
        layout.addWidget(button)

        add_dialog.setLayout(layout)
        add_dialog.exec()
    
    def add_to_receipt(self, food_name, qty):
        try:
            qty = int(qty)
            if qty > 0:
                # verify if the item is already in the receipt
                for item_set in self.receipt_items:
                    if food_name in item_set:
                        item_set[food_name]['quantity'] += qty
                        item_set[food_name]['total_price'] = item_set[food_name]['quantity'] * item_set[food_name]['price']
                        QMessageBox.information(self, 'Update Complete', f"Updated {food_name} quantity to {item_set[food_name]['quantity']} in the receipt.")
                        self.update_receipt_display()
                        return
                # If the item is not found, add a new entry
                for food_item in self.food_items:
                    if food_item['name'] == food_name:
                        item_set = {
                            'name': food_name,
                            'quantity': qty,
                            'price': food_item['price'],
                            'total_price': qty * food_item['price']
                        }
                        self.receipt_items.append({food_name: item_set})
                        QMessageBox.information(self, 'Added Complete', f"Added {qty} {food_name} to the receipt.")
                        label = QLabel(f"{qty}x {food_name} ----- ${item_set['total_price']}")
                        label.setFixedSize(250,50)
                        label.setStyleSheet('color: black; font-size: 15px; background-color: #F5CCA0; border: 2px solid black; border-radius:10px;')
                        label.mousePressEvent = lambda event, food_name=food_name: self.delete_item_dialog(food_name, event)
                        self.order_summary_layout.addWidget(label)
                        break

            else:
                QMessageBox.warning(self, 'Sign Error', "Quantity should be a positive integer.")
        except ValueError:
            QMessageBox.warning(self, 'Invalid Number', "Invalid quantity. Please enter a valid number.")

    def confirm(self):
        self.printall = Receipt_print()
        self.printall.exec()

    def update_receipt_display(self):
        for i in reversed(range(self.order_summary_layout.count())):
            self.order_summary_layout.itemAt(i).widget().setParent(None)

        for item_set in reversed(self.receipt_items):
            for food_name, item in item_set.items():
                label = QLabel(f"{item['quantity']}x {food_name} ----- ${item['total_price']}")
                label.setFixedSize(250, 50)
                label.setStyleSheet('color: black; font-size: 15px; background-color: #F5CCA0; border: 2px solid black; border-radius: 10px')

                self.order_summary_layout.addWidget(label, Qt.AlignmentFlag.AlignTop)
                label.mousePressEvent = lambda event, food_name=food_name: self.delete_item_dialog(food_name, event)

    def delete_item_dialog(self, food_name, event):
        reply = QMessageBox.question(
            self, 'Confirm Deletion',
            f"Do you want to delete {food_name} from the receipt?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            # Delete the item from the receipt_items list
            self.receipt_items = [item_set for item_set in self.receipt_items if food_name not in item_set]

            # Update the display
            self.update_receipt_display()

class Receipt_print(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.toprint = cartUI.receipt_items
        self.initUI()
    
    def initUI(self):
        uisetup.setup_ui(self,'Confirm',350,520)

        # #i remove it temporarily to check what design suits the system
        receipt_bg = QFrame(self)
        receipt_bg.setStyleSheet('background-color: white; border: 1.5px solid black')
        receipt_bg.setGeometry(10,10,328,450)

        linehorizontal = QFrame(self)
        linehorizontal.setFrameShape(QFrame.Shape.HLine)
        linehorizontal.setFrameShadow(QFrame.Shadow.Sunken)
        linehorizontal.setStyleSheet('height: 2px; color: black')

        linehorizontal1 = QFrame(self)
        linehorizontal1.setFrameShape(QFrame.Shape.HLine)
        linehorizontal1.setFrameShadow(QFrame.Shadow.Sunken)
        linehorizontal1.setStyleSheet('height: 2.5px; color: black')

        self.pay = QPushButton(self)
        self.pay.setText('PAY')
        self.pay.setFixedSize(100,50)
        self.pay.setStyleSheet('''
            QPushButton{
                background-color: #557C55;
                color: white;
                font-size: 15px;
                font-weight: bold;
                border: none;
                border-radius: 10px}
                                   
            QPushButton:hover{
                background-color: green;
                color: white;
                border: 1px solid green;
            }
    
''')

        self.total = QLabel(self)
        self.totalval = str(sum(values['total_price'] for items in self.toprint for values in items.values()))
        self.total.setText(f'TOTAL: ${self.totalval}')
        self.total.setStyleSheet('''
            color: black;
            font-weight: bold;
            font-family: Poppins, Helvetica, sans-serif;
            font-size: 15px;
''')

        self.receipttitle = QLabel(self)
        self.receipttitle.setText('''
Thanks for your order!
                                  
Items: 
''')
        self.receipttitle.setStyleSheet('''
            color: black;
            font-weight: bold;
            font-family: Poppins, Helvetica, sans-serif;
            font-size: 15px;
''')

        purchase_items = QVBoxLayout()

        for items in self.toprint:
            for item_val in items.values():
                item = QLabel(self)
                item.setText(f"{item_val['name']}: {item_val['quantity']}x --- ${item_val['total_price']}")
                item.setStyleSheet('margin-left: 5px;color: black; font-size: 15px')
                purchase_items.addWidget(item)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.receipttitle)
        main_layout.addWidget(linehorizontal1)
        main_layout.addLayout(purchase_items)
        main_layout.addStretch(1)
        main_layout.addWidget(linehorizontal)
        main_layout.addWidget(self.total)
        main_layout.addWidget(self.pay, Qt.AlignmentFlag.AlignBottom)
        
        self.pay.clicked.connect(self.clicks)
        self.setLayout(main_layout)

    def clicks(self):
        try:
            base_path = os.getcwd() 
            temp_dir = os.path.join(base_path, 'temp')
            os.makedirs(temp_dir, exist_ok=True)
            file_path = os.path.join(temp_dir, 'Receipt.txt')
            with open(file_path, 'w') as receipt:
                receipt.write('''
Thanks for your order!
                                  
Items: 
''')
                for items in self.toprint:
                    for item_val in items.values():
                        item = f"{item_val['name']}: {item_val['quantity']}x --- ${item_val['total_price']}"
                        receipt.write(f'{item}\n')
                total = str(sum(values['total_price'] for items in self.toprint for values in items.values()))
                receipt.write(F'\n\nTOTAL: ${total}')
            
                    
            QMessageBox.information(self, 'Confirmation', 'Receipt Generated')
        except Exception as e:
            print(e)
            QMessageBox.information(self,'Error Payment', 'Payment Failed')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = cartUI()
    main_window.show()
    sys.exit(app.exec())

#      create an txt file 