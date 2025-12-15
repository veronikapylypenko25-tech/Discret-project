#1
def find_primes (a:int, b:int):
    result = []
    for num in range(a, b + 1):
        if num < 2:
            continue
        divisible = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                divisible = False
                break
        if divisible:
            result.append(num)
    return result
#2
def unique_characters(s):
    characters_used = []
    for char in s:
        if char in characters_used:
            return False
        else:
            characters_used.append(char)
            return True

#3
def fibonacci(n):
    result = []
    n1, n2 = 1, 1
    for i in range(n):
        result.append(n1)
        n1, n2 = n2, n1 + n2
    return result

#4
def swapcase(s):
    result = ""
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
            return result

#5
def encrypt(mes, shift):
    result = ""
    for char in mes:
        if char.isalpha():
            if char.islower():
                base_char = 'a'
            else:
                base_char = 'A'
            result += chr((ord(char) - ord(base_char) + shift) % 26 + ord(base_char))
        else:
            result += char
    return result

def decrypt(mes, shift):
    result = ""
    for char in mes:
        if char.isalpha():
            if char.islower():
                base_char = 'a'
            else:
                base_char = 'A'
            result += chr((ord(char) - ord(base_char) - shift) % 26 + ord(base_char))
        else:
            result += char
    return result

if __name__ == "__main__":
    print(find_primes (1, 10))
    print(unique_characters("abcdefg"))
    print(unique_characters("abcdeff"))
    print(fibonacci(5))
    print(swapcase("Hello World! "))
    encrypted = encrypt("Hello!", 3)
    print(encrypted)
    print(decrypt(encrypted, 3))