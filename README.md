# BenBotAsync
Python wrapper for the BenBot API.

[![Downloads](https://pepy.tech/badge/benbotasync)](https://pepy.tech/project/benbotasync)
[![Requires: Python 3.x](https://img.shields.io/pypi/pyversions/BenBotAsync.svg)](https://pypi.org/project/BenBotAsync/)
[![BenBot Version: 1.0.1](https://img.shields.io/pypi/v/BenBotAsync.svg)](https://pypi.org/project/BenBotAsync/)

## Installing:
### ~~Synchronous~~: **Deprecated for now.**
~~Windows:~~ ``py -3 -m pip install BenBot``<br>
~~Linux/macOS:~~ ``python3 -m pip install BenBot``

### Asynchronous:
Windows: ``py -3 -m pip install BenBotAsync``<br>
Linux/macOS: ``python3 -m pip install BenBotAsync``

## Examples:
```
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
loop.close()
```

This would output:<br>
```CID_029_Athena_Commando_F_Halloween```

fortnitepy example:
```
import fortnitepy
import BenBotAsync

client = fortnitepy.Client(
    auth=fortnitepy.EmailAndPasswordAuth(
        email='example@email.com',
        password='password123'
    )
)

@client.event
async def event_friend_message(message):
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
