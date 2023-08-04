# Q1
def merge_lists_into_dict(keys, values):
    if len(keys) != len(values):
        raise ValueError("Both lists must be of the same size.")
    
    dictionary = {}
    for key, value in zip(keys, values):
        if key in dictionary:
            print(f"Warning: Duplicate key '{key}'. Overwriting previous value.")
        dictionary[key] = value
    
    return dictionary

def get_input_list():
    input_list = input("Enter a list of elements separated by spaces: ").split()
    return input_list

def main():
    print("Enter the first list (unique elements):")
    keys_list = get_input_list()

    print("Enter the second list (same size as the first list):")
    values_list = get_input_list()

    if len(keys_list) != len(values_list):
        print("Error: Both lists must be of the same size.")
        return

    merged_dict = merge_lists_into_dict(keys_list, values_list)
    print("Merged Dictionary:")
    print(merged_dict)

if __name__ == "__main__":
    main()



# Q2
def paragraph_to_list(paragraph):
    words = paragraph.split()
    filtered_words = [word for word in words if len(word) > 4]
    return filtered_words

def main():
    user_input = input("Enter a sentence or paragraph: ")
    result_list = paragraph_to_list(user_input)
    print("Words with more than 4 letters:")
    print(result_list)

if __name__ == "__main__":
    main()


# Q3
def count_words_in_string(string, word):
    count = 0
    start = 0
    while True:
        index = string.find(word, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count

def cats_and_dogs_appear_equal(string):
    # Count occurrences of "cat" and "dog" in the string
    cat_count = count_words_in_string(string.lower(), "cat")
    dog_count = count_words_in_string(string.lower(), "dog")
    
    # Compare the counts and return True if they are equal
    return cat_count == dog_count

# Take user input
user_input = input("Enter a string: ")

# Check if "cat" and "dog" appear the same number of times and display the result
if cats_and_dogs_appear_equal(user_input):
    print("True: 'cat' and 'dog' appear the same number of times.")
else:
    print("False: 'cat' and 'dog' do not appear the same number of times.")




# Q4
def is_leap_year(year):
    # Leap year is divisible by 4, but not divisible by 100, unless it's also divisible by 400.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_season(month, day):
    # Function to determine the season based on the month and day
    if (month == 12 and day >= 21) or (month <= 3 and day < 21):
        return "Winter"
    elif 3 < month < 6 or (month == 3 and day >= 21) or (month == 6 and day < 21):
        return "Spring"
    elif 6 < month < 9 or (month == 6 and day >= 21) or (month == 9 and day < 21):
        return "Summer"
    else:
        return "Autumn"

def get_days_in_year(year):
    return 366 if is_leap_year(year) else 365

def get_next_leap_year(year):
    next_year = year + 1
    while True:
        if is_leap_year(next_year):
            return next_year
        next_year += 1

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    day = int(input("Enter the day (1-31): "))

    season = get_season(month, day)
    print(f"The season on {month}/{day} is {season}.")

    if is_leap_year(year):
        print(f"{year} is a leap year. It has 366 days.")
    else:
        next_leap_year = get_next_leap_year(year)
        print(f"{year} is not a leap year. The next leap year is {next_leap_year}.")

if __name__ == "__main__":
    main()


# Q7
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_of_list(numbers):
    if len(numbers) < 2:
        raise ValueError("The list must contain 2 or more numeric values.")
    
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]
    
    try:
        result = gcd_of_list(numbers)
        print("The Greatest Common Divisor (GCD) is:", result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()








