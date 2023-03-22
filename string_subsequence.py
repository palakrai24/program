# https://leetcode.com/problems/is-subsequence/

def isSubsequence(s, t):
    """
    level-easy
    :type s: str
    :type t: str
    :rtype: bool
    time - 0(n)
    space - O(1)
    """
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == len(s) else False
s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))
# https://leetcode.com/problems/number-of-matching-subsequences/description/
s = "abcdea"
words = ["ab","bb","acd","ace"]
def Subsequencecount1(s, words):
    """
    level-medium
    :type s: str
    :type t: str
    :rtype: bool
    time - O(words*n)
    space - O(1)
    """
    count_subsequence = 0
    for word in words:
        if isSubsequence(word,s):
            count_subsequence+=1
    return count_subsequence
print(Subsequencecount1(s, words),'method1')
def Subsequencecount2(s, words):
    """
        find - timecomlexity is 0(n*m)
        level-medium
        :type s: str
        :type t: str
        :rtype: bool
        time - O(len(words)*len(max_char)*n)
        space - O(1)
        """
    ct = 0
    for word in words:
        indx = 0
        found = True
        for char in word:
            indx = s.find(char, indx)
            if indx == -1:
                found = False
                break
            indx+=1
        if found :
            ct+=1
    return ct

print(Subsequencecount2(s, words),'method2')

def Subsequencecount3(s, words):
    """
        find - timecomlexity is 0(n*m)
        level-medium
        :type s: str
        :type t: str
        :rtype: bool
        time - O(len(words)*len(max_char)*logn)
        space - O(s)
        """
    from collections import defaultdict
    d = defaultdict(list)
    for i,char in enumerate(s):
        d[char].append(i)

    def binary_search(arr,target):
        l =0
        r = len(arr)

        while(l<r):
            mid = (l+r)//2
            if arr[mid]>target:
                r = mid
            else:
                l=mid+1
        return l
    ct=0

    for word in words:
        prev = -1
        found = True
        for char in word:
            idx = binary_search(d[char], prev)
            if idx==len(d[char]):
                found=False
                break
            prev =d[char][idx]
        if found:
            ct+=1
    return ct

print(Subsequencecount3(s, words),'method3')

https://github.com/gutty333/Hard-Programming-Challenges/blob/master/27_WildcardCharacters.cpp
https://github.com/AnoshaRehan/Coding-Challenges/blob/main/htmlElements.py
https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/


