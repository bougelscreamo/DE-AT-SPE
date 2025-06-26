# 1.
+ Inefficient Memory Utilization (pd.read_csv)
+ Lack of Incremental (Chunked) Processing
+ Unnecessary Data Loading
+ Late Filtering and Aggregation
+ Lack of Parallel or Distributed Processing

# 2.
```
import dask.dataframe as dd

df = dd.read_csv('large_file.csv', usecols=['price', 'category'])
filtered = df[df['price'] > 100]
result = filtered.groupby('category')['price'].sum().compute()
result.to_csv('output.csv')
```
