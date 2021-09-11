import json

from airtools.core.id import ID
from airtools.geom.coord import Coord
from airtools.geom.sector import Sector
from airtools.io.json import JsonDecoder


class __World__:
    """
    Collection of all known fixes and sectors.
    """

    def __init__(self, fixes: dict[ID, Coord] = {}, sectors:  dict[ID, Sector] = {}):
        """
        Construct an instance with an initial set of fixes and sectors.
        """

        self.fixes: dict[ID, Coord] = {}
        self.sectors: dict[ID, Sector] = {}

    def load_fixes(self, filepath: str):
        """
        Load additional fix data from a file.
        """

        with open(str(filepath), 'r') as file:
            self.fixes = {**self.fixes, **
                          json.loads(file.read(), cls=JsonDecoder)}

    def load_sectors(self, filepath: str):
        """
        Load additional sector data from a file.
        """

        with open(str(filepath), 'r') as file:
            self.sectors = {**self.sectors, **
                            json.loads(file.read(), cls=JsonDecoder)}

    def keep(self, sectors: list[ID], rad: float):
        """
        Prune all sectrols except the given remaing sectors list.
        Also prune all fixes further than a given distance [NM] of the remaing sectors.
        """

        remaining_sectors = {}
        for id in sectors:
            remaining_sectors[id] = self.sectors[id]
        self.sectors = remaining_sectors

        remaining_fixes = {}
        for id, coord in self.fixes.items():
            for sector in self.sectors.values():
                if sector.dist(coord) <= rad:
                    remaining_fixes[id] = coord
                continue
        self.fixes = remaining_fixes


World = __World__()
