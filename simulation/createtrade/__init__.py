from simulation.createtrade.BinanceTradeConductorSimulation import BinanceTradeConductorSimulation

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'TRADE_KEY': 'binance:trade'
    }

    simulation = BinanceTradeConductorSimulation(options)
    simulation.store_trade_for_execution()
