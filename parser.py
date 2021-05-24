# This is a sample Python script.
import re
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
def global_Pars(fileName):
    f = open('examples/'+fileName)
    configDict = dict()
    for line in f:
        var = line[0:line.index('=')]
        val = line[line.index('=') + 1:len(line)]
        if '.' in var:
            key = var[0:line.index('.')]
            subKey = var[line.index('.') + 1: len(line)]
        else:
            key = var
            subKey = val
        if key in configDict:
            configDict[key][subKey] = val[: -1]
        else:
            configDict[key] = {subKey: val[: -1]}
    print(configDict)
    return configDict

def RCC_Pars(configDict):
    rccConfigDict = dict()
    if 'SYSCLKFreq_VALUE' in configDict['RCC'].keys():
        rccConfigDict['F_CPU'] = configDict['RCC']['SYSCLKFreq_VALUE']

    if 'AHBCLKDivider' in configDict['RCC'].keys():
        indexFirstDigit = re.search("\d", configDict['RCC']['AHBCLKDivider'])
        rccConfigDict['AHBPrescaler'] = configDict['RCC']['AHBCLKDivider'][indexFirstDigit.start(): len(configDict['RCC']['AHBCLKDivider'])]

    if 'APB1CLKDivider' in configDict['RCC'].keys():
       indexFirstDigit = re.search("\d", configDict['RCC']['APB1CLKDivider'])
       rccConfigDict['APB1Prescaler'] = configDict['RCC']['APB1CLKDivider'][indexFirstDigit.start(): len(configDict['RCC']['APB1CLKDivider'])]

    if 'APB2CLKDivider' in configDict['RCC'].keys():
        indexFirstDigit = re.search("\d", configDict['RCC']['APB2CLKDivider'])
        rccConfigDict['APB2Prescaler'] = configDict['RCC']['APB2CLKDivider'][indexFirstDigit.start(): len(configDict['RCC']['APB2CLKDivider'])]

    if 'HSEDivPLL' in configDict['RCC'].keys():
       indexFirstDigit = re.search("\d", configDict['RCC']['HSEDivPLL'])
       rccConfigDict['HSEDivider'] = configDict['RCC']['HSEDivPLL'][indexFirstDigit.start(): len(configDict['RCC']['HSEDivPLL'])]

    if 'AHBCLKDivider' in configDict['RCC'].keys():
        indexFirstDigit = re.search("\d", configDict['RCC']['AHBCLKDivider'])
        rccConfigDict['AHBPrescaler'] = configDict['RCC']['AHBCLKDivider'][indexFirstDigit.start(): len(configDict['RCC']['AHBCLKDivider'])]

    if 'PLLSourceVirtual' in configDict['RCC'].keys():
        if configDict['RCC']['PLLSourceVirtual'][-3:] == 'HSE':
            rccConfigDict['clockSource'] = 'External'
        else:
            rccConfigDict['clockSource'] = 'Internal'

    if 'PLLMUL' in configDict['RCC'].keys():
        indexFirstDigit = re.search("\d", configDict['RCC']['PLLMUL'])
        rccConfigDict['Multipler'] = configDict['RCC']['PLLMUL'][indexFirstDigit.start(): len(configDict['RCC']['PLLMUL'])]

    if 'TimSys_Div' in configDict['RCC'].keys():
        indexFirstDigit = re.search("\d", configDict['RCC']['TimSys_Div'])
        rccConfigDict['SystemTimer'] = configDict['RCC']['TimSys_Div'][indexFirstDigit.start(): len(configDict['RCC']['TimSys_Div'])]

    if 'SYSCLKSource' in configDict['RCC'].keys():
        indexFirstDigit = re.search('RCC_SYSCLKSOURCE_', configDict['RCC']['SYSCLKSource'])
        rccConfigDict['SystemClock'] = configDict['RCC']['SYSCLKSource'][indexFirstDigit.end(): len(configDict['RCC']['SYSCLKSource'])]

    if 'PLLDivider' in configDict['RCC'].keys():
        indexFirstDigit = re.search("\d", configDict['RCC']['PLLDivider'])
        rccConfigDict['PLLDivider'] = configDict['RCC']['PLLDivider'][indexFirstDigit.start(): len(configDict['RCC']['PLLDivider'])]

    if 'PLLM' in configDict['RCC'].keys():
        rccConfigDict['PLLM'] = configDict['RCC']['PLLM']

    if 'PLLN' in configDict['RCC'].keys():
        rccConfigDict['PLLN'] = configDict['RCC']['PLLN']

    print(rccConfigDict)

    return rccConfigDict

