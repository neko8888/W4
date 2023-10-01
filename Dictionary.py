import streamlit as st

# Task 1: Populating a dictionary
first_name = 'John'
last_name = 'Doe'
favorite_hobby = 'Python'
sports_hobby = 'gym'
age = 82

my_dict = {
    'name': f'{first_name} {last_name}',
    'age': age,
    'hobbies': [favorite_hobby, sports_hobby]
}

# Task 2: Accessing and merging dictionaries
dict1 = dict(key1='This is not that hard', key2='Python is still cool')
dict2 = {'key1': 123, 'special_key': 'secret'}
dict3 = dict([('key2', 456), ('keyX', 'X')])

# Merge dictionaries without modifying the originals
my_dict = {**dict1, **dict2, **dict3}
special_value = my_dict.pop('special_key', None)

# Streamlit app
st.title('Dictionary Operations')

st.header('Task 1: Populating a Dictionary')
st.write("Resulting Dictionary:")
st.write(my_dict)

st.header('Task 2: Accessing and Merging Dictionaries')
st.write("Merged Dictionary:")
st.write(my_dict)
st.write(f"Special Value: {special_value}")

# Check that the originals are untouched
st.write("Original dict1:")
st.write(dict1)
st.write("Original dict2:")
st.write(dict2)
st.write("Original dict3:")
st.write(dict3)
