from parlindrome_int import is_palindrome
import pytest

class TestPalindrome(object):
    def test_negative_value(self):
        assert is_palindrome(int(-1))==False
        assert is_palindrome(int(-9999))==False

    def test_single_digit(self):
        assert is_palindrome(int(0))==True
        assert is_palindrome(int(9))==True

    def test_normal_value(self):
        assert is_palindrome(int(121))==True
        assert is_palindrome(int(12321))==True
        assert is_palindrome(int(123456))==False
        assert is_palindrome(int(999999999))==True

    def test_zero_ending_value(self):
        assert is_palindrome(int(10))==False
        assert is_palindrome(int(1000))==False