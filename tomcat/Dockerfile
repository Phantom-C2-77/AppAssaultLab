FROM tomcat:9.0.30-jdk11

# Enable AJP connector (Ghostcat CVE-2020-1938)
COPY server.xml /usr/local/tomcat/conf/server.xml

# Enable Manager app with weak credentials
COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml
COPY context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml
COPY context.xml /usr/local/tomcat/webapps/host-manager/META-INF/context.xml

# Flag
RUN echo "FLAG{t0mcat_gh0stcat_ajp_pwn3d}" > /flag.txt && chmod 644 /flag.txt
RUN mkdir -p /usr/local/tomcat/webapps/ROOT && \
    echo '<html><body><h1>Widget Corp - Internal Portal</h1><p>Tomcat Application Server</p></body></html>' > /usr/local/tomcat/webapps/ROOT/index.html

EXPOSE 8080 8009
