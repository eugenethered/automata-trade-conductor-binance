FROM python:3.10.6-alpine AS BUILDER
LABEL stage=BUILDER
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN apk add --no-cache build-base libffi-dev && pip install --no-cache-dir -r requirements.txt

FROM python:3.10.6-alpine
RUN addgroup apprunner && adduser apprunner -D -H -G apprunner
USER apprunner
WORKDIR /app
COPY --from=BUILDER /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --chown=apprunner:apprunner ./binancetrade ./binancetrade

ENV PYTHONPATH="${PYTHONPATH}:/app/binancetrade" \
    REDIS_SERVER_ADDRESS=127.0.0.1 \
    REDIS_SERVER_PORT=6379 \
    TRADE_TRANSFORMATIONS_KEY=binance:transformation:mv:trade \
    TRADE_KEY=binance:trade \
    MISSING_KEY=binance:mv:missing \
    AUTH_INFO_KEY=binance:auth:info \
    VERSION=0.1 \
    PROCESS_RUN_PROFILE_KEY=binance:process:mv:run-profile \
    PROCESS_KEY=binance:process:mv:status

CMD ["python", "binancetrade/__main__.py"]
