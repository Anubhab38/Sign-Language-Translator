import asyncio

from viam.robot.client import RobotClient
from viam.components.camera import Camera
from viam.services.vision import VisionClient
from viam.services.mlmodel import MLModelClient


async def connect():
    opts = RobotClient.Options.with_api_key(

        api_key='zuvjajd71m2uyork69zj82mpqum0ba6m',

        api_key_id='007cfa7e-a62c-4402-a286-989d078e2a4b'
    )
    return await RobotClient.at_address('signlanguagetranslator-main.8fg7gzw5ei.viam.cloud', opts)


async def main():
    machine = await connect()

    print('Resources:')
    print(machine.resource_names)

    # camera
    camera = Camera.from_robot(machine, "camera")
    camera_return_value = await camera.get_image()
    print(f"camera get_image return value: {camera_return_value}")

    # vision
    vision = VisionClient.from_robot(machine, "vision")
    vision_return_value = await vision.get_properties()
    print(f"vision get_properties return value: {vision_return_value}")

    # mlmodel
    mlmodel = MLModelClient.from_robot(machine, "mlmodel")
    mlmodel_return_value = await mlmodel.metadata()
    print(f"mlmodel metadata return value: {mlmodel_return_value}")

    # Don't forget to close the machine when you're done!
    await machine.close()


if __name__ == '__main__':
    asyncio.run(main())
