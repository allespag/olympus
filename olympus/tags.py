import json
import typing as tp
from enum import StrEnum
from pathlib import Path
from random import choice

from pydantic import BaseModel, Field


class Color(StrEnum):
    MIDNIGHT_GREEN = "#146173"
    AUBURN = "#96332D"
    GOLD_METALLIC = "#CBAE57"
    OLIVE = "#72752D"


class Tag(BaseModel):
    name: str
    audio: str
    content: str
    color: str = Field(default_factory=lambda: choice(list(Color)))


class TagCollection(BaseModel):
    items: dict[str, Tag]

    def __getitem__(self, key: str) -> Tag:
        return self.items[key]

    @classmethod
    def from_json(cls, json_path: Path | str) -> tp.Self:
        if isinstance(json_path, str):
            json_path = Path(json_path)

        with json_path.open("r", encoding="utf-8") as json_file:
            content = json.load(json_file)

        items = {item["name"]: item for item in content}

        return cls(items=items)
