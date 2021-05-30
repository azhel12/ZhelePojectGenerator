import global_pars
import GPIO_pars
import RCC_pars
import SPI_pars
import Timer_pars

def parser(fileName):
        configDict = dict()

        rawConfigDict = global_pars.global_Pars(fileName)

        if 'SYSCLKFreq_VALUE' in rawConfigDict['RCC'].keys():
                configDict['F_CPU'] = rawConfigDict['RCC']['SYSCLKFreq_VALUE']

        configDict['GPIO_Conf'] = GPIO_pars.GPIO_Pars(rawConfigDict)
        configDict['RCC_Conf'] = RCC_pars.RCC_Pars(rawConfigDict)
        configDict['SPI_Conf'] = SPI_pars.SPI_pars(rawConfigDict)
        #Timer_Conf = Timer_pars.Timer_Pars('TIM16', configDict)

        return configDict

