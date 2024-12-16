# Python solution

def process_file_and_compare():
    left_list, right_list = getFileData()

    # Step 3: Sort the lists
    left_list.sort()
    right_list.sort()

    # Step 4: Calculate the differences
    differences = 0
    for left, right in zip(left_list, right_list):  # Using zip to compare corresponding elements
        differences += abs(left - right)

    # Step 5: Output the results
    print(f"The differences are: {differences}")

def find_the_difference():
    left_list, right_list = getFileData()  # Get the lists from the file

    # Step 1: Build a frequency dictionary for the right list
    right_dict = {}
    for right in right_list:
        if right not in right_dict:
            right_dict[right] = 1
        else:
            right_dict[right] += 1

    # Step 2: Calculate the similarity score
    similarity_score = 0
    for left in left_list:
        if left in right_dict:  # Check if the number appears in the right list
            similarity_score += left * right_dict[left]  # Multiply by its occurrence count

    print(f"The similarity score is: {similarity_score}")


def getFileData():
    # Step 1: Read data from the file
    try:
        with open("day1c1input.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("The file day1c1input.txt does not exist.")
        return

    # Step 2: Parse and convert numbers from the file into two lists (left and right)
    left_list = []
    right_list = []

    for line in lines:
        try:
            left, right = map(int, line.strip().split("   "))  # Assuming space-separated values
            left_list.append(left)
            right_list.append(right)
        except ValueError:
            print(f"Skipping invalid line: {line.strip()}")
    return left_list, right_list

# Run the function to compare lists
process_file_and_compare()
find_the_difference()
