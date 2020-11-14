def hello_func(greetring):
    return '{} Function.'.format(greetring)
#print(hello_func("hello"))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
#student_info("Math","art",name='Manil',age=22)


courses=['Math','Art']
info = {'name':'MAnil',"age":22}
#student_info(*courses,**info)


`#work
def leap_year(year):
    return year % 4  == 0
print(leap_year(2020))`