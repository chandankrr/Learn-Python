dic = {"religion": "the brief in and worship of a superhuman controlling power, especially a personal God or gods.",
       "orthodox": "following or conforming to the traditional or generally accepted rules or beliefs of a religious, philosophy, or practice",
       "computer": "an electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program",
       "WWW": "WWW stand for Word Wide Web, the leading information retrieval service of the Internet"}

print(dic.keys())

word = input("\nEnter word from above list: ")
print(f"\t{word}: {dic[word]}")
