import matplotlib.pyplot as _plt
import numpy as _np
from typing import (
        List as _List,
        Dict as _Dict
        )
from matplotlib.pyplot import (
        Figure as _Figure,
        Axes as _Axes
        )
from pandas import DataFrame as _DataFrame
from datamodels import (
        Aggregations as _Aggregations
        )

_plt.style.use("ggplot")

def base_fig(f):
    fig, ax = _plt.subplots(1, 1)
    def generate_fig(*args):
        ax.clear()
        f(*args, ax=ax)
        return fig
    return generate_fig

@base_fig
def hour_consumption(
        data: _Dict,
        selected_cluster: int,
        lines: _List[str],
        ax: _Axes
        ) -> _Figure:
    colors = {
            "std": "#83A59755",
            "mean": "#448488",
            "min": "#272727",
            "max": "#989719"
            }
    cluster = data[selected_cluster]

    for l in lines:
        if l == "std":
            low_cint = _np.array(cluster["mean"]) - _np.array(cluster["std"])
            low_cint[low_cint < 0] = 0

            ax.fill_between(
                    _np.arange(24),
                    low_cint,
                    _np.array(cluster["mean"]) + _np.array(cluster["std"]),
                    color=colors[l],
                    label=l
                    )
        else:
            ax.plot(
                    _np.arange(24), cluster[l],
                    color=colors[l], label=l
                    )
    ax.set_xticks(_np.arange(24))
    ax.set_xlabel("Hora")
    ax.set_ylabel("Energía normalizada")
    ax.set_title("Estadisticos descriptivos")
    ax.set_xlim([0, 23])
    ax.legend()

@base_fig
def field_hist(
        data: _Dict,
        selected_cluster: int,
        selected_field: str,
        ax: _Axes
        ) -> _Figure:
    values = data[selected_cluster][selected_field]
    ax.bar(values.keys(), values.values())
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)
    ax.set_ylabel("Número de usuarios")
    ax.set_title("Conteos por categoría")

@base_fig
def n_pie(
        data: _Dict,
        selected_cluster: int,
        ax: _Axes
        ) -> _Figure:
    values = data[selected_cluster]
    proportion = values["n_proportion"]
    ax.pie(
            [proportion, 1 - proportion],
            labels=[selected_cluster, "otros"],
            explode=[0.1, 0.0],
            shadow=True, autopct="%1.1f%%"
            )
    ax.set_title(f"Número de usuarios {values['number']}")
