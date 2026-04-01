FROM tomcat:9.0.30-jdk11

RUN apt-get update && apt-get install -y --no-install-recommends dos2unix \
    && rm -rf /var/lib/apt/lists/*

# Enable AJP connector (Ghostcat CVE-2020-1938)
COPY server.xml /usr/local/tomcat/conf/server.xml
RUN dos2unix /usr/local/tomcat/conf/server.xml

# Enable Manager app — copy from webapps.dist to webapps
RUN cp -r /usr/local/tomcat/webapps.dist/manager /usr/local/tomcat/webapps/manager && \
    cp -r /usr/local/tomcat/webapps.dist/host-manager /usr/local/tomcat/webapps/host-manager

# Weak credentials — MUST come after manager copy
COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml
RUN dos2unix /usr/local/tomcat/conf/tomcat-users.xml

# Remove IP restrictions on Manager app
COPY context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml
COPY context.xml /usr/local/tomcat/webapps/host-manager/META-INF/context.xml
RUN dos2unix /usr/local/tomcat/webapps/manager/META-INF/context.xml && \
    dos2unix /usr/local/tomcat/webapps/host-manager/META-INF/context.xml

# Verify files are readable
RUN cat /usr/local/tomcat/conf/tomcat-users.xml

# Flag
RUN echo "FLAG{t0mcat_gh0stcat_ajp_pwn3d}" > /flag.txt && chmod 644 /flag.txt
RUN mkdir -p /usr/local/tomcat/webapps/ROOT && \
    echo '<html><body><h1>Widget Corp - Internal Portal</h1><p>Tomcat Application Server</p></body></html>' > /usr/local/tomcat/webapps/ROOT/index.html

EXPOSE 8080 8009
