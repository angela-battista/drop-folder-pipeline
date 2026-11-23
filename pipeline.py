from pathlib import Path
import pandas as pd

DROP = Path("drop")

for file in DROP.glob("*.csv"):
    df = pd.read_csv(file)
    print(file.name, len(df), "rows")
