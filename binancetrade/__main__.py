import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder
from config.report.holder.ConfigReporterHolder import ConfigReporterHolder
from core.arguments.command_line_arguments import option_arg_parser

from binancetrade.BinanceTradeConductor import BinanceTradeConductor

if __name__ == '__main__':
    command_line_arg_parser = option_arg_parser()
    args = command_line_arg_parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logging.info(f'Binance Trade Executor starting with OPTIONS {args.options}')

    RedisCacheHolder(args.options)

    ConfigReporterHolder(args.options)

    trade_executor = BinanceTradeConductor(args.options)
    trade_executor.conduct_trading()
