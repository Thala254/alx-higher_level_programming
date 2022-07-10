# 0x0C. Python - Almost a circle

This project is a review of few concepts learnt so far in Python:
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file
- args and kwargs
- Serialization/Deserialization
- JSON

## Resources
- [args/kwargs](https://alx-intranet.hbtn.io/rltoken/7gc6UzxSL81HcuAwklUbuQ)
- [JSON encoder and decoder](https://alx-intranet.hbtn.io/rltoken/rGVU9mt57rVURGnjK6n4_Q)
- [unittest module](https://alx-intranet.hbtn.io/rltoken/soictNXCPE18ASL3INoeew)
- [Python test cheatsheet](https://alx-intranet.hbtn.io/rltoken/uI9iskBCcNo5pc7j9Vy86A)

## Objectives
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Tasks
- **[models](models)** - package for classes used in the project
  - **[base.py](models/base.py)** - Contains the base class `Base`
  - **[rectangle.py](models/rectangle.py)** - Contains the class `Rectangle`, a subclass of `Base`
  - **[square.py](models/square.py)** - Contains the class `Square`, a subclass of `Rectangle`
- **[tests](tests)**
  - **[test_models](tests/test_models)** - Test package for the project
    - **[test_base.py](tests/test_models/test_base.py)** - Test suite for the class `Base`
    - **[test_rectangle.py](tests/test_models/test_rectangle.py)** - Test suite for the class `Rectangle`
    - **[test_square.py](tests/test_models/test_square.py)** - Test suite for the class `Square`
