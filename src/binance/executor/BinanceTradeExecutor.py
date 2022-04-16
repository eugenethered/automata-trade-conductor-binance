from binance.spot import Spot
from core.trade.InstrumentTrade import InstrumentTrade
from trade.executor.TradeExecutor import TradeExecutor

from src.binance.executor.handler.TradeSubmissionHandler import TradeSubmissionHandler
from src.binance.executor.transformer.BinanceTradeTransformer import BinanceTradeTransformer


class BinanceTradeExecutor(TradeExecutor):

    def __init__(self, options, trade_transformer: BinanceTradeTransformer):
        self.options = options
        self.trade_transformer = trade_transformer
        self.spot_client = Spot(self.options['BINANCE_API_KEY'], self.options['BINANCE_API_SECRET'])
        # todo: need to obtain updates for order (Market | Limit)

    def trade(self, trade: InstrumentTrade) -> InstrumentTrade:
        trade_submission_handler = TradeSubmissionHandler(trade)
        trade_submission_handler.submit_trade(self.submit_market_order)
        return trade

    def submit_market_order(self, trade: InstrumentTrade):
        trade_parameters = self.trade_transformer.transform(trade)
        return self.spot_client.new_order(
            symbol=trade_parameters['SYMBOL'],
            side=trade_parameters['SIDE'],
            type=trade_parameters['ORDER_TYPE'],
            quantity=trade_parameters['QUANTITY'],
            timeInForce=trade_parameters['ORDER_CANCELLATION_OPTION']
        )
