#list_sort is returned at the end. list_temp stores the temporary values for the sort
list_sort = []
list_temp = []

while True: #makes a list of input numbers
    inp = input()
    
    if inp.isnumeric(): #only appends if the items are numbers
        list_sort.append([int(inp)])
        
    else:
        break

while True: #loops for every layer of the merge
    if len(list_sort) != 1:
        while True: #loops for every list in the merge
            if len(list_sort) > 1:
                list_temp.append([])
                
                while True: #loops for every item in every list
                    if len(list_sort[0])!=0 and len(list_sort[1])!=0: 
                        if list_sort[0][0] > list_sort[1][0]: #compares the first terms of two lists and appends the smallest
                            list_temp[-1].append(list_sort[1][0])
                            del list_sort[1][0]
                            
                        else:
                            list_temp[-1].append(list_sort[0][0])
                            del list_sort[0][0]
                            
                        
                    elif len(list_sort[0])==0: #appends the rest of the 2nd list if it is left over
                        list_temp[-1]+=list_sort[1]
                        break
                        
                    else: #appends the rest of the 1st list if it is left over
                        list_temp[-1]+=list_sort[0]
                        break
                            
            
                del list_sort[0] #deletes the two nested lists of items that have been sorted
                del list_sort[0]
                
            elif len(list_sort) == 1: #appends the final list to the end if there is an odd number
                list_temp.append(list_sort[0])
                del list_sort[0]
                    
            else: #terminates this layer of merging
                break
        
        list_sort = list_temp #reset variables
        list_temp = []
        
        print(list_sort)
        
    else: #terminates once all items have been sorted into one list
        break
