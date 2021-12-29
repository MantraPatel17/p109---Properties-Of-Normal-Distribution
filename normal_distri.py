import csv
import statistics
import pandas as pd

reader = pd.read_csv("StudentsPerformance.csv")


data = reader["reading score"].tolist()


b = len(data)


mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)
std_dev = statistics.stdev(data)



std1start = mean-std_dev
std1end = mean+std_dev

std2start = mean-(2 * std_dev)
std2end = mean+(2 * std_dev)

std3start = mean-(3 * std_dev)
std3end = mean+(3 * std_dev)




list_of_data_within_1_std_deviation_W = [
    result for result in data if result > std1start and result < std1end]

list_of_data_within_2_std_deviation_W = [
    result for result in data if result > std2start and result < std2end]

list_of_data_within_3_std_deviation_W = [
    result for result in data if result > std3start and result < std3end]

a1 = len(list_of_data_within_1_std_deviation_W)
a2 = len(list_of_data_within_2_std_deviation_W)
a3 = len(list_of_data_within_3_std_deviation_W)

percentage1 = (a1*100)/b
percentage2 = (a2*100)/b
percentage3 = (a3*100)/b

print("Mean: ",mean)
print("____________________________________________________________________|")
print("Mode: ",mode)
print("____________________________________________________________________|")
print("Median: ",median)
print("____________________________________________________________________|")
print("Percentage: of data lies within 1 standard deviation : ", percentage1)
print("____________________________________________________________________|")
print("Percentage: of data lies within 2 standard deviation : ", percentage2)
print("____________________________________________________________________|")
print("Percentage: of data lies within 3 standard deviation : ", percentage3)


