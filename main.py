import sys
sys.path.append("parsers")
import jinja2
from jinja2 import Template
from majorParser import parser

configDict = parser(sys.argv[1])

if 'RCC_Conf' in configDict.keys():
    with open('templates/RCC_template.tpl', 'r') as file:
        content = file.read()

    template = jinja2.Template(content)
    ConfigureClock = template.render(RCC_Conf=configDict['RCC_Conf'])

if 'GPIO_Conf' in configDict.keys():
    with open('templates/GPIO_template.tpl', 'r') as file:
        content = file.read()

    template = jinja2.Template(content)
    ConfigureGPIO = template.render(GPIO_Conf=configDict['GPIO_Conf'])

if 'SPI_Conf' in configDict.keys():
    with open('templates/SPI_template.tpl', 'r') as file:
        content = file.read()

    template = jinja2.Template(content)
    ConfigureSPI = template.render(SPI_Conf=configDict['SPI_Conf'])

if (len(sys.argv) > 2):
    outF = open(sys.argv[2], 'w')
else:
    outF = open('config.cpp', 'w')

with open('templates/template.tpl', 'r') as file:
    content = file.read()

template = jinja2.Template(content)
outF.write(template.render(F_CPU=configDict['F_CPU'],
                           ConfigureClock=ConfigureClock,
                           ConfigureGPIO=ConfigureGPIO,
                           ConfigureSPI=ConfigureSPI))
