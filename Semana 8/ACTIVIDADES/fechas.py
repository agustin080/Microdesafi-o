from datetime import datetime, timedelta

ahora = datetime.now()
cumpleaños = datetime.strptime("2024-10-23", "%Y-%m-%d")

diferencia = cumpleaños - ahora

print(f"La diferencia es de {diferencia.seconds}")


