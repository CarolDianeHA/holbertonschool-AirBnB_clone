#!/usr/bin/python3
"""Init file to create a python package."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
