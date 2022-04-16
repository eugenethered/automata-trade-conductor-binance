from binance.spot import Spot
from core.trade.InstrumentTrade import InstrumentTrade
from trade.executor.TradeExecutor import TradeExecutor

from src.binance.executor.handler.TradeSubmissionHandler import TradeSubmissionHandler


class BinanceTradeExecutor(TradeExecutor):

    def __init__(self, options):
        self.options = options
        self.spot_client = Spot(self.options['BINANCE_API_KEY'], self.options['BINANCE_API_SECRET'])
        # todo: need to obtain updates for order (Market | Limit)

    def trade(self, trade: InstrumentTrade) -> InstrumentTrade:
        trade_submission_handler = TradeSubmissionHandler(trade)
        trade_submission_handler.submit_trade(self.submit_market_order)
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
