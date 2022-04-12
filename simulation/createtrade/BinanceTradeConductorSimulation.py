from cache.holder.RedisCacheHolder import RedisCacheHolder
from core.trade.CurrencyTradeOrder import CurrencyTradeOrder
from trade.TradeConductor import TradeConductor


class BinanceTradeConductorSimulation:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options)
        self.trade_conductor = TradeConductor(options)

    def store_trade_for_execution(self):
        trade = CurrencyTradeOrder('USDT', 'BTC', 10, 'BUY')
        self.trade_conductor.store_trade_to_execute(trade)
        print(f'Trade stored for execution')
