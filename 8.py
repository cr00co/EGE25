w = 'ВДЕРЬ'
count = 0
for x1 in w:
    for x2 in w:
        for x3 in w:
            for x4 in w:
                for x5 in w:
                    for x6 in w:
                        for x7 in w:
                            count += 1
                            words = x1 + x2 + x3 + x4 + x5 + x6 + x7
                            if 'В' not in words:
                                print(count, words)






