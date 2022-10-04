def isCryptSolution(crypt, solution):
        newsol = list(zip(*reversed(solution)))
        newstring1 = ''
        total = 0
        for word in range(len(crypt)-1):
            subtotal, sol_total = 0, 0
            newstring = ''
            for char in crypt[word]:
                idx = newsol[0].index(char)
                newstring = newstring + newsol[1][idx]
                subtotal = int(newstring)
                # if newstring[0] == '0':
                #     return False
            total = total + subtotal
        for char1 in crypt[-1]:
            nidx = newsol[0].index(char1)
            newstring1 = newstring1 + newsol[1][nidx]
            sol_total = int(newstring1)
        if total == sol_total and newstring[0] != '0':
            return print('True')
        elif total == 0 and newstring[0] == '0' and len(newstring) == 1:
            return print('True')
        else:
            return print('False')
crypt = ["BASE", "BAL", "GAMES"]
solution = [['A', '4'],
            ['B', '2'],
            ['E', '1'],
            ['G', '0'],
            ['L', '5'],
            ['M', '9'],
            ['S', '6']]
isCryptSolution(crypt, solution)
