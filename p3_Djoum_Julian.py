def find_dup_str(s,n):
    length = len(s)
    userN = n
    m = n
    # These are incremented every time the tempString is updated
    tempStartIndex = 0
    tempEndIndex = n
    # The total number of times a comparison has been made
    checkNum = 0
    checkStartIndex = 1
    checkStartIndex2 = checkStartIndex
    
    for tempStartIndex in range(length-n):
        # Save the first n letters of the substring
        tempString = s[tempStartIndex:tempEndIndex]
        print("\n*********Comparison Starts With this tempString*********")
        print("\nCurrent Temporary String: ")
        print(tempString)
        
        # Compare if the first n letters that I saved are found anywhere else through
        # out the string
        
        # n gets reset to original value
        n = m
        checkStartIndex = checkStartIndex2
        while(n != length):
            #print("New Check Start Index Value:", checkStartIndex)
            #print("New Temp End Index Value:", n)
            print("\nCurrent Substring of myString: ")
            print(s[checkStartIndex:n+1])
            if(s[checkStartIndex:n+1] == tempString):
                print("\nMatch Found after: ", checkNum, "unsuccessful attempt(s)!")
                return tempString
            else:
                print("\nMatch not found.")
                checkNum += 1
                checkStartIndex += 1
                n += 1
                print("\nUnsuccessful check number: ", checkNum)
                #print("Start index of current myString check:", checkStartIndex-1)
                continue
        # If the substring isn't found the first time through then iterate the new tempString
        print("\nThe tempString of: ", tempString, " was not found duplicated in: ", s)
        #print("\nLet's try this over again with a new tempString for attempt number: ", tempStartIndex+2)
        tempStartIndex += 1
        tempEndIndex += 1
        checkStartIndex2 += 1
        m += 1
    #print("\nThere was no duplicate substring of length",userN,"found in the ",s,"string.")
    return ""

def find_max_dups(s):
    print("\n*********Finding the Max Duplicated Substring*********")
    subStringLength = len(s)
    count = 0
    i = 0
    n = 1
    for n in range(subStringLength-1):
        if(find_dup_str(s, n) != ""):
            print("\nDuplicate found in the string, count is incremented.")
            count += 1
            i = n
        else:
            #print("\nNo duplicate substring of length: ",n," found, on to the next potential n value.")
            n += 1
    if(count == 0):
        print("\nNo duplicates found in the string at all.")
        return ""
    if(count > 0):
        print("\n=== The max number of duplicates found in the string is:", count,"===")
        return find_dup_str(s,i), count
        
print("Welcome to the Duplicate Substring Finder!")
# Problem 3 Part A Code
s = input("Enter the string that you want to use: ")
n = int(input("Enter the length of the duplicate substring that you want to find: "))
find_dup_str(s, n)

# Problem 3 Part B Code
s2 = input("Enter the string that you want to use find the max duplicates in: ")
s3, newCount = find_max_dups(s2)
print("\n=== The max number of duplicates found in the string is:", newCount,"===")
