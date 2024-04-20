from lib.social_network import *

def test_post_contrusts():
    accounts = Account(1, 'iamcool@gmail.com', 'i_am_cool')
    assert accounts.id == 1
    assert accounts.email == 'iamcool@gmail.com'
    assert accounts.username == 'i_am_cool'

def test_both_are_equal():
    account1 = Account(1, 'iamcool@gmail.com', 'i_am_cool')
    account2 = Account(1, 'iamcool@gmail.com', 'i_am_cool')
    assert account1 == account2

def test_the_format():
    account = Account(1, 'iamcool@gmail.com', 'i_am_cool')
    assert str(account) == "Account(1, iamcool@gmail.com, i_am_cool)"
    