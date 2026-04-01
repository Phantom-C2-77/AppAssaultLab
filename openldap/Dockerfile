FROM osixia/openldap:1.5.0

# Force fresh initialization with bootstrap LDIF
ENV LDAP_ORGANISATION="Widget Corp"
ENV LDAP_DOMAIN="widgetcorp.local"
ENV LDAP_BASE_DN="dc=widgetcorp,dc=local"
ENV LDAP_ADMIN_PASSWORD="admin123"
ENV LDAP_TLS="false"
ENV LDAP_REMOVE_CONFIG_AFTER_SETUP="false"
ENV LDAP_READONLY_USER="true"
ENV LDAP_READONLY_USER_USERNAME="readonly"
ENV LDAP_READONLY_USER_PASSWORD="readonly123"
ENV LDAP_RFC2307BIS_SCHEMA="true"

# Allow anonymous read access
ENV LDAP_ACCESS_CONTROL="to * by anonymous read by users read by self write by * none"

# Add seed data as bootstrap LDIF — runs during container init
COPY bootstrap.ldif /container/service/slapd/assets/config/bootstrap/ldif/custom/50-seed.ldif
