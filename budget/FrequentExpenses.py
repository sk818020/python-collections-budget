from budget import Expense
import collections

expenses = Expense.Expenses()

expenses.read_expenses(r'C:\Users\jared\PycharmProjects\python-collections-budget\data\spending_data.csv')

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)

print(top5)
