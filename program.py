# IMPORT APP PACKAGES
# ///////////////////////////////////////////////////////////////
from mavsdk import System
from qasync import asyncSlot # asyncClose

class program:
    def __init__(self):
        self.connected = True

@asyncSlot()
async def connect_drone():
    print("IT WORKED!!!")
    drone = System()
    await drone.connect()  # default arg: system_address="udp://:14540"

    print("-- Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("---- Connected!")
            break
