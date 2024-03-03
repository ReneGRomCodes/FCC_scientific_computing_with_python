def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        error_message = "Error: Too many problems."
        if show_answers:
            print(error_message)
        return error_message

    for problem in problems:
        if "/" in problem or "*" in problem:
            error_message = "Error: Operator must be '+' or '-'."
            if show_answers:
                print(error_message)
            return error_message

        elif " " not in problem[:5] or " " not in problem[-5:]:
            error_message = "Error: Numbers cannot be more than four digits."
            if show_answers:
                print(error_message)
            return error_message

        elif problem.find(" + ") > 0:  # TODO prints error_message twice if case is triggered.
            error_message = "Error: Numbers must only contain digits."
            n = problem.find(" + ")
            digits_only = problem[:n] + problem[n+3:]

            if not digits_only.isdigit():
                print(error_message)
                return error_message

        elif problem.find(" - ") > 0:  # TODO prints error_message twice if case is triggered.
            error_message = "Error: Numbers must only contain digits."
            n = problem.find(" - ")
            digits_only = problem[:n] + problem[n+3:]

            if not digits_only.isdigit():
                print(error_message)
                return error_message

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
