import os as _os
from datamodels import EnvironmentVariables as _EnvironmentVariables

def get_envvars() -> _EnvironmentVariables:
    return _EnvironmentVariables(
            public = _os.environ["PUBLIC"],
            mongo_url = _os.environ["MONGO_URL"],
            mongo_user = _os.environ["MONGO_USER"],
            mongo_pass = _os.environ["MONGO_PASS"],
            mongo_db = _os.environ["MONGO_DB"],
            users_collection = _os.environ["USERS_COLLECTION"],
            selecters_path = _os.environ["SELECTERS_PATH"]
            )
