FROM debian:buster-slim

# CVE-2014-6271 — Shellshock simulation
# We install an older bash and create a vulnerable CGI setup
# Note: Modern bash is patched, so we simulate the vulnerability
# by creating a CGI script that passes user input to bash unsafely

RUN apt-get update && apt-get install -y --no-install-recommends \
    apache2 curl \
    && rm -rf /var/lib/apt/lists/*

# Enable CGI
RUN a2enmod cgi

# Create vulnerable CGI scripts that pass headers to bash eval
# This simulates Shellshock by using eval on user-controlled input
RUN mkdir -p /usr/lib/cgi-bin && \
    printf '#!/bin/bash\necho "Content-Type: text/plain"\necho ""\n# VULN: Evaluates User-Agent header unsafely (Shellshock simulation)\nif [ -n "$HTTP_USER_AGENT" ]; then\n  eval "UA=$HTTP_USER_AGENT" 2>/dev/null\nfi\necho "System Status: OK"\necho "Hostname: $(hostname)"\necho "Date: $(date)"\necho "Uptime: $(uptime)"\necho "User-Agent: $HTTP_USER_AGENT"\n' > /usr/lib/cgi-bin/status.cgi && \
    chmod +x /usr/lib/cgi-bin/status.cgi

RUN printf '#!/bin/bash\necho "Content-Type: text/html"\necho ""\necho "<html><body><h2>User Info</h2><pre>"\necho "User: $(whoami)"\necho "ID: $(id)"\n# VULN: Directly executes command from X-Custom header\nif [ -n "$HTTP_X_CUSTOM" ]; then\n  eval "$HTTP_X_CUSTOM" 2>&1\nfi\necho "</pre></body></html>"\n' > /usr/lib/cgi-bin/user.cgi && \
    chmod +x /usr/lib/cgi-bin/user.cgi

# Flag
RUN echo "FLAG{sh3llsh0ck_bash_rc3_pwn3d}" > /flag.txt && chmod 644 /flag.txt

# Web content
RUN echo '<html><body><h1>Widget Corp - Legacy Server</h1><p>Internal monitoring system</p><p><a href="/cgi-bin/status.cgi">System Status</a></p><p><a href="/cgi-bin/user.cgi">User Info</a></p></body></html>' > /var/www/html/index.html

EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]
