from cache.holder.RedisCacheHolder import RedisCacheHolder
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder

from simulation.submittrade.TradeCreatorAndSubmitter import TradeCreatorAndSubmitter

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '10.104.71.60',
        'REDIS_SERVER_PORT': 6379,
        'TRADE_TRANSFORMATIONS_KEY': 'binance:transformation:trade',
        'TRADE_KEY': 'test:trade',
        'MISSING_KEY': 'binance:missing',
        'AUTH_INFO_KEY': 'binance:auth:info',
        'PROCESS_KEY': 'binance:process:mv:status',
        'PROCESS_RUN_PROFILE_KEY': 'binance:process:mv:run-profile'
    }

    RedisCacheHolder(options)

    ConfigReporterHolder(options)

    creator_submitter = TradeCreatorAndSubmitter(options)
    creator_submitter.create_trade()
    creator_submitter.submit_trade()

