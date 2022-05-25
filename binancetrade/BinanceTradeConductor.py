from processmanager.ScheduledProcess import ScheduledProcess
from trade.TradeConductor import TradeConductor
from traderepo.repository.TradeRepository import TradeRepository
from tradetransformrepo.repository.TradeTransformRepository import TradeTransformRepository

from binancetrade.executor.BinanceTradeExecutor import BinanceTradeExecutor
from binancetrade.executor.transformer.BinanceTradeTransformer import BinanceTradeTransformer


class BinanceTradeConductor(ScheduledProcess):

    def __init__(self, options):
        super().__init__(options, 'binance', 'trade-conductor')
        self.options = options
        repository = TradeTransformRepository(self.options)
        trade_transformer = BinanceTradeTransformer(repository)
        trade_repository = TradeRepository(self.options)
        trade_executor = BinanceTradeExecutor(self.options, trade_transformer)
        self.trade_conductor = TradeConductor(self.options, trade_repository, trade_executor)

    def process_to_run(self):
        self.trade_conductor.perform_trade()
