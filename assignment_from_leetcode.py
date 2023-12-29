# -*- coding: utf-8 -*-
"""Assignment from leetcode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KsfZ_XN0IwTM0EB67JIgudDSstbSlGbZ

**1**  You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

def mergeletters(word1,word2):
  word=""
  for i in range(min(len1,len2)):
    word+=word1[i]+word2[i]
  if len1>len2:
    word+=word1[i+1:]
  elif len2>len1:
    word+=word2[i+1:]
  return word


word1=input("Enter first word : ")
len1=len(word1)
word2=input("Enter second word : ")
len2=len(word2)

mergeletters(word1,word2)

"""**2** Youare given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.
"""

class Solution(object):
    def findTheDifference(self, s:str, t:str)->str:
      self.s=s
      self.t=t
      dict1={}
      for letter in t:
        if letter in dict1:
          dict1[letter]+=1
        else:
          dict1[letter]=1
      #subtract letters in t
      for letter in s:
        dict1[letter]-=1

      for letter,number in dict1.items():
        if number==1:
          return letter

obj=Solution()
s="pqrst"
t="pqrstu"

obj.findTheDifference(s,t)

"""**3** Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack."""

haystack=input("Enter the first string : ")
needle=input("Enter the second string : ")

if needle in haystack:
  print (haystack.index(needle))
else:
  print (-1)

"""**4** Given two strings s and t, return true if t is an anagram of s, and false otherwise.

"""

class Solution(object):
    def isAnagram(self, s:str, t:str):
        if len(s)==len(t):
          for i in range(len(s)):
            if t[i] in s:
              p=0
            else:
              p=1
          if p==0:
            return True
          else:
            return False
        return False


obj=Solution()
s=input("Enter first string : ")
t=input("Enter second string : ")
obj.isAnagram(s,t)

"""Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together."""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        self.s=s

"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
  
"""

class Solution(object):
    def moveZeroes(self, nums):
        newnum = nums[:]  # Make a copy of nums

        j = len(nums) - 1
        k = 0

        for i in nums:
            if i == 0:
                newnum[j] = i
                j = j - 1
            else:
                newnum[k] = i
                k = k + 1

        return newnum

nums = [1, 2, 0, 3, 0, 4, 5]
obj = Solution()
result = obj.moveZeroes(nums)
print(result)

"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution(object):
    def plusOne(self, digits):
      num=int("".join(map(str,digits)))
      num+=1
      return [int (n) for n in str(num)]

obj=Solution()
digits=[9]
obj.plusOne(digits)

"""There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""

class Solution(object):
    def arraySign(self, nums):
      self.nums=nums
      p=1
      for i in nums:
        p*=i
      return p
    def signFunc(self,x):
      self.x=x
      if x>0:
        return 1
      elif x<0:
        return -1
      else:
        return 0


obj=Solution()
nums=[-1,-2,-3,-4,3,2,1]
x=obj.arraySign(nums)
obj.signFunc(x)

"""A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.


"""

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
      self.arr=arr
      arr.sort()
      diff=arr[1]-arr[0]
      for i in range(2,len(arr)):
        if (arr[i]-arr[i-1])!= diff:
          return False
        else:
          return True




obj=Solution()
arr=[1,5,3]
obj.canMakeArithmeticProgression(arr)

"""An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.


"""

class Solution(object):
    def isMonotonic(self, nums):
      self.nums=nums
      increasing = decreasing = True
      for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
          increasing = False
        elif nums[i] > nums[i-1]:
          decreasing = False
      return increasing or decreasing


obj=Solution()
nums=[1, 3, 2]
obj.isMonotonic(nums)

"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

class Solution(object):
    def romanToInt(self, s):
      self.s=s


      roman={ "I":1,
              "V":5,
              "X":10,
              "L":50,
              "C":100,
              "D":500,
              "M":1000}
      summ= 0
      for i in range(len(s)-1,-1,-1):
        num = roman[s[i]]
        if 3*num < summ:
          summ = summ-num
        else:
          summ = summ+num
      return summ




obj=Solution()
num="IX"
obj.romanToInt(num)