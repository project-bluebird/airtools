import json
from os import path

from airtools.geom.coord import Coord
from airtools.geom.sector import Sector


class Airspace:
    """
    Collection of all known fixes and sectors.
    """

    fixes: dict[str, Coord]        # Dictionary of fix positions.
    sectors: dict[str, Sector]     # Dictionary of all sectors.

    def __init__(self, fixes_filepath: path, sectors_filepath: path):
        """
        Load the initial dictionary files of fixes and sectors.
        """

        self.load_fixes(fixes_filepath)
        self.load_sectors(sectors_filepath)

    def load_fixes(self, filepath: path):
        """
        Load additional fix data from a file.
        """

        with open(str(filepath), 'r') as file:
            self.fixes = {**self.fixes, **json.loads(file.read())}

    def load_sectors(self, filepath: path):
        """
        Load additional sector data from a file.
        """

        with open(str(filepath), 'r') as file:
            self.sectors = {**self.sectors, **json.loads(file.read())}

    def keep(self, sectors: list[str], rad: float):
        """
        Prune all sectrols except the given remaing sectors list.
        Also prune all fixes further than a given distance [NM] of the remaing sectors.
        """

        remaining_sectors = {}
        for id in sectors:
            remaining_sectors[id] = self.sectors[id]
        self.sectors = remaining_sectors

        remaining_fixes = {}
        for fix_id, coord in self.fixes.items():
            for sec_id, sector in self.sectors.items():
                if sector.dist(coord) <= rad:
                    remaining_fixes[fix_id] = coord
                continue
        self.fixes = remaining_fixes
