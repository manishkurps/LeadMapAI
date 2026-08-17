"""
Business Model

Every business extracted from Google Maps
will be stored inside this object.
"""

from dataclasses import dataclass, asdict


@dataclass
class Business:

    name: str = ""

    category: str = ""

    rating: str = ""

    reviews: str = ""

    address: str = ""

    phone: str = ""

    website: str = ""

    email: str = ""

    maps_link: str = ""

    status: str = ""


    def to_dict(self):
        return asdict(self)