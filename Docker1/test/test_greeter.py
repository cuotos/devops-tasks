import pytest
import greeter

def test_can_print_hello_world():

  actual = greeter.get_hello("dan")

  assert actual == "Hello dan"