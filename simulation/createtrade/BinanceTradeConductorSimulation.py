from cache.holder.RedisCacheHolder import RedisCacheHolder
from core.number.BigFloat import BigFloat
from core.trade.InstrumentTrade import InstrumentTrade
from trade.TradeConductor import TradeConductor

from src.binance.executor.BinanceTradeExecutor import BinanceTradeExecutor


class BinanceTradeConductorSimulation:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options)
        # trade executor - not required for this simulation
        trade_executor: BinanceTradeExecutor = None
        self.trade_conductor = TradeConductor(options, trade_executor)

    def store_trade_for_execution(self):
        trade = InstrumentTrade('USDT', 'BTC', BigFloat('0.000025'))
        self.trade_conductor.store_trade_to_execute(trade)
        print(f'Trade stored for execution')
