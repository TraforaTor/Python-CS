s = input('Input your string:')
if s.isalpha() :
    print('Contains only letters')
if s.isupper() :
    print('Contains only capital letters')
if s.islower() :
    print('Contains only lowercase letters')
if s.isdecimal() :
    print('Contains only decimal numeric digits')
if s.isalnum() :
    print('Contains only letters and/or digits')
if s[0].isupper() :
    print('It starts with a capital letter')
if s[-1] == '.' :
    print('Ends with a point')