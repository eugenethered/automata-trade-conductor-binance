import argparse

from core.arguments.ParseDictionaryArgs import ParseDictionaryArgs


def init_arg_parser() -> argparse.ArgumentParser:

    command_line_argument_parser = argparse.ArgumentParser(
        usage='%(prog)s [OPTIONS] URL',
        description='Binance Automata Trade Executor'
    )

    command_line_argument_parser.add_argument(
        '-v', '--version', action='version',
        # todo: VERSION must be DRY (having this here + setup.cfg breaks DRY!)
        version=f"{command_line_argument_parser.prog} version 0.0.1"
    )

    command_line_argument_parser.add_argument('--options', nargs='*', required=False, help='Specific options for Binance trade executor.', action=ParseDictionaryArgs)

    command_line_argument_parser.add_argument('url', help='Binance trade executor URL.')

    return command_line_argument_parser
