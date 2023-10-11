###
### CS667 Data Science with Python, Homework 5, Jon Organ
###

import pandas as pd
import matplotlib.pyplot as plt

# Question 1 ============================================================
print("Question 1:")
file = pd.read_csv("US-Presidents.csv")

file = file.drop(file[file.President == "Joe Biden"].index)
file = file.drop(file[file.President == "Donald Trump"].index)
file = file.drop(file[file.President == "Barack Obama"].index)
file = file.drop(file[file.President == "George W. Bush"].index)
file = file.drop(file[file.President == "Bill Clinton"].index)
file = file.drop(file[file.President == "Jimmy Carter"].index)
print("CSV loaded into frame and living presidents removed...\n")


# Question 2 ============================================================
print("Question 2:")
fig = plt.figure()

plot = file.groupby(['Political party[11]']).count().plot(kind='pie', y='President', legend=None, 
	title="Political Affiliation of Presidents").get_figure()
plot.set_size_inches(10,10)

plot.legend(loc="upper right")
plot.savefig("Q2_PoliticalAffiliation_Pie.png")
print("Pie chart of political affiliation generated...\n")


# Question 3 ============================================================
print("Question 3:")
print("Yes, some presidents switched political parties\n")


# Question 4 ============================================================
print("Question 4:")
parties = [x for x in file["Political party[11]"].unique()]
for party in parties:
	if "/" in party:
		continue
	temp = file[file["Political party[11]"] == party]


	fig1 = plt.figure()

	plot1 = temp.groupby(['Religion(s)']).count().plot(kind='pie', y='Political party[11]', legend=None,
		title="Religious Affiliation by " + party + " Party").get_figure()
	plot1.set_size_inches(10,10)

	plot1.legend(loc="upper right")
	plot1.savefig("Q4_" + party + "_ReligiousAffiliation.png")
	print("Pie chart of religious affiliation by " + party + " party generated...\n")



