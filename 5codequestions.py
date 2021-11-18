def hello_name(username):
    print(f"hello_{username.upper()}")

hello_name("username")
#-----------------------------
def first_odds():
    for x in range(1,101):
        if x % 2 != 0:
            print(x)
first_odds() #calling function

#----------------------------------
def max_num_in_list(a_list):
    print(max(a_list))
max_num_in_list([5, 50]) # put [] inside () so it can read the list

#----------------------------------------


# if the given year is a leap year
# leap year is divisible by 4
# not divisible by 100, unless divisible by 400
# return should be boolean type, if true= true statement, opposite false
def is_leap_year(a_year):
    # This is the function body
    # to combine 2 conditions: and
    #no need for two ifs
    # 4 not % 100 so not == to 0
    # not % 100 syntax:
    #return (boolean)= T/F
    # booleans always Captal T F
    if a_year % 4 == 0 and a_year % 100 != 0:
        if a_year % 400 == 0:
            return True
    elif a_year % 4 != 0:
        return False
    return True # if it doesnt catch any of the ones above
print(is_leap_year(1968))
    
    
#------------------------------

#num is variable (each indiv # in any list)
#a_list is what we want to loop for
# : if you write something with more info coming use :
# consecutive is consistent 
# index [o] getting 1st # in list, counter = 1st # in list
# break= breaking outside of for loop
# for loop run through info given
# index of 0 if 1st # of list

def is_consecutive(a_list):
    counter= a_list[0]
    for num in a_list:
        if num != counter:
            return False
        counter += 1
        # num
    return True

print(is_consecutive([2,3,4,5,6,7]))

