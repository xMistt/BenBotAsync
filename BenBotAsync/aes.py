class FortniteAES:
    """Represents a Fortnite playlist.

    Attributes
    ----------
    raw: :class:`Dict[:class:`str`, Any]`
        Raw data from BenBot (can be used to reconstruct object)
    main_key: :class:`Union[:class`str`, class:`bool:]`:
        The main aes key of the version or None if it isn't defined yet.
    dynamic_keys: :class:`dict`:
        All aes keys of dynamic pak files (pak1000+) with their file name as key.
    """
    def __init__(self, data) -> None:
        self.raw = data

        self.main_key = data.get('mainKey')
        self.dynamic_keys = data.get('dynamicKeys')

