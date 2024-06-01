import json
import sqlite3

from typing import List, Dict


def query_database(query: str) -> List[Dict]:
    conn = sqlite3.connect('embrapa_db')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    conn.close()
    results = [dict(zip(columns, row)) for row in rows]
    return results


def results_to_json(results: List[Dict]) -> str:
    try:
        return json.dumps(results, ensure_ascii=False)
    except Exception as e:
        print(e)
        return json.dumps([])
