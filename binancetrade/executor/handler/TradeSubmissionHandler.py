import logging

from binance.error import ClientError
from core.trade.InstrumentTrade import InstrumentTrade, Status
from utility.json_utility import as_data

from binancetrade.executor.transformer.error.TradeTransformException import TradeTransformException


class TradeSubmissionHandler:

    def __init__(self, trade: InstrumentTrade):
        self.trade = trade

    def submit_trade(self, func):
        try:
            response = func(self.trade)
            # todo: unpack response -> standarized method
            self.update_submitted_trade(response)
        except TradeTransformException as error:
            # todo: all errors updated -> standarized method
            self.update_trade_with_error(error.error_message, 10000)
        except ClientError as error:
            # todo: all errors updated -> standarized method
            self.update_trade_with_error(error.error_message, error.error_code)
            logging.warning(f'Could not submit trade -> {self.trade}')

    def update_submitted_trade(self, trade_submission_response):
        order_id = as_data(trade_submission_response, 'orderId')
        self.trade.status = Status.SUBMITTED
        self.trade.order_id = str(order_id)

    def update_trade_with_error(self, error_message, error_code):
        self.trade.status = Status.ERROR
        self.trade.description = self.add_category_to_description(error_message, error_code)

    @staticmethod
    def add_category_to_description(error_message, error_code):
        categorized_description_error = '{}' + f' - {error_message} [{error_code}]'
        if error_code == -1013:
            categorized_description_error = categorized_description_error.format('Not Enough Funds')
        if error_code == -1022 or error_code == -2014:
            categorized_description_error = categorized_description_error.format('API Keys Not Valid')
        if error_code == -1106 or error_code == -1117:
            categorized_description_error = categorized_description_error.format('Order Parameter Issue')
        if error_code == -1121:
            categorized_description_error = categorized_description_error.format('Instrument Invalid')
        if error_code == 10000:
            categorized_description_error = categorized_description_error.format('Trade Transform Rule')
        else:
            categorized_description_error = categorized_description_error.format('Other')
        return categorized_description_error
