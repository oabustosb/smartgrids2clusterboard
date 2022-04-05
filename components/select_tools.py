import os as _os
import json as _json
import streamlit as _st
from datamodels import (
        Selecter as _Selecter,
        Selecters as _Selecters, 
        SelectResults as _SelectResults,
        EnvironmentVariables as _EnvironmentVariables
        )
from typing import (
        List as _List,
        Dict as _Dict
        )

def load_selecters(
        env_vars: _EnvironmentVariables
        ) -> _Selecters:
    with open(env_vars.selecters_path) as f:
        data = _json.load(f)

    return _Selecters(
            kind=_Selecter(
                **data["kind"]
                ),
            zone=_Selecter(
                **data["zone"]
                ),
            vendor=_Selecter(
                **data["vendor"]
                )
            )

def make_selecter(
        selecter: _Selecter
        ) -> str:
    button = _st.sidebar.selectbox(
            selecter.text,
            selecter.options
            )
    return button

def make_selecter_line() -> _List[str]:
    return _st.multiselect(
            "",
            options=["mean", "std", "min", "max"],
            default=["mean", "std"]
            )

def make_selecters(
        selecters: _Selecters
        ) -> _SelectResults:
    kind = make_selecter(selecters.kind)
    if kind == "zona":
        zone = make_selecter(selecters.zone)
    else:
        zone = None
    if kind == "operador":
        vendor = make_selecter(selecters.vendor)
    else:
        vendor = None

    return _SelectResults(
            kind=kind,
            zone=zone,
            vendor=vendor
            )

def make_cluster_selecter(
        clusters: _List
        ):
    cluster = _st.sidebar.selectbox("Cluster:", clusters)
    return cluster

def make_field_selecter(
        data: _Dict,
        selected_cluster: int
        ):
    cluster = data[selected_cluster]
    *keys, = filter(lambda x: x not in ["mean", "std", "min", "max", "number", "n_proportion"], cluster.keys())
    field = _st.selectbox("Campo:", keys)
    return field
    
