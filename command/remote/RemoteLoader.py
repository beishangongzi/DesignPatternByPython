from command.remote.CeilingFanOffCommand import CeilingFanOffCommand
from command.remote.CeilingFanOnCommand import CeilingFanOnCommand
from command.remote.GarageDoorDownCommand import GarageDoorDownCommand
from command.remote.GarageDoorUpCommand import GarageDoorUpCommand
from command.remote.LightOffCommand import LightOffCommand
from command.remote.LightOnCommand import LightOnCommand
from command.remote.CeilingFan import CeilingFan
from command.remote.GarageDoor import GarageDoor
from command.remote.Light import Light
from command.remote.RemoteControl import RemoteControl


class RemoteLoader:
    def main(self):
        remoteControl = RemoteControl()
        livingRoomLight = Light("living Room")
        kitchenLight = Light("kitchen")
        ceilingFan = CeilingFan("Living Room")
        garageDoor = GarageDoor("Garage")

        livingRoomLightOn = LightOnCommand(livingRoomLight)
        livingRoomLightOff = LightOffCommand(livingRoomLight)
        kitchenLightOn = LightOffCommand(kitchenLight)
        kitchenLightOff = LightOffCommand(kitchenLight)
        ceilingFanOff = CeilingFanOffCommand(ceilingFan)
        ceilingFanOn = CeilingFanOnCommand(ceilingFan)
        garageDoorUp = GarageDoorUpCommand(garageDoor)
        garageDoorOnDown = GarageDoorDownCommand(garageDoor)

        remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff)
        remoteControl.setCommand(1, kitchenLightOn, kitchenLightOff)
        remoteControl.setCommand(2, ceilingFanOn, ceilingFanOff)
        remoteControl.setCommand(3, garageDoorUp, garageDoorOnDown)

        print(remoteControl)
        remoteControl.onButtonWasPushed(0)
        remoteControl.offButtonWasPushed(0)
        remoteControl.onButtonWasPushed(1)
        remoteControl.offButtonWasPushed(1)
        remoteControl.onButtonWasPushed(2)
        remoteControl.offButtonWasPushed(2)
        remoteControl.onButtonWasPushed(3)
        remoteControl.offButtonWasPushed(3)



if __name__ == '__main__':
    r = RemoteLoader()
    r.main()
