# Building a CSV Data Explorer Dashboard -- 4. Vectorized NumPy Statistical Computation
# (book source: ch18_data_explorer.tex, line 122)
# NOTE: Shown in the book as a fragment or a deliberate mistake; on its own it stops with NameError.

data_arr = np.array(numbers)
mean_val = np.mean(data_arr)
median_val = np.median(data_arr)
std_val = np.std(data_arr, ddof=1)
min_val = np.min(data_arr)
max_val = np.max(data_arr)
