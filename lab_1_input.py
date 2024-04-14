def process_data(data):
    result = []
    for item in data:
        if item['type'] == 'A':
            if item['value'] > 100:
                result.append({'type': 'A', 'value': item['value'] * 2})
            else:
                result.append({'type': 'A', 'value': item['value']})
        elif item['type'] == 'B':
            if item['value'] < 50:
                result.append({'type': 'B', 'value': item['value'] * 3})
            else:
                result.append({'type': 'B', 'value': item['value']})
        elif item['type'] == 'C':
            if item['value'] % 2 == 0:
                result.append({'type': 'C', 'value': item['value'] + 10})
            else:
                result.append({'type': 'C', 'value': item['value'] - 5})
    return result