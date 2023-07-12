from alpaca.trading.client import TradingClient
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QTextEdit, QDialog, QLineEdit, \
    QComboBox, QDialogButtonBox
from essential_function import view_account_info, view_portfolio, place_orders


class OrderDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.symbol_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.type_select = QComboBox()

        # Add items to type_select dropdown
        self.type_select.addItems(['Buy', 'Sell'])

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Symbol'))
        layout.addWidget(self.symbol_input)
        layout.addWidget(QLabel('Quantity'))
        layout.addWidget(self.quantity_input)
        layout.addWidget(QLabel('Type'))
        layout.addWidget(self.type_select)
        layout.addWidget(QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel))

        # Set dialog layout
        self.setLayout(layout)


class TradingBotApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.account_info_button = QPushButton('View Account Information')
        self.portfolio_button = QPushButton('View Gain/Loss of Portfolio')
        self.order_button = QPushButton('Place Orders')
        self.log_area = QTextEdit()

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.account_info_button)
        layout.addWidget(self.portfolio_button)
        layout.addWidget(self.order_button)
        layout.addWidget(QLabel('Logs'))
        layout.addWidget(self.log_area)

        # Set layout
        self.setLayout(layout)

        # Connect signals
        self.account_info_button.clicked.connect(self.display_account_info)
        self.portfolio_button.clicked.connect(self.display_portfolio)
        self.order_button.clicked.connect(self.place_order)

    def display_account_info(self):
        account_info = view_account_info()
        self.log_area.append(account_info)

    def display_portfolio(self):
        portfolio_gain_loss = view_portfolio()
        self.log_area.append(portfolio_gain_loss)

    def place_order(self):
        dialog = OrderDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            symbol = dialog.symbol_input.text()
            quantity = dialog.quantity_input.text()
            order_type = dialog.type_select.currentText()
            order_details = place_orders(symbol, quantity, order_type)
            self.log_area.append(order_details)


app = QApplication([])
window = TradingBotApp()
window.show()
app.exec()
