import uuid


class SessionService:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id: str = None) -> str:
        sid = str(uuid.uuid4())
        self.sessions[sid] = {"user": user_id}
        return sid

    def get_session(self, sid: str):
        return self.sessions.get(sid)
