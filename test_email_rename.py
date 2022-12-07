import pytest
from email_rename import strip_name, compare_email
from mock_emails import mock_long_matching_email, \
     mock_short_matching_email,\
     mock_partial_matching_email,\
     mock_non_matching_email,\
     mock_matching_email_unique_attachment

#strip_name tests

def test_normal_two_word_name():
    assert strip_name("John Doe") == "DoeJ"

def test_email_address_with_name_colon_separator():
    assert strip_name("John.Doe@test.com") == "DoeJ"

def test_larger_than_three_word_name():
    assert strip_name("John Jay Doe") == "DoeJ"

def test_lowercase_name():
    assert strip_name("john doe") == "DoeJ"

def test_comma_separated_name():
    assert strip_name("Doe,John") == "DoeJ"    

def test_colon_separated_name():
    assert strip_name("John.Doe") == "DoeJ"

def test_name_with_special_characters():
    assert strip_name("'-John Doe!!'$") == "DoeJ"

def test_email_address_with_amalgamated_name():
    assert strip_name("jdoe@test.com") == "Jdoe"

def test_amalgamated_name():
    assert strip_name("jdoe") == "Jdoe"

def test_blank_name():
    assert strip_name("") == False

def test_name_and_email_address():
    assert strip_name("John Doe <jdoe@test.com.au>") == 'DoeJ'

#compare_email tests

def test_compare_same_emails():
    assert compare_email(mock_long_matching_email,
                         mock_long_matching_email) == 'duplicate'

def test_compare_long_short_email():
    assert compare_email(mock_long_matching_email,
                         mock_short_matching_email) == False

def test_matching_email():
    assert compare_email(mock_short_matching_email,
                         mock_long_matching_email) == True

def test_non_matching_email():
    assert compare_email(mock_short_matching_email,
                         mock_non_matching_email) == False

def test_unique_attachment():
    assert compare_email(mock_matching_email_unique_attachment,
                         mock_long_matching_email) == False

def test_partial_matching_email():
    assert compare_email(mock_partial_matching_email,
                          mock_long_matching_email) == False

    
    

    
