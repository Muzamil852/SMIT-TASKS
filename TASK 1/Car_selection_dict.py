car_data = {
    "Toyota ":{ "Corolla Xli":{
                "Model": "2007",
                "Price" :"7500000"},
                        
                "Yaris Gli": {
                "Model": "2010",
                "Price" :  "5300000"},
                          
                "Raize Z": {
                "Model": "2017",
                "Price" : "4700000"}},
    "Suzuki":{
                "Alto VXR":{
                "Model" :"2025",
                "Price" : "2800000"},
                      
                "Swift Glx": {
                "Model": "2021",
                "Price": "3500000"},
                 
                "Cultus VXL AGS" :{
                "Model" :"2020",
                "Price" : "2500000"}},           
    "Honda":{
                "Civic RS":{
                "Model": "2021",
                "Price" : "9000000"},
                      
                "City Aspire":{
                "Model" : "2024",
                "Price" : "5300000"},
                        
                "BRV I-VTEC":{
                "Model" : "2019",
                "Price" : "3800000"}
         }
}

company_list = list(car_data)
for index, company in enumerate(company_list, start=1):
    print(f"{index}. {company}")

user_company = int(input("Enter your selection: "))

if user_company >= 1 and user_company <= len(company_list):
    company_name = company_list[user_company-1]
    print("\n")

    car_list = list(car_data[company_name])

    for index, car in enumerate(car_list, start=1):
        print(f"{index}. {car}")

    user_car = int(input("Enter your selection: "))
    if user_car >= 1 and user_car <= len(company_list):
        car_name = car_list[user_car-1]
        car_details = car_data[company_name][car_name]
        print("*"*20)
        print("Name:", car_name)
        print("Model:", car_details.get("Model"))
        print("price:", car_details.get("Price"))

    else:
        print("Wrong Selection...")
else:
    print("Wrong Selection...")