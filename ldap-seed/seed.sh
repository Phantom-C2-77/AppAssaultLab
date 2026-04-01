#!/bin/bash
echo "[*] Waiting for LDAP server..."
for i in $(seq 1 60); do
    if ldapsearch -x -H ldap://openldap:389 -b "dc=widgetcorp,dc=local" -s base > /dev/null 2>&1; then
        echo "[+] LDAP is ready"
        break
    fi
    sleep 3
done

sleep 15
echo "[*] Adding organizational units..."

# Add OUs with retry
for attempt in 1 2 3; do
    ldapadd -x -H ldap://openldap:389 -D "cn=admin,dc=widgetcorp,dc=local" -w admin123 << 'EOF' 2>/dev/null && break
dn: ou=People,dc=widgetcorp,dc=local
objectClass: organizationalUnit
ou: People

dn: ou=Groups,dc=widgetcorp,dc=local
objectClass: organizationalUnit
ou: Groups

dn: ou=ServiceAccounts,dc=widgetcorp,dc=local
objectClass: organizationalUnit
ou: ServiceAccounts
EOF
    echo "[-] OU add attempt $attempt failed, retrying..."
    sleep 5
done

sleep 5
echo "[*] Adding users..."

# Add users with retry
for attempt in 1 2 3; do
    ldapadd -x -H ldap://openldap:389 -D "cn=admin,dc=widgetcorp,dc=local" -w admin123 << 'EOF' 2>/dev/null && break
dn: cn=admin.jenkins,ou=ServiceAccounts,dc=widgetcorp,dc=local
objectClass: inetOrgPerson
cn: admin.jenkins
sn: Jenkins
givenName: Admin
mail: jenkins@widgetcorp.local
uid: admin.jenkins
userPassword: admin
description: Jenkins CI/CD admin account - FLAG{ld4p_an0n_b1nd_dump}

dn: cn=svc.deploy,ou=ServiceAccounts,dc=widgetcorp,dc=local
objectClass: inetOrgPerson
cn: svc.deploy
sn: Deploy
givenName: Service
mail: deploy@widgetcorp.local
uid: svc.deploy
userPassword: deploy123
description: Production deployment service account

dn: cn=john.smith,ou=People,dc=widgetcorp,dc=local
objectClass: inetOrgPerson
cn: john.smith
sn: Smith
givenName: John
mail: j.smith@widgetcorp.local
uid: john.smith
userPassword: Welcome123!
title: Senior Developer

dn: cn=mary.chen,ou=People,dc=widgetcorp,dc=local
objectClass: inetOrgPerson
cn: mary.chen
sn: Chen
givenName: Mary
mail: m.chen@widgetcorp.local
uid: mary.chen
userPassword: DevOps2026!
title: DevOps Lead

dn: cn=david.wilson,ou=People,dc=widgetcorp,dc=local
objectClass: inetOrgPerson
cn: david.wilson
sn: Wilson
givenName: David
mail: d.wilson@widgetcorp.local
uid: david.wilson
userPassword: P@ssw0rd123
title: IT Administrator
description: Has admin access to all systems
EOF
    echo "[-] User add attempt $attempt failed, retrying..."
    sleep 5
done

# Verify
echo "[*] Verifying..."
COUNT=$(ldapsearch -x -H ldap://openldap:389 -b "dc=widgetcorp,dc=local" "(objectClass=person)" cn 2>/dev/null | grep -c "^cn:")
echo "[+] Found $COUNT users"
echo "[+] LDAP seed complete"
