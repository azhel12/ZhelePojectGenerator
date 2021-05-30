import re

def GPIO_Input_Pars(portName, rawConfigDict):
    portConf = dict()
    portConf['Conf'] = "In"
    if 'GPIO_PuPd' in rawConfigDict[portName].keys():
        indexFirstDigit = re.search("_", rawConfigDict[portName]['GPIO_PuPd'])
        portConf['PuPd'] = rawConfigDict[portName]['GPIO_PuPd'][indexFirstDigit.end(): len(rawConfigDict[portName]['GPIO_PuPd'])]

    if 'GPIO_Label' in rawConfigDict[portName].keys():
        portConf['Label'] = rawConfigDict[portName]['GPIO_Label']

    return portConf

def GPIO_Output_Pars(portName, rawConfigDict):
    portConf = dict()

    portConf['Conf'] = "Out"

    index = re.search("_", rawConfigDict[portName]['GPIO_PuPd'])
    portConf['PuPd'] = rawConfigDict[portName]['GPIO_PuPd'][index.end(): len(rawConfigDict[portName]['GPIO_PuPd'])]

    index = re.search("GPIO_MODE_OUTPUT_", rawConfigDict[portName]['GPIO_ModeDefaultOutputPP'])
    portConf['GPIO_Mode'] = rawConfigDict[portName]['GPIO_ModeDefaultOutputPP'][index.end(): len(rawConfigDict[portName]['GPIO_ModeDefaultOutputPP'])]
    if 'GPIO_Speed' in rawConfigDict[portName].keys():
        index = re.search("GPIO_SPEED_FREQ_", rawConfigDict[portName]['GPIO_Speed'])
        portConf['GPIO_Speed'] = rawConfigDict[portName]['GPIO_Speed'][index.end(): len(rawConfigDict[portName]['GPIO_Speed'])]
    else:
        portConf['GPIO_Speed'] = 'LOW'

    if 'GPIO_Label' in rawConfigDict[portName].keys():
        portConf['Label'] = rawConfigDict[portName]['GPIO_Label']

    return portConf

def GPIO_Analog_Pars(portName, rawConfigDict):
    portConf = dict()
    portConf['Conf'] = "Analog"

    if 'GPIO_Label' in rawConfigDict[portName].keys():
        portConf['Label'] = rawConfigDict[portName]['GPIO_Label']

    return portConf

def GPIO_Pars(rawConfigDict):
    portsName = {'Pa1', 'Pa2', 'Pa3', 'Pa4', 'Pa5', 'Pa6', 'Pa7', 'Pa8', 'Pa9', 'Pa10', 'Pa11', 'Pa12', 'Pa13', 'Pa14', 'Pb1'}
    GPIO_Conf = dict()

    for portName in portsName:
        if str.upper(portName) in rawConfigDict.keys():
            if rawConfigDict[str.upper(portName)]['Signal'] == 'GPIO_Output':
                GPIO_Conf[portName] = GPIO_Output_Pars(str.upper(portName), rawConfigDict)
            if rawConfigDict[str.upper(portName)]['Signal'] == 'GPIO_Input':
                GPIO_Conf[portName] = GPIO_Input_Pars(str.upper(portName), rawConfigDict)
            if rawConfigDict[str.upper(portName)]['Signal'] == 'GPIO_Analog':
                GPIO_Conf[portName] = GPIO_Analog_Pars(str.upper(portName), rawConfigDict)

    return GPIO_Conf