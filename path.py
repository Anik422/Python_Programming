from pathlib import Path
from zipfile import ZipFile
from . import new
import urllib


with ZipFile("file.zip", 'W') as zip:
    for path in Path("new").rglob("*.*"):
        zip.write(path)