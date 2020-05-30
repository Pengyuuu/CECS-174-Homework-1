import math

#constants
secondsDay = 86400
speed_of_light = 299792458
ulaCharge = 14830
spaceXInsurance = 0.3
spaceXCharge = 2720
lightYear = 9460730472580800

choice = 0

while choice != 4:

    #prompt user
    print('Main menu: \n1. Warp speed \n2. Cost to Launch \n' \
      '3. Time Dilation  \n4. Quit \n')

    choice = int(input('Please choose an option: '))

    #validate
    while choice < 1 or choice > 4:
        choice = int(input('Please choose an option: '))

    #choice number 1
    #input and validation
    if choice == 1:
        ship_speed = float(input("Please input ship's speed in " \
                             "units of warp factor: "))
        while ship_speed < 0:
            ship_speed = float(input("Please input ship's speed in " \
                                 "units of warp factor: "))
        ship_speed = (((ship_speed ** 10) ** (1/3)) * speed_of_light)

        #print results
        print('You are now traveling at',format(ship_speed, ',.2f'), \
          'meters per second.')

    #choice number 2    
    elif choice == 2:
        satellite_mass = float(input("Please enter satellite's mass in kilograms: "))
        while satellite_mass < 1:
            satellite_mass = float(input("Please enter satellite's mass in " \
                                     "kilograms: "))
        satellite_manufacture = float(input("Please enter satellite's manufacture " \
                                        "cost in US dollars: "))
        while satellite_manufacture < 1:
            satellite_manufacture = float(input("Please enter satellite's " \
                                            "manufacture cost in US dollars: "))

        #calculate costs
        ulaCost = satellite_mass * ulaCharge
        spaceInsurance = satellite_manufacture * spaceXInsurance
        spaceXCost = ((satellite_mass * spaceXCharge) + spaceInsurance)

        #print results
        if ulaCost < spaceXCost:
            savings = spaceXCost - ulaCost
            print('United Launch Alliance will save you $',format(savings, ',.2f'), \
              ' on this launch.', sep = '')
        elif spaceXCost < ulaCost:
            savings = ulaCost - spaceXCost
            print('SpaceX will save you $',format(savings, ',.2f'),' on this launch.', sep = '')
        else:
            print('Both providers cost the same amount')

    #choice number 3
    elif choice == 3:
        travel_distance = float(input('Enter travel distance in light years: '))
        while travel_distance < 1 and travel_distance > 0:
            travel_distance = float(input('Enter travel distance in light years: '))
        ship_velocity = float(input('Enter space ship velocity as a fraction of ' \
                                'the speed of light: '))
        while ship_velocity < 0.1 or ship_velocity == 1.0 or ship_velocity > 1.0:
            ship_velocity = float(input('Enter space ship velocity as a fraction of ' \
                                    'the speed of light: '))

        #calculate time dilation on earth
        distance = travel_distance * lightYear
        speed = ship_velocity * speed_of_light
        time = distance / speed
        time = time / secondsDay

        #calculate time dilation on ship
        shipTime = (distance / speed) // secondsDay
        time_dilation = (math.sqrt(1 - ((speed ** 2) / (speed_of_light ** 2)))) * shipTime

        #print results
        time = format(time, ',.0f')
        time = int(time)
        if time >= 365:
            years = time // 365
            days = time - 365
            print('An observer on Earth ages',years,'years,',days,'days during the trip')
        else:
            print('An observer on Earth ages',time,'days during the trip')

        if time_dilation >= 365:
            shipYears = time_dilation // 365
            shipDays = time_dilation - 365
            print('A passenger on the ship ages',shipYears,'years,',shipDays,'days during the trip')
        else:
            time_dilation = math.floor(time_dilation)
            print('A passenger on the ship ages',time_dilation,'days during the trip')
    print()

print('Goodbye')

        


    

    
