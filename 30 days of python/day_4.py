string1 = ['30', 'days', 'of', 'python']
print(f"#1&2 {" ".join(string1)}")

print("\n")
company = "Coding For All" #3
# String formatting
print(f'#4 original : {company}')
print(f'#5 length : {len(company)}')
print(f'#6 upper : {company.upper()}')
print(f'#7 lower : {company.lower()}')
print(f'#8 capitalize : {company.capitalize()}')
print(f'\ttitle : {company.title()}')
print(f'\tswapcase : {company.swapcase()}')

print("\n")
print(f'#9 first word : {company[0:6]}') #slicing (output: first word : Coding)
print(f"#10 index found at : {company.find('Coding')}") #finding (output : 0)
print(f'\t index found at :{company.index('Coding')}') #indexing but unlike find if the substring was not found it gives an error

print('\n')
print(f'#11 {company.replace('Coding', 'Python')}') #replaces
print(f'#12 {company.replace('Coding', 'Python').replace('All','Everyone')}') #replaces two things atonce by chaining

print("\n")
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_list = companies.split(",")
print(f"#14 {companies_list}")

print('\n')
print(f"#15 character at 0 : {company[0]}")
print(f"#16 last index : {company[-1]}")
print(f"#17 character at index 10 : {company[10]}")

print('\n')
pyhton_acronym = "P4A"
print(f"#18 {pyhton_acronym}")
another_acronym = "C4A"
print(f"#19 {another_acronym}")

print('\n')
print(f"#20 first accurance of C : {company.index("C")}")
print(f"#21 first accurance of F : {company.index("F")}")
print(f"#22 last acurance of l : {company.rfind("l")}")

print("\n")
sentence = "You cannot end a sentence with because because because is a conjunction"
print(f"#23 first accurance of \"because\" in the following sentece \"{sentence}\" : {sentence.index("because")}")
print(f"#24 last accurance of \"because\" in the following sentece \"{sentence}\" : {sentence.rindex("because")}")
print(f"#25 strip out because from the sentence : {sentence.replace("because because because", "")}")
print(f"#26 the first occurance of \"because\" : {sentence.find("because")}")


print("\n")
print(f"#28 Does 'Coding For All' start with a substring Coding? : {company.startswith("Coding")}")
print(f"#29 Does 'Coding For All' end with a substring coding? : {company.endswith("coding")}")

print('\n')
print(f"#30 striping spaces from \'   Coding For All      \' : {'   Coding For All      '.strip()}")

print('\n')
print("""#31 Which one of the following variables return True when we use the method isidentifier():
        30DaysOfPython
        thirty_days_of_python""")
print(f"asnwer is the second one, because the first one cant be a variable name : {"thirty_days_of_python".isidentifier()}")

print("\n")
print(f"#32 .join() : {' #'.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])}")

print("\n#34")
print(f"  name   \t age \t country \t city")
print(f"mohammed \t 22 \t Ethiopia \t Addis Ababa")