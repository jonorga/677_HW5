###
### CS667 Data Science with Python, Homework 5, Jon Organ
###

import pandas as pd

# Question 1 ============================================================
file = pd.read_csv("US-Presidents.csv")

file = file.drop(file[file.President == "Joe Biden"].index)
file = file.drop(file[file.President == "Donald Trump"].index)
file = file.drop(file[file.President == "Barack Obama"].index)
file = file.drop(file[file.President == "George W. Bush"].index)
file = file.drop(file[file.President == "Bill Clinton"].index)
file = file.drop(file[file.President == "Jimmy Carter"].index)


# Question 2 ============================================================