import logging

from binance.spot import Spot
from core.trade.InstrumentTrade import InstrumentTrade
from coreauth.AuthenticatedCredentials import AuthenticatedCredentials
from trade.executor.TradeExecutor import TradeExecutor

from binancetrade.executor.handler.TradeSubmissionHandler import TradeSubmissionHandler
from binancetrade.executor.transformer.BinanceTradeTransformer import BinanceTradeTransformer


class BinanceTradeExecutor(TradeExecutor):

    def __init__(self, options, trade_transformer: BinanceTradeTransformer):
        self.log = logging.getLogger(__name__)
        self.options = options
        self.trade_transformer = trade_transformer
        (self.api_key, self.api_secret) = self.init_auth_credentials()
        self.spot_client = None

    def init_auth_credentials(self):
        authenticated_credentials = AuthenticatedCredentials(self.options)
        api_key = authenticated_credentials.obtain_auth_value('API_KEY')
        api_secret = authenticated_credentials.obtain_auth_value('API_SECRET')
        return api_key, api_secret

    def lazy_init_spot_client(self):
        if self.spot_client is None:
            self.spot_client = Spot(self.api_key, self.api_secret)

    def trade(self, trade: InstrumentTrade) -> InstrumentTrade:
        self.lazy_init_spot_client()
        trade_submission_handler = TradeSubmissionHandler(trade)
        trade_submission_handler.submit_trade(self.submit_market_order)
        return trade

    def submit_market_order(self, trade: InstrumentTrade):
        trade_parameters = self.trade_transformer.transform(trade)
        return self.spot_client.new_order(
            symbol=trade_parameters['SYMBOL'],
            side=trade_parameters['SIDE'],
            type=trade_parameters['ORDER_TYPE'],
            quantity=trade_parameters['QUANTITY']
        )
