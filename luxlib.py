from typing import Union

def main():
    sum_digits_in_string_list(["1", "2", "3", "4"])
    askuserint("Uh")
    askuserlist("Uh")

def sum_digits_in_string_list(string_list: list[Union[str, int]]):
    total_sum = 0
    for item in string_list:
        try:
            total_sum += int(item)
        except ValueError:
            pass
    return total_sum

def askuserint(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except:
            print("Please enter a number")

def askuserlist(prompt: str, separator: str) -> list:
    while True:
        try:
            return input(prompt).split(separator)
        except:
            print(f"Invalid input. Please enter elements separated by only {separator}.")

if __name__ == "__main__":
    main()