from cache.holder.RedisCacheHolder import RedisCacheHolder


class TradeCraftHandler:

    def __init__(self, options):
        self.cache = RedisCacheHolder(options)

    @staticmethod
    def obtain_trade():
        return {
            'currency_from': 'USDT',
            'currency_to': 'BTC',
            'quantity': 10,
            'price': 40000,
            'side': 'BUY'
        }

    def store_trade_for_execution(self, key):
        trade = self.obtain_trade()
        self.cache.store(key, trade)
        print(f'Stored trade for execution')
