# --- TEXT FILE WORD COUNTER ---

filename = "sample.txt"
user_file_name = input("Enter the name of the file: ")
if len(user_file_name) > 1:
    filename = user_file_name



with open(filename, "r", encoding='utf-8') as file:
    text = file.read()
    word_count = len(text.split())
    characters = len(text)
    characters_no_spaces = len(text.replace(" ", ""))
    print(f"Word count: {word_count}")
    print(f"Characters: {characters}")
    print(f"Characters (no spaces): {characters_no_spaces}")



