import time
import asyncio
import requests

async def function1():
    #await asyncio.sleep(5)
    url = "https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg?auto=compress&cs=tinysrgb&w=600"
    response = requests.get(url)
    open('image1.jpg', 'wb').write(response.content)
    
    print("Function 1 is running")

async def function2():
    #await asyncio.sleep(1)
    url = "https://images.pexels.com/photos/1624496/pexels-photo-1624496.jpeg"
    response = requests.get(url)
    open('image2.jpg', 'wb').write(response.content)

    print("Function 2 is running")

async def function3():
    #await asyncio.sleep(3)
    url = "https://images.pexels.com/photos/1242347/pexels-photo-1242347.jpeg"
    response = requests.get(url)
    open('image3.jpg', 'wb').write(response.content)

    print("Function 3 is running")

#take time to run all functions
# async def main():
#     await function1()
#     await function2()
#     await function3()
async def main():
    await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
#dont take time to run all functions   
if __name__ == "__main__":
    print("Start time:", time.time())
    asyncio.run(main())
    print("End time:", time.time())
