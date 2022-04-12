from src.binance.BinanceTradeConductor import BinanceTradeConductor


class BinanceTradeConductorSimulation:

    def __init__(self, url, options):
        self.binance_trade_conductor = BinanceTradeConductor(url, options)

    def execute_trade(self):
        self.binance_trade_conductor.conduct_trading()
