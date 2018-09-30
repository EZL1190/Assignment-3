import webget
import csv
import matplotlib.pyplot as plt

#url = ''
#if __name__ == '__main__':
#    url = input("URL to download: ")

#webget.download(url)

filename = 'rows.csv'

# 1start
state1 = ''
deaths1 = 0
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        if int(row[0]) == 2016 and row[1] == 'All Causes':
            if int(row[4]) > deaths1:
                state1 = row[3]
                deaths1 = int(row[4])
print('\n\n')
print('1. Which state has the most deaths in the year of 2016? (All causes)? ')
print(state1 + ' : ' + str(deaths1))
# 1 end

# 2 start
state2 = ''
deaths2 = 0
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        if int(row[0]) == 2016 and row[1] == 'All Causes':
            if int(row[4]) < deaths2 or deaths2 == 0:
                    state2 = row[3]
                    deaths2 = int(row[4])

print('\n\n')
print('2. Which state has the least deaths in the year of 2016? (All causes)? ')
print(state2 + ' : ' + str(deaths2))
#2 end

# 3 start
state3 = ''
difference3 = 0

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        deaths_1999 = 0
        deaths_2016 = 0
        
        if int(row[0]) == 1999 and row[1] == 'All Causes':
            deaths_1999 = float(row[5])
        elif int(row[0]) == 2016 and row[1] == 'All Causes':
            deaths_2016 = float(row[5])
            if deaths_2016 - deaths_1999 < difference3 or state3 == '':
                difference3 = deaths_2016 - deaths_1999
                state3 = row[3]
print('\n\n')
print('3. Which state has had the smallest increase in deaths from 1999-2016? (All causes)? ')
print(state3 + ' : ' + str(difference3))
# 3 end

# 4 start
state4 = ''
deaths4 = 0
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        if int(row[0]) == 2005 and row[2] == 'Kidney disease':
            if int(row[4]) > deaths4 :
                    state4 = row[3]
                    deaths4 = int(row[4])

print('\n\n')
print('4. Which state has the most deaths caused by kidney disease in the year of 2005? ')
print(state4 + ' : ' + str(deaths4))
# 4 end

# 5 start

state5 = ''
difference5 = 0
deaths5 = []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        deaths_1999 = 0
        deaths_2016 = 0
        
        if int(row[0]) == 1999 and row[2] == "Alzheimer's disease":
            deaths_1999 = float(row[5])
        elif int(row[0]) == 2016 and row[2] == "Alzheimer's disease":
            deaths_2016 = float(row[5])
            if deaths_2016 - deaths_1999 > difference5 or state5 == '':
                differenc5e = deaths_2016 - deaths_1999
                state5 = row[3]

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        if row[3] == state5 and row[2] == "Alzheimer's disease":
            deaths5.append(row[4])

print('\n\n')
print('5. Which state has had the biggest increase in the death of Alzheimers from 1999-2016? Plot the increase year for year using matplotlib ')
print(deaths5)

plt.plot(deaths5, linewidth=20)
# Set chart title and label axes. 
plt.title("increase in the death", fontsize=24)
plt.xlabel("Years", fontsize=14)
plt.ylabel("Deaths", fontsize=14)
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.locator_params(nbins=36)
plt.show()



# 5 end
