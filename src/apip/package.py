from __future__ import annotations
from dataclasses import dataclass

import httpx
from index import Index


@dataclass(frozen=True)
class Release:
    digests: dict[str, str]
    filename: str
    has_sig: bool
    md5_digest: str
    packagetype: str
    python_version: str
    requires_python: str
    size: int
    upload_time: str
    url: str
    yanked: bool
    yanked_reason: str


@dataclass(frozen=True)
class Metadata:
    author: str
    author_email: str


@dataclass(frozen=True)
class Package:
    name: str
    classifiers: list[str]
    description: str
    package_url: str
    project_url: str
    project_urls: dict[str, str]
    requirements: list[Package]
    version: str
    versions: dict[str, Release]
