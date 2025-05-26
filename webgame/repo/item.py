from typing import NamedTuple


class ItemDef(NamedTuple):
    itemType: str = 'gear'
    itemId: int = 0
    itemCount: int = 1
    ident: str = 'body'

    def toResponse(self):
        if self.itemType in ['gold', 'starmoney']:
            return {self.itemType: str(self.itemCount)}
        return {
                self.itemType: {
                    str(self.itemId): str(self.itemCount)
                    }
                }
