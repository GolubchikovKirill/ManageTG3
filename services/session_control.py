import os
from pyrogram import Client


class SessionManager:
    def __init__(self, base_path: str = "sessions"):
        self.base_path = base_path

    def _get_session_path(self, phone_number: str) -> str:
        return os.path.join(self.base_path, f"{phone_number}.session")

    def create_session(self, phone_number: str, api_id: int, api_hash: str) -> Client:
        session_path = self._get_session_path(phone_number)
        return Client(
            name=session_path,
            api_id=api_id,
            api_hash=api_hash,
            in_memory=False
        )

    def get_session(self, phone_number: str, api_id: int, api_hash: str) -> Client:
        session_path = self._get_session_path(phone_number)
        if os.path.exists(session_path):
            return Client(
                name=session_path,
                api_id=api_id,
                api_hash=api_hash,
                in_memory=False
            )
        else:
            raise FileNotFoundError(f"Session for {phone_number} not found.")

    def delete_session(self, phone_number: str):
        session_path = self._get_session_path(phone_number)
        if os.path.exists(session_path):
            os.remove(session_path)
        else:
            raise FileNotFoundError(f"Session for {phone_number} not found.")