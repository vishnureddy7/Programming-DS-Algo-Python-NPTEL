#link for the question
#https://onlinecourses.nptel.ac.in/noc19_cs08/progassignment?name=116

def longestPalSubstr(string):
    maxLength = 1
    start = 0
    length = len(string)
    low = 0
    high = 0
    for i in range(1, length):
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
    return maxLength,string[start:start + maxLength]
n=int(input());
s=input();
l=longestPalSubstr(s)
print(l[0],l[1],sep='\n');
