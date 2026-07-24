import random

abc = 'abcdefghijklmnopqrstuvwxyz'

def even_odd_swap(x):
    if len(x) % 2 != 0:
        x = x + ' '
    evens = x[0::2]
    odds = x[1::2]
    s = ''
    for i in range(len(evens)):
        s = s + odds[i] + evens[i]
    return s

def swap_middle(x):
    if len(x) % 2 != 0:
        x = x + ' '
    mid = len(x) // 2
    return x[mid:] + x[:mid]

def reverse(x):
    return x[::-1]

def caesar(x, n):
    s = ''
    for char in x:
        if char == ' ':
            s += ' '
        else:
            idx = abc.find(char)
            s += abc[(idx + n) % 26]
    return s

def atbash(x):
    s = ''
    for char in x:
        if char == ' ':
            s += ' '
        else:
            idx = abc.find(char)
            s += abc[25 - idx]
    return s

def vigenere_enc(x, key):
    s = ''
    for i, char in enumerate(x):
        if char == ' ':
            s += ' '
        else:
            p_idx = abc.find(char)
            k_idx = abc.find(key[i % len(key)])
            s += abc[(p_idx + k_idx) % 26]
    return s

def vigenere_dec(x, key):
    s = ''
    for i, char in enumerate(x):
        if char == ' ':
            s += ' '
        else:
            c_idx = abc.find(char)
            k_idx = abc.find(key[i % len(key)])
            s += abc[(c_idx - k_idx) % 26]
    return s

def beaufort_enc(x, key):
    s = ''
    for i, char in enumerate(x):
        if char == ' ':
            s += ' '
        else:
            p_idx = abc.find(char)
            k_idx = abc.find(key[i % len(key)])
            s += abc[(k_idx - p_idx) % 26]
    return s

def beaufort_dec(x, key):
    return beaufort_enc(x, key)

headers = ['python', 'spyware', 'ciphertext', 'py']

secret_code = ''
for _ in range(10):
    secret_code += abc[random.randint(0, 25)]

chosen_header = random.choice(headers)
raw_msg = chosen_header + secret_code

op = random.randint(0, 3)
if op == 1:
    enc_msg = even_odd_swap(raw_msg)
elif op == 2:
    enc_msg = reverse(raw_msg)
elif op == 3:
    enc_msg = swap_middle(raw_msg)
else:
    enc_msg = raw_msg

cipher_type = random.randint(0, 3)
shift_key = 'key'

if cipher_type == 1:
    msg_enemy = atbash(enc_msg)
elif cipher_type == 2:
    msg_enemy = vigenere_enc(enc_msg, shift_key)
elif cipher_type == 3:
    msg_enemy = beaufort_enc(enc_msg, shift_key)
else:
    msg_enemy = caesar(enc_msg, random.randint(1, 25))

pad_front = ''
pad_back = ''
for _ in range(random.randint(2, 5)):
    pad_front += abc[random.randint(0, 25)]
for _ in range(random.randint(2, 5)):
    pad_back += abc[random.randint(0, 25)]

msg_enemy = pad_front + msg_enemy + pad_back

print('I am hearing ...')
print(msg_enemy)
print()

cracked = False

for key_try in range(26):
    for mode in range(4):
        if mode == 0:
            candidate = caesar(msg_enemy, key_try)
        elif mode == 1:
            candidate = atbash(msg_enemy)
        elif mode == 2:
            candidate = vigenere_dec(msg_enemy, shift_key)
        else:
            candidate = beaufort_dec(msg_enemy, shift_key)

        for sl in range(len(candidate)):
            for el in range(sl + 1, len(candidate) + 1):
                sub = candidate[sl:el]
                
                variants = [
                    sub,
                    even_odd_swap(sub),
                    reverse(sub),
                    swap_middle(sub)
                ]
                
                for v in variants:
                    for h in headers:
                        if v.startswith(h):
                            possible_secret = v[len(h):].strip()
                            if len(possible_secret) == 10:
                                
                                matched_nested = False
                                for other_h in headers:
                                    if other_h != h and other_h in possible_secret:
                                        matched_nested = True
                                
                                if not matched_nested or h == 'python':
                                    print('code cracked ...')
                                    print('Secret code is ...')
                                    print(possible_secret)
                                    cracked = True
                                    break
                    if cracked:
                        break
                if cracked:
                    break
            if cracked:
                break
        if cracked:
            break
    if cracked:
        break
