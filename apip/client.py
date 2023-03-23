from apip.abc.installer import Installer
import asyncio
import sys
import re


class Client(Installer):
    """
    The main class for the apip API wrapper. This class is used to interact with the Pip and PyPi API.

    :param index: The index to install the package from.
    :type index: str
    """

    def __init__(self, index="https://pypi.org/simple"):
        Installer.__init__(self, index)

    async def list(self):
        """
        Lists all installed packages and returns them in a list of Package objects.

        :return: A list of Package objects for all installed packages.
        :rtype: list
        """
        packages = []
        proc = await asyncio.create_subprocess_shell(
            f"{sys.executable} -m pip list", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        output = await proc.communicate()
        output = output[0].decode()
        output = '\n'.join(output.splitlines()[2:])
        pkg = re.findall("[\w-]+(?= )", output)
        versions = re.findall("(?<= )[\d\.]+", output)
        for package, version in zip(pkg, versions):
            packages.append(await self.get(package, version))
        return packages
