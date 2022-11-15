# Binery search 

def test_location(cards , query, mid):
    mid_number = cards[mid]

    if mid_number == query:
        if mid - 1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found' 
    elif mid_number < query:
        return 'right' 
    else:
        return 'left'

def locate_card(cards , query): 
    low, high = 0 , len(cards) - 1 
    while low <= high:     
        mid = (low + high) // 2 
        result = test_location(cards , query , mid)

        if result == 'found':
            return mid 
        elif result == 'left':
            high = mid - 1 
        elif result == 'right':
            low = mid + 1
    return -1


# creating test cases: 
tests=[] 

#1
tests.append({
    'input' : {
        'cards':[11,22,33,44,55] , 
        'query':44
    } , 
    'output':3
})

#2
tests.append(
    {
        'input':{
            'cards':[123,1,3,1,3,4,5,7,8] , 
            'query':4
        }, 
        'output':5
    }
)

#3 
tests.append(
    {
        'input':{
            'cards':[123,1,3,1,3,4,5,7,8] , 
            'query':55
        }, 
        'output':-1
    }
)

#4 
tests.append(
    {
        'input':{
            'cards':[1,2,3,4,5,6,6,6,6,6,6,6,6,8,9,10] , 
            'query':6
        }, 
        'output':5
    }
)

count=0
for test in tests:
    result = locate_card(**test['input']) == test['output']
    print(f'Test #{count} result: ', result)
    count+=1
