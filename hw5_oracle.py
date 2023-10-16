###
### CS667 Data Science with Python, Homework 5, Jon Organ
###

# TODO: Get CMG and SPY files
import pandas as pd
import matplotlib.pyplot as plt

generate_all = False

file_cmg = pd.read_csv("cmg_weeks.csv")
file_spy = pd.read_csv("spy_weeks.csv")


# Question 1.1 =================================================================================================
# TODO: For each of the five years
	# TODO: Compute mean and standard deviation for all weeks, negative weeks, and non negative weeks
def Q11ComputeData(file):
	data = [[], [], [], [], []]
	year = 0
	while year < 5:
		data[year] = [["Week 1", "Week 2", "Week 3", "Week 4"]]
		temp1 = file[(file["Week_of_Month"] == 1) & (file["Week"] >= year * 50) & (file["Week"] < (year + 1) * 50)]
		temp2 = file[(file["Week_of_Month"] == 2) & (file["Week"] >= year * 50) & (file["Week"] < (year + 1) * 50)]
		temp3 = file[(file["Week_of_Month"] == 3) & (file["Week"] >= year * 50) & (file["Week"] < (year + 1) * 50)]
		temp4 = file[(file["Week_of_Month"] == 4) & (file["Week"] >= year * 50) & (file["Week"] < (year + 1) * 50)]

		temp = [temp1["Avg_Return"].mean(), temp2["Avg_Return"].mean(), temp3["Avg_Return"].mean(), 
			temp4["Avg_Return"].mean()]
		data[year].append(temp)
		temp = [temp1["Volatility"].mean(), temp2["Volatility"].mean(), temp3["Volatility"].mean(), 
			temp4["Volatility"].mean()]
		data[year].append(temp)

		temp = [len(temp1[temp1["Avg_Return"] < 0].index), len(temp2[temp2["Avg_Return"] < 0].index), 
			len(temp3[temp3["Avg_Return"] < 0].index), len(temp4[temp4["Avg_Return"] < 0].index)]
		data[year].append(temp)
		temp = [temp1["Avg_Return"][temp1["Avg_Return"] < 0].mean(),
			temp2["Avg_Return"][temp2["Avg_Return"] < 0].mean(),
			temp3["Avg_Return"][temp3["Avg_Return"] < 0].mean(),
			temp4["Avg_Return"][temp4["Avg_Return"] < 0].mean()]
		data[year].append(temp)
		temp = [temp1["Volatility"][temp1["Avg_Return"] < 0].mean(),
			temp2["Volatility"][temp2["Avg_Return"] < 0].mean(),
			temp3["Volatility"][temp3["Avg_Return"] < 0].mean(),
			temp4["Volatility"][temp4["Avg_Return"] < 0].mean()]
		data[year].append(temp)

		temp = [len(temp1[temp1["Avg_Return"] >= 0].index), len(temp2[temp2["Avg_Return"] >= 0].index), 
			len(temp3[temp3["Avg_Return"] >= 0].index), len(temp4[temp4["Avg_Return"] >= 0].index)]
		data[year].append(temp)
		temp = [temp1["Avg_Return"][temp1["Avg_Return"] >= 0].mean(),
			temp2["Avg_Return"][temp2["Avg_Return"] >= 0].mean(),
			temp3["Avg_Return"][temp3["Avg_Return"] >= 0].mean(),
			temp4["Avg_Return"][temp4["Avg_Return"] >= 0].mean()]
		data[year].append(temp)
		temp = [temp1["Volatility"][temp1["Avg_Return"] >= 0].mean(),
			temp2["Volatility"][temp2["Avg_Return"] >= 0].mean(),
			temp3["Volatility"][temp3["Avg_Return"] >= 0].mean(),
			temp4["Volatility"][temp4["Avg_Return"] >= 0].mean()]
		data[year].append(temp)
		
		year += 1

	return data

Q11_cmg_data = Q11ComputeData(file_cmg)
Q11_spy_data = Q11ComputeData(file_spy)

# Question 1.2 =================================================================================================
# TODO: take data from question 1.1 and generate tables for each year
print("Question 1.2:")
def Q12generateTable(data, name, year, q):
	data = zip(*data)
	df = pd.DataFrame(data, columns=[name, 'R Average Return', 'R Standard Deviation', '-R Total',
	 '-R Average Return', '-R Standard Deviation', '+R Total', '+R Average Return', '+R Standard Deviation'])
	fig, ax = plt.subplots()
	fig.patch.set_visible(False)
	ax.axis('off')
	ax.axis('tight')
	ax.table(cellText=df.values, colLabels=df.columns, loc='center').set_fontsize(18)

	print("Saving", name, "Y", year, "Table...")
	fig.savefig("oracle_results/Q" + q + "_" + name + "_Y" + year + "_Table.png", dpi=1200)

