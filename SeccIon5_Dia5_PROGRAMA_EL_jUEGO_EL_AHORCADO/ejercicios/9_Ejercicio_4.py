def contarPrimos(num_final):

    for i in range(num_final + 1):
        if i > 1:
            for j in range(i+1):
                if j > 1:
                    if i % j == 0 and i != j:
                        print(f'División acutual: {i}/{j}')
                        print(f'{i} no es primo')
                        break
                    else:
                        if i == j:
                            print(f'División acutual: {i}/{j}')
                            print(f'{i} es primo')
                            
contarPrimos(10)