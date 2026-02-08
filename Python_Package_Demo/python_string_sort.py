def sort_strings_using_sorted(inp_str):
    return "".join(sorted(inp_str))

if __name__ == "__main__":
    inp_str = "bbccdefbbaa"
    print("Original String:", inp_str)
    print("Sorted String:", sort_strings_using_sorted(inp_str))