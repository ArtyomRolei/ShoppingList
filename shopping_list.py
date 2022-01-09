# This is a shopping list program. You press Enter and the first of the planned purchases disappears from the list in
# the console.

# The shopping list itself in string:
payTupleStr = "Milk, cheese, yogurt, sour cream, Tomatoes, cucumbers, Ice cream"


# Removes an extra space at the beginning of the line:
def delete_front_space(some_string):
	if len(some_string) > 0:
		while some_string[0] == " ":
			some_string = some_string[1:]
	return some_string


# For a beautiful print:
def my_pprint(some_tuple):
	t_len = len(some_tuple)
	for i in range(0, t_len):
		if i < t_len-1:
			l_end = ","
		else:
			l_end =""
		print(i, " ", delete_front_space(some_tuple[i]), end=l_end)
		print()


def mainloop():
	pay_tuple = tuple(payTupleStr.split(","))  # Convert to a tuple to save resources (instead of a list)
	max_index = len(pay_tuple)  # The maximum index of the list item to iterate over
	current_index = 0
	while current_index < max_index:
		my_pprint(pay_tuple[current_index:])
		current_index += 1
		input()


if __name__ == "__main__":
	mainloop()
