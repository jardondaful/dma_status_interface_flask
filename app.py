from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/data')
def get_data():
    conn = sqlite3.connect('/Users/jardondaful/Downloads/flask_test/database.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM system_info")
    data = c.fetchall()
    conn.close()
    return jsonify([
        {
            'id': row[0],
            'ipv4_address': row[1],
            'cpu_info': row[2],
            'storage_device': row[3],
            'storage_total': row[4],
            'storage_used': row[5],
            'storage_avail': row[6],
            'used_ram_info': row[7],
            'computer_type': row[8],
            'serial_number': row[9]
        } for row in data
    ])

@app.route('/')
def index():
    conn = sqlite3.connect('/Users/jardondaful/Downloads/flask_test/database.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM system_info")
    data = c.fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
