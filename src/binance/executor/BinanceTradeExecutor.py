from binance.spot import Spot
from core.trade.InstrumentTrade import InstrumentTrade
from trade.executor.TradeExecutor import TradeExecutor


class BinanceTradeExecutor(TradeExecutor):

    def __init__(self, options):
        self.options = options
        self.spot_client = Spot(self.options['BINANCE_API_KEY'], self.options['BINANCE_API_SECRET'])
        # todo: need to obtain updates for orders (Market | Limit)

    def trade(self, trade: InstrumentTrade) -> InstrumentTrade:
        # todo: handle errors (not enough funds)
        # todo: handle wrong arguments (e.g. GTC not needed)
        # todo: handle wrong instrument
        # todo: handle API key fails
        # todo: wrong market
        # todo: ERROR format -> binance.error.ClientError: (400, -2010, 'Account has insufficient balance for requested action.')
        response = self.submit_market_order(trade)
        print(f'response -> {response}')
        return trade

    def submit_market_order(self, trade: InstrumentTrade):
        symbol = self.convert_to_symbol(trade)
        side = 'BUY' # todo: need rules for obtaining side
        order_type = 'MARKET'
        order_cancellation_option = 'GTC' # todo: need rules for cancellation option
        quantity = self.convert_to_quantity(trade)
        return self.spot_client.new_order(symbol=symbol, side=side, type=order_type, quantity=quantity, timeInForce=order_cancellation_option)

    @staticmethod
    def convert_to_symbol(trade: InstrumentTrade):
        return f'{trade.instrument_from}{trade.instrument_to}'

    @staticmethod
    def convert_to_quantity(trade: InstrumentTrade):
        return trade.quantity
