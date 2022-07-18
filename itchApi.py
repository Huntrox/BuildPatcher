from typing import List
from typing import Any
from dataclasses import dataclass
import json
import asyncio
import requests 
import subprocess


class ItchApi:
    def __init__(self, url):
        self.url = url
        self.root = None
        self.games = []
        self.error = False

    async def get_games(self):
        
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, requests.get, self.url)
        response = await future
        # generate the object using json.dumps()
        # corresponding to json data
        json_data = json.loads(response.text)
        #check if  json_data contains the key "errors"
        if "errors" in json_data and "invalid key" in json_data['errors']:
            self.error = True
            return
        self.root = Root.from_dict(json_data)
        # loop through root.games and print game id and title
        for game in self.root.games:
            username = game.user.username;
            game_id = game.url.split(f'itch.io/')[1]
            str = f"{username}/{game_id}"
            self.games.append(str)
        return self.root.games
    
    async def upload_build(self, build_path, game_page, channel, version):
        butler_command = f'butler push {build_path} {game_page}:{channel} --userversion {version}'
        cmd = f'cmd.exe /k "{butler_command}"'

        output = subprocess.Popen(['start','cmd','/k',butler_command], shell = True, stdin = subprocess.PIPE, stdout = subprocess.PIPE, text = True)

        return output.stdout


@dataclass
class User:
    id: int
    url: str
    cover_url: str
    username: str
    display_name: str

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        _id = int(obj.get("id"))
        _url = str(obj.get("url"))
        _cover_url = str(obj.get("cover_url"))
        _username = str(obj.get("username"))
        _display_name = str(obj.get("display_name"))
        return User(_id, _url, _cover_url, _username, _display_name)


@dataclass
class Game:
    user: User
    p_android: bool
    published: bool
    created_at: str
    p_windows: bool
    p_osx: bool
    p_linux: bool
    type: str
    title: str
    url: str
    id: int
    cover_url: str
    published_at: str

    @staticmethod
    def from_dict(obj: Any) -> 'Game':
        _user = User.from_dict(obj.get("user"))
        _p_android = bool(obj.get("p_android"))
        _published = bool(obj.get("published"))
        _created_at = str(obj.get("created_at"))
        _p_windows = bool(obj.get("p_windows"))
        _p_osx = bool(obj.get("p_osx"))
        _p_linux = bool(obj.get("p_linux"))
        _type = str(obj.get("type"))
        _title = str(obj.get("title"))
        _url = str(obj.get("url"))
        _id = int(obj.get("id"))
        _cover_url = str(obj.get("cover_url"))
        _published_at = str(obj.get("published_at"))
        return Game(_user,  _p_android,   _published, _created_at,  _p_windows, _p_osx, _p_linux, _type, _title, _url,  _id, _cover_url, _published_at)


@dataclass
class Root:
    games: List[Game]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _games = [Game.from_dict(y) for y in obj.get("games")]
        return Root(_games)
