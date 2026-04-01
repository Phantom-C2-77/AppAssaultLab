FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    ldap-utils dos2unix \
    && rm -rf /var/lib/apt/lists/*

COPY seed.sh /seed.sh
RUN dos2unix /seed.sh && chmod +x /seed.sh

CMD ["bash", "/seed.sh"]
