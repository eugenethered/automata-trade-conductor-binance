from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash
from tradetransformrepo.TradeTransform import TradeTransform
from tradetransformrepo.repository.TradeTransformRepository import TradeTransformRepository


class TradeTransformStoreHandler:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options, held_type=RedisCacheProviderWithHash)
        self.repository = TradeTransformRepository(options)

    @staticmethod
    def obtain_transformations():
        return [
            TradeTransform(trade='BTC/USDT',
                           transform={
                            'instrument': 'BTCUSDT',
                            'side': 'SELL',
                            'orderType': 'MARKET'
                            }),
            TradeTransform(trade='USDT/BTC',
                           transform={
                            'instrument': 'BTCUSDT',
                            'side': 'BUY',
                            'orderType': 'MARKET'
                            }),

            TradeTransform(trade='BUSD/USDT',
                           transform={
                               'instrument': 'BUSDUSDT',
                               'side': 'SELL',
                               'orderType': 'MARKET'
                           }),
            TradeTransform(trade='USDT/BUSD',
                           transform={
                               'instrument': 'BUSDUSDT',
                               'side': 'BUY',
                               'orderType': 'MARKET'
                           })
        ]

    def store_transformations(self):
        transformations = self.obtain_transformations()
        self.repository.store_all(transformations)
        print(f'Stored [{len(transformations)}] transformations')
