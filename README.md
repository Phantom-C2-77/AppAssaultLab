# AppAssault Lab — Attacking Common Applications

```
    ╔══════════════════════════════════════════╗
    ║                                          ║
    ║   APP ASSAULT LAB                        ║
    ║   Attacking Common Applications          ║
    ║                                          ║
    ║   15 Vulnerable Apps | 15 CVEs           ║
    ║   Real Exploits | Real RCE               ║
    ║                                          ║
    ╚══════════════════════════════════════════╝
```

**A collection of intentionally vulnerable real-world applications for practicing exploitation techniques.**

Each application runs a specific vulnerable version with known CVEs and misconfigurations. Enumerate, exploit, and gain RCE on each target.

---

## Quick Start

```bash
git clone https://github.com/Phantom-C2-77/AppAssaultLab.git
cd AppAssaultLab
docker compose up -d

# Wait 3-5 minutes for all services to initialize
# Open scoreboard: http://localhost:7777
```

### Requirements
- Docker + Docker Compose
- 8GB+ RAM (recommended 16GB)
- Kali Linux or equivalent pentest OS

---

## Targets

### Content Management Systems (CMS)

| Target | Version | CVE | Port | Technique |
|--------|---------|-----|------|-----------|
| WordPress | 5.6 | CVE-2021-29447 (XXE) + WPScan | 8001 | Plugin enumeration → XXE → credential leak |
| Joomla | 4.2.7 | CVE-2023-23752 (Info Disclosure) | 8002 | API info leak → admin access → template RCE |
| Drupal | 8.5.0 | CVE-2018-7600 (Drupalgeddon2) | 8003 | Unauthenticated RCE via form API |

### Servlet Containers & DevOps

| Target | Version | CVE/Vuln | Port | Technique |
|--------|---------|----------|------|-----------|
| Tomcat | 9.0.30 | CVE-2020-1938 (Ghostcat) + Manager Deploy | 8004/8009 | AJP file read → WAR deploy → RCE |
| Jenkins | 2.441 | CVE-2024-23897 (File Read) + Script Console | 8005 | Arbitrary file read → credentials → RCE |
| GitLab CE | 13.10.2 | CVE-2021-22205 (RCE via ExifTool) | 8006 | Image upload → RCE |

### Infrastructure & Monitoring

| Target | Version | CVE/Vuln | Port | Technique |
|--------|---------|----------|------|-----------|
| Splunk | 8.2.0 | Default creds + Custom App RCE | 8007 | admin:changeme → scripted input → RCE |
| Nagios XI | 5.7.5 | CVE-2021-25296 (Authenticated RCE) | 8008 | Default creds → command injection → RCE |
| Zabbix | 5.0.0 | CVE-2022-23131 (Auth Bypass + RCE) | 8009 | SAML bypass → script execution → RCE |

### Ticketing & Collaboration

| Target | Version | CVE/Vuln | Port | Technique |
|--------|---------|----------|------|-----------|
| osTicket | 1.15.8 | File upload bypass + SQL injection | 8010 | Upload .phar → execute → RCE |
| Roundcube | 1.5.0 | CVE-2023-5631 (Stored XSS → RCE chain) | 8011 | XSS → CSRF → command execution |

### CGI & Legacy

| Target | Version | CVE/Vuln | Port | Technique |
|--------|---------|----------|------|-----------|
| Apache + CGI | 2.4.49 | CVE-2021-41773 (Path Traversal + RCE) | 8012 | Path traversal → CGI execution → RCE |
| Shellshock | Bash 4.3 | CVE-2014-6271 (Shellshock) | 8013 | CGI bash injection → RCE |

### Data & Services

| Target | Version | CVE/Vuln | Port | Technique |
|--------|---------|----------|------|-----------|
| phpMyAdmin | 4.8.1 | CVE-2018-12613 (LFI → RCE) | 8014 | Local file inclusion → session file → RCE |
| OpenLDAP | 2.4 | Anonymous bind + info disclosure | 8015 | Anonymous query → credential dump |

---

## Attack Methodology

For each target:

1. **Discovery** — Port scan, service identification, version detection
2. **Enumeration** — Application-specific enumeration (WPScan, droopescan, etc.)
3. **Exploitation** — Exploit the CVE or misconfiguration
4. **Post-Exploitation** — Read the flag, demonstrate impact

---

## Recommended Tools

- [nmap](https://nmap.org/) — Service discovery and version detection
- [WPScan](https://github.com/wpscanteam/wpscan) — WordPress vulnerability scanner
- [droopescan](https://github.com/SamJoan/droopescan) — Drupal/Joomla/WordPress scanner
- [Metasploit](https://www.metasploit.com/) — Exploit framework
- [Burp Suite](https://portswigger.net/burp) — Web proxy
- [curl](https://curl.se/) — HTTP client
- [searchsploit](https://www.exploit-db.com/searchsploit) — Exploit database search
- [nuclei](https://github.com/projectdiscovery/nuclei) — Vulnerability scanner

---

## Disclaimer

**All applications are intentionally vulnerable.** Do NOT expose to the internet. Run locally or in an isolated network for training only.

---

## Author

**Opeyemi Kolawole** — [GitHub](https://github.com/Phantom-C2-77)

## License

BSD 3-Clause

## References

- [Vulhub](https://github.com/vulhub/vulhub) — Pre-built vulnerable Docker environments
- [OWASP Vulnerable Container Hub](https://owasp.org/www-project-vulnerable-container-hub/)
- [HTB Academy — Attacking Common Applications](https://academy.hackthebox.com/)
