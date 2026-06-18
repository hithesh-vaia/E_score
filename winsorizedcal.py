



def calc_winsorized_score(value:float,p5:float,p95:float):
    winsorized_value = min(max(value, p5), p95)
    winsorized_percentile= (winsorized_value - p5)/(p95-p5)
    return winsorized_percentile