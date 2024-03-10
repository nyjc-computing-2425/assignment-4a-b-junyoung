nric = input('Enter an NRIC number: ')

# Type your code below
def validate(nric):
  nric_no = nric[1:-1]
  length = len(nric_no)
  int(nric_no)
  for char in nric[1:-1]:
      try:
          nric_no = [int(char) for char in nric[1:-1]]
      except ValueError:
        return 1

  nric_end = nric[-1]
  if nric.startswith(("S", "T", "F", "G")) and nric_end.isalpha():
      digit_weight = [2, 7, 6, 5, 4, 3, 2]
      final = 0
      for i in range(length):
          inter = 0
          inter = nric_no[i] * digit_weight[i]
          final = int(final) + int(inter)
      if nric.startswith(("T", "G")):
          final = final + 4
          final = final % 11
      else:
          final = final % 11

      if nric.startswith(("S", "T")):
          dict_1 = {0: "J", 1: "Z", 2: "I", 3: "H", 4: "G", 5: "F", 6: "E", 7: "D", 8: "C", 9: "B", 10: "A"}
          last_alpha = dict_1[final]
          if nric[-1] == last_alpha:
              return 0
          else:
              return 1

      elif nric.startswith(("F", "G")):
          dict_2 = {0: "X", 1: "W", 2: "U", 3: "T", 4: "R", 5: "Q", 6: "P", 7: "N", 8: "M", 9: "L", 10: "K"}
          last_alpha = dict_2[final]
          if nric[-1] == last_alpha:
              return 0
          else:
              return 1

  else:
      return 1

answer = validate(nric)
if answer == 0:
  print("NRIC is valid.")
elif answer == 1:
  print("NRIC is invalid.")