'''Ori Weis'''
29.4.21
from numpy import *
import math
def ret_sum(A):
    sum=0
    for i in A:
        sum+=i
    return sum

'''Targil 1'''
def input_from_user():
    list1=[]
    print("enter numbers for addition enter stop to stop\n")
    inpstr=input("")
    while(inpstr!="stop"):
        list1.append(int(inpstr))
        inpstr = input("")
    sum=sum_of_array(list1)
    return sum

def sum_of_array(list1):
    sum=0
    for i in list1:
        sum+=i
    print("sum is : "+str(sum))
    return sum

'''Targil 2'''
def tictactoeSolver(mat):
    if (mat[0][0]== mat[0][1]== mat[0][1]==1) or (mat[1][0]== mat[1][1]== mat[2][1]==1) or \
            (mat[2][0]== mat[2][1]== mat[2][2]==1):
        print("Player 1 won the game")
    elif(mat[0][0]== mat[1][0]== mat[2][0]==1) or (mat[1][0]== mat[1][1]== mat[2][1]==1) or \
            (mat[0][2]== mat[1][2]== mat[2][2]==1):
        print("Player 1 won the game")
    elif (mat[0][0] == mat[1][1] == mat[2][2] == 1) or (mat[2][0] == mat[1][1] == mat[2][0] == 1) :
        print("Player 1 won the game")

    elif (mat[0][0]== mat[0][1]== mat[0][1]==2) or (mat[1][0]== mat[1][1]== mat[2][1]==2) or \
            (mat[2][0]== mat[2][1]== mat[2][2]==2):
        print("Player 2 won the game")
    elif(mat[0][0]== mat[1][0]== mat[2][0]==2) or (mat[1][0]== mat[1][1]== mat[2][1]==2) or \
            (mat[0][2]== mat[1][2]== mat[2][2]==2):
        print("Player 2 won the game")
    elif (mat[0][0] == mat[1][1] == mat[2][2] == 2) or (mat[2][0] == mat[1][1] == mat[2][0] == 2) :
        print("Player 2 won the game")

    else:
        print("tie")

'''Targil 3'''
def compress_string():
    str1=input("Enter String To compress ")
    new_str=""
    count=1
    for i in range(len(str1)-1):
        if(str1[i]==str1[i+1]):
            count+=1
        else:
            new_str+=str1[i]
            new_str+=str(count)
            count=0
    new_str += str1[i]
    new_str += str(count)
    print(new_str)
    return new_str

'''Targil 4'''
def roundup(x):
    return int(math.ceil(x / 10.0)) * 10
def is_valid_ID(id):
    dup=1
    sum=0
    if(len(id)!=9 or id==""):
        return False
    for i in range(len(id)-1):
        addi=dup*int(id[i])#addi is the potential addition
        if(addi>9):
            addi=addi%10+int(addi/10)
        sum+=addi
        if(dup==1):
            dup=2
        else:
            dup=1
    sifra=roundup(sum)-sum
    if(sifra==int(id[len(id)-1])):
        return True
    else:
        return False

'''Targil 5'''
def function1(num):
    return num*num
def map_Func(list1, function1):
    return [function1(item) for item in list1]

'''main Function To Run'''
def main():
    print("Ori Weis's Project\n")

    '''Targil 1'''
    input_from_user()

    '''Targil 2'''
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]
    print(game)
    tictactoeSolver(game)

    '''Targil 3'''
    compress_string()

    '''Targil 4'''
    id = input("Enter ID For ID Checking ")
    print(is_valid_ID(id))

    '''Targil 5'''

    my_list=[1,2,3,4,5,6,7,8,9,10]
    my_list=map_Func(my_list,function1)
    print(my_list)

#calling For main Function
main()

