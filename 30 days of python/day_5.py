#Exercise 1

print('\n')
    #1 declare an empty list
lst = [] 
    #2 declare a list with more than 5 items
lst2 = [1, 2, 3, 4, 5, 6]
    #3 length
print(len(lst2))
    #4 first, middle and last items
first_index = 0
middle_index = len(lst2) // 2
last_index = len(lst2) - 1
print(f"First item : {lst2[first_index]} \t Middle item : {lst2[middle_index]} \t Last item : {lst2[last_index]}")

    #5 name, age, height, marital status, address
mixed_data_type = ["mohammed", 22, 1.77, False, "Ferencay"]

print('\n')
    #6 Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

    #7 print the list
print(it_companies)

    #8 print the number of companies in the list
print(f"number of companies : {len(it_companies)}")

    #9 print first, middle and last elements
print(f"First item : {it_companies[0]} \t Middle item : {it_companies[len(it_companies) // 2]} \t Last item : {it_companies[-1]}")

    #10 chane one of the companies and print it
it_companies[0] = "Nvidia"
print(it_companies)

    #11 add an it company to it_companies
it_companies.append("Facebook")
print(it_companies)

    #12 insert a company at the middle of the list
it_companies.insert(len(it_companies) // 2, "Intel")
print(it_companies)

    #13 change one of the th companies to upperCase
it_companies[4] = it_companies[4].upper();
print(it_companies)

    #14 join the companies list with the  '#;  ' string
print('#;  '.join(it_companies))

    #15 check if one of the companies exists in the list
print("Nvidia" in it_companies)

    #16 sort the list
it_companies.sort()
print(it_companies)

    #17 sort the list in decending
it_companies.sort(reverse=True)
print(it_companies)

    #18 slice out the first 3 elements
print(it_companies[:3])

    #19 slice out the last three elements
print(it_companies[-3:])

    #20 slice out the middle element
print(it_companies[len(it_companies) // 2 : (len(it_companies)//2) + 1])

    #21 remove the first element 
del it_companies[0]
print(it_companies)

    #22 remove the middle element or elements from the list
length = len(it_companies)
mid = length // 2
if (len(it_companies) % 2 == 0):
    del it_companies[mid-1 : mid+1]
else:
    del it_companies[mid]
print(it_companies)
    #23 remove the last company
del it_companies[-1]
print(it_companies)

    #24 remove all it companies from the list
it_companies.clear()
print(it_companies)

    #25 destroy the it_companies list
del it_companies

print('\n')
    #26 join the following list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

    #27 insert python and redux
full_stack.append("python")
full_stack.append("redux")
print(full_stack)



#EXERCISE 2
    #solve the following 

age = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    #1 find the min and max age by sorting
age.sort()
min_age = age[0]
max_age = age[-1]
print(f"min age : {min_age} \t max age : {max_age}")

    #2 add the min and max age to the list again
age.append(min_age)
age.append(max_age)
print(age)

    #3 find the midian
length = len(age)
mid = length // 2
if(length % 2 == 0): 
    midian = (age[mid - 1] + age[mid]) / 2
else:
    midian = age[mid]
print(f"midian : {midian}")

    #4 find the average
total = sum(age)
average = total / length
print(f"average age : {average}")

    #5 range
age.sort()
range = age[-1] - age[0] 
print(f"range : {range}")

print("\n")
    #1 print the middle country/countries
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
length = len(countries)
mid = length // 2
if(length % 2 == 0):
    middle_countries = countries[mid-1:mid+1]
else: 
    middle_countries = countries[mid]
print(middle_countries)

    #2 devide the list into two equal parts
if(length % 2 == 0):
    first_half = countries[:mid]
    second_half = countries[mid:]
else: 
    first_half = countries[:mid+1]
    second_half = countries[mid+1:]
print("\n")
print(f"first half : {", ".join(first_half)}")
print(f"length of first half : {len(first_half)}")
print("\n")
print(f"second half : {", ".join(second_half)}")
print(f"length of second half : {len(second_half)}")

print("\n")
#-1 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
china, russia, USA, *rest = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(china, russia, USA, "\n", *rest)