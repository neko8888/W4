import streamlit as st

# Function to count even numbers
def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

# Function to find wanted people
WANTED_PEOPLE = ['John Doe', 'Clint Eastwood', 'Chuck Norris']

def find_wanted_people(names_to_check):
    return [name for name in names_to_check if name in WANTED_PEOPLE]

# Function to calculate average length of words
def average_length_of_words(sentence):
    words = sentence.split()
    if len(words) == 0:
        return 0
    total_length = sum(len(word) for word in words)
    return round(total_length / len(words), 1)

# Streamlit app
st.title("Python Programming Tasks")

# Task 1: Count Even Numbers
st.header("Task 1: Count Even Numbers")
numbers_input = st.text_input("Enter a list of numbers separated by spaces:")
if st.button("Count Even Numbers"):
    numbers = [int(num) for num in numbers_input.split()]
    result = count_even_numbers(numbers)
    st.write(f"Number of even numbers: {result}")

# Task 2: Find Wanted People
st.header("Task 2: Find Wanted People")
names_input = st.text_input("Enter a list of names separated by commas:")
if st.button("Find Wanted People"):
    names_to_check = [name.strip() for name in names_input.split(',')]
    wanted_people = find_wanted_people(names_to_check)
    st.write("Wanted People:")
    for name in wanted_people:
        st.write(name)

# Task 3: Average Length of Words in a Sentence
st.header("Task 3: Average Length of Words")
sentence_input = st.text_input("Enter a sentence:")
if st.button("Calculate Average Length"):
    result = average_length_of_words(sentence_input)
    st.write(f"Average length of words: {result}")
