"""
The program will calculate how much money the user can spend every day till the end of month,
depending on how much money he/she has.
The program will ask this in lei and forint and return the result in forint.
"""
from calendar import monthrange
from datetime import date

EXCHANGE_RATE = 71.4

# ask for input and check if it's a valid integer and store it
forint = ""
while forint == "":
	forint = input("How much forints do you have?")
	if not forint.isdigit() or not int(forint) >= 0:
		print("You must enter a positive integer or 0.")
		forint = ""
	else:
		forint = int(forint)

# ask for input and check if it's a valid integer and store it
lei = ""
while lei == "":
	lei = input("How much lei do you have?")
	if not lei.isdigit() or not int(lei) >= 0:
		print("You must enter a positive integer or 0.")
		lei = ""
	else:
		lei = int(lei)

# calculate how many days are left from the current month
today_string = str(date.today())
date_items_string = today_string.split("-")
date_items_int = []
for i in date_items_string:
	date_items_int.append(int(i))

month_tuple = monthrange(date_items_int[0], date_items_int[1])
length_of_month = month_tuple[1]

days_left_from_month = length_of_month - date_items_int[2]


# exchanges the lei into forint
def exchange_ron_to_huf(amount):
	return amount * EXCHANGE_RATE


# calculate the daily amount of spendable money for this month
def calc_money_per_day_real(huf, ron):
	huf2 = exchange_ron_to_huf(ron)
	return (huf + huf2) / (days_left_from_month + 1)


# calculate the daily amount of spendable money
# for this month and the first week of the next
def calc_money_per_day_safe(huf, ron,):
	huf2 = exchange_ron_to_huf(ron)
	return (huf + huf2) / (days_left_from_month + 8)

result = calc_money_per_day_real(forint, lei)
safe_result = calc_money_per_day_safe(forint, lei)
print("There are %d days till the end of the month (including today)." % (days_left_from_month + 1))
print("Your money is enough to spend %d forint every day." % result)
print("If you want your money last one week longer you should spend %d forint a day." % safe_result)
