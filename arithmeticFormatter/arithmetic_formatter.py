def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return 'Error: Too many problems.'
    
    first_line = []
    second_line = []
    dashes = []
    answers = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must contain two operands and one operator"
        
        first,operator,second = parts

        if operator not in ('+','-'):
            return "Error: Operator must be '+' or '-'."
        
        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(first),len(second))+2
        if operator == '+':
            answer = str(int(first) + int(second))
        else:
            answer = str(int(first) - int(second))


        first_line.append(first.rjust(width))
        second_line.append(operator+" "+second.rjust(width-2))
        dashes.append('-' * width)
        answers.append(answer.rjust(width))

    if show_answers:
        problems =( "    ".join(first_line)+"\n"+
                        "    ".join(second_line)+"\n"+
                        "    ".join(dashes)+"\n"+
                        "    ".join(answers))
    else:
        problems =( "    ".join(first_line)+"\n"+
                        "    ".join(second_line)+"\n"+
                        "    ".join(dashes))

    return problems

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')