class Item:
    def __init__(self,id, item_name, item_price, item_quantity):
        self.id = id
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def __str__(self):
        return f"{self.item_name} | {self.item_price} | {self.item_quantity}"

    @classmethod
    def from_db(cls, row:dict):
        if not row:
            return None

        return cls(row.get("id"),
                   row.get("item_name"),
                   row.get("item_price"),
                   row.get("item_quantity")
        )