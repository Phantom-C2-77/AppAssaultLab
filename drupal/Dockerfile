FROM drupal:8.5.0

# CVE-2018-7600 — Drupalgeddon2 (Unauthenticated RCE)
# This version is vulnerable out of the box

# Setup writable directories and auto-install with SQLite
RUN mkdir -p /var/www/html/sites/default/files && \
    cp /var/www/html/sites/default/default.settings.php /var/www/html/sites/default/settings.php && \
    chmod 666 /var/www/html/sites/default/settings.php && \
    chown -R www-data:www-data /var/www/html/sites/default

# Create settings that skip the install wizard with SQLite
RUN echo "\n\
\$databases['default']['default'] = array (\n\
  'database' => '/var/www/html/sites/default/files/.sqlite',\n\
  'prefix' => '',\n\
  'namespace' => 'Drupal\\\\Core\\\\Database\\\\Driver\\\\sqlite',\n\
  'driver' => 'sqlite',\n\
);\n\
\$settings['hash_salt'] = 'insecure_hash_salt_for_lab';\n\
\$settings['install_profile'] = 'standard';\n\
" >> /var/www/html/sites/default/settings.php

# Flag
RUN echo "FLAG{drupalg3dd0n2_rc3_pwn3d}" > /flag.txt && chmod 644 /flag.txt

EXPOSE 80
