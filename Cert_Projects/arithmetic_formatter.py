def validate_problems(problems):
    """Check 'problems' argument for specific conditions in 'arithmetic_arranger()' function according to given task and
    returns 'error_message' if any condition is met."""

    # Check if there are more than 5 problems.
    if len(problems) > 5:
        error_message = "Error: Too many problems."
        return error_message

    # Iterate through each problem to check for various conditions.
    for problem in problems:
        # Check for multiplication or division operations.
        if "/" in problem or "*" in problem:
            error_message = "Error: Operator must be '+' or '-'."
            return error_message

        # Check if numbers exceed four digits or if there are missing spaces.
        elif " " not in problem[:5] or " " not in problem[-5:]:
            error_message = "Error: Numbers cannot be more than four digits."
            return error_message

        # Check for invalid characters in addition operation.
        elif problem.find(" + ") > 0:
            error_message = "Error: Numbers must only contain digits."
            n = problem.find(" + ")
            digits_only = problem[:n] + problem[n+3:]

            # Check if the remaining string contains only digits.
            if not digits_only.isdigit():
                return error_message

        # Check for invalid characters in subtraction operation.
        elif problem.find(" - ") > 0:
            error_message = "Error: Numbers must only contain digits."
            n = problem.find(" - ")
            digits_only = problem[:n] + problem[n+3:]

            # Check if the remaining string contains only digits.
            if not digits_only.isdigit():
                return error_message


def draw_format(problems):
    """Slice items in list 'problems' into operand1, operand2, operator and evaluates each item, and return them in
    formatted strings."""

    # Starting variables to be returned as formatted strings.
    first_line = ""
    second_line = ""
    third_line = ""
    result_line = ""

    # Iterate over list 'problems' to build formatted strings.
    problems_counter = 1
    for problem in problems:

        # Identify operand1 end index.
        index = 0
        while True:
            if problem[index] == " ":
                break
            else:
                index += 1

        # Identify operand2 beginning index.
        reverse_index = -1
        while True:
            if problem[reverse_index] == " ":
                break
            else:
                reverse_index += -1

        # Identify operator index.
        formatted_reverse_index = reverse_index * (-1)
        if index >= formatted_reverse_index:
            n_dash = index + 2
        else:
            n_dash = formatted_reverse_index + 1

        # Identify operator.
        if "+" in problem:
            operator = "+"
        else:
            operator = "-"

        # Variables to build formatted strings for return values.
        n_problems = len(problems)
        space_between_problems = "    "
        result = eval(problem)
        first_line_space = n_dash - index
        second_line_space = n_dash + reverse_index - 1
        result_line_space = n_dash - len(str(result))

        # Create return values through string concatenation.
        if problems_counter == n_problems:
            first_line += " " * first_line_space + problem[:index]
            second_line += operator + " " * second_line_space + problem[reverse_index:]
            third_line += "-" * n_dash
            result_line += " " * result_line_space + str(result)
        else:
            first_line += " " * first_line_space + problem[:index] + space_between_problems
            second_line += operator + " " * second_line_space + problem[reverse_index:] + space_between_problems
            third_line += "-" * n_dash + space_between_problems
            result_line += " " * result_line_space + str(result) + space_between_problems

        problems_counter += 1

    return first_line, second_line, third_line, result_line


def arithmetic_arranger(problems, show_answers=False):
    """Arrange arithmetic problems vertically and optionally display the answers.
        Args:
            problems (list): List of strings representing arithmetic problems in the format "operand1 operator operand2".
            show_answers (bool, optional): Whether to display the answers. Defaults to False.
        Returns a formatted string containing the arranged arithmetic problems, with or without answers.
        If the number of problems exceeds five or an invalid operator or operand is provided,
        an error message is returned instead of the arranged problems.
        """

    # Check for validity of items in 'problems'.
    error_message = validate_problems(problems)
    if error_message:
        return error_message

    # Format and return 'problems'.
    first, second, third, result = draw_format(problems)
    if show_answers:
        output = first + "\n" + second + "\n" + third + "\n" + result
        return output
    else:
        output = first + "\n" + second + "\n" + third
        return output


# Function calls to test functionality and outputs.
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
