import json
import pandas as pd
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--path")
    args = parser.parse_args()
    fname = args.path.split("/")[-1].split(".")[0]

    df = pd.read_parquet(args.path)
    valid = pd.read_csv(args.path.split(".")[0] + ".tsv", sep="\t")
    valid.columns = [fname, "category"]

    if fname == "all":
        df2 = df.copy()
    elif fname in ["area_antioquia", "area_caribe", "area_nordeste", "area_oriental", "area_suroccidental"]:
        df2 = df[df["zona"] == fname].copy()
    else:
        df2 = df[df["operador"] == fname].copy()

    df2 = df2.merge(valid, on=fname)
    df2 = df2[df2["category"] != "Descartado"]
    df2[fname] = df2[fname].astype("str") + " " + df2["category"]
        
    res = {}
    for name, group in df2.groupby(fname):
        cluster = {}
        values = group[map(str, range(24))].values
        cluster["mean"] = values.mean(axis=0).tolist()
        cluster["std"] = values.std(axis=0).tolist()
        cluster["min"] = values.min(axis=0).tolist()
        cluster["max"] = values.max(axis=0).tolist()
        cluster["n_proportion"] = values.shape[0] / df2.shape[0]
        cluster["number"] = values.shape[0]

        for col in ["tipo_usuario", "nivel_tension_estrato", "municipio", "departamento", "altitud", "clima", "zona"]:
            cluster[col] = group[col].value_counts().to_dict()
        res[name] = cluster

    with open(f"data/{fname}.json", "w") as f:
        json.dump(res, f)
