def even_odd_swap(x):
    if len(x)%2!=0:
        x = x + ' '
    
    even_letters = x[::2]
    odd_letters = x[1::2]
    
    s = ''
    for i in range(len(even_letters)):
        s = s + even_letters
        s = s + odd_letters
       
        


        return s
def reverse(x):
    s = x[::-1]
    return s
def reverse_word(x):
    words = x.split()

    s = ''
    for kk in range(len(words)):
        s = s+reverse(words[kk])+' '
        return s
def reverse_word_concise(x):
    words = x.split()

    s = ''
    for  everyword in words:
        s = s+reverse(everyword)+' '
        return s
def swap_middle(x):
    if len(x)%2!=0:
        x = x+' '
    first_half = x[0:int(len(x)/2):1]
    second_half = x[int(len(x)/2)::1]
    s = ''
    s = s + second_half
    s = s + first_half

    return s
def swap_middle_rev(x):
    x_swap = swap_middle(x)
    s = reverse(x_swap)
    return s
def swap_middle_rev_decode(x):
    x_rev = reverse(x)
    s = swap_middle(x_rev)
    return s





x = 'Python is cool'    
x_even_odd = even_odd_swap(x)
x_rev      =  reverse(x)
x_rev_word = reverse_word_concise(x)
x_swap_middle = swap_middle(x)
x_swap_middle_rev = swap_middle_rev(x)
#Now we will decode the encrypted messages
x_even_odd_decode = even_odd_swap(x_even_odd)
x_rev_decode = reverse(x_rev)
x_swap_middle_decode = swap_middle(x_swap_middle)
x_decode = swap_middle_rev_decode(x_swap_middle_rev)
# BONUS COMES AFTER BASIC!!!


n = 6
E_key = [4, 5, 1, 3, 2, 0]

def general_swap(message, n, key):
    if len(message)%n!=0:
        message = message + (n- len(message)%n)* ' '
        s = ''
        for kk in range (int(len(message)/n)):
            temp = message[kk*n:(kk+1)*n:1]
            for jj in key:
                s = s + temp[jj]
        return s        

x_enc_general = general_swap(x,n,E_key)

D_key = [0]*n

for kk in range(n):
    D_key[kk]= E_key.index(kk)
print(D_key)    













