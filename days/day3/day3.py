import re

def flatten_file_content():
    try:
        with open("day3c1input.txt", "r") as file:
            # Read the file and join all the lines into a single string
            content = file.read().replace("\n", "")  # Read everything and strip newline characters
            return content
    except FileNotFoundError:
        print("The file day3c1input.txt does not exist.")
        return None


def sum_valid_mul_instructions(lines):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, lines)

    total_sum = 0

    for match in matches:
        x, y = map(int, match)  # Extract the two integers and convert to int
        total_sum += x * y  # Perform the multiplication and add to the sum

    return total_sum

def sum_valid_mul_instructions_with_conditions(memory):
    # Regex to match mul(X,Y), do(), and don't() instructions
    pattern = r"do\(\).*?don't\(\)"

    pattern1 = r".*do\(\)(.*)"

    # Find all matching instructions (in order of occurrence)
    instructions = re.findall(pattern, memory)
    instructions.append(re.findall(pattern1, memory))
    total = 0
    for instruction in instructions:
        total += sum_valid_mul_instructions(instruction)
    return total


print(sum_valid_mul_instructions(flatten_file_content()))
print(sum_valid_mul_instructions_with_conditions(flatten_file_content()))
