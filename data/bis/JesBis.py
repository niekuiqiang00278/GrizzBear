from data.base.wrapper.EvsWrapper import EvsWrapper
from root.utils.StateUtils import StateUtils
from root.plux.XState import XSkin

class JesHit:
    def __init__(self):
        pass
    @XSkin()
    def km0(self,state:StateUtils):
        print('km0')
        state.errn('fff')
    @XSkin()
    def km1(self, state: StateUtils):
        print('km1')
class JesBis(JesHit):
    def __init__(self):
        JesHit.__init__(self)

    @EvsWrapper()
    def k0(self,state:StateUtils):
        self.km0(state=state)
        self.km1(state=state)

if __name__ == '__main__':
    JesBis().k0()