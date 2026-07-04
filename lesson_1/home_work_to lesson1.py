# 1.
# def print_string_reversed(s):
#      if s is None or s.strip() == '':
#          print('Wrong string')
#      else:
#          print(s[::-1])
# print_string_reversed("Shalom")

# 2
# def is_isr_phone_number(phone):
#     if phone is None or phone.strip() == '':
#         return None
#
#     if len(phone) == 10 and phone[0] and phone.isdigit():
#         return True
#     return False
# print(is_isr_phone_number('555555555'))
# print(is_isr_phone_number("0541234567"))
# print(is_isr_phone_number("541234567"))
# print(is_isr_phone_number(""))
# print(is_isr_phone_number(None))
# 4
# def get_words_reversed(words):
#     return " ".join(words.split()[::-1])
# print(get_words_reversed("Hello! World, IBM"))

# 5
# def print_words_reverse_in_column(s):
#     if s is None or s.strip() == "":
#         print("Wrong string")
#         return
#     words = s.split()
#     for word in words:
#         print(word[::-1])
#
# print(print_words_reverse_in_column("Hello my nice World"))
