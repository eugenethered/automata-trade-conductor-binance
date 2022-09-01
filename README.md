# Automata Binance Trade Conductor

## Docker
1. `docker build . -t persuadertechnology/automata-trade-conductor:binance-0.1`
2. `docker image prune --filter label=stage=BUILDER`

## Publishing to Docker Repository
todo: automate this...
1. `docker push persuadertechnology/automata-trade-conductor:binance-0.1`

## Publishing Prerequisites
Need to log in to via docker cli i.e. `docker login -u`
