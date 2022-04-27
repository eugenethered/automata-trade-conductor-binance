import unittest

from binance.error import ClientError
from core.trade.InstrumentTrade import InstrumentTrade, Status

from binancetrade.executor.handler.TradeSubmissionHandler import TradeSubmissionHandler


class TradeSubmissionHandlerTestCase(unittest.TestCase):

    def test_should_update_trade_as_submitted(self):
        trade = InstrumentTrade('USDT', 'BTC', 100)
        self.assertEqual(trade.status, Status.NEW)
        self.assertEqual(trade.description, None)

        trade_submission_handler = TradeSubmissionHandler(trade)

        def trade_submit_function(trade):
            pass

        trade_submission_handler.submit_trade(trade_submit_function)
        self.assertEqual(trade.status, Status.SUBMITTED)
        self.assertEqual(trade.description, None)

    def test_should_raise_exception_when_account_has_insufficient_amount_to_trade(self):
        trade = InstrumentTrade('USDT', 'BTC', 100)
        self.assertEqual(trade.status, Status.NEW)
        self.assertEqual(trade.description, None)

        trade_submission_handler = TradeSubmissionHandler(trade)

        def trade_submit_function(trade):
            raise ClientError(error_code=-2010, error_message='Account has insufficient balance for requested action.', status_code=None, header=None)

        trade_submission_handler.submit_trade(trade_submit_function)
        self.assertEqual(trade.status, Status.ERROR)
        self.assertEqual(trade.description, 'Account has insufficient balance for requested action.')


if __name__ == '__main__':
    unittest.main()
