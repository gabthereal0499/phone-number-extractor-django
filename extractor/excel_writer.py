import pandas as pd
import os

def save_to_excel(numbers, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.DataFrame(numbers, columns=["Phone Number"])
    df.to_excel(output_path, index=False)
