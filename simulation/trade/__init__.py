from simulation.trade.TradeCraftHandler import TradeCraftHandler

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379
    }

    TRADE_KEY = 'binance:trade'

    trade_handler = TradeCraftHandler(options)
    trade_handler.store_trade_for_execution(TRADE_KEY)
