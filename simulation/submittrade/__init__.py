from cache.holder.RedisCacheHolder import RedisCacheHolder
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder

from simulation.submittrade.TradeCreatorAndSubmitter import TradeCreatorAndSubmitter

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'TRADE_TRANSFORMATIONS_KEY': 'binance:trade:transformations',
        'TRADE_KEY': 'test:trade',
        'MISSING_KEY': 'binance:missing'
    }

    RedisCacheHolder(options)

    ConfigReporterHolder(options)

    creator_submitter = TradeCreatorAndSubmitter(options)
    creator_submitter.create_trade()
    creator_submitter.submit_trade()

