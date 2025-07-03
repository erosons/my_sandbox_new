import pandas as pd
import numpy as np
from pathlib import Path

y = np.array(np.arange(8))
print(y)

# convert to Tabular data
x = pd.read_csv(Path("data.csv"))
print(x)
