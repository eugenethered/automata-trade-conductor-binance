# Automata Binance Trade Executor

## Packaging
`python3 -m build`

## Dependencies (IDE Terminal)
`pip install persuader-technology-automata-core`
`pip install persuader-technology-automata-utilities`
`pip install persuader-technology-automata-redis`
`pip install persuader-technology-automata-trade.executor`
`pip install binance-connector`

## Running

### IDE
1. Go to `Run`
2. Choose `Edit configurations...`
3. In `Paramaters:` 
   ```
   --options REDIS_SERVER_ADDRESS=192.168.1.90 REDIS_SERVER_PORT=6379 TRADE_TRANSFORM_RULES_KEY=binance:trade:transform-rules TRADE_KEY=binance:trade BINANCE_API_KEY=<API_KEY> BINANCE_API_SECRET=<API_SECRET>
   ```