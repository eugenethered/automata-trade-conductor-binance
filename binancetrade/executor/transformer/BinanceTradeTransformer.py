import logging
from typing import List

from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.missing.Context import Context
from core.trade.InstrumentTrade import InstrumentTrade
from coreutility.collection.dictionary_utility import as_data
from missingrepo.Missing import Missing
from tradetransformrepo.TradeTransform import TradeTransform
from tradetransformrepo.repository.TradeTransformRepository import TradeTransformRepository

from binancetrade.executor.transformer.error.TradeTransformException import TradeTransformException


class BinanceTradeTransformer:

    def __init__(self, repository: TradeTransformRepository):
        self.log = logging.getLogger('BinanceTradeTransformer')
        self.repository = repository
        self.config_reporter = ConfigReporterHolder()
        self.transform_rules = self.load_transform_rules()

    def load_transform_rules(self):
        trade_transformations = self.repository.retrieve()
        return dict(self.unpack_transform_rules(trade_transformations))

    @staticmethod
    def unpack_transform_rules(trade_transformations: List[TradeTransform]):
        for trade_transform in trade_transformations:
            yield trade_transform.trade, trade_transform.transform

    def transform(self, trade: InstrumentTrade):
        trade_key = self.obtain_trade_key(trade)
        if trade_key in self.transform_rules:
            trade_transform = self.transform_rules[trade_key]
            (instrument, side, order_type) = self.extract_transform_constituents(trade_transform)
            trade_parameters = {
                'SYMBOL': instrument,
                'SIDE': side,
                'ORDER_TYPE': order_type,
                'QUANTITY': trade.quantity
            }
            return trade_parameters
        else:
            self.log.warning(f'{trade_key} does not have a trade transformation')
            missing = Missing(trade_key, Context.TRADE, 'binance', f'Catastrophic cannot trade {trade_key}')
            self.config_reporter.report_missing(missing)
            raise TradeTransformException(f'{trade_key} does not have a trade transformation')

    @staticmethod
    def obtain_trade_key(trade: InstrumentTrade):
        return f'{trade.instrument_from}/{trade.instrument_to}'

    @staticmethod
    def extract_transform_constituents(transform):
        return as_data(transform, 'instrument'), as_data(transform, 'side'), as_data(transform, 'orderType')

