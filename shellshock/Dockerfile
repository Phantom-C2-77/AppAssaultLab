FROM ubuntu:14.04

# CVE-2014-6271 — Shellshock (Bash RCE via CGI)
# Ubuntu 14.04 ships with vulnerable Bash 4.3

RUN apt-get update && apt-get install -y apache2

# Enable CGI
RUN a2enmod cgi

# Create vulnerable CGI script
RUN mkdir -p /usr/lib/cgi-bin && \
    printf '#!/bin/bash\necho "Content-Type: text/plain"\necho ""\necho "System Status: OK"\necho "Hostname: $(hostname)"\necho "Date: $(date)"\necho "Uptime: $(uptime)"\n' > /usr/lib/cgi-bin/status.cgi && \
    chmod +x /usr/lib/cgi-bin/status.cgi

# Another CGI for discovery
RUN printf '#!/bin/bash\necho "Content-Type: text/html"\necho ""\necho "<html><body><h2>User Info</h2><pre>"\necho "User: $(whoami)"\necho "ID: $(id)"\necho "</pre></body></html>"\n' > /usr/lib/cgi-bin/user.cgi && \
    chmod +x /usr/lib/cgi-bin/user.cgi

# Flag
RUN echo "FLAG{sh3llsh0ck_bash_rc3_pwn3d}" > /flag.txt && chmod 644 /flag.txt

# Web content
RUN echo '<html><body><h1>Widget Corp - Legacy Server</h1><p>Internal monitoring system</p><p><a href="/cgi-bin/status.cgi">System Status</a></p></body></html>' > /var/www/html/index.html

EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
