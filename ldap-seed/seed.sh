#!/bin/bash
echo "[*] Waiting for LDAP server..."
for i in $(seq 1 30); do
    if ldapsearch -x -H ldap://openldap:389 -b "dc=widgetcorp,dc=local" -s base > /dev/null 2>&1; then
        echo "[+] LDAP is ready"
        break
    fi
    sleep 2
done

sleep 3

# Add organizational units
ldapadd -x -H ldap://openldap:389 -D "cn=admin,dc=widgetcorp,dc=local" -w admin123 << 'EOF'
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

sleep 1

# Add users with passwords (some weak, some in descriptions)
ldapadd -x -H ldap://openldap:389 -D "cn=admin,dc=widgetcorp,dc=local" -w admin123 << 'EOF'
dn: cn=admin.jenkins,ou=ServiceAccounts,dc=widgetcorp,dc=local
objectClass: inetOrgPerson
cn: admin.jenkins
sn: Jenkins
givenName: Admin
mail: jenkins@widgetcorp.local
uid: admin.jenkins
userPassword: admin
description: Jenkins CI/CD admin account — FLAG{ld4p_an0n_b1nd_dump}

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

dn: cn=backup.svc,ou=ServiceAccounts,dc=widgetcorp,dc=local
objectClass: inetOrgPerson
cn: backup.svc
sn: Backup
givenName: Service
mail: backup@widgetcorp.local
uid: backup.svc
userPassword: Backup2026!
description: Automated backup service — SSH key at /opt/backups/.ssh/id_rsa
EOF

echo "[+] LDAP users seeded"
echo "[+] LDAP seed complete"
