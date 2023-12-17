def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  top = []
  bottom = []
  lines = []
  results = []

  for problem in problems:
      left, operator, right = problem.split()

      if operator not in ['+', '-']:
          return "Error: Operator must be '+' or '-'."

      if not left.isdigit() or not right.isdigit():
          return "Error: Numbers must only contain digits."

      if len(left) > 4 or len(right) > 4:
          return "Error: Numbers cannot be more than four digits."

      width = max(len(left), len(right)) + 2
      top.append(left.rjust(width))
      bottom.append(operator + right.rjust(width - 1))
      lines.append('-' * width)

      if show_answers:
          if operator == '+':
              result = str(int(left) + int(right))
          else:
              result = str(int(left) - int(right))
          results.append(result.rjust(width))

  arranged_problems = '    '.join(top) + '\n' + '    '.join(bottom) + '\n' + '    '.join(lines)
  if show_answers:
      arranged_problems += '\n' + '    '.join(results)
    

  return arranged_problems