import streamlit as st

# Fill missing pieces
words = ['PYTHON', 'JOHN', 'chEEse', 'hAm', 'DOE', '123']
upper_case_words = []

for word in words:
    if word.isupper():
        upper_case_words.append(word)

assert upper_case_words == ['PYTHON', 'JOHN', 'DOE']
st.header("Task 1: Fill the missing pieces")
st.write("Upper-case words:", upper_case_words)

# Calculate sum of dic values
magic_dict = dict(val1=44, val2='secret value', val3=55.0, val4=1)

# Your implementation
sum_of_values = sum(value for value in magic_dict.values() if isinstance(value, (int, float)))

assert sum_of_values == 100

st.header("Task 2: Calculate the sum of dict values")
st.write("Sum of numeric values:", sum_of_values)

# Create list of strings based on a list of numbers
numbers = [1, 3, 4, 6, 81, 80, 100, 95]

# Your implementation
my_list = []
for num in numbers:
    if num % 5 == 0 and num % 2 == 1:
        my_list.append('five odd')
    elif num % 5 == 0 and num % 2 == 0:
        my_list.append('five even')
    elif num % 2 == 1:
        my_list.append('odd')
    else:
        my_list.append('even')

assert my_list == ['odd', 'odd', 'even', 'even', 'odd', 'five even', 'five even', 'five odd']
st.header("Task 3: Create a list of strings based on numbers")
st.write("Resulting list:", my_list)
