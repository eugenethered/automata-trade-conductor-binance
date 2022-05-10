from trade.TradeConductor import TradeConductor
from traderepo.repository.TradeRepository import TradeRepository
from tradetransformrepo.repository.TradeTransformRepository import TradeTransformRepository

from binancetrade.executor.BinanceTradeExecutor import BinanceTradeExecutor
from binancetrade.executor.transformer.BinanceTradeTransformer import BinanceTradeTransformer


class BinanceTradeConductor:

    def __init__(self, options):
        self.options = options
        repository = TradeTransformRepository(self.options)
        trade_transformer = BinanceTradeTransformer(repository)
        trade_repository = TradeRepository(self.options)
        trade_executor = BinanceTradeExecutor(self.options, trade_transformer)
        self.trade_conductor = TradeConductor(self.options, trade_repository, trade_executor)

    def conduct_trading(self):
        # todo: need simple schedular
        self.trade_conductor.perform_trade()
