# About

Quantum cryptography basics [here](https://youtu.be/6H_9l9N3IXU?t=448).

What is [BB84](https://en.wikipedia.org/wiki/BB84) ??

# Usage

```
usage: main.py [-h] [-v] [-e] key_amount key_size

Quantum key distribution with protocol BB84

positional arguments:
  key_amount     Amount of keys to create
  key_size       Size of each key in bytes

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Verbose output
  -e, --eve      Eve is present
```

# Example

Without eve:
```
./main.py 10000 3
Eve detected 0/10000 times
```

With eve:
```
./main.py 10000 3 --eve
Eve detected 9989/10000 times
```

With verbose output enabled:
```
./main.py 3 16 --verbose
 Alice's key: [147, 183, 224, 125, 185, 53, 171, 36, 126, 3, 17, 93, 226, 211, 178, 239]
 Bob's key:   [147, 183, 224, 125, 185, 53, 171, 36, 126, 3, 17, 93, 226, 211, 178, 239]
 Eve detected: False
 Eve detected 0/3 times

 Alice's key: [176, 145, 185, 233, 151, 169, 46, 216, 99, 98, 6, 85, 138, 71, 51, 44]
 Bob's key:   [176, 145, 185, 233, 151, 169, 46, 216, 99, 98, 6, 85, 138, 71, 51, 44]
 Eve detected: False
 Eve detected 0/3 times

 Alice's key: [173, 84, 23, 125, 193, 112, 40, 201, 215, 50, 89, 136, 251, 215, 248, 154]
 Bob's key:   [173, 84, 23, 125, 193, 112, 40, 201, 215, 50, 89, 136, 251, 215, 248, 154]
 Eve detected: False
 Eve detected 0/3 times

Eve detected 0/3 times
```


