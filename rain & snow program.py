#checking weather is raining or snowing (if it is true either of its true)

def getData(weather):
    val=True
    data=""
    while val:
        data=input(f" is it {weather}").lower()
        val  = checking(data)

    return data

def checking (data):
    if data == "Yes" or data == "no":
        return False
    else:
        return True

rain = getData("Raining")
snow = getData("snowing")

if rain == "yes" or snow == "yes":
    print("True")
else:
    print("False")
