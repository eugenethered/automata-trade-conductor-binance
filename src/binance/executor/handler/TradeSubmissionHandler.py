from binance.error import ClientError
from core.trade.InstrumentTrade import InstrumentTrade, Status


class TradeSubmissionHandler:

    def __init__(self, trade: InstrumentTrade):
        self.trade = trade

    def submit_trade(self, func):
        try:
            response = func(self.trade)
            print(f'Trade got the following response! -> {response}')
            self.update_trade_as_submitted()
        except ClientError as error:
            self.update_trade_with_error(error.error_message)

    def update_trade_as_submitted(self):
        self.trade.status = Status.SUBMITTED

    def update_trade_with_error(self, error_message):
        self.trade.status = Status.ERROR
        self.trade.description = error_message
