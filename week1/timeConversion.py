from datetime import datetime

def timeConversion(s):
    try:
        # Converte para o formato 24h
        hora_24h = datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")
        return hora_24h
    except ValueError:
        return "Invalid"
        
if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
