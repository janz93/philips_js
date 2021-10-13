import asyncio
import logging
from haphilipsjs import ConnectionFailure, PhilipsTV

logging.basicConfig(level=logging.DEBUG)

async def main():
    tv = PhilipsTV("192.168.178.22", 6)
    await tv.setTransport(True)
    data = await tv.getSystem()
    print("system data:\n")
    state = await tv.pairRequest("my_test_app", "My Test App", "mox", "OSX", "native")

    pin = input("Enter pin:")

    username, password = await tv.pairGrant(state, pin)

    print(username)
    print(password)

    channels = await tv.getChannelLists()
    print("Channel list:\n")
    print(channels)
    application = await tv.getApplication()
    print("current application:\n")
    print(application)
    screenstate = await tv.getScreenState()
    print('current screenstate:\n')
    print(screenstate)
    powerState = await tv.getPowerState()
    print('current powerstate:\n')
    print(powerState)
    powerState = await tv.getScreenState()
    print('current powerstate:\n')
    print(powerState)


asyncio.run(main())