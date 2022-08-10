#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from typing import Collection
from requests.models import get_auth_from_url
from dotenv import load_dotenv
import click
import requests
import os
from typing import List

from pprint import pprint

load_dotenv()


class Game:
    def __init__(self, json_obj):
        self.json_obj = json_obj

    @property
    def identifier(self) -> str:
        return self.json_obj["identifier"]

    @property
    def title(self) -> str:
        return self.json_obj["title"]

    def __repr__(self) -> str:
        return str(self.json_obj)


class Collection:
    def __init__(self, json_obj):
        self.json_obj = json_obj

    @property
    def games(self) -> List[Game]:
        return [Game(item["gameDetails"]) for item in self.json_obj["games"]]


class KallaxClient:

    root_url: str
    session: requests.Session

    def __init__(self):
        self.session = requests.Session()
        self.root_url = os.getenv("KALLAX_API_URL", "")
        token = os.getenv("KALLAX_API_KEY")
        if token is None:
            raise Exception("You must defined KALLAX_API_KEY env var")
        self.session.headers["Accept"] = "application/json"
        self.session.headers["x-api-key"] = token

    def get_url(self, endpoint: str) -> str:
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"
        return self.root_url + endpoint

    @property
    def collection(self) -> Collection:
        endpoint = self.get_url("/collection")
        req = self.session.get(endpoint)
        return Collection(req.json())

    def game(self, game_id: str):
        endpoint = self.get_url("/owns") + "/" + game_id
        req = self.session.get(endpoint)
        return req.json()


@click.command()
def dump_collection():
    collection = KallaxClient().collection
    for game in collection.games:
        print(game)


if __name__ == "__main__":
    dump_collection()
