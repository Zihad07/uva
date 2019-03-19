
number_of_data_set = int(input())

while(number_of_data_set):
    x,y  = map(int, input().split())

    if x<y:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")
    
    number_of_data_set -= 1