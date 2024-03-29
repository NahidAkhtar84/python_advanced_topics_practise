import asyncio


async def fetch_data():
    print('Starts fetching....')
    await asyncio.sleep(2)
    print('Done Sleeping...')
    return {'data': 1}
    
async def printing_data():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)
        
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(printing_data())
    
    val = await task1
    print(val)
    await task2
    
asyncio.run(main())