# a list of car brands and their various prices
cars={'Chevolert camaro': 39000000, 'Nissan rogue': 750000, 'Kia sportage': 780000, 'Renault 19': 82000, 'Toyota highlander': 652000,\
 'Honda accord': 28600, 'Hyundai Santafe': 790000, 'Audi A5': 698000, 'Lexus SUV': 75600000, 'Jeep wrangler': 4760000, 'Alfa romeo Giulia ti':9876000,\
 'Dodge viper': 2599000, 'Subaru Impressa': 327000, 'Porche 911 GT3': 45870000, 'Volkswagen golf': 579000, 'Rolls Royce Ghost': 90300000000000000,\
 'Mercedes Benz 300SL': 1560000000, 'McLaren sienna': 4370000000000, 'Ford Transit': 209800, 'Tesla Model 3': 5480900000000000000,\
 'Infiniti QX50': 3702000000, 'Chrysler sedan': 68300000, 'Lamborghini Urus': 5623000000000000000, 'Aston Martin':7852300000000000,\
 'Acura integra': 567000000, 'Abarth 124 Coupe': 2590000000, 'BMW XM': 14570000000, 'Range Rover sport':3487000000, ' Bentley Contential': 29073400000000 }
# prompt user to enter car name
car_Brand=input('Enter car brand: ')
#verify if car brand is available
if car_Brand in cars:
    print('YES,the %s is avaliable', car_Brand)
    print('The cost is $', cars[car_Brand])
else:
    print('Error',car_Brand, 'is unavaiable at the moment')

     
    