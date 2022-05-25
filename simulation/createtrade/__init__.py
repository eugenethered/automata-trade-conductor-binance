from cache.holder.RedisCacheHolder import RedisCacheHolder
from core.number.BigFloat import BigFloat
from core.trade.InstrumentTrade import InstrumentTrade, Status
from traderepo.repository.TradeRepository import TradeRepository

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379,
        'TRADE_KEY': 'binance:trade'
    }

    RedisCacheHolder(options)

    trade = InstrumentTrade('USDT', 'BUSD', BigFloat('11'), status=Status.NEW)

    trade_repository = TradeRepository(options)
    trade_repository.store_trade(trade)

    print('Trade created!')
