import asyncio

async def my_func():
    print('This is just a function')
    await another_func('demo text')
    print('It waits untill another function run and execute fully!')
    
async def another_func(text):
    await asyncio.sleep(1)
    print('the text is: {}'.format(text))
    

# RuntimeWarning: coroutine 'my_func' was never awaited
# my_func()

# SyntaxError: 'await' outside function
# await my_func()

asyncio.run(my_func())