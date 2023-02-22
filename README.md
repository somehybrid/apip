# apip
[![Built with Python](https://img.shields.io/badge/-Python-3c679c?style=for-the-badge&logo=Python&logoColor=fae583)](https://python.org)
[![Built with Aiohttp](https://img.shields.io/badge/-Aiohttp-FFFFFF?style=for-the-badge&logo=Aiohttp&logoColor=blue)](https://docs.aiohttp.org/en/stable/)

An easy, high level wrapper for the PyPi API. It wraps Pip and PyPi into an easier to use package in Python.

---

## Features
- Easy to use, high level API.
- Fully asynchronous and non-blocking.

---

## Installation
**Requires Python 3.7+**

To install `apip` on PyPi, run 
```shell
pip install apip
```
---

## Quickstart
To get started and see what `apip` can do, run some example programs.
```python
>>> import apip
>>> import asyncio
>>> pip = apip.Pip()
>>> asyncio.run(pip.get("module"))
>>> print(asyncio.run(pip.list()))
```
