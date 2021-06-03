import asyncio

async def my_func():
    print('This is just a function')
    task = asyncio.create_task(another_func('demo text'))
    
    # If we add await to task then it will wait
    # await task
    
    print('It does not wait to execute for another func, because we created a task and do not mention to wait.')
    
async def another_func(text):
    print('the text is: {}'.format(text))
    await asyncio.sleep(1)
    
    

# RuntimeWarning: coroutine 'my_func' was never awaited
# my_func()

# SyntaxError: 'await' outside function
# await my_func()

asyncio.run(my_func())