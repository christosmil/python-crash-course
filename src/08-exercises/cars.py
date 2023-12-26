def make_car(manufacturer, model, **kwargs):
    """Create a dictionary about a car's information."""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car = make_car('toyota', 'yaris', color='black', transmission='manual')
print(car)
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)