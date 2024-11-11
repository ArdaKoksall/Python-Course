import random



num_list = []

def setlist():
    for i in range(0, 10):
        num_list.append(random.randint(1, 100))


def print_even_index():
    print("Numbers on even indexes:", end=" ")
    for i in range(0, 10):
        if i % 2 == 0:
            print(num_list[i], end=" ")



def print_even_values():
    print("Even numbers:", end=" ")
    for i in range(0, 10):
        if num_list[i] % 2 == 0:
            print(num_list[i], end=" ") 


def print_reverse():
    print("Reversed list:", end=" ")
    for i in range(9, -1, -1):
        print(num_list[i], end=" ")            

def print_first_last():
    print("First and last numbers:", num_list[0], num_list[9])


def main():
    setlist()
    print("Generated list:", num_list)
    print_even_index()
    print()
    print_even_values()
    print()
    print_reverse()
    print()
    print_first_last()


if __name__ == "__main__":
    main()