def octal_to_decimal(octal_number):
    decimal_number = 0
    power = 0
    
    # Octal sayıyı sağdan sola doğru tarar
    while octal_number != 0:
        # Her basamağı Decimal'e dönüştürme
        digit = octal_number % 10
        decimal_number += digit * (8 ** power)
        # Basamak sayısını artırma
        power += 1
        # Octal sayıyı bir basamak sağa kaydırma
        octal_number //= 10
        
    return decimal_number

# Kullanıcıdan Octal sayıyı alır
octal_input = int(input("Octal sayıyı girin: "))

# Octal sayıyı Decimal'e dönüştürme
decimal_output = octal_to_decimal(octal_input)
print("Decimal karşılığı:", decimal_output)
