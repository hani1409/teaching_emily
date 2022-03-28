def main():

    eList = ['Hani', 'Bridget', 'Emily', 'Gabby', 'Luke', 'Tata', 'Gedo', 'Grammy', 'Poppy']

    print('********************************************')
    for x in eList:
        if x == 'Luke':
            print('*********')
            print('* %s * '%x)
            print('*********')
        else:
            continue
    print('********************************************')

    obj1    = 12345
    obj2    = 'Test test test'
    obj3    = 'Cute Cute Cute'
    obj4    = obj1
    
    print(obj1)
if __name__ == '__main__':
    main()