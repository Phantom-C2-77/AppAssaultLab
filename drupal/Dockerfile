FROM drupal:8.5.0

# CVE-2018-7600 — Drupalgeddon2 (Unauthenticated RCE)
# The vulnerability exists in the Form API and is exploitable
# even when Drupal is on the install page

# Setup writable directories
RUN mkdir -p /var/www/html/sites/default/files && \
    cp /var/www/html/sites/default/default.settings.php /var/www/html/sites/default/settings.php && \
    chmod 666 /var/www/html/sites/default/settings.php && \
    chown -R www-data:www-data /var/www/html/sites/default

# Flag
RUN echo "FLAG{drupalg3dd0n2_rc3_pwn3d}" > /flag.txt && chmod 644 /flag.txt

EXPOSE 80
