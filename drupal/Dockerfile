FROM drupal:8.5.0

# CVE-2018-7600 — Drupalgeddon2 (Unauthenticated RCE)
# This version is vulnerable out of the box

# Use SQLite so no separate DB needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 netcat-openbsd curl \
    && rm -rf /var/lib/apt/lists/*

# Flag
RUN echo "FLAG{drupalg3dd0n2_rc3_pwn3d}" > /flag.txt && chmod 644 /flag.txt

# Auto-install Drupal with SQLite
RUN mkdir -p /var/www/html/sites/default/files && \
    cp /var/www/html/sites/default/default.settings.php /var/www/html/sites/default/settings.php && \
    chown -R www-data:www-data /var/www/html/sites/default

EXPOSE 80
