import json

from airtools.geom.coord import Coord


class JsonEncoder(json.JSONEncoder):
    """
    JSON encoding wrapper.
    """

    def default(self, obj):
        """
        If the given object implements an as_json method, return that JSON.
        Alternatively, attempt to return the default encoding (if it exists).
        """

        if hasattr(obj, "as_json"):
            return obj.as_json()
        else:
            return json.JSONEncoder.default(self, obj)


class JsonDecoder(json.JSONDecoder):
    """
    JSON decoding wrapper.
    """

    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(
            self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        if "lat" in dct:
            if "long" in dct:
                if len(dct) == 2:
                    return Coord(dct["lat"], dct["long"])
        return dct
