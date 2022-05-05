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
            return {'orderId': '8888-8888'}

        trade_submission_handler.submit_trade(trade_submit_function)
        self.assertEqual(trade.status, Status.SUBMITTED)
        self.assertEqual(trade.description, None)
        self.assertEqual(trade.order_id, '8888-8888')

    def test_should_raise_exception_when_account_has_insufficient_amount_to_trade(self):
        trade = InstrumentTrade('USDT', 'BTC', 100)
        self.assertEqual(trade.status, Status.NEW)
        self.assertEqual(trade.description, None)

        trade_submission_handler = TradeSubmissionHandler(trade)

        def trade_submit_function(trade):
            raise ClientError(error_code=-1013, error_message='Account has insufficient balance for requested action.', status_code=None, header=None)

        trade_submission_handler.submit_trade(trade_submit_function)
        self.assertEqual(trade.status, Status.ERROR)
        self.assertEqual(trade.description, 'Not Enough Funds - Account has insufficient balance for requested action. [-1013]')


if __name__ == '__main__':
    unittest.main()
