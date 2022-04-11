from trade.TradeConductor import TradeConductor


class BinanceTradeConductor:

    def __init__(self, url, options):
        self.url = url
        self.options = options
        self.trade_conductor = TradeConductor(self.options)

    def conduct_trading(self):
        trade = self.trade_conductor.fetch_trade_to_execute()
        print(f'trade: {trade}')
        # todo: take the next actions
