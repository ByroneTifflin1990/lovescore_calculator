import string

print("Welcome to the L❤️VE SCORE calculator!")
def user_names():
    while True:
        first_name = input("What is your name?: ").lower()
        second_name = input("What is the name of your crush?: ").lower()

        # Check if inputs contain only letters
        if not first_name.isalpha() or not second_name.isalpha():
            print("❌ Please enter ONLY letters of the alphabet.")
            continue  # Restart the loop
        else:
            return first_name, second_name  # Return valid names


def calculate_love_score(name1, name2):
    # Define the letters in "TRUE" and "LOVE"
    true_list = "true"
    love_list = "love"

    # Count occurrences of "TRUE" letters
    true_count = sum(name1.count(letter) + name2.count(letter) for letter in true_list)

    # Count occurrences of "LOVE" letters
    love_count = sum(name1.count(letter) + name2.count(letter) for letter in love_list)

    # Combine the counts
    love_score = int(f"{true_count}{love_count}")
    print(f"❤️ Love Score = {love_score}")


# Get user inputs
first_name, second_name = user_names()

# Calculate and print love score
calculate_love_score(first_name, second_name)




