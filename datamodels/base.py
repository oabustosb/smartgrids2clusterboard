import os as _os
from pydantic import BaseModel as _BaseModel
from pymongo.database import Database as _Database
from pymongo.collection import Collection as _Collection
from pymongo import MongoClient as _MongoClient
from numpy import ndarray as _ndarray
from typing import (
        List as _List,
        Optional as _Optional
        )

class EnvironmentVariables(_BaseModel):
    public: str
    mongo_url: str
    mongo_user: str
    mongo_pass: str
    mongo_db: str
    users_collection: str
    selecters_path: str

class Databases(_BaseModel):
    mongo_client: _MongoClient
    mongo_db: _Database
    users_collection: _Collection
    class Config:
        arbitrary_types_allowed = True

class Selecter(_BaseModel):
    text: str
    options: _List[str]

class Selecters(_BaseModel):
    kind: Selecter
    zone: Selecter
    vendor: Selecter

class SelectResults(_BaseModel):
    kind: str
    zone: _Optional[str]
    vendor: _Optional[str]

class Aggregations(_BaseModel):
    mean: _ndarray
    std: _ndarray
    min: _ndarray
    max: _ndarray
    class Config:
        arbitrary_types_allowed = True

