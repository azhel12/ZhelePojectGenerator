# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import jinja2
import parser
from jinja2 import Template

RCC_Conf = parser.RCC_Pars(parser.global_Pars('f4.ioc'))
GPIO_Conf = parser.PortState_Pars(parser.global_Pars('f030f4p6.ioc'))
Timer_Conf = parser.Timer_Pars('TIM16', parser.global_Pars('f030f4p6.ioc'))
outF = open('test.cpp', 'w')

with open('template.txt', 'r') as file:
    content = file.read()

    template = jinja2.Template(content)
outF.write(template.render(RCC_Conf=RCC_Conf, GPIO_Conf=GPIO_Conf))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
