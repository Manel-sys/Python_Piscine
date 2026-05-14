from importlib import import_module
from importlib import metadata


def check_package(name: str, description: str) -> bool:
    try:
        import_module(name)
        version = metadata.version(name)
        print(f"[OK] {name} ({version}) - {description} ready")
        return True
    except (ImportError, metadata.PackageNotFoundError):
        print(f"[MISSING] {name} - {description} not ready")
        return False


def main() -> None:
    print("LOADING STATUS: Loading program...\n")
    print("Cheking dependencies:")

    dependencies: list[bool] = [
        check_package("pandas", "Data manipulation"),
        check_package("numpy", "Numerical computation"),
        check_package("requests", "Network access"),
        check_package("matplotlib", "Visualization")
        ]

    if not all(dependencies):
        print("Missing dependencies found!\n")
        print("To install dependencies using pip, run:")
        print("pip install -r requirements.txt")
        print("python3 loading.py\n")

        print("To install dependencies using Poetry, run:")
        print("poetry install")
        print("poetry run python loading.py")
        return

    import pandas as pd  # type: ignore
    import numpy as np  # type: ignore

    print("\nAnalyzing Matrix Data")
    date: str = "2026-05-13"
    data: pd.DataFrame = fetch_matrix_data(date)
    if data.empty:
        return

    processed: np.ndarray = process_data(data)

    time: pd.Index = data.index
    visualize_data(time, processed, date)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")




def fetch_matrix_data(date: str) -> "pd.DataFrame":  # type: ignore # noqa
    import pandas as pd  # type: ignore
    import requests  # type: ignore
    try:

        url: str = (
            "https://servicebus.ren.pt/datahubapi/electricity/"
            f"ElectricityProductionBreakdownDaily?culture=en-US&date={date}"
            )
        response: requests.Response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        series = data["series"]

        df = pd.DataFrame({item["name"]: item["data"] for item in series})
        df["time"] = data["xAxis"]["categories"]
        df = df.set_index("time")
        return df

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch REN data: {e}")
        df = pd.DataFrame()
        return df


def process_data(data: "pd.DataFrame") -> "np.ndarray":  # type: ignore # noqa
    import pandas as pd  # type: ignore # noqa
    import numpy as np  # type: ignore

    print(f"Processing {len(data)} data points")

    renewables: list[str] = ["Hydro", "Solar", "Wind", "Biomass", "Wave"]
    renewable_df: pd.DataFrame = data[renewables]
    renewable_values: np.ndarray = renewable_df.to_numpy()
    total_renewable: np.ndarray = np.sum(renewable_values, axis=1)

    return total_renewable


def visualize_data(time: "pd.Series", values: "np.ndarray", date: str) -> None:  # type: ignore # noqa
    print("Generating visualization\n")

    import matplotlib.pyplot as plt  # type: ignore

    plt.plot(time, values)
    plt.title(f"Total Renewable Energy Production on {date}")
    plt.xlabel("Time")
    plt.ylabel("MW")

    plt.xticks(time[::8], rotation=45)
    plt.tight_layout()

    plt.savefig("matrix_analysis.png")


if __name__ == "__main__":
    main()
