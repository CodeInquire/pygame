class Item:

    def __init__(self, tag, name, desc, value=None, effect=None):

        self.tag = tag
        self.name = name
        self.desc = desc
        self.value = value
        self.effect = effect

    def use(self, onWho):

        return self.effect(onWho)

    
