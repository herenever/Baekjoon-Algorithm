def solution(s):
    dict = {}
    subsets = convert(s)
    for subset in subsets:
        subset = map(int,subset.split(","))
        add(subset,dict)
    answer = list(dict)
    return answer

def convert(s):
    temp = s[1:len(s)-1]
    temp = temp.replace("},","")
    temp = temp[1:len(temp)-1]
    temp = temp.split("{")
    temp.sort(key = len)
    return temp

def add(subset,dict):
    for char in subset:
        if char not in dict:
            dict[int(char)] = char

# a = solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")
# print(a)