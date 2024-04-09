def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Calcula a sequência de Collatz para números entre 1 e 100000
max_length = 0
number_with_max_sequence = 0

for i in range(1, 100001):
    length = len(collatz_sequence(i))
    if length > max_length:
        max_length = length
        number_with_max_sequence = i

print(f"O número {number_with_max_sequence} tem a maior sequência de Collatz com tamanho {max_length}.")
