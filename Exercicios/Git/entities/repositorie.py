from dataclasses import dataclass


@dataclass
class Repositories:
    url_repo: str
    name_repo: str
    is_fork: str
    size: int
    created_t: str
    language: str