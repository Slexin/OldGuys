def isPalindrome(strng):
    if strng.strip() == "":
        print("It's not a palindrome!")
        return
    if strng.lower() == strng.lower()[::-1]:
        print("It's a palindrome!")
    else:
        print("It's NOT a palindrome!")

isPalindrome(input(""))