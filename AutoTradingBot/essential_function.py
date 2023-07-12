from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, GetAssetsRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key')  # Replace 'api-key' and 'secret-key' with your actual keys


def view_account_info():
    # Get our account information
    account = trading_client.get_account()

    # Prepare account information string
    account_info = f"Account is currently {'restricted' if account.trading_blocked else 'not restricted'} from trading.\n"
    account_info += f'${account.buying_power} is available as buying power.'
    return account_info


def view_portfolio():
    # Get our account information
    account = trading_client.get_account()

    # Check our current balance vs. our balance at the last market close
    balance_change = float(account.equity) - float(account.last_equity)
    portfolio_gain_loss = f'Today\'s portfolio balance change: ${balance_change}'
    return portfolio_gain_loss


def place_orders(symbol, quantity, order_type):
    # Create market order data
    side = OrderSide.BUY if order_type == 'Buy' else OrderSide.SELL
    market_order_data = MarketOrderRequest(
        symbol=symbol,
        qty=quantity,
        side=side,
        time_in_force=TimeInForce.GTC
    )

    # Submit the order
    market_order = trading_client.submit_order(market_order_data)

    # Prepare order details string
    order_details = 'Order Details:\n'
    for property_name, value in market_order.items():
        order_details += f'"{property_name}": {value}\n'
    return order_details
