# apip
[![Built with Python](https://img.shields.io/badge/-Python-3c679c?style=for-the-badge&logo=Python&logoColor=fae583)](https://python.org)
[![Built with Aiohttp](https://img.shields.io/badge/-Aiohttp-FFFFFF?style=for-the-badge&logo=Aiohttp&logoColor=blue)](https://docs.aiohttp.org/en/stable/)

An easy, high level wrapper for the PyPi API. It wraps Pip and PyPi into an easier to use package in Python.

---

## Installation
**Requires Python 3.7+**

To install `apip` on PyPi, run 
```shell
pip install apip
```
---

## Quickstart

```python
>>> import apip
>>> import asyncio
>>> pip = apip.Client()
>>> asyncio.run(pip.get("module"))
>>> print(asyncio.run(pip.list()))
```
<<<<<<< HEAD
=======

---

## Documentation
Check the documentation for `apip` [here](https://apip.readthedocs.io/en/latest).
>>>>>>> 210fcb6 (v0.3)
