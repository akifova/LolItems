class Champion:
    name = None
    role = None
    recommended_item_list = []

    def __init__(self, name, role, recommended_item_list):
        self.name = name
        self.role = role
        self.recommended_item_list = recommended_item_list

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def get_recommended_item_list(self):
        return self.recommended_item_list
