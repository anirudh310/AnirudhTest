from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    try:
        return subprocess.check_output("top -b -n 1", shell=True, text=True)
    except Exception as e:
        return str(e)

@app.route('/htop')
def htop():
    system_username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = get_top_output()
    
    response = f"""
    <h1>Name: Anirudh Sharma</h1>
    <h2>Username: {system_username}</h2>
    <h3>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h3>
    <pre>{top_output}</pre>
    """
    return response
if __name__ == '__main__':  # ✅ Corrected syntax
    app.run(host='0.0.0.0', port=5000)

