#!/bin/bash
# Wait for WordPress to be ready then configure it
echo "[*] Waiting for WordPress..."
for i in $(seq 1 60); do
    if curl -sf http://wordpress/ > /dev/null 2>&1; then
        echo "[+] WordPress is ready"
        break
    fi
    sleep 5
done

# Install WP-CLI and configure WordPress
echo "[*] Installing WordPress..."
curl -sf "http://wordpress/wp-admin/install.php?step=2" \
    -d "weblog_title=Widget+Corp+Blog&user_name=admin&admin_password=P@ssw0rd123&admin_password2=P@ssw0rd123&admin_email=admin@widgetcorp.local&blog_public=0&pw_weak=1" \
    2>/dev/null || true

sleep 2

# Create a post with flag embedded
curl -sf -u admin:P@ssw0rd123 \
    "http://wordpress/xmlrpc.php" \
    -H "Content-Type: text/xml" \
    -d '<?xml version="1.0"?><methodCall><methodName>wp.newPost</methodName><params><param><value><int>1</int></value></param><param><value><string>admin</string></value></param><param><value><string>P@ssw0rd123</string></value></param><param><value><struct><member><name>post_title</name><value><string>Internal Security Notes</string></value></member><member><name>post_content</name><value><string>Security audit completed. Reference: FLAG{w0rdpr3ss_xxe_m3dia_pwn3d}. All findings remediated except media upload handler.</string></value></member><member><name>post_status</name><value><string>private</string></value></member></struct></value></param></params></methodCall>' \
    2>/dev/null || true

echo "[+] WordPress setup complete"
