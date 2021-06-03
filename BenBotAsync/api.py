from .http import HTTPClient
from .exceptions import InvalidVersion
from .aes import FortniteAES
from .cosmetics import FortniteCosmetics

from typing import Any


class BenBot:
    def __init__(self) -> None:
        self.http = HTTPClient()

        self.cosmetics = FortniteCosmetics(self)

    async def added_files(self, **params: Any) -> dict:
        """|coro|

        Returns all files that were added since the passed version or the previous version.

        Parameters
        ----------
        version: Optional[:class:`str`]
            The version of which the current files should be compared with. Defaults to the previous version.

        Raises
        ------
        InvalidVersion
            If you passed a version and this version was invalid.

        Returns
        -------
        :class:`list`:
            A list containing all files that were added since the passed version or the previous version.
        """
        data = await self.http.request(method="GET", url="/files/added", params=params)

        if "Invalid version" in str(data):
            raise InvalidVersion(data['error'])

        return data

    async def get_aes(self, **params: Any) -> FortniteAES:
        """|coro|

        Get the main aes key and dynamic aes key of the passed version or the current version.

        Parameters
        ----------
        version: Optional[:class:`str`]
            The version of which the aes keys should be returned. Default is the current game version.

        Raises
        ------
        InvalidVersion
            If you passed a version and this version was invalid.

        Returns
        -------
        :class:`FortniteAES`:
            FortniteAES object containing the aes information.
        """
        data = await self.http.request(method="GET", url="/aes", params=params)

        if "Invalid version" in str(data):
            raise InvalidVersion(data['error'])

        return FortniteAES(data)

