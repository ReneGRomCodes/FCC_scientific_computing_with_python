def validate_problems(problems):
    """Check 'problems' argument for specific conditions in 'arithmetic_arranger()' function according to given task and
    returns 'error_message' if any condition is met."""

    if len(problems) > 5:
        error_message = "Error: Too many problems."
        return error_message

    for problem in problems:
        if "/" in problem or "*" in problem:
            error_message = "Error: Operator must be '+' or '-'."
            return error_message

        elif " " not in problem[:5] or " " not in problem[-5:]:
            error_message = "Error: Numbers cannot be more than four digits."
            return error_message

        elif problem.find(" + ") > 0:
            error_message = "Error: Numbers must only contain digits."
            n = problem.find(" + ")
            digits_only = problem[:n] + problem[n+3:]

            if not digits_only.isdigit():
                return error_message

        elif problem.find(" - ") > 0:
            error_message = "Error: Numbers must only contain digits."
            n = problem.find(" - ")
            digits_only = problem[:n] + problem[n+3:]

            if not digits_only.isdigit():
                return error_message


def draw_format(problems):
    """Slice items in list 'problems' into operand #1, operand #2 and operator, and return them in formatted strings."""

    n_problems = len(problems)
    space_between_problems = "    "
    first_line = ""
    second_line = ""
    third_line = ""
    problems_counter = 1

    for problem in problems:

        index = 0
        while True:
            if problem[index] == " ":
                break
            else:
                index += 1

        reverse_index = -1
        while True:
            if problem[reverse_index] == " ":
                break
            else:
                reverse_index += -1

        formatted_reverse_index = reverse_index * (-1)
        if index >= formatted_reverse_index:
            n_dash = index + 2
        else:
            n_dash = formatted_reverse_index + 1

        if "+" in problem:
            operator = "+"
        else:
            operator = "-"

        first_line_space = n_dash - index
        second_line_space = n_dash + reverse_index - 1
        if problems_counter == n_problems:
            first_line += " " * first_line_space + problem[:index]
            second_line += operator + " " * second_line_space + problem[reverse_index:]
            third_line += "-" * n_dash
        else:
            first_line += " " * first_line_space + problem[:index] + space_between_problems
            second_line += operator + " " * second_line_space + problem[reverse_index:] + space_between_problems
            third_line += "-" * n_dash + space_between_problems

        problems_counter += 1

    return first_line, second_line, third_line


def arithmetic_arranger(problems, show_answers=False):

    error_message = validate_problems(problems)
    if error_message:
        print(error_message)
        return error_message

    first, second, third = draw_format(problems)
    print(first)
    print(second)
    print(third)


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