def GPIO_Output_Pars(portName, configDict):
    portConf = dict()

    portConf['Conf'] = "Out"

    index = re.search("_", configDict[portName]['GPIO_PuPd'])
    portConf['PuPd'] = configDict[portName]['GPIO_PuPd'][index.end(): len(configDict[portName]['GPIO_PuPd'])]

    index = re.search("GPIO_MODE_OUTPUT_", configDict[portName]['GPIO_ModeDefaultOutputPP'])
    portConf['GPIO_Mode'] = configDict[portName]['GPIO_ModeDefaultOutputPP'][index.end(): len(configDict[portName]['GPIO_ModeDefaultOutputPP'])]
    if 'GPIO_Speed' in configDict[portName].keys():
        index = re.search("GPIO_SPEED_FREQ_", configDict[portName]['GPIO_Speed'])
        portConf['GPIO_Speed'] = configDict[portName]['GPIO_Speed'][index.end(): len(configDict[portName]['GPIO_Speed'])]
    else:
        portConf['GPIO_Speed'] = 'LOW'

    if 'GPIO_Label' in configDict[portName].keys():
        portConf['Label'] = configDict[portName]['GPIO_Label']

    print(portConf)

    return portConf

def GPIO_Input_Pars(portName,configDict):
    portConf = dict()
    portConf['Conf'] = "In"
    if 'GPIO_PuPd' in configDict[portName].keys():
        indexFirstDigit = re.search("_", configDict[portName]['GPIO_PuPd'])
        portConf['PuPd'] = configDict[portName]['GPIO_PuPd'][indexFirstDigit.end(): len(configDict[portName]['GPIO_PuPd'])]

    if 'GPIO_Label' in configDict[portName].keys():
        portConf['Label'] = configDict[portName]['GPIO_Label']

    print(portConf)

    return portConf

def GPIO_Analog_Pars(portName, configDict):
    portConf = dict()
    portConf['Conf'] = "Analog"

    if 'GPIO_Label' in configDict[portName].keys():
        portConf['Label'] = configDict[portName]['GPIO_Label']

    return portConf

def Timer_Pars(timerName, configDict):
    timerConf = dict();

    if 'AutoReloadPreload' in configDict[timerName].keys():
        index = re.search("TIM_AUTORELOAD_PRELOAD_", configDict[timerName]['AutoReloadPreload'])
        timerConf['Preload'] = configDict[timerName]['AutoReloadPreload'][index.end(): len(configDict[timerName]['AutoReloadPreload'])]

    if 'ClockDivision' in configDict[timerName].keys():
        index = re.search("TIM_CLOCKDIVISION_DIV", configDict[timerName]['ClockDivision'])
        timerConf['ClockDivision'] = configDict[timerName]['ClockDivision'][index.end(): len(configDict[timerName]['ClockDivision'])]

    if 'Channel' in configDict[timerName].keys():
        index = re.search("TIM_CHANNEL_", configDict[timerName]['Channel'])
        timerConf['Channel'] = configDict[timerName]['Channel'][index.end(): len(configDict[timerName]['Channel'])]

    if 'RepetitionCounter' in configDict[timerName].keys():
        timerConf['RepetitionCounter'] = configDict[timerName]['RepetitionCounter']


    print(timerConf)

    return timerConf
def PortState_Pars(configDict):
    portsName = {'Pa1', 'Pa2', 'Pa3', 'Pa4', 'Pa5', 'Pa6', 'Pa7', 'Pa8', 'Pa9', 'Pa10', 'Pa11', 'Pa12', 'Pa13', 'Pa14', 'Pb1'}
    GPIO_Conf = dict()

    for portName in portsName:
        if str.upper(portName) in configDict.keys():
            if configDict[str.upper(portName)]['Signal'] == 'GPIO_Output':
                GPIO_Conf[portName] = GPIO_Output_Pars(str.upper(portName), configDict)
            if configDict[str.upper(portName)]['Signal'] == 'GPIO_Input':
                GPIO_Conf[portName] = GPIO_Input_Pars(str.upper(portName), configDict)
            if configDict[str.upper(portName)]['Signal'] == 'GPIO_Analog':
                GPIO_Conf[portName] = GPIO_Analog_Pars(str.upper(portName), configDict)

    return GPIO_Conf






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
