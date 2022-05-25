# Automata Binance Trade Conductor

## Packaging
`python3 -m build`

## Dependencies (IDE Terminal)
`pip install binance-connector persuader-technology-automata-trade.executor`

## Running

### IDE
1. Go to `Run`
2. Choose `Edit configurations...`
3. In `Paramaters:` 
   ```
   --options 
     REDIS_SERVER_ADDRESS=192.168.1.90 
     REDIS_SERVER_PORT=6379 
     TRADE_TRANSFORMATIONS_KEY=binance:trade:transformations 
     TRADE_KEY=binance:trade 
   ```