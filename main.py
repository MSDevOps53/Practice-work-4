from create_file import create_file
from process_file import process_file
from display_file import print_file

file1_name = "TF6_1.txt"
file2_name = "TF6_2.txt"


def main():
    print("TEXT FILE PROCESSING")
    print("Practical work - Variant 6")
    print("--------------------------------")

    if not create_file(file1_name):
        return

    if not process_file(file1_name, file2_name):
        return

    if not print_file(file2_name):
        return

    print("\nProgram completed successfully!")


if __name__ == "__main__":
    main()