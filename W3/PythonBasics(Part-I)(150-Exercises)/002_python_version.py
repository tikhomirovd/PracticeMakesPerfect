readme = f"""
----------------------------------------------------------------------------------------------------------------------
Second exercise from: https://www.w3resource.com/python-exercises/python-basic-exercises.php

2. Write a Python program to get the Python version you are using.

Sample Output:

###################################

Python version                                                                                                
3.5.2 (default, Sep 10 2016, 08:21:44)                                                                        
[GCC 5.4.0 20160609]                                                                                          
Version info.                                                                                                 
sys.version_info(major=3, minor=5, micro=2, releaselevel='final', serial=0)

###################################

----------------------------------------------------------------------------------------------------------------------
"""


def get_python_version():
    import sys

    version = sys.version
    info = sys.version_info

    print("\nExercise Output:\n")
    print("###################################\n")
    print(f"Python Version:\n{version}\nVersion Info:\n{info}")
    print("\n###################################")


if __name__ == "__main__":
    print(readme)
    get_python_version()
