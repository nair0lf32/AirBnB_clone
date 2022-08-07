#!/usr/bin/python3
"""Init module used to create a new instance of FileStorage"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
