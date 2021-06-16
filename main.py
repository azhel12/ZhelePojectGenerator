import jinja2
import parser
import sys
from jinja2 import Template
sys.path.append("./parsers")
from majorParser import parser

configDict = parser(sys.argv[1] )

if configDict['RCC_Conf']:
    with open('templates/RCC_template.tpl', 'r') as file:
        content = file.read()

    template = jinja2.Template(content)
    ConfigureClock = template.render(RCC_Conf=configDict['RCC_Conf'])
else:
    ConfigureClock = ""

if configDict['GPIO_Conf']:
    with open('templates/GPIO_template.tpl', 'r') as file:
        content = file.read()

    template = jinja2.Template(content)
    ConfigureGPIO = template.render(GPIO_Conf=configDict['GPIO_Conf'])
else:
    ConfigureGPIO = ""

if configDict['SPI_Conf']:
    with open('templates/SPI_template.tpl', 'r') as file:
        content = file.read()

    template = jinja2.Template(content)
    ConfigureSPI = template.render(SPI_Conf=configDict['SPI_Conf'])
else:
    ConfigureSPI = ""

if configDict['I2C_Conf']:
    with open('templates/I2C_template.tpl', 'r') as file:
        content = file.read()

    template = jinja2.Template(content)
    ConfigureI2C = template.render(I2C_Conf=configDict['I2C_Conf'])
else:
    ConfigureI2C = ""

if configDict['Usart_Conf']:
        with open('templates/Usart_template.tpl', 'r') as file:
            content = file.read()

        template = jinja2.Template(content)
        ConfigureUsart = template.render(USART_Conf=configDict['Usart_Conf'])
else:
    ConfigureUsart = ""

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
                           ConfigureSPI=ConfigureSPI,
                           ConfigureI2C=ConfigureI2C,
                           ConfigureUsart=ConfigureUsart))
