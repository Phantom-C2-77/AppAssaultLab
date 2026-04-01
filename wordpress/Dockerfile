FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl dos2unix \
    && rm -rf /var/lib/apt/lists/*

COPY setup.sh /setup.sh
RUN dos2unix /setup.sh && chmod +x /setup.sh

CMD ["bash", "/setup.sh"]
