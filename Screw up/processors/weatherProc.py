class WeatherProc:
	def __init__(self):
		pass

	def consume(val):
		ret = ""
		forecasts = val["forecast"]["txt_forecast"]["forecastday"]
		for f in forecasts:
			add = ""
			add += f["title"] + ": " + f["icon"] + "\n\t"
			add += f["fcttext_metric"] + "\n\n"
			ret += add
		return ret
