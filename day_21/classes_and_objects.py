# Day 21: 30 Days of Python Programming

# EXERCISES: LEVEL 1

import statistics

class Statistics:
    def count (arr):
        return len(arr)
    def sum (arr):
        return sum(arr)
    def min (arr):
        return min(arr)
    def max (arr):
        return max(arr)
    def range (arr):
        return max(arr) - min(arr)
    def mean (arr):
        return statistics.mean(arr)
    def median (arr):
        return statistics.median(arr)
    def mode (arr):
        return statistics.mode(arr)
    def stdev (arr):
        return statistics.stdev(arr)
    def variance (arr):
        return statistics.variance(arr)
    def freq_dist (arr):
        return [(arr.count(num), num) for num in set(arr)]

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26] 

print('Count: ', Statistics.count(ages))
print('Sum: ', Statistics.sum(ages))
print('Min: ', Statistics.min(ages))
print('Max: ', Statistics.max(ages))
print('Range: ', Statistics.range(ages))
print('Mean: ', Statistics.mean(ages))
print('Median: ', Statistics.median(ages))
print('Mode: ', Statistics.mode(ages))
print('Standard deviation: ', Statistics.stdev(ages))
print('Variance: ', Statistics.variance(ages))
print('Frequency distribution: ', Statistics.freq_dist(ages))

# EXERCISES: LEVEL 2

class PersonAccount:
    def __init__ (self, first_name='John', last_name='Doe', incomes=[], expenses=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = incomes
        self.expenses = expenses
    def total_income (self):
        incomes = [income['value'] for income in self.incomes]
        return sum(incomes)
    def total_expense (self):
        expenses = [expense['cost'] for expense in self.expenses]
        return sum(expenses)
    def account_info (self):
        return {
            'Name': f'{self.first_name} {self.last_name}',
            'Incomes': self.incomes,
            'Expenses': self.expenses
        }
    def add_income (self, income):
        self.incomes.append(income)
    def add_expense (self, expense):
        self.expenses.append(expense)
    def account_balance (self):
        return self.total_income() - self.total_expense()
    

alex = PersonAccount('Alex', 'Kist')

alex.add_income({
    'value': 10,
    'description': 'etc'
})

alex.add_expense({
    'cost': 5,
    'description': 'etc'
})

print('Total income: ', alex.total_income())
print('Total expenses: ', alex.total_expense())
print('Account info:\n', alex.account_info())
print('Account balance: ', alex.account_balance())