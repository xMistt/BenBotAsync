# BenBotAsync
Python wrapper for the BenBot API.

[![Downloads](https://pepy.tech/badge/benbotasync)](https://pepy.tech/project/benbotasync)
[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/BenBotAsync.svg)](https://pypi.org/project/BenBotAsync/)
[![BenBot Version: 1.0.1](https://img.shields.io/pypi/v/BenBotAsync.svg)](https://pypi.org/project/BenBotAsync/)

# NOTICE:
On the 30th of July 2022, the Ben Bot API shut down, with this message from the developer, FabianFG;<br>
It was an honor to help so many people with an idea that initially seemed nearly impossible to realize but turned into something pretty cool. Now I just don't feel like I have the time or dedication to continue properly supporting it so this will be the official end of BenBot.<br>
Therefore with BenBot shutting down, this wrapper is now useless. Now, an alternative I would recommend is Fortnite-API which has almost all of the features that BenBot had. I have made a wrapper for this API as well with similar functions, the name of that package is FortniteAPIAsync (https://pypi.org/project/FortniteAPIAsync/)

## Installing:
### ~~Synchronous~~: **Deprecated, use the async version.**
~~Windows:~~ ``py -3 -m pip install BenBot``<br>
~~Linux/macOS:~~ ``python3 -m pip install BenBot``

### Asynchronous:
Windows: ``py -3 -m pip install BenBotAsync``<br>
Linux/macOS: ``python3 -m pip install BenBotAsync``

## Examples:
```py
import BenBotAsync
import asyncio


async def ben_search():
    result = await BenBotAsync.get_cosmetic(
        lang="en",
        searchLang="en",
        matchMethod="full",
        name="Ghoul Trooper"
    )

    print(result.id)

loop = asyncio.get_event_loop()
loop.run_until_complete(ben_search())

```

This would output:<br>
```CID_029_Athena_Commando_F_Halloween```

fortnitepy example:
```py
import fortnitepy
import BenBotAsync


client = fortnitepy.Client(
    auth=fortnitepy.EmailAndPasswordAuth(
        email='example@email.com',
        password='password123'
    )
)


@client.event
async def event_friend_message(message: fortnitepy.FriendMessage) -> None:
    args = message.content.split()
    split = args[1:]
    content = " ".join(split)

    if args[0] == '!skin':
        skin = await BenBotAsync.get_cosmetic(
            lang="en",
            searchLang="en",
            matchMethod="contains",
            name=content,
            backendType="AthenaCharacter"
        )

        await client.user.party.me.set_outfit(asset=skin.id)


client.run()

```

You can check out the documentation for BenBotAsync [here](https://stoplight.io/p/docs/gh/xMistt/BenBotAsync).
