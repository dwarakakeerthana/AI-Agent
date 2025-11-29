import sqlite3
import json
from pathlib import Path


class MemoryBank:
    def __init__(self, db_path: str = "memory/memory.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS runs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    profile TEXT,
                    pipeline TEXT,
                    created_ts DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                """
            )

    def save_run_summary(self, profile: dict, pipeline: list) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO runs (profile, pipeline) VALUES (?, ?)", (json.dumps(profile), json.dumps(pipeline)))
            return cur.lastrowid

    def list_runs(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, profile, pipeline, created_ts FROM runs ORDER BY id DESC LIMIT 50")
            rows = cur.fetchall()
            return [dict(id=r[0], profile=json.loads(r[1]), pipeline=json.loads(r[2]), created_ts=r[3]) for r in rows]
