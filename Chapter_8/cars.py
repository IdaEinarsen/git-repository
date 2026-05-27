# 8.14 Cars

def make_car(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""
    
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    
    return car_info


# Function call
car = make_car('Dacia', 'Sandero', color='Silver', tow_package=False)

print(car)

# I need to be better at using comments to know what type of method im using in my codes! 
