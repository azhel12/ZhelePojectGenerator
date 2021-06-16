import global_pars
import GPIO_pars
import RCC_pars
import SPI_pars
import I2C_pars
import Usart_pars
import Timer_pars

def parser(fileName):
        configDict = dict()

        rawConfigDict = global_pars.global_Pars(fileName)

        if 'SYSCLKFreq_VALUE' in rawConfigDict['RCC'].keys():
                configDict['F_CPU'] = rawConfigDict['RCC']['SYSCLKFreq_VALUE']

        configDict['GPIO_Conf'] = GPIO_pars.GPIO_Pars(rawConfigDict)
        configDict['RCC_Conf'] = RCC_pars.RCC_Pars(rawConfigDict)
        configDict['SPI_Conf'] = SPI_pars.SPI_pars(rawConfigDict)
        configDict['I2C_Conf'] = I2C_pars.I2C_pars(rawConfigDict)
        configDict['Usart_Conf'] = Usart_pars.Usart_Pars(rawConfigDict)
        #Timer_Conf = Timer_pars.Timer_Pars('TIM16', configDict)

        return configDict






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
