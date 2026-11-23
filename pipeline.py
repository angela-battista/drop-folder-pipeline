from pathlib import Path
import pandas as pd
import shutil

DROP = Path("drop")
REJECTED = Path("rejected")

EXPECTED_COLUMNS = {
    "customers": ["customer_id", "customer_name", "email_domain", "signup_date", "region"],
    "orders": ["order_id", "customer_id", "order_date", "order_status"],
    "order_items": ["order_item_id", "order_id", "product_name", "category", "quantity", "unit_price"],
    "returns": ["return_id", "order_id", "return_date", "return_type", "return_reason_desc", "refund_amount"],
}


def validate(df, table_name):
    problems = []
    if table_name not in EXPECTED_COLUMNS:
        problems.append("unknown file name")
        return problems
    if df.empty:
        problems.append("file has no rows")
    missing = [c for c in EXPECTED_COLUMNS[table_name] if c not in df.columns]
    if missing:
        problems.append(f"missing columns: {missing}")
    return problems


for file in DROP.glob("*.csv"):
    df = pd.read_csv(file)
    problems = validate(df, file.stem)
    if problems:
        print(file.name, "FAILED:", problems)
        shutil.move(str(file), REJECTED / file.name)
        (REJECTED / file.stem + ".reason.txt").write_text("\n".join(problems))
