from stats import report_maker
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path_of_file = sys.argv[1]

report_maker(path_of_file)
