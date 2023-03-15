#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  t.me/ReQuestChat
#  Copyright (C) 2021 The Authors

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.

#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


""" logging things """

import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        logging.StreamHandler()
    ]
)

def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)

""" mandatory imports """

import asyncio
import re

""" bloated imports """

import aiohttp
import os
from typing import Dict

""" helper function to make an HTTP request """

async def fetch_website(
    input_url: str,
    custom_headers: Dict = None
) -> str:
    # LOGGER(__name__).info(input_url)
    second_response = None
    async with aiohttp.ClientSession() as session:
        try:
            one_response = await session.get(
                input_url,
                headers=custom_headers
            )
            second_response = await one_response.text()
        except:  # noqa: E722
            return False
    # LOGGER(__name__).info(second_response)
    return second_response

""" wrapper for getting the credentials """

def get_config(name: str, d_v=None, should_prompt=False):
    """ accepts one mandatory variable
    and prompts for the value, if not available """
    val = os.environ.get(name, d_v)
    if not val and should_prompt:
        try:
            val = input(f"enter {name}'s value: ")
        except EOFError:
            val = d_v
        print("\n")
    return val

""" fetch posts and returns in the required format """

async def ctl():
    io = "https://t.me/ReQuestChat"
    A = get_config("A", "A")
    G = get_config("G", "G")
    H = get_config("H", "H")
    b = await fetch_website(
        A,
        {
            H: G
        }
    )
    B = re.compile(get_config("B", "B"))
    cl = B.match(b)
    f = []

    if not cl:
        return f
    f.append(cl.group(1))
    return f


async def fpt():
    a = await cl()
    with open("T", "w+") as fod:
        dump(a, fod, indent=2)



asyncio.run(fpt())
