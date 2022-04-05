import pandas as _pd
import re as _re
from pandas import DataFrame as _DataFrame
from typing import (
        List as _List,
        Dict as _Dict
        )
from datamodels import (
        Databases as _Databases,
        SelectResults as _SelectResults
        )
def make_dataframe(
        result: _List[_Dict],
        cluster_field: str
        ) -> _DataFrame:
    df = _pd.DataFrame(result)
    return df.rename(columns={cluster_field: "cluster"})

def get_data(
        select_results: _SelectResults,
        dbs: _Databases
        ) -> _Dict:
    query = {}
    if select_results.kind == "all":
        query["name"] = select_results.kind
    elif select_results.kind == "operador":
        query["name"] = select_results.vendor
    else:
        query["name"] = select_results.zone
    data = dbs.users_collection.find_one(query)
    return data
    
def get_clusters(
        data: _Dict,
        ) -> _List:
    *clusters, = filter(lambda x: _re.match(r"\d+", x) is not None, data)
    return clusters

