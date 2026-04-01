FROM drupal:8.5.0

# CVE-2018-7600 — Drupalgeddon2 (Unauthenticated RCE)
# This version is vulnerable out of the box
# No apt-get needed — Debian Stretch repos are EOL

# Flag (using echo which is built-in, no packages needed)
RUN echo "FLAG{drupalg3dd0n2_rc3_pwn3d}" > /flag.txt && chmod 644 /flag.txt

# Setup writable directories for Drupal install
RUN mkdir -p /var/www/html/sites/default/files && \
    cp /var/www/html/sites/default/default.settings.php /var/www/html/sites/default/settings.php && \
    chown -R www-data:www-data /var/www/html/sites/default

EXPOSE 80
