###
### CS667 Data Science with Python, Homework 5, Jon Organ
###

import pandas as pd
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None  # default='warn'

file_cmg = pd.read_csv("cmg_weeks.csv")
file_spy = pd.read_csv("spy_weeks.csv")

def CleanPoints(file):
	file = file.drop((file[file.Avg_Return < 0].index) & (file[file.Color == "Green"].index))
	file = file.drop((file[file.Avg_Return > 0].index) & (file[file.Color == "Red"].index))
	return file


clean_cmg = CleanPoints(file_cmg)
clean_spy = CleanPoints(file_spy)


def GeneratePlot(frame, name, year):
	scatter_plot = plt.figure()
	axes1 = scatter_plot.add_subplot(1, 1, 1)
	axes1.scatter(frame["Avg_Return"], frame["Volatility"], color=frame["Color"], s=50)
	axes1.set_title("Average Return vs Volatility for " + name)
	axes1.set_xlabel("Average Return")
	axes1.set_ylabel("Volatility")
	scatter_plot.savefig("linear_results/" + name + "_Avg_Return_V_Volatility_Y" + year + ".png")


year_line_cmg = len(clean_cmg.index) / 2
year_line_spy = len(clean_spy.index) / 2

year_1_cmg = clean_cmg[clean_cmg["Week"] <= year_line_cmg]
year_2_cmg = clean_cmg[clean_cmg["Week"] > year_line_cmg]
year_1_spy = clean_spy[clean_spy["Week"] <= year_line_spy]
year_2_spy = clean_spy[clean_spy["Week"] > year_line_spy]

year_2_cmg.loc[year_2_cmg['Avg_Return'] >= 0, 'Color'] = "Green"
year_2_cmg.loc[year_2_cmg['Avg_Return'] < 0, 'Color'] = "Red"
year_2_spy.loc[year_2_spy['Avg_Return'] >= 0, 'Color'] = "Green"
year_2_spy.loc[year_2_spy['Avg_Return'] < 0, 'Color'] = "Red"

GeneratePlot(year_1_cmg, "CMG", "1")
GeneratePlot(year_2_cmg, "CMG", "2")
GeneratePlot(year_1_spy, "SPY", "1")
GeneratePlot(year_2_spy, "SPY", "2")