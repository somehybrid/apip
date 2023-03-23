import asyncio
import pytest
import apip

client = apip.Client()

pytest_plugins = ('pytest_asyncio', )

@pytest.mark.asyncio
async def test_list():
    proc = await asyncio.create_subprocess_exec("pip list", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    output = await proc.communicate()[0]
    assert await client.list() == 