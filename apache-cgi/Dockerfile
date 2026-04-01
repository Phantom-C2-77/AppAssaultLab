FROM httpd:2.4.49

# CVE-2021-41773 — Path Traversal + RCE via CGI
# This version has the path traversal vulnerability

# Enable CGI module
RUN sed -i 's/#LoadModule cgid_module/LoadModule cgid_module/' /usr/local/apache2/conf/httpd.conf && \
    sed -i 's/#LoadModule cgi_module/LoadModule cgi_module/' /usr/local/apache2/conf/httpd.conf

# Configure to allow CGI execution and path traversal
RUN echo '<Directory />' >> /usr/local/apache2/conf/httpd.conf && \
    echo '    Require all granted' >> /usr/local/apache2/conf/httpd.conf && \
    echo '</Directory>' >> /usr/local/apache2/conf/httpd.conf && \
    echo 'ScriptAlias /cgi-bin/ "/usr/local/apache2/cgi-bin/"' >> /usr/local/apache2/conf/httpd.conf

# Create a CGI script
RUN mkdir -p /usr/local/apache2/cgi-bin && \
    printf '#!/bin/bash\necho "Content-Type: text/plain"\necho ""\necho "CGI Script Running"\necho "Server: $(hostname)"\n' > /usr/local/apache2/cgi-bin/test.cgi && \
    chmod +x /usr/local/apache2/cgi-bin/test.cgi

# Flag
RUN echo "FLAG{ap4che_p4th_tr4v3rsal_rc3}" > /flag.txt && chmod 644 /flag.txt

# Web content
RUN echo '<html><body><h1>Widget Corp - Web Server</h1><p>Apache HTTP Server</p></body></html>' > /usr/local/apache2/htdocs/index.html

EXPOSE 80
