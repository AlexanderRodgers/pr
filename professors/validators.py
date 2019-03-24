from django.core.exceptions import ValidationError

def difficulty(value):
    if value < 1 or value > 10:
        raise ValidationError('%s is out of acceptable range of possible values' % value)

def class_num(value):
    if value < 100 or value > 700:
        raise ValidationError('%s is out of acceptable range of possible values' % value)

def quarter(value):
    print(type(value))
    if value < 0 or value > 3:
        raise ValidationError('%s is out of acceptable range of possible values' % value)

def grade_system(value):
    grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-',
                'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
    if value not in grades:
        raise ValidationError('%s is not a possible grade' % value)