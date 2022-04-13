from cache.holder.RedisCacheHolder import RedisCacheHolder

from simulation.executetrade.BinanceTradeConductorSimulation import BinanceTradeConductorSimulation

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'TRADE_KEY': 'binance:trade',
        'BINANCE_API_KEY': '<API_KEY>',
        'BINANCE_API_SECRET': '<API_SECRET>'
    }

    RedisCacheHolder(options)

    simulation = BinanceTradeConductorSimulation(options)
    simulation.execute_trade()

