#add somethign to shopping list
#Origin shopping list
shopping_list = ["apples", "cherries"]

#defining add_to_list function
def add_to_list(item):
    shopping_list.append(item) #add one item to the list
    return shopping_list #return back to new list with new item

def check_duplicate(item):
    if item not in shopping_list:
        add_to_list(item)
    else: 
        print "you already added that dodo!"
    return shopping_list


def main():

    print check_duplicate("bananas")
    

if __name__ == '__main__':
    main()