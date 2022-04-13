# Automata Binance Trade Executor

## Packaging
`python3 -m build`

## Clean the build
`rm -fr dist automata.trade.executor.binance.egg-info`

## Running

### IDE
1. Go to `Run`
2. Choose `Edit configurations...`
3. In `Paramaters:` 
   ```
   --options REDIS_SERVER_ADDRESS=192.168.1.90 REDIS_SERVER_PORT=6379 TRADE_KEY=binance:trade BINANCE_API_KEY=<API_KEY> BINANCE_API_SECRET=<API_SECRET>

   ```