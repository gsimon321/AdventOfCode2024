def getFileData():
    # Step 1: Read data from the file
    try:
        with open("day2c1input.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("The file day1c1input.txt does not exist.")
        return

    data_2d_array = []  # Initialize the 2D array (list of lists)

    for i, line in enumerate(lines):
        try:
            # Split line by spaces (or appropriate delimiter) and convert each value to an integer
            current_row = list(map(int, line.strip().split()))  # Assuming single-space-separated values
            data_2d_array.append(current_row)  # Append the parsed row to the 2D array
        except ValueError:
            print(f"Skipping invalid line {i}: {line.strip()}")  # Use index for better debugging

    return data_2d_array

def numberOfSafeReports():
    data = getFileData()  # Get the data, a list of lists
    count = 0

    # Check each row for safety
    for row in data:
        if is_safe_report(row):
            count += 1  # Report is safe without using the Problem Dampener
        else:
            # Try removing every level to see if the report becomes safe
            for i in range(len(row)):
                modified_row = row[:i] + row[i + 1:]  # Remove the i-th level
                if is_safe_report(modified_row):  # Check if modified row is safe
                    count += 1  # Now this report counts as safe
                    break  # No need to try removing other levels

    return count


def is_safe_report(row):
    is_increasing = None  # Initialize to None (undetermined direction)

    # Compare each number with its next neighbor
    for i in range(len(row) - 1):
        difference = row[i + 1] - row[i]

        if abs(difference) < 1 or abs(difference) > 3:  # Rule: Difference must be between 1 and 3
            return False

        if is_increasing is None:  # Determine direction on the first comparison
            is_increasing = difference > 0
        elif is_increasing and difference < 0:  # Inconsistent with increasing
            return False
        elif not is_increasing and difference > 0:  # Inconsistent with decreasing
            return False

    return True  # The report is safe if all checks pass

#print(is_safe_report([1, 3, 2, 6, 7]))
print(numberOfSafeReports())