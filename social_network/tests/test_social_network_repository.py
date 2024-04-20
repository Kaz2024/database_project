from lib.social_network import *
from lib.social_network_repository import *

def test_all_in_social_network(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    result = repository.all()
    assert result == [
        Account(1, 'iamcool@gmail.com', 'i_am_cool'),
        Account(2, 'tired@gmail.com', 'i_am_tired'),
        Account(3, 'icecream@gmail.com', 'i_am_icecream')]
    
def test_find_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    result = repository.find(1)
    assert result == Account(1, 'iamcool@gmail.com', 'i_am_cool')

# def test_get_post_counts(db_connection):
#     db_connection.seed("seeds/social_network.sql")
#     repository = AccountRepository(db_connection)
#     result = repository.get_post_counts
#     assert result == {"i_am_cool" :2,
#                     "i_am_tired" :0,
#                     "i_am_icecream":1}

def test_create_accounts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    account = Account(None, 'i_am_cooofe@gmail.com', 'I_am_cooofe')
    assert repository.create(account) is None
    result = repository.all()
    # result = repository.create(Account(None, 'i_am_cooofe@gmail.com', 'I_am_cooofe'))
    assert result == [
        Account(1, 'iamcool@gmail.com', 'i_am_cool'),
        Account(2, 'tired@gmail.com', 'i_am_tired'),
        Account(3, 'icecream@gmail.com', 'i_am_icecream'),
        Account(4, 'i_am_cooofe@gmail.com', 'I_am_cooofe')
    ]

def test_delete_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    repository.delete(5)
    result = repository.all()
    assert result == [
        Account(1, 'iamcool@gmail.com', 'i_am_cool'),
        Account(2, 'tired@gmail.com', 'i_am_tired'),
        Account(3, 'icecream@gmail.com', 'i_am_icecream')
    ]
