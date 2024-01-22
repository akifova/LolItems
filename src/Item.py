class Item:
    def __init__(self, name, description, stats):
        self.name = name
        self.description = description
        self.stats = stats

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_stats(self):
        return self.stats

    def __str__(self):
        return f"Item(name={self.name}, description={self.description}, stats={self.stats})"