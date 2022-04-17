import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from core.trade.InstrumentTrade import InstrumentTrade
from utility.json_utility import as_data

from binance.executor.transformer.error.TradeTransformException import TradeTransformException


class BinanceTradeTransformer:

    def __init__(self, options):
        self.transform_rules = self.load_transform_rules(options)

    def load_transform_rules(self, options):
        cache = RedisCacheHolder()
        transform_rules = cache.fetch(options['TRADE_TRANSFORM_RULES_KEY'], as_type=dict)
        return dict(self.unpack_transform_rules(transform_rules))

    @staticmethod
    def unpack_transform_rules(transform_rules):
        for transform_rule in transform_rules:
            yield as_data(transform_rule, 'trade'), as_data(transform_rule, 'transform')

    def transform(self, trade: InstrumentTrade):
        trade_key = self.obtain_trade_key(trade)
        if trade_key in self.transform_rules:
            transform_rule = self.transform_rules[trade_key]
            trade_parameters = {
                'SYMBOL': as_data(transform_rule, 'instrument'),
                'SIDE': as_data(transform_rule, 'side'),
                'ORDER_TYPE': as_data(transform_rule, 'orderType'),
                'QUANTITY': trade.quantity
            }
            return trade_parameters
        else:
            logging.warning(f'No Trade Transformation Rule for trade:{trade_key}')
            raise TradeTransformException(f'{trade_key} does not have a trade transform rule')

    @staticmethod
    def obtain_trade_key(trade: InstrumentTrade):
        return f'{trade.instrument_from}/{trade.instrument_to}'
