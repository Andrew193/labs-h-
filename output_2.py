class DataAnalyzer:
  def __init__(self, data):
    self.data = data

  def _calculate_statistics(self):
    total = sum(self.data)
    count = len(self.data)
    return total, count

  def calculate_total(self):
    return self._calculate_statistics()[0]

  def calculate_average(self):
    total, count = self._calculate_statistics()
    return total / count if count != 0 else 0

  def calculate_minimum(self):
    return min(self.data) if self.data else None

  def calculate_maximum(self):
    return max(self.data) if self.data else None
