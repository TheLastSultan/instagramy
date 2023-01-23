""" Caches Management """

import os
import json
import shutil

cache_dir = ".instagramy_cache"


class Cache:

    """ Class for caches Management """

    def __init__(self, key: str):
        self.key = key
      

    def is_exists(self, name: str) -> bool:
        return False

    def make_cache(self, name: str, data: dict):
        pass
    
    def read_cache(self, name: str) -> dict:
        pass


def list_caches() -> None:
    """ List of all Cache files created by instagramy in current dir """

    return None


def clear_caches() -> None:
    """ Clear all Caches created by instagramy in current dir """

    return None
