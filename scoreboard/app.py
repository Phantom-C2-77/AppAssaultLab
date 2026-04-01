from flask import Flask, request, render_template_string, jsonify
import hashlib
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_PATH = "/app/scoreboard.db"

FLAGS = [
    {"id": 1, "name": "WordPress Compromise", "category": "CMS", "points": 20, "difficulty": "Easy",
     "hash": hashlib.sha256(b"FLAG{w0rdpr3ss_xxe_m3dia_pwn3d}").hexdigest(),
     "desc": "Exploit WordPress 5.6 — CVE-2021-29447 XXE or WPScan enumeration", "cve": "CVE-2021-29447"},
    {"id": 2, "name": "Joomla Info Leak", "category": "CMS", "points": 20, "difficulty": "Easy",
     "hash": hashlib.sha256(b"FLAG{j00mla_4pi_1nf0_l3ak}").hexdigest(),
     "desc": "Exploit Joomla 4.2.7 — CVE-2023-23752 unauthenticated API disclosure", "cve": "CVE-2023-23752"},
    {"id": 3, "name": "Drupalgeddon2 RCE", "category": "CMS", "points": 25, "difficulty": "Medium",
     "hash": hashlib.sha256(b"FLAG{drupalg3dd0n2_rc3_pwn3d}").hexdigest(),
     "desc": "Exploit Drupal 8.5.0 — CVE-2018-7600 unauthenticated remote code execution", "cve": "CVE-2018-7600"},
    {"id": 4, "name": "Tomcat Ghostcat", "category": "Servlet", "points": 30, "difficulty": "Medium",
     "hash": hashlib.sha256(b"FLAG{t0mcat_gh0stcat_ajp_pwn3d}").hexdigest(),
     "desc": "Exploit Tomcat 9.0.30 — CVE-2020-1938 AJP file read + Manager WAR deploy", "cve": "CVE-2020-1938"},
    {"id": 5, "name": "Jenkins File Read", "category": "DevOps", "points": 30, "difficulty": "Medium",
     "hash": hashlib.sha256(b"FLAG{j3nk1ns_cl1_f1l3_r3ad}").hexdigest(),
     "desc": "Exploit Jenkins 2.441 — CVE-2024-23897 arbitrary file read via CLI", "cve": "CVE-2024-23897"},
    {"id": 6, "name": "GitLab ExifTool RCE", "category": "DevOps", "points": 40, "difficulty": "Hard",
     "hash": hashlib.sha256(b"FLAG{g1tlab_ex1ft00l_rc3}").hexdigest(),
     "desc": "Exploit GitLab CE 13.10.2 — CVE-2021-22205 RCE via malicious image upload", "cve": "CVE-2021-22205"},
    {"id": 7, "name": "Splunk Custom App RCE", "category": "Monitoring", "points": 30, "difficulty": "Medium",
     "hash": hashlib.sha256(b"FLAG{splunk_d3fault_cr3ds_rc3}").hexdigest(),
     "desc": "Exploit Splunk 8.2.0 — default credentials + custom scripted input RCE", "cve": "Default Credentials"},
    {"id": 8, "name": "Apache Path Traversal RCE", "category": "CGI", "points": 25, "difficulty": "Medium",
     "hash": hashlib.sha256(b"FLAG{ap4che_p4th_tr4v3rsal_rc3}").hexdigest(),
     "desc": "Exploit Apache 2.4.49 — CVE-2021-41773 path traversal to CGI RCE", "cve": "CVE-2021-41773"},
    {"id": 9, "name": "Shellshock Bash RCE", "category": "CGI", "points": 20, "difficulty": "Easy",
     "hash": hashlib.sha256(b"FLAG{sh3llsh0ck_bash_rc3_pwn3d}").hexdigest(),
     "desc": "Exploit Bash 4.3 — CVE-2014-6271 Shellshock via CGI request headers", "cve": "CVE-2014-6271"},
    {"id": 10, "name": "phpMyAdmin LFI to RCE", "category": "Data", "points": 35, "difficulty": "Hard",
     "hash": hashlib.sha256(b"FLAG{phpmyadm1n_lf1_rc3}").hexdigest(),
     "desc": "Exploit phpMyAdmin 4.8.1 — CVE-2018-12613 LFI to session file RCE", "cve": "CVE-2018-12613"},
    {"id": 11, "name": "LDAP Anonymous Bind", "category": "Data", "points": 15, "difficulty": "Easy",
     "hash": hashlib.sha256(b"FLAG{ld4p_an0n_b1nd_dump}").hexdigest(),
     "desc": "Exploit OpenLDAP — anonymous bind to enumerate users and credentials", "cve": "Misconfiguration"},
]

TOTAL_POINTS = sum(f["points"] for f in FLAGS)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flag_id INTEGER, flag_name TEXT, points INTEGER,
        submitted_at TEXT, captured INTEGER DEFAULT 0
    )""")
    conn.commit()
    conn.close()

init_db()

HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>AppAssault Lab</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0e1a;color:#e8ecf4;font-family:'Segoe UI',sans-serif;font-size:13px}
.nav{background:#111827;border-bottom:1px solid #1f2937;padding:12px 24px;display:flex;justify-content:space-between;align-items:center}
.nav h1{color:#ef4444;font-size:20px}.nav span{color:#6b7280;font-size:12px}
.container{max-width:950px;margin:24px auto;padding:0 20px}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:20px}
.stat{background:#111827;border:1px solid #1f2937;border-radius:10px;padding:18px;text-align:center}
.stat .val{font-size:28px;font-weight:700}.stat .lbl{font-size:11px;color:#6b7280;margin-top:4px}
.card{background:#111827;border:1px solid #1f2937;border-radius:10px;padding:20px;margin-bottom:16px}
.card h3{margin-bottom:12px;font-size:15px}
table{width:100%;border-collapse:collapse}
th{text-align:left;padding:8px;color:#6b7280;font-size:11px;border-bottom:1px solid #1f2937}
td{padding:8px;border-bottom:1px solid #1f2937;font-size:12px}
.badge{padding:2px 8px;border-radius:4px;font-size:10px;font-weight:600}
.badge-easy{background:rgba(16,185,129,0.15);color:#10b981}
.badge-medium{background:rgba(245,158,11,0.15);color:#f59e0b}
.badge-hard{background:rgba(239,68,68,0.15);color:#ef4444}
.captured{color:#10b981}.not-captured{color:#6b7280}
.cve{color:#ef4444;font-family:monospace;font-size:11px}
input[type=text]{padding:10px 14px;background:#0a0e1a;border:1px solid #2a3050;border-radius:8px;color:#e8ecf4;font-size:14px;font-family:monospace;width:300px}
button{padding:10px 20px;background:#ef4444;color:white;border:none;border-radius:8px;font-weight:600;cursor:pointer;font-size:14px}
#result{margin-top:10px;font-size:14px}
</style></head><body>
<div class="nav"><h1>AppAssault Lab</h1><span>Attacking Common Applications | {{ captured }}/{{ total }} | {{ points }}/{{ total_points }} pts</span></div>
<div class="container">
<div class="stats">
<div class="stat"><div class="val" style="color:#10b981">{{ captured }}</div><div class="lbl">Apps Compromised</div></div>
<div class="stat"><div class="val" style="color:#ef4444">{{ points }} / {{ total_points }}</div><div class="lbl">Points</div></div>
<div class="stat"><div class="val" style="color:#a78bfa">{{ pct }}%</div><div class="lbl">Completion</div></div>
</div>
<div class="card"><h3>Submit Flag</h3>
<div style="display:flex;gap:8px"><input type="text" id="flag-input" placeholder="FLAG{...}">
<button onclick="submitFlag()">Submit</button></div><div id="result"></div></div>
<div class="card"><h3>Targets</h3>
<table><thead><tr><th>#</th><th>Target</th><th>CVE</th><th>Category</th><th>Points</th><th>Difficulty</th><th>Status</th></tr></thead>
<tbody>{% for f in flags %}
<tr><td>{{ f.id }}</td><td>{{ f.name }}<br><span style="color:#6b7280;font-size:10px">{{ f.desc }}</span></td>
<td><span class="cve">{{ f.cve }}</span></td><td>{{ f.category }}</td><td>{{ f.points }}</td>
<td><span class="badge badge-{{ f.difficulty|lower }}">{{ f.difficulty }}</span></td>
<td>{% if f.captured %}<span class="captured">PWNED</span>{% else %}<span class="not-captured">Active</span>{% endif %}</td></tr>
{% endfor %}</tbody></table></div>
<div class="card"><h3>Submit via API</h3>
<pre style="background:#0a0e1a;padding:10px;border-radius:6px;border:1px solid #1f2937;font-size:11px;color:#e8ecf4">curl -X POST http://localhost:7777/api/submit -H "Content-Type: application/json" -d '{"flag":"FLAG{...}"}'</pre></div>
</div>
<script>
async function submitFlag(){const i=document.getElementById('flag-input'),r=document.getElementById('result'),f=i.value.trim();if(!f)return;
const resp=await fetch('/api/submit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({flag:f})});
const d=await resp.json();if(d.correct){if(d.already)r.innerHTML='<span style="color:#f59e0b">Already pwned: '+d.name+'</span>';
else{r.innerHTML='<span style="color:#10b981">PWNED! '+d.name+' +'+d.points+' pts</span>';setTimeout(()=>location.reload(),1500)}}
else r.innerHTML='<span style="color:#ef4444">Invalid flag</span>';i.value=''}
document.getElementById('flag-input').addEventListener('keydown',function(e){if(e.key==='Enter')submitFlag()});
</script></body></html>"""

@app.route("/")
def index():
    conn = sqlite3.connect(DB_PATH)
    captured_ids = [r[0] for r in conn.execute("SELECT flag_id FROM submissions WHERE captured=1").fetchall()]
    conn.close()
    flags = [dict(f, captured=f["id"] in captured_ids) for f in FLAGS]
    captured = len(captured_ids)
    points = sum(f["points"] for f in FLAGS if f["id"] in captured_ids)
    pct = int(captured * 100 / len(FLAGS)) if FLAGS else 0
    return render_template_string(HTML, flags=flags, captured=captured, total=len(FLAGS), points=points, total_points=TOTAL_POINTS, pct=pct)

@app.route("/api/submit", methods=["POST"])
def submit():
    data = request.get_json() or {}
    flag = data.get("flag", "").strip()
    if not flag:
        return jsonify({"correct": False, "message": "No flag provided"})
    flag_hash = hashlib.sha256(flag.encode()).hexdigest()
    for f in FLAGS:
        if f["hash"] == flag_hash:
            conn = sqlite3.connect(DB_PATH)
            existing = conn.execute("SELECT id FROM submissions WHERE flag_id=? AND captured=1", (f["id"],)).fetchone()
            if existing:
                conn.close()
                return jsonify({"correct": True, "already": True, "name": f["name"], "points": f["points"]})
            conn.execute("INSERT INTO submissions (flag_id, flag_name, points, submitted_at, captured) VALUES (?,?,?,?,1)",
                (f["id"], f["name"], f["points"], datetime.now().isoformat()))
            conn.commit()
            conn.close()
            return jsonify({"correct": True, "already": False, "name": f["name"], "points": f["points"]})
    return jsonify({"correct": False, "message": "Invalid flag"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
