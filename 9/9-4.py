import pandas as pd  
series_a = pd.Series([1, 2, 3])
series_b = pd.Series([4, 5, 6])
vertical_stack = pd.concat([series_a, series_b], axis=0)
print("Vertical Stack:\n", vertical_stack)
horizontal_stack = pd.concat([series_a, series_b], axis=1)
print("Horizontal Stack:\n", horizontal_stack)
