import streamlit as st

# Streamlit UI elements
st.title("Lists")

# Code snippet 1: Manipulating a List
st.header("Manipulating a List")

# Let's create an empty list
my_list = []

# Let's add some values
my_list.append('Python')
my_list.append('is ok')
my_list.append('sometimes')

# Let's remove 'sometimes'
my_list.remove('sometimes')

# Let's change the second item
my_list[1] = 'is neat'

# Display the modified list
st.write("Modified List:", my_list)

# Verify that it's correct
assert my_list == ['Python', 'is neat']

# Code snippet 2: Creating a New List
st.header("Creating a New List")

original = ['I', 'am', 'learning', 'hacking', 'in']

# Your implementation here
modified = original.copy()
modified[3] = 'lists'
modified.append('Python')

# Display the original and modified lists
st.write("Original List:", original)
st.write("Modified List:", modified)

# Verify assertions
assert original == ['I', 'am', 'learning', 'hacking', 'in']
assert modified == ['I', 'am', 'learning', 'lists', 'in', 'Python']

# Code snippet 3: Creating a Merged Sorted List
st.header("Creating a Merged Sorted List")

list1 = [6, 12, 5]
list2 = [6.2, 0, 14, 1]
list3 = [0.9]

# Your implementation here
my_list = sorted(list1 + list2 + list3, reverse=True)

# Display the merged and sorted list
st.write("Merged and Sorted List:", my_list)

# Verify the assertion
assert my_list == [14, 12, 6.2, 6, 5, 1, 0.9, 0]