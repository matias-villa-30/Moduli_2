import random

codigo3_a = random.randint(0, 9)
codigo3_b = random.randint(0, 9)
codigo3_c = random.randint(0,9)

codigo4_a = random.randint(1,6)
codigo4_b = random.randint(1, 6)
codigo4_c = random.randint(1, 6)
codigo4_d = random.randint(1,6)

codigo_3 = codigo3_a, codigo3_b, codigo3_c
codigo_4 = codigo4_a, codigo4_b, codigo4_c, codigo4_d

print(f"Kolmenumeroisen koodi on: {codigo_3}")
print(f"Neinumeroisen koodi on: {codigo_4}")