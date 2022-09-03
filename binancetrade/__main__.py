import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.environment.EnvironmentVariables import EnvironmentVariables
from logger.ConfigureLogger import ConfigureLogger

from binancetrade.BinanceTradeConductor import BinanceTradeConductor


def start():
    ConfigureLogger()

    environment_variables = EnvironmentVariables()

    log = logging.getLogger('Binance Position Conductor')
    log.info('position conductor initialized')

    RedisCacheHolder(environment_variables.options, held_type=RedisCacheProviderWithHash)

    ConfigReporterHolder(environment_variables.options)

    conductor = BinanceTradeConductor(environment_variables.options)
    conductor.start_process_schedule()


if __name__ == '__main__':
    start()
