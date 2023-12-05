
mes = "nig  "
mes1 = " 'Er'"
mes2 = "  app "

print(mes)
print(mes1)
print(mes2)
print(mes2.strip())

mes = mes.rstrip()
mes1 = mes1.lstrip()

mes3 = f"{mes.lower()}{mes1.upper()}"

print(mes3.title())



