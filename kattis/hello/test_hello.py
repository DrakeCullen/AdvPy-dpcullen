#!/usr/bin/env python3
from hello import hello

def test_hello():
    assert hello() == "Hello World!" 
    
    print("All test cases passed.")


if __name__ == "__main__":
    test_hello()