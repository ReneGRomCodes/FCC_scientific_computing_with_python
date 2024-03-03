def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        if "/" in problem or "*" in problem:
            return "Error: Operator must be '+' or '-'."
        elif " " not in problem[:5] or " " not in problem[-5:]:
            return "Error: Numbers cannot be more than four digits."

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
