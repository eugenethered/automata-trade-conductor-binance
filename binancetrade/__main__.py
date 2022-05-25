import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.arguments.command_line_arguments import option_arg_parser
from logger.ConfigureLogger import ConfigureLogger

from binancetrade.BinanceTradeConductor import BinanceTradeConductor


def start():
    ConfigureLogger()

    command_line_arg_parser = option_arg_parser('persuader-technology-automata-trade-conductor-binance')
    args = command_line_arg_parser.parse_args()

    log = logging.getLogger('Binance Position Conductor')
    log.info('position conductor initialized')

    RedisCacheHolder(args.options)

    ConfigReporterHolder(args.options)

    conductor = BinanceTradeConductor(args.options)
    conductor.start_process_schedule()


if __name__ == '__main__':
    start()
