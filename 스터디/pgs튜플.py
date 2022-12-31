def solution(s):
    dict = {}
    subsets = convert(s)
    for subset in subsets:
        subset = map(int,subset.split(","))
        add(subset,dict)
    answer = list(dict)
    return answer

def convert(s):
    temp = s.replace("}}","")
    temp = temp.replace("{{","")
    temp = temp.split("},{")
    temp.sort(key = len)
    return temp

def add(subset,dict):
    for char in subset:
        if char not in dict:
            dict[int(char)] = char

a = solution("{{123},{123,11}}")
print(a)