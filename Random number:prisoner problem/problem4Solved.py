import operator
cipher = [0, 22, 25, 23, 22, 3, 1, 22, 0, 0, 22, 25, 23, 0, 6, 4, 0, 13, 21, 0, 6, 23, 17, 10, 23, 21, 0, 13, 22, 1, 7, 6, 23, 0, 6, 23, 3, 13, 0, 13, 21, 1, 22, 25, 16, 23, 3, 13, 1, 0, 6, 23, 14, 13, 1, 24, 0, 22, 21, 10, 5, 5, 23, 3, 0, 6, 23, 21, 16, 13, 1, 8, 21, 4, 1, 24, 4, 3, 3, 22, 7, 21, 22, 5, 22, 10, 0, 3, 4, 8, 23, 22, 10, 21, 5, 22, 3, 0, 10, 1, 23, 22, 3, 0, 22, 0, 4, 19, 23, 4, 3, 14, 21, 4, 8, 4, 13, 1, 21, 0, 4, 21, 23, 4, 22, 5, 0, 3, 22, 10, 25, 16, 23, 21, 4, 1, 24, 25, 2, 22, 11, 11, 22, 21, 13, 1, 8, 23, 1, 24, 0, 6, 23, 14, 0, 22, 24, 13, 23, 0, 22, 21, 16, 23, 23, 11, 1, 22, 14, 22, 3, 23, 4, 1, 24, 25, 2, 4, 21, 16, 23, 23, 11, 0, 22, 21, 4, 2, 7, 23, 23, 1, 24, 0, 6, 23, 6, 23, 4, 3, 0, 4, 15, 6, 23, 4, 1, 24, 0, 6, 23, 0, 6, 22, 10, 21, 4, 1, 24, 1, 4, 0, 10, 3, 4, 16, 21, 6, 22, 15, 19, 21, 0, 6, 4, 0, 5, 16, 23, 21, 6, 13, 21, 6, 23, 13, 3, 0, 22, 13, 0, 13, 21, 4, 15, 22, 1, 21, 10, 14, 14, 4, 0, 13, 22, 1, 24, 23, 18, 22, 10, 0, 16, 2, 0, 22, 25, 23, 7, 13, 21, 6, 23, 24, 0, 22, 24, 13, 23, 0, 22, 21, 16, 23, 23, 11, 0, 22, 21, 16, 23, 23, 11, 11, 23, 3, 15, 6, 4, 1, 15, 23, 0, 22, 24, 3, 23, 4, 14, 4, 2, 0, 6, 23, 3, 23, 13, 21, 0, 6, 23, 3, 10, 25, 5, 22, 3, 13, 1, 0, 6, 4, 0, 21, 16, 23, 23, 11, 22, 5, 24, 23, 4, 0, 6, 7, 6, 4, 0, 24, 3, 23, 4, 14, 21, 14, 4, 2, 15, 22, 14, 23, 7, 6, 23, 1, 7, 23, 6, 4, 18, 23, 21, 6, 10, 5, 5, 16, 23, 24, 22, 5, 5, 0, 6, 13, 21, 14, 22, 3, 0, 4, 16, 15, 22, 13, 16, 14, 10, 21, 0, 8, 13, 18, 23, 10, 21, 11, 4, 10, 21, 23, 0, 6, 23, 3, 23, 13, 21, 0, 6, 23, 3, 23, 21, 11, 23, 15, 0, 0, 6, 4, 0, 14, 4, 19, 23, 21, 15, 4, 16, 4, 14, 13, 0, 2, 22, 5, 21, 22, 16, 22, 1, 8, 16, 13, 5, 23, 5, 22, 3, 7, 6, 22, 7, 22, 10, 16, 24, 25, 23, 4, 3, 0, 6, 23, 7, 6, 13, 11, 21, 4, 1, 24, 21, 15, 22, 3, 1, 21, 22, 5, 0, 13, 14, 23, 0, 6, 23, 22, 11, 11, 3, 23, 21, 21, 22, 3, 21, 7, 3, 22, 1, 8, 0, 6, 23, 11, 3, 22, 10, 1, 24, 14, 4, 1, 21, 15, 22, 1, 0, 10, 14, 23, 16, 2, 0, 6, 23, 11, 4, 1, 8, 21, 22, 5, 24, 23, 21, 11, 13, 21, 23, 24, 16, 22, 18, 23, 0, 6, 23, 16, 4, 7, 21, 24, 23, 16, 4, 2, 0, 6, 23, 13, 1, 21, 22, 16, 23, 1, 15, 23, 22, 5, 22, 5, 5, 13, 15, 23, 4, 1, 24, 0, 6, 23, 21, 11, 10, 3, 1, 21, 0, 6, 4, 0, 11, 4, 0, 13, 23, 1, 0, 14, 23, 3, 13, 0, 22, 5, 0, 6, 23, 10, 1, 7, 22, 3, 0, 6, 2, 0, 4, 19, 23, 21, 7, 6, 23, 1, 6, 23, 6, 13, 14, 21, 23, 16, 5, 14, 13, 8, 6, 0, 6, 13, 21, 17, 10, 13, 23, 0, 10, 21, 14, 4, 19, 23, 7, 13, 0, 6, 4, 25, 4, 3, 23, 25, 22, 24, 19, 13, 1, 7, 6, 22, 7, 22, 10, 16, 24, 5, 4, 3, 24, 23, 16, 21, 25, 23, 4, 3, 0, 22, 8, 3, 10, 1, 0, 4, 1, 24, 21, 7, 23, 4, 0, 10, 1, 24, 23, 3, 4, 7, 23, 4, 3, 2, 16, 13, 5, 23, 25, 10, 0, 0, 6, 4, 0, 0, 6, 23, 24, 3, 23, 4, 24, 22, 5, 21, 22, 14, 23, 0, 6, 13, 1, 8, 4, 5, 0, 23, 3, 24, 23, 4, 0, 6, 0, 6, 23, 10, 1, 24, 13, 21, 15, 22, 18, 23, 3, 23, 24, 15, 22, 10, 1, 0, 3, 2, 5, 3, 22, 14, 0, 6, 22, 21, 23, 25, 22, 10, 3, 1, 1, 22, 0, 3, 4, 18, 23, 16, 23, 3, 3, 23, 0, 10, 3, 1, 21, 11, 10, 9, 9, 16, 23, 21, 0, 6, 23, 7, 13, 16, 16, 4, 1, 24, 14, 4, 19, 23, 21, 10, 21, 3, 4, 0, 6, 23, 3, 25, 23, 4, 3, 0, 6, 22, 21, 23, 13, 16, 16, 21, 7, 23, 6, 4, 18, 23, 0, 6, 4, 1, 5, 16, 2, 0, 22, 22, 0, 6, 23, 3, 21, 0, 6, 4, 0, 7, 23, 19, 1, 22, 7, 1, 22, 0, 22, 5, 0, 6, 10, 21, 15, 22, 1, 21, 15, 13, 23, 1, 15, 23, 24, 22, 23, 21, 14, 4, 19, 23, 15, 22, 7, 4, 3, 24, 21, 4, 1, 24, 0, 6, 10, 21, 0, 6, 23, 1, 4, 0, 13, 18, 23, 6, 10, 23, 22, 5, 3, 23, 21, 22, 16, 10, 0, 13, 22, 1, 13, 21, 22, 18, 23, 3, 7, 13, 0, 6, 0, 6, 23, 11, 4, 16, 23, 15, 4, 21, 0, 22, 5, 0, 6, 22, 10, 8, 6, 0, 4, 1, 24, 23, 1, 0, 23, 3, 11, 3, 13, 21, 23, 21, 22, 5, 8, 3, 23, 4, 0, 11, 13, 0, 15, 6, 4, 1, 24, 14, 22, 14, 23, 1, 0, 7, 13, 0, 6, 0, 6, 13, 21, 3, 23, 8, 4, 3, 24, 0, 6, 23, 13, 3, 15, 10, 3, 3, 23, 1, 0, 21, 0, 10, 3, 1, 4, 7, 3, 2, 4, 1, 24, 16, 22, 21, 23, 0, 6, 23, 1, 4, 14, 23, 22, 5, 4, 15, 0, 13, 22, 1, 21, 22, 5, 0, 2, 22, 10, 1, 22, 7, 0, 6, 23, 5, 4, 13, 3, 22, 11, 6, 23, 16, 13, 4, 1, 2, 14, 11, 6, 13, 1, 0, 6, 2, 22, 3, 13, 21, 22, 1, 21, 25, 23, 4, 16, 16, 14, 2, 21, 13, 1, 21, 3, 23, 14, 23, 14, 25, 23, 3, 23, 24]

freq = {}
for letter in cipher:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

freq = dict(sorted(freq.items(),key=operator.itemgetter(1),reverse = True))
print(freq)

#letterfreq = [e,t,a,o,n,r,i,s,h,d,l,f,c,m,u,g,y,p,w,b,v,k,x,j,q,z]
#letterfreq = "etaonrishdlfcmugypwbvkxjqz"

secretkey = "etoashrnidulfmwpcybgkvqzxj"

guess = {}
i = 0

for key,value in freq.items():
    guess[key] = secretkey[i]
    i += 1
print(guess)
for i in cipher:
    print(guess[i], end = '')