i = 0
if generate_all:
	while i < 5:	
		Q12generateTable(Q11_cmg_data[i], "CMG", str(i + 1), "1.2")
		Q12generateTable(Q11_spy_data[i], "SPY", str(i + 1), "1.2")
		i += 1
else:
	print("Generate tables set to false...\n")
	

# Question 1.3 =================================================================================================
# TODO: Are there more weeks with negative or non-negative returns in total?
print("Question 1.3:")
if file_cmg["Week"][file_cmg["Avg_Return"] >= 0].count() > file_cmg["Week"][file_cmg["Avg_Return"] < 0].count():
	print("There are more non-negative weeks than negative weeks for CMG")
else:
	print("There are more negative weeks than non-negative weeks for CMG")
if file_spy["Week"][file_spy["Avg_Return"] >= 0].count() > file_spy["Week"][file_spy["Avg_Return"] < 0].count():
	print("There are more non-negative weeks than negative weeks for SPY")
else:
	print("There are more negative weeks than non-negative weeks for SPY")

# Question 1.4 =================================================================================================
# TODO: Is the absolute value of the average returns greater for negative or non-negative returns?
print("\nQuestion 1.4:")
print("There seems to be large fluctuation from year to year and week to week in terms of average return"
	+ "\nThere doesn't seem to be a clear pattern of whether CMG loses more than it gains")

print("\nQuestion 1.5:")
print("No. These results change frequently and don't seem to depend on the week of the month")

# Question 2 =================================================================================================
# TODO: Answers from analyzing tables
print("\nQuestion 2.1:")
print("There doesn't seem to be any consistancy across weeks of the month, no obvious patterns emerge.\n")

print("\nQuestion 2.2:")
print("In addition to a lack of patttern within a given year, there doesn't seem to be a pattern from "
	+ "year to year\n")

print("\nQuestion 2.3:")
print("Year 1 best week: week 4, worst week: week 1")
print("Year 2 best week: week 1, worst week: week 3")
print("Year 3 best week: week 3, worst week: week 1")
print("Year 4 best week: week 4, worst week: week 2")
print("Year 5 best week: week 1, worst week: week 2\n")

print("\nQuestion 2.4:")
print("Yes, these weeks change year to year, the only notable thing is week 4 is never the worst and"
	+ " week 2 is never the best\n")

# Question 3 =================================================================================================
# TODO: Compute aggregate table across all 5 years for both stocks
def Q3ComputeData(file):
	data = [["Week 1", "Week 2", "Week 3", "Week 4"]]
	temp1 = file[file["Week_of_Month"] == 1]
	temp2 = file[file["Week_of_Month"] == 2]
	temp3 = file[file["Week_of_Month"] == 3]
	temp4 = file[file["Week_of_Month"] == 4]

	temp = [temp1["Avg_Return"].mean(), temp2["Avg_Return"].mean(), temp3["Avg_Return"].mean(), 
		temp4["Avg_Return"].mean()]
	data.append(temp)
	temp = [temp1["Volatility"].mean(), temp2["Volatility"].mean(), temp3["Volatility"].mean(), 
		temp4["Volatility"].mean()]
	data.append(temp)

	temp = [len(temp1[temp1["Avg_Return"] < 0].index), len(temp2[temp2["Avg_Return"] < 0].index), 
		len(temp3[temp3["Avg_Return"] < 0].index), len(temp4[temp4["Avg_Return"] < 0].index)]
	data.append(temp)
	temp = [temp1["Avg_Return"][temp1["Avg_Return"] < 0].mean(),
		temp2["Avg_Return"][temp2["Avg_Return"] < 0].mean(),
		temp3["Avg_Return"][temp3["Avg_Return"] < 0].mean(),
		temp4["Avg_Return"][temp4["Avg_Return"] < 0].mean()]
	data.append(temp)
	temp = [temp1["Volatility"][temp1["Avg_Return"] < 0].mean(),
		temp2["Volatility"][temp2["Avg_Return"] < 0].mean(),
		temp3["Volatility"][temp3["Avg_Return"] < 0].mean(),
		temp4["Volatility"][temp4["Avg_Return"] < 0].mean()]
	data.append(temp)

	temp = [len(temp1[temp1["Avg_Return"] >= 0].index), len(temp2[temp2["Avg_Return"] >= 0].index), 
		len(temp3[temp3["Avg_Return"] >= 0].index), len(temp4[temp4["Avg_Return"] >= 0].index)]
	data.append(temp)
	temp = [temp1["Avg_Return"][temp1["Avg_Return"] >= 0].mean(),
		temp2["Avg_Return"][temp2["Avg_Return"] >= 0].mean(),
		temp3["Avg_Return"][temp3["Avg_Return"] >= 0].mean(),
		temp4["Avg_Return"][temp4["Avg_Return"] >= 0].mean()]
	data.append(temp)
	temp = [temp1["Volatility"][temp1["Avg_Return"] >= 0].mean(),
		temp2["Volatility"][temp2["Avg_Return"] >= 0].mean(),
		temp3["Volatility"][temp3["Avg_Return"] >= 0].mean(),
		temp4["Volatility"][temp4["Avg_Return"] >= 0].mean()]
	data.append(temp)

	return data
