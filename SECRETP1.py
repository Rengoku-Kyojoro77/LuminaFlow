def swap_chunk(text, n):
    rem = len(text) % (2 * n)
    if rem != 0:
        text += ' ' * ((2 * n) - rem)
    res = ''
    for i in range(0, len(text), 2 * n):
        a = text[i : i + n]
        b = text[i + n : i + 2 * n]
        res += b + a
    return res

def swap_chunk_decode(text, n):
    return swap_chunk(text, n)

def mid_chunks(text, n):
    rem = len(text) % n
    if rem != 0:
        text += ' ' * (n - rem)
    size = len(text) // n
    arr = []
    for i in range(n):
        arr.append(text[i * size : (i + 1) * size])
    mid = n // 2
    swapped = arr[mid:] + arr[:mid]
    return ''.join(swapped)

def mid_chunks_decode(text, n):
    rem = len(text) % n
    if rem != 0:
        text += ' ' * (n - rem)
    size = len(text) // n
    arr = []
    for i in range(n):
        arr.append(text[i * size : (i + 1) * size])
    mid = n - (n // 2)
    swapped = arr[mid:] + arr[:mid]
    return ''.join(swapped)

def row_col(text, n):
    rem = len(text) % n
    if rem != 0:
        text += ' ' * (n - rem)
    arr = [''] * n
    for i in range(len(text)):
        arr[i % n] += text[i]
    return ''.join(arr)

def row_col_decode(text, n):
    rows = len(text) // n
    arr = [''] * rows
    for i in range(len(text)):
        arr[i % rows] += text[i]
    return ''.join(arr)

def arb_col(text, order):
    n = len(order)
    rem = len(text) % n
    if rem != 0:
        text += ' ' * (n - rem)
    arr = [''] * n
    for i in range(len(text)):
        arr[i % n] += text[i]
    res = ''
    for idx in order:
        res += arr[idx]
    return res

def arb_col_decode(text, order):
    n = len(order)
    rows = len(text) // n
    arr = []
    for i in range(n):
        arr.append(text[i * rows : (i + 1) * rows])
    orig = [''] * n
    for i, idx in enumerate(order):
        orig[idx] = arr[i]
    res = ''
    for r in range(rows):
        for c in range(n):
            res += orig[c][r]
    return res

def rail(text, n):
    arr = [''] * n
    row = 0
    step = 1
    for char in text:
        arr[row] += char
        row += step
        if row == n - 1 or row == 0:
            step = -step
    return ''.join(arr)

def rail_decode(text, n):
    arr = []
    for i in range(n):
        arr.append([])
    row = 0
    step = 1
    for i in range(len(text)):
        arr[row].append(i)
        row += step
        if row == n - 1 or row == 0:
            step = -step
    flat = []
    for sub in arr:
        flat.extend(sub)
    res = [''] * len(text)
    for i, char in enumerate(text):
        res[flat[i]] = char
    return ''.join(res)

def group5(text):
    clean = text.replace(' ', '')
    arr = []
    for i in range(0, len(clean), 5):
        arr.append(clean[i : i + 5])
    return ' '.join(arr)

msg = 'hold your horses'
print(group5(swap_chunk(msg, 2)))
print(swap_chunk_decode(swap_chunk(msg, 2), 2))
print()
print(group5(mid_chunks(msg, 4)))
print(mid_chunks_decode(mid_chunks(msg, 4), 4))
print()
print(group5(row_col(msg, 3)))
print(row_col_decode(row_col(msg, 3), 3))
print()
print(group5(arb_col(msg, [2, 0, 1])))
print(arb_col_decode(arb_col(msg, [2, 0, 1]), [2, 0, 1]))
print()
print(group5(rail(msg, 3)))
print(rail_decode(rail(msg, 3), 3))