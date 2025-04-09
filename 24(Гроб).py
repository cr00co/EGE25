s = open('24_17641.txt').readline()
while '+*' in s: s = s.replace('+*', '+ *')
while '*+' in s: s = s.replace('*+', '* +')
while '++' in s: s = s.replace('++', '+ +')
while '**' in s: s = s.replace('**', '* *')

m = -float('inf')

lens_of_correct_substring = []

list_of_strings = s.split(' ')

for string in list_of_strings:
    if len(string) > m:
        for i in range(len(string)):
            for j in range(i + 1, len(string)):
                substring = string[i:j+1]
                if substring[0] not in '+*':
                    if substring[-1] not in '+*' and substring[0:2] not in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']:
                        m = max(len(substring), m)
                        if eval(substring) == 0:
                            lens_of_correct_substring.append(len(substring))

print(max(lens_of_correct_substring))
