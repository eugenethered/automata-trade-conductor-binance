import logging

from cache.holder.RedisCacheHolder import RedisCacheHolder

from binance.BinanceTradeConductor import BinanceTradeConductor
from binance.arguments.command_line_arguments import init_arg_parser

if __name__ == '__main__':
    command_line_arg_parser = init_arg_parser()
    args = command_line_arg_parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    logging.info(f'Binance Trade Executor starting with OPTIONS {args.options}')

    RedisCacheHolder(args.options)

    trade_executor = BinanceTradeConductor(args.options)
    trade_executor.conduct_trading()
