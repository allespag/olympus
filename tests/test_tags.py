import json
from pathlib import Path

import pytest

from olympus.main import STATIC_FOLDER
from olympus.tags import TagCollection


@pytest.fixture
def tags_path() -> Path:
    return STATIC_FOLDER / "data" / "tags.json"


@pytest.fixture
def tags(tags_path: Path) -> TagCollection:
    return TagCollection.from_json(tags_path)


def test_json_exists(tags_path: Path):
    assert tags_path.exists()


def test_tags_duplicate(tags_path: Path, tags: TagCollection):
    with tags_path.open("r", encoding="utf-8") as json_file:
        content = json.load(json_file)

    assert len(content) == len(tags.items)


def test_audio_exists(tags: TagCollection):
    for tag in tags.items.values():
        p = STATIC_FOLDER / "audio" / tag.audio
        assert p.exists()
