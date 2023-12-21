def a_function(mandatory, default='Miami', *args, **kwargs):
    print(f'Your mandatory variable: {mandatory}.')
    print(f'Your default variable: {default}.')
    print(f'Your args variable: {args}.')
    print(f'The type of variable for args is: {(type(args))}')
    print(f'Your kwargs variable: {kwargs}.')
    print(f'The type of variable for kwargs is: {(type(kwargs))}')



if __name__ == '__main__':

    name = 'Hector'
    age = 35
    hobbies = ['swimming', 'running', 'F5', 'coding']
    more_info = {'profession': 'cybersecurity', 'city': 'tampa'}

    a_function(name, 1, **more_info)
    print('****************************')

    a_function(name, 'tacos', 'tampa', 305, 40000)
    print('****************************')

    a_function(name, profession='cybersecurity', city='Tampa', 
               balance=40000, birthdate='10/15/2023', season='summer')
    print('****************************')


    '''
    Variables in functions are positional.

    In the function above the first variable is considered mandatory.
    When you activate the function you must pass at least one variable.

    The second variable is what is called a default variable.  If
    nothing is passed in the second position, it will default to what it
    is assigned when you create the function.

    args accepts either nothing or an infinite amount of variables.
    This is so powerful because you can then reference all of those items
    in one variable, and it is collected as a Tuple.

    kwargs accepts either nothing or an infinite combination of key:value
    pairs.  This is incredibly powerful for writing healthy, reusable functions
    when coding API calls, which primarily use JSON for paylod, and JSON is
    just key, value pairs.
    '''