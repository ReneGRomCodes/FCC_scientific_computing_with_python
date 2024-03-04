def validate_problems(problems):

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


def arithmetic_arranger(problems, show_answers=False):

    error_message = validate_problems(problems)
    if error_message:
        print(error_message)
        return error_message

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
