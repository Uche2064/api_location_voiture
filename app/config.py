from pydantic import BaseSetting

class Setting(BaseSetting):
    db_name: str
    db_username: str
    db_host: str
    db_port: int