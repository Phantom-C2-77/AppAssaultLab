FROM tomcat:9.0.30-jdk11

# Enable AJP connector (Ghostcat CVE-2020-1938)
COPY server.xml /usr/local/tomcat/conf/server.xml

# Enable Manager app — copy from webapps.dist to webapps
RUN cp -r /usr/local/tomcat/webapps.dist/manager /usr/local/tomcat/webapps/manager && \
    cp -r /usr/local/tomcat/webapps.dist/host-manager /usr/local/tomcat/webapps/host-manager

# Weak credentials — write directly to avoid CRLF issues
RUN printf '<?xml version="1.0" encoding="UTF-8"?>\n<tomcat-users>\n  <role rolename="manager-gui"/>\n  <role rolename="manager-script"/>\n  <role rolename="admin-gui"/>\n  <user username="tomcat" password="tomcat" roles="manager-gui,manager-script,admin-gui"/>\n</tomcat-users>\n' > /usr/local/tomcat/conf/tomcat-users.xml

# Remove IP restrictions on Manager app
RUN printf '<?xml version="1.0" encoding="UTF-8"?>\n<Context antiResourceLocking="false" privileged="true">\n</Context>\n' > /usr/local/tomcat/webapps/manager/META-INF/context.xml && \
    printf '<?xml version="1.0" encoding="UTF-8"?>\n<Context antiResourceLocking="false" privileged="true">\n</Context>\n' > /usr/local/tomcat/webapps/host-manager/META-INF/context.xml

# Flag
RUN echo "FLAG{t0mcat_gh0stcat_ajp_pwn3d}" > /flag.txt && chmod 644 /flag.txt
RUN mkdir -p /usr/local/tomcat/webapps/ROOT && \
    echo '<html><body><h1>Widget Corp - Internal Portal</h1><p>Tomcat Application Server</p></body></html>' > /usr/local/tomcat/webapps/ROOT/index.html

EXPOSE 8080 8009
