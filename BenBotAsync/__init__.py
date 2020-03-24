"""
“Commons Clause” License Condition v1.0
Copyright Oli 2020

The Software is provided to you by the Licensor under the
License, as defined below, subject to the following condition.
Without limiting other conditions in the License, the grant
of rights under the License will not include, and the License
does not grant to you, the right to Sell the Software.
For purposes of the foregoing, “Sell” means practicing any or
all of the rights granted to you under the License to provide
to third parties, for a fee or other consideration (including
without limitation fees for hosting or consulting/ support
services related to the Software), a product or service whose
value derives, entirely or substantially, from the functionality
of the Software. Any license notice or attribution required by
the License must also include this Commons Clause License
Condition notice.

Software: BenBotAsync
License: Apache 2.0
"""

from typing import Tuple, Union, Any

from .enums import *
from .cosmetics import BRCosmetic
from .exceptions import InvalidParameters, NotFound

import aiohttp
import base64
import codecs
import fortnitepy
import traceback
import functools
import asyncio
import json

__name__ = 'BenBotAsync'
__version__ = '2.0.2'
__author__ = 'xMistt'

BEN_BOT_BASE = 'https://benbotfn.tk/api/v1'


# Credit to Terbau for this function.
async def json_or_text(response: aiohttp.ClientResponse) -> Union[str, dict]:
    text = await response.text(encoding='utf-8')
    if 'application/json' in response.headers.get('content-type', ''):
        return json.loads(text)
    return text


async def get_cosmetic(**params: Any):
    """Search cosmetic function which can be used without creating HTTP client."""
    async with aiohttp.ClientSession() as session:
        async with session.request(method='GET', url=f'{BEN_BOT_BASE}/cosmetics/br/search', params=params) as r:
            data = await json_or_text(r)

            if 'At least one search parameter is required' in str(data):
                raise InvalidParameters('At least one valid search parameter is required.')

            if 'Could not find any cosmetic matching parameters' in str(data):
                raise NotFound('Could not find any cosmetic matching parameters.')

            return BRCosmetic(data)
