#!/bin/bash
# Binance market order for slightly > $10

# 1. Set the API Key + Secret
API_KEY="<YOUR-API-KEY>"
API_SECRET="<YOUR-API-SECRET>"

# 2. Get the timestamp
TIMESTAMP="$(( $(date +%s) *1000))"
TIMESTAMP_PARAMETER="timestamp=${TIMESTAMP}"

# 3 Create the order (BUY = USDT->BUSD | SELL = BUSD->USDT)
ORDER_SYMBOL="BUSDUSDT"
ORDER_SIDE="SELL"
ORDER_TYPE="MARKET"
ORDER_QUANTITY="11"

# 4. Create the "URI Request"
URI_REQUEST="symbol=${ORDER_SYMBOL}&side=${ORDER_SIDE}&type=${ORDER_TYPE}&quantity=${ORDER_QUANTITY}&recvWindow=5000&${TIMESTAMP_PARAMETER}"

# 5. Sign the "URI Request"
SIGNATURE=`echo -n $URI_REQUEST | openssl dgst -sha256 -hmac $API_SECRET | cut -c 10-`
SIGNATURE_PARAMETER="signature=${SIGNATURE}"

# 6. POST request
BINANCE_BASE_URL="https://api.binance.com"

echo -e "\nSpot Trade API\n"

URI="/api/v3/order"
URL=${BINANCE_BASE_URL}${URI}

curl -H "X-MBX-APIKEY: ${API_KEY}" -X POST $URL -d "${URI_REQUEST}&${SIGNATURE_PARAMETER}"

echo -e "\n\nURL: $URL\n"
