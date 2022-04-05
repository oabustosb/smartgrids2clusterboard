import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from auth import session
from auth.password import with_password, validate_access

from utils import get_envvars
from components.select_tools import (
        make_selecters, load_selecters, make_cluster_selecter,
        make_selecter_line, make_field_selecter
        )
from components.statics import page_desc, fig_desc, bar_desc
from components.download import download_csv
from visualize.figs import hour_consumption, field_hist, n_pie
from db.read import get_data, get_clusters
from db.base import init_databases

session_state = session.get(
        password=False
        )
env_vars = get_envvars()
dbs = init_databases(env_vars)

@with_password(session_state)
def main():
    selecters = load_selecters(env_vars)
    select_results = make_selecters(selecters)
    if not validate_access(select_results, session_state):
        st.write("Acceso denegado")
        return

    data = get_data(select_results, dbs)
    clusters = get_clusters(data)
    selected_cluster = make_cluster_selecter(clusters)

    cluster = data[selected_cluster]
    df = pd.DataFrame({metric: data for metric, data in cluster.items() if metric in ["mean", "std", "min", "max"]})
    page_desc()
    st.write(df)
    download_csv(df)
    fig_desc()
    lines = make_selecter_line()
    fig = hour_consumption(data, selected_cluster, lines)
    st.pyplot(fig)

    bar_desc()
    selected_field = make_field_selecter(data, selected_cluster)
    fig = field_hist(data, selected_cluster, selected_field)
    st.pyplot(fig)

    fig = n_pie(data, selected_cluster)
    st.pyplot(fig)

if __name__ == '__main__':
    main()
