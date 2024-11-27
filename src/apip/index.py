from __future__ import annotations
from dataclasses import dataclass
from urllib.parse import urljoin
import httpx


@dataclass
class Index:
    url: str
    supports_json: bool
    client: httpx.AsyncClient
