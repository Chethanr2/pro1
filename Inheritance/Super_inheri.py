class vehicle:
    def Start(self):
        print('Starting engine')

    def Stop(self):
        print('Stop engine')


class TwoWheeler(vehicle):
    def Say(self):
        super().Start()
        print('I am TwoWheeler Vehicle')
        super().Stop()

Pulsar = TwoWheeler()
Pulsar.Say()