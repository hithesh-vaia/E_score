
value=95
p5=10
p95=15
winsorized_value = min(max(value, p5), p95)


winsorized_percentile= (winsorized_value - p5)/(p95-p5)