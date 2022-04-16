from cache.holder.RedisCacheHolder import RedisCacheHolder


class TransformRuleStoreHandler:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options)

    @staticmethod
    def obtain_transformation_rules():
        return [
            {
                'trade': 'BTC/USDT',
                'transform': {
                    'instrument': 'BNBUSDT',
                    'side': 'SELL',
                    'orderType': 'MARKET'
                }
            },
            {
                'trade': 'USDT/BTC',
                'transform': {
                    'instrument': 'BNBUSDT',
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

    def store_transformation_rules(self, key):
        transformation_rules = self.obtain_transformation_rules()
        self.cache.store(key, transformation_rules)
        print(f'Stored [{len(transformation_rules)}] transformation rules')
