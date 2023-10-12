###
### CS667 Data Science with Python, Homework 5, Jon Organ
###

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
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
print("\n")

# Question 2 ============================================================
print("Question 2:")
fig = plt.figure()

plot = file.groupby(['Political party[11]']).count().plot(kind='pie', y='President', legend=None, 
	title="Political Affiliation of Presidents").get_figure()
plot.set_size_inches(10,10)

plot.legend(loc="upper right")
plot.savefig("results/Q2_PoliticalAffiliation_Pie.png")
print("Pie chart of political affiliation generated...\n")
print("\n")

# Question 3 ============================================================
print("Question 3:")
print("Yes, some presidents switched political parties\n")
print("\n")

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
	plot1.savefig("results/Q4_" + party + "_ReligiousAffiliation.png")
	print("Pie chart of religious affiliation by " + party + " party generated...")

print("\n")

# Question 5 ============================================================
print("\nQuestion 5:")
file_length = len(file.index)
file["age at start"] = ''
file["century"] = ''

i = 0
while i <= file_length:
	if i == 38:
		i += 1
		continue
	holder = file["start of presidency"].get(i)
	cent = file["Years in office"].get(i)[:2]
	file.at[i, "century"] = cent
	
	years = int(holder[:2])
	split1 = holder.split(",")
	days = float(split1[1][1:-5])
	perc = days / 365
	years += perc
	file.at[i, "age at start"] = years

	i += 1


for party in parties:
	if "/" in party:
		continue
	temp = file[file["Political party[11]"] == party]
	fig2, ax2 = plt.subplots()
	ax2.plot(temp["No."], temp["age at start"])
	ax2.set(xlabel='President Number', ylabel='Age at start',
	       title='Start Age of President for ' + party)
	ax2.grid()
	fig2.savefig("results/Q5_Start_Age_" + party + ".png")

	temp17 = file[(file["Political party[11]"] == party) & (file["century"] == "17")]
	temp18 = file[(file["Political party[11]"] == party) & (file["century"] == "18")]
	temp19 = file[(file["Political party[11]"] == party) & (file["century"] == "19")]
	
	if len(temp17.index) == 0:
		print("18th century median age for " + party
		 + " party is N/A (no presidents of this party for this century)")
	else:
		print("18th century median age for " + party + " party is " 
			+ str(round(temp17["age at start"].median(), 2)))
	if len(temp18.index) == 0:
		print("19th century median age for " + party
		 + " party is N/A (no presidents of this party for this century)")
	else:
		print("19th century median age for " + party + " party is " 
			+ str(round(temp18["age at start"].median(), 2)))
	if len(temp19.index) == 0:
		print("20th century median age for " + party
		 + " party is N/A (no presidents of this party for this century)")
	else:
		print("20th century median age for " + party + " party is " 
			+ str(round(temp19["age at start"].median(), 2)))
	print("Line chart of start age by " + party + " party generated...\n")

print("There doesn't appear to be any trends amongst the median age of presidents by century"
	+ "\nand party. This could be due to a relatively small sample size.")


print("\n")

# Question 6 ============================================================
print("\nQuestion 6:")

