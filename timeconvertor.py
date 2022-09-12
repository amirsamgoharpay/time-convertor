def convert(seconds):
	hours = seconds // 3600
	mins  = seconds%3600//60
	sec = seconds - (hours * 3600) - (mins * 60)
	if len(str(hours)) == 1 :
		hours = "0" + str(hours)
	if len(str(mins)) == 1 :
		mins = "0" + str(mins)	
	if len(str(sec)) == 1 :
		sec = "0" + str(sec)
	return f"{hours}:{mins}:{sec}"

if __name__ == "__main__" :
	seconds = int(input("type the seconds : "))
	result = convert(seconds)
	print(result)