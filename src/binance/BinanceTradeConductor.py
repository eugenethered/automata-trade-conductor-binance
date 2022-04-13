from trade.TradeConductor import TradeConductor

from src.binance.executor.BinanceTradeExecutor import BinanceTradeExecutor


class BinanceTradeConductor:

    def __init__(self, options):
        self.options = options
        trade_executor = BinanceTradeExecutor(self.options)
        self.trade_conductor = TradeConductor(self.options, trade_executor)

    def conduct_trading(self):
        self.trade_conductor.perform_trade()
