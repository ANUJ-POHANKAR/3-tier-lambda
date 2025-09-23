import os
import json
import pymysql

# Read database credentials from environment variables
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

def lambda_handler(event, context):
    # Connect to MySQL
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    cur = conn.cursor(pymysql.cursors.DictCursor)

    # Handle GET request
    if event.get('httpMethod') == 'GET':
        cur.execute("SELECT id, name, description FROM items LIMIT 100")
        rows = cur.fetchall()
        return {'statusCode': 200, 'body': json.dumps(rows)}

    # Handle POST request
    elif event.get('httpMethod') == 'POST':
        body = json.loads(event.get('body') or '{}')
        cur.execute(
            "INSERT INTO items (name, description) VALUES (%s, %s)",
            (body.get('name'), body.get('description'))
        )
        conn.commit()
        return {'statusCode': 201, 'body': json.dumps({'id': cur.lastrowid})}

    # Default response
    return {'statusCode': 404, 'body': 'Not found'}
