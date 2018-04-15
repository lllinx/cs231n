import pandas as pd
import quandl
import sklearn

df = quandl.get("WIKI/GOOGL")
df.head()