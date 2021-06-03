from .enums import *

from typing import List, Any


class BRCosmetic:
    """Represents a Fortnite playlist.

    Attributes
    ----------
    raw: :class:`Dict[:class:`str`, Any]`
        Raw data from BenBot (can be used to reconstruct object)
    id: :class:`str`:
        The id of the cosmetic.
    path: :class:`str`:
        The path in the game files where this cosmetic was located.
    icons: :class:`dict`:
        Dictionary containing 3 keys: icon, featured & series.
    name: :class:`str`:
        Display Name of this cosmetic.
    description: :class:`str`:
        The displayed description of this cosmetic.
    short_description: :class:`str`:
        The displayed short description of this cosmetic.
    backend_type: Enum[:class:`BackendType`]:
        The type of this cosmetic in the backend.
    rarity: :class:`str`:
        The displayed rarity of this cosmetic.
    backend_rarity: Enum[:class:`BackendRarity`]:
        The displayed short description of this cosmetic.
    set: :class:`str`:
        The displayed set of this cosmetic.
    set_text: :class:`str`:
        The whole "Part of the ... set" text with the set.
    series: :class:`dict`:
        Dictionary containing 2 keys: name & colors.
    variants: :class:`list`:
        List containing the data of the cosmetics variants.
    gameplay_tags: :class:`list`:
        List containing the gameplay tags of this cosmetic.
    """
    def __init__(self, data: dict) -> None:
        self.data = data

        self.id = data.get('id')
        self.path = data.get('path')
        self.icons = data.get('icons')
        self.name = data.get('name')
        self.description = data.get('description')
        self.short_description = data.get('shortDescription')
        self.backend_type = BackendType(data.get('backendType'))
        self.rarity = data.get('rarity')
        self.backend_rarity = BackendRarity(data.get('backendRarity'))
        self.set = data.get('set')
        self.set_text = data.get('setText')
        self.series = data.get('series')
        self.variants = data.get('variants')
        self.gameplay_tags = data.get('gameplayTags')


class FortniteCosmetics:
    def __init__(self, client) -> None:
        self.http = client.http

    async def get_all_cosmetics(self, **params: Any) -> List[BRCosmetic]:
        """|coro|

        Get all Cosmetics that exist.

        Parameters
        ----------
        lang: Optional[:class:`str`]
            The language code that should be used, defaults to 'en'.

        Returns
        -------
        :class:`list[:class`BRCosmetic`]`:
            List of all cosmetics that exist in BRCosmetic objects.
        """
        data = await self.http.request(method="GET", url="/files/added", params=params)

        return [BRCosmetic(cosmetic) for cosmetic in data]





