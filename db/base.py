from pymongo import MongoClient as _MongoClient
from datamodels import (
        EnvironmentVariables as _EnvironmentVariables,
        Databases as _Databases
        )

def init_databases(
        env_vars: _EnvironmentVariables
        ) -> _Databases:
    client = _MongoClient(
            env_vars.mongo_url.format(
            env_vars.mongo_user,
            env_vars.mongo_pass
            )
        )
    mongo_db = client[env_vars.mongo_db]
    users_collecton = mongo_db[env_vars.users_collection]
    return _Databases(
            mongo_client=client,
            mongo_db=mongo_db,
            users_collection=users_collecton
            )
