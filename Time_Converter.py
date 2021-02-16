#### Time Converter
def timeConverter(seconds):
        jam = detik // 3600
        seconds = detik % 3600
        menit = seconds // 60
        seconds = seconds % 60
        if detik >= 0 and detik <= 359999:
            return (f'{jam:02}:{menit:02}:{seconds:02}')
        elif detik < 0:
            return "Invalid Input!"
        elif (detik > 359999):
            return "Invalid Input!"
try:
    detik = int(input("Masukan Jumlah Detik: "))
    seconds = int(detik)
    print(timeConverter(seconds))
except:
    print("Invalid Input!")


    