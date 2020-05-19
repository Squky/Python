# Doing if-statements here

safety_alert = 'blue'

weather = input("what is the weather today? ")
if weather == 'stormy' and safety_alert == 'red':
    print('duck for cover')
elif weather == 'stormy' and safety_alert == 'blue':
    print('test')
elif weather == 'rainy':
    print('bring umbrella')
elif weather == 'stormy':
    print('Stay at home1 and watch the storm : ) ')

else:
    print('put on sun lotion')
