from parlindrome_int import is_palindrome
import sys

def main(argv):
    print(is_palindrome(int(argv[0])))

if __name__=='__main__':
    main(sys.argv[1:])

