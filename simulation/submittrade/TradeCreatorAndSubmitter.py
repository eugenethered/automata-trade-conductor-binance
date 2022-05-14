from core.number.BigFloat import BigFloat
from core.trade.InstrumentTrade import InstrumentTrade, Status
from traderepo.repository.TradeRepository import TradeRepository

from binancetrade.BinanceTradeConductor import BinanceTradeConductor


class TradeCreatorAndSubmitter:

    def __init__(self, options):
        self.trade_repository = TradeRepository(options)
        self.conductor = BinanceTradeConductor(options)

    def create_trade(self):
        trade = InstrumentTrade('USDT', 'BUSD', BigFloat('11'), Status.NEW)
        self.trade_repository.store_trade(trade)

    def submit_trade(self):
        self.conductor.conduct_trading()



