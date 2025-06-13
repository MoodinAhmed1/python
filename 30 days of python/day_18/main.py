# Day Regular Expressions
# regular expression or RegEx can help us find patterns in different data types, to use it we must first import it (import re)
import re
#syntax
# re.match(substring, string, re.IGNORECASE)
# substring is what we are looking for, string is where we are looking the string in, re.I ignores casing

txt = 'I love to teach python and javaScript'
not_match = re.match("LOVE", txt, re.I)  # returns none because re.match looks from the start and it starts with i.... not with love.
match = re.match("I LOVE TO TEACH", txt, re.I) # returns place because match() starts looking from the begginging if the string i love....
print(not_match) 
print(match)

print(match.span()) #where does our matching subString start and end
start, end = match.span()
substring = txt[start:end]
print(substring)

#Search()
# unlike match which only looks through but only starting from the begning ... search looks for the substring all throughout our string ... but only return the first match
search = re.search("LOVE", txt, re.I)
start, end = search.span()
substring = txt[start:end]
print(substring)

# findall()
# this fuunction return all matche=s in a list
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
found_list = re.findall("[Pp]ython", txt)
print(found_list)

# sub()
# replaces a substring with a new one
replaced_sentence = re.sub('Python|python', 'javascript', txt)
print(replaced_sentence)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
replaced_sentence = re.sub("%", "", txt)
print(replaced_sentence)

# Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
splited_txt = re.split("\n", txt)
print(splited_txt)

# RegEx variable
# r''
regEx_variable = r"[Aa]pple"
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regEx_variable, txt)
print(matches)

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regEx_variable = r"\d+" #all 1 one more digits
lst_numbers = re.findall(regEx_variable, txt)
print(lst_numbers)

txt = '''Apple and banana are fruits'''
regEx_pattern = r"[a].+" #contains a followed with 1 or more characters ... there for a alone would not show
lst_including_a = re.findall(regEx_pattern, txt)
print(lst_including_a)

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regEx_pattern = r"[Ee]-?[Mm]ail" #E/e, - optinal may or maynot be there, M/mail
result = re.findall(regEx_pattern, txt)
print(result)

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regEx_pattern = r"\d{4}" #contains exactly 4 digits
result = re.findall(regEx_pattern, txt)
print(result)

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r"^[Tt]his"  #including this 
result = re.findall(regex_pattern, txt)
print(result)

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r"[^A-Za-z ]+" # if ^ is inside [] it means negate... meaning dont include the follwoing, in our case A-Za-z and space
result = re.findall(regex_pattern, txt)
print(result)

