from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# Dashboard ka layout
html_template = """
<html>
    <body style="font-family: sans-serif; padding: 20px;">
        <h1>🛡️ Cyber-Toolbox Dashboard</h1>
        <form method="POST" action="/scan">
            <input type="text" name="url" placeholder="Enter Target URL..." style="width: 300px; padding: 10px;">
            <button type="submit" name="action" value="all">🚀 Scan All (Full Audit)</button>
        </form>
        {% if result %} <h3>Audit Report:</h3> <pre style="background: #f4f4f4; padding: 15px;">{{ result }}</pre> {% endif %}
    </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(html_template)

@app.route("/scan", methods=["POST"])
def scan():
    target = request.form.get("url")
    if not target.startswith("http"): target = "http://" + target
    
    report = f"--- Scanning: {target} ---\n\n"
    
    # Automation: Yahan hum aapke banaye tools ko simulate kar rahe hain
    try:
        # 1. Header Scan
        r = requests.get(target, timeout=5)
        report += f"[+] Server Headers: {dict(list(r.headers.items())[:3])}...\n"
        
        # 2. CMS Check (Simulation)
        if "wp-content" in r.text: report += "[!] CMS: WordPress detected!\n"
        else: report += "[-] CMS: Not found (Custom Site).\n"
        
        # 3. API Status
        report += f"[+] Target Status: {r.status_code} OK\n"
        
    except Exception as e:
        report += f"[!] Scan Error: {e}"
        
    return render_template_string(html_template, result=report)

if __name__ == "__main__":
    app.run(debug=True)