import dask.dataframe as dd

INPUT_FILE = "measurements.txt"
OUTPUT_FILE = "wyniki.txt"

def main():
    df = dd.read_csv(
        INPUT_FILE,
        sep=";",
        names=["station", "value"],
        dtype={"station": "object", "value": "float64"},
        blocksize="64MB"
    )

    result = df.groupby("station").agg(
        min_value=("value", "min"),
        mean_value=("value", "mean"),
        max_value=("value", "max"),
    )

    result = result.compute().sort_index()

    with open(OUTPUT_FILE, "w") as out:
        for station, row in result.iterrows():
            out.write(f"{station}={row['min_value']:.1f}/{row['mean_value']:.1f}/{row['max_value']:.1f}\n")

    print(f"Wyniki zapisano do {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
