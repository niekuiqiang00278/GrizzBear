from root.plux.XWrapper import XWrapper
from root.utils.StateUtils import StateUtils


class EvsWrapper(XWrapper):

    def sync_function(self, func, *args, **kwargs):
        state = StateUtils()
        return func(*args, **kwargs, state=state)
