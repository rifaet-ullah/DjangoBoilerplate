import random
from dataclasses import dataclass
from pathlib import Path
from string import ascii_letters, punctuation, digits

from environs import Env


@dataclass
class Config:
    config_path: str | None = None

    def __post_init__(self):
        self.__env = Env()
        self.__env.read_env()
        self.__default_secret_key = "".join(
            random.choices(ascii_letters + digits + punctuation, k=50)
        )

    @property
    def project_root(self) -> Path:
        return Path.cwd().parent

    @property
    def is_debug_mode_on(self) -> bool:
        return self.__env.bool("DEBUG", default=True)

    @property
    def secret_key(self) -> str:
        return self.__env.str("SECRET_KEY", default=self.__default_secret_key)

    @property
    def allowed_hosts(self) -> list[str]:
        return self.__env.list("ALLOWED_HOSTS", default=[])

    @property
    def db_name(self) -> str:
        return self.__env.str("NAME", default="db")

    @property
    def db_user(self) -> str:
        return self.__env.str("USER")

    @property
    def db_password(self) -> str:
        return self.__env.str("Password")

    @property
    def db_url(self) -> str:
        return self.__env.str("HOST", default="localhost")

    @property
    def db_port(self) -> int:
        return self.__env.str("PORT", default=5432)
