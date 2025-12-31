class Palindrome:
    def Palindrome_count(self,s):
        n = len(s)
        palindrome = set()
        for mask in range(1,1 << n):
            subsequence = ""
            for i in range(n):
                if mask & (1 << i):
                    subsequence += s[i]
            if subsequence == subsequence[::-1]:
                palindrome.add(subsequence)
        print("\nPalindromic Subsequences:")
        for p in sorted(palindrome):
            print(p)
        print("\nCount of Palindrome Subsequences: ",len(palindrome))
s = str(input("Enter the string :: "))
P = Palindrome()
print("Count of Palindromic Subsequences",P.Palindrome_count(s))