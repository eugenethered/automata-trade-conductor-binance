from simulation.transform.TradeTransformStoreHandler import TradeTransformStoreHandler

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379
    }

    TRADE_TRANSFORMATIONS_KEY = 'binance:trade:transformations'

    transform_handler = TradeTransformStoreHandler(options)
    transform_handler.store_transformations(TRADE_TRANSFORMATIONS_KEY)
