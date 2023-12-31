#############################################################################
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "tOqZCBNB8xTmQ07xa3gJVefFEiplHXEQ"

while True:
    orig = input("ciudad de origen: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("ciudad de destino: ")
    if dest == "quit" or dest == "q":
        break
    
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = Una ruta exitosa.\n")
        print("Dirección desde " + (orig) + " hacia " + (dest))
        print("Duración del viaje:   " + str(json_data["route"]["formattedTime"]))
        print("Kilometros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Combustible usado (Ltr):" + str("{:.3f}".format(((json_data["route"]["distance"])*1.61)/10)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("\n****************************************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("****************************************************************\n")
    else:
        print("\n************************************************************************")
        print("Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