print("\nQuestion 3:")
cmg_q3_data = Q3ComputeData(file_cmg)
spy_q3_data = Q3ComputeData(file_spy)
if generate_all:
	Q12generateTable(cmg_q3_data, "CMG", "1-5", "3")
	Q12generateTable(spy_q3_data, "SPY", "1-5", "3")
else:
	print("Generate tables set to false...\n")

# Question 3.1 =================================================================================================
# TODO: What are the best and worst weeks from tables generated in last question
print("\nQuestion 3.1:")
print("CMG aggregate best week: week 1, worst week: week 4")
print("SPY aggregate best week: week 1, worst week: week 3\n")

# Question 3.2 =================================================================================================
# TODO: Are these the same weeks for both stocks?
print("\nQuestion 3.2:")
print("CMG and SPY had the same best week, but different worst weeks.\n")


# Question 3.3 =================================================================================================
# TODO: For each of the weeks in your original weeks file, how many were outside the standard deviation?
	# See PDF for equation
print("\nQuestion 3.3:")

def Q33GetData(file):
	file_length = len(file.index)
	file_median = file["Avg_Return"].mean()
	file_std = file["Avg_Return"].std()
	count = 0
	i = 0
	while i <= file_length:
		temp = file["Avg_Return"].get(i)
		try:
			if temp < file_median - (2 * file_std) or temp > file_median + (2 * file_std):
				count += 1
		except:
			do_nothing = True
		i += 1
	outside = count / file_length
	if outside < 0.05:
		print(str(round(outside*100,2)) + "% of the weeks are outside of the specified range, "
			+ "this is consistant with the normality of returns")
	else:
		print(str(round(outside*100,2)) + "% of the weeks are outside of the specified range, "
			+ "this is inconsistant with the normality of returns")

Q33GetData(file_cmg)
Q33GetData(file_spy)
print("")


# Question 4.1 =================================================================================================
# TODO: You trade each week perfectly with CMG, starting with $100, how much do you make after 5 years?
print("\nQuestion 4.1:")

def Q412(file):
	balance = 100
	file_length = len(file.index)
	i = 0
	while i < file_length - 1:
		today_stock = balance / file["Close"].get(i)
		tmr_stock = balance / file["Close"].get(i + 1)
		difference = abs(today_stock - tmr_stock)
		balance += difference * file["Close"].get(i + 1)
		i += 1
	return str(round(balance, 2))

og_cmg = pd.read_csv("cmg_with_color.csv")
bal_cmg = Q412(og_cmg)
print("Starting with $100 on the first day, CMG will have $" + bal_cmg + " on the last day\n")

# Question 4.2 =================================================================================================
# TODO: Same as 4.1 except for SPY
print("\nQuestion 4.2:")

og_spy = pd.read_csv("spy_with_color.csv")
bal_spy = Q412(og_spy)
print("Starting with $100 on the first day, SPY will have $" + bal_spy + " on the last day\n")

# Question 4.3 =================================================================================================
# TODO: How long would it take for your stock and SPY to make $176 starting from $100
print("\nQuestion 4.3:")
def Q43(file):
	balance = 100
	end = -1
	file_length = len(file.index)
	i = 0
	while i < file_length - 1:

		today_stock = balance / file["Close"].get(i)
		tmr_stock = balance / file["Close"].get(i + 1)
		difference = abs(today_stock - tmr_stock)
		balance += difference * file["Close"].get(i + 1)
		if balance > 176:
			end = i
			i = file_length
		i += 1
	return str(end)
print("Starting with $100, CMG will reach $176 by day " + Q43(og_cmg))
print("Starting with $100, SPY will reach $176 by day " + Q43(og_spy) + "\n")


# Question 5.1 =================================================================================================
# TODO: for both stocks, how much will you make with buy and hold?
print("\nQuestion 5.1")


# Question 5.2 =================================================================================================
# TODO: How does the results of 5.1 compare to 4


# Question 5.3 =================================================================================================
# TODO: Buy and hold except you put it into cash at end of may, and back into stock on last day of august
	# Summarize in table, see PDF


# Question 5.4 =================================================================================================
# TODO: Both stocks, buy and hold 12 times, except each time, for one month of the year, sell on the first trading
# day of that month, and buy on the last trading day of that month
	# Summarize in table, see PDF


# Question 6 =================================================================================================
# TODO: For both stocks trade each week with the oracle
# Generate random number r between 0 and 1, if p >= r, the oracle predicts true value, otherwise opposite
# Generate table doing this ten times for p = 0 to 1 with 0.1 steps


# Question 6.1 =================================================================================================
# TODO: What value of p equals buy and hold results?


# Question 6.2 =================================================================================================
# TODO: Any patterns in table from question 6?


# Question 7.1 =================================================================================================
# TODO: Compute table from question


