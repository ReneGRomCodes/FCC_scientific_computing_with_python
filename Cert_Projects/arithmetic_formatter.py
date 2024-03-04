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


def draw_format(problems):  # First sort-of-working draft of 'draw_format()' function.
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

        if index >= reverse_index:  # TODO 'reverse_index' always negative? 'index' therefore always '> reverse_index'?
            n_dash = index + 2      # TODO therefore n_dash is always 'index + 2'!!!
        else:
            n_dash = reverse_index + 2

        first_line_space = n_dash - index
        second_line_space = n_dash + reverse_index

        print(" " * first_line_space + problem[:index])
        print(" " * second_line_space + problem[reverse_index:])
        print("-" * n_dash)


def arithmetic_arranger(problems, show_answers=False):

    error_message = validate_problems(problems)
    if error_message:
        print(error_message)
        return error_message

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
