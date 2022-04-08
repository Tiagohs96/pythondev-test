periods = [1, 5, 6, 10, 11, 20, 21, 25, 26, 40, 41, 50]
points = [14, 9, 24, 2, 44, 8, 41, 4, 46, 26, 11, 31, 18, 24, 21, 4, 22, 50, 6, 36]

class Period:
    def __init__(self, period_start, period_end):
        self.start = period_start
        self.end = period_end
        self.points = []
        self.point_count = 0

        self.populate_points()

    def populate_points(self):
        for point in points:
            if point > self.start and point < self.end:
                self.points.append(point)
                self.point_count += 1

def generate_period_list():
    period_list = []
    index = 1

    for index in range(1, len(periods)):
        period = Period(periods[index-1], periods[index])
        period_list.append(period)
    
    import pdb;pdb.set_trace()
    return period_list

if __name__ == '__main__':
    period_list = generate_period_list()

