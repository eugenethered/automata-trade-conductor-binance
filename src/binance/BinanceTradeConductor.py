from trade.TradeConductor import TradeConductor

from src.binance.executor.BinanceTradeExecutor import BinanceTradeExecutor
from src.binance.executor.transformer.BinanceTradeTransformer import BinanceTradeTransformer


class BinanceTradeConductor:

    def __init__(self, options):
        self.options = options
        trade_transformer = BinanceTradeTransformer(self.options)
        trade_executor = BinanceTradeExecutor(self.options, trade_transformer)
        self.trade_conductor = TradeConductor(self.options, trade_executor)

    def conduct_trading(self):
        self.trade_conductor.perform_trade()
