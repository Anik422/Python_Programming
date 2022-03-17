car_power = ''
start_count = False

while True:
    car_power = input("> ").lower()
    if car_power == 'start':
        if start_count:
            print("Car already start.")
        else:
            start_count = True
            print('car started... Ready to go...')
    elif car_power == 'stop':
       if not start_count:
           print('Car already stop.')
       else:
           start_count = False
           print('Car stopped.')
    elif car_power == 'quit':
        break
    elif car_power == 'help':
        print('''
Start - to start the car.
Stop - to stop the car.
Quit - to exit.
            ''')
    else:
        print("I don't understand that...")
