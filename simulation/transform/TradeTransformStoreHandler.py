from cache.holder.RedisCacheHolder import RedisCacheHolder


class TradeTransformStoreHandler:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options)

    @staticmethod
    def obtain_transformations():
        return [
            {
                'trade': 'BTC/USDT',
                'transform': {
                    'instrument': 'BTCUSDT',
                    'side': 'SELL',
                    'orderType': 'MARKET'
                }
            },
            {
                'trade': 'USDT/BTC',
                'transform': {
                    'instrument': 'BTCUSDT',
                    'side': 'BUY',
                    'orderType': 'MARKET'
                }
            },
            {
                'trade': 'BUSD/USDT',
                'transform': {
                    'instrument': 'BUSDUSDT',
                    'side': 'SELL',
                    'orderType': 'MARKET'
                }
            },
            {
                'trade': 'USDT/BUSD',
                'transform': {
                    'instrument': 'BUSDUSDT',
                    'side': 'BUY',
                    'orderType': 'MARKET'
                }
            },
        ]

    def store_transformations(self, key):
        transformations = self.obtain_transformations()
        self.cache.store(key, transformations)
        print(f'Stored [{len(transformations)}] transformations')
