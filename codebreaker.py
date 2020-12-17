# string of alphabet
alpha = 'abcdefghijklmnopqrstuvwxyz'

# function for breaking transposed string
def transposed(text, places):

  ans = ''

  for i in text.lower():
    if i in alpha:
      ans += alpha[(alpha.index(i) - places) % 26]
    elif i == '.':
      ans += '.'
    elif i == ' ':
      ans += ' '
    elif i == "'":
      ans += "'"
    elif i == ',':
      ans += ','
    elif i == '!':
      ans += '!'
    elif i == '?':
      ans += '?'
    else:
      continue

  return(ans.capitalize())

#function for breaking reversed alphabet string
def mirror(text):

  ans = ''

  for i in text.lower():
    if i in alpha:
      ans += alpha[abs(alpha.index(i) - 25)]
    elif i == '.':
      ans += '.'
    elif i == ' ':
      ans += ' '
    elif i == "'":
      ans += "'"
    elif i == ',':
      ans += ','
    elif i == '!':
      ans += '!'
    elif i == '?':
      ans += '?'
    else:
      continue

  return(ans.capitalize())

print(transposed("Wklv lv d vhfuhw frgh.", 3))
print(mirror("Svool Dliow!"))