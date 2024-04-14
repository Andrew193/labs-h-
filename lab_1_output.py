class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.strategies = {
            'A': TypeAStrategy(),
            'B': TypeBStrategy(),
            'C': TypeCStrategy()
        }

    def process_data(self):
        result = []
        for item in self.data:
            strategy = self.strategies[item['type']]
            result.append(strategy.process(item))
        return result

class TypeAStrategy:
    def process(self, item):
        if item['value'] > 100:
            return {'type': 'A', 'value': item['value'] * 2}
        else:
            return {'type': 'A', 'value': item['value']}

class TypeBStrategy:
    def process(self, item):
        if item['value'] < 50:
            return {'type': 'B', 'value': item['value'] * 3}
        else:
            return {'type': 'B', 'value': item['value']}

class TypeCStrategy:
    def process(self, item):
        if item['value'] % 2 == 0:
            return {'type': 'C', 'value': item['value'] + 10}
        else:
            return {'type': 'C', 'value': item['value'] - 5}