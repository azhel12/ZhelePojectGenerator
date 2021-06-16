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

    if 'GPIO_PuPd' in rawConfigDict[portName].keys():
        index = re.search("_", rawConfigDict[portName]['GPIO_PuPd'])
        portConf['PuPd'] = rawConfigDict[portName]['GPIO_PuPd'][index.end(): len(rawConfigDict[portName]['GPIO_PuPd'])]

    if 'GPIO_ModeDefaultOutputPP' in rawConfigDict[portName].keys():
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
    number = 0
    portsName = []

    while ('Pin' + str(number) in rawConfigDict['Mcu']):
        index = rawConfigDict['Mcu']['Pin' + str(number)].find('-')
        portsName.append(str.capitalize(str.lower(rawConfigDict['Mcu']['Pin' + str(number)])))
        number = number + 1

    GPIO_Conf = dict()

    for portName in portsName:
        if str.upper(portName) in rawConfigDict.keys():
            if rawConfigDict[str.upper(portName)]['Signal'] == 'GPIO_Output':
                index = portName.find('-')
                if index != -1:
                    GPIO_Conf[portName[0: index]] = GPIO_Output_Pars(str.upper(portName), rawConfigDict)
                else:
                    GPIO_Conf[portName] = GPIO_Output_Pars(str.upper(portName), rawConfigDict)

            if rawConfigDict[str.upper(portName)]['Signal'] == 'GPIO_Input':
                index = portName.find('-')
                if index != -1:
                    GPIO_Conf[portName[0: index]] = GPIO_Input_Pars(str.upper(portName), rawConfigDict)
                else:
                    GPIO_Conf[portName] = GPIO_Input_Pars(str.upper(portName), rawConfigDict)

            if rawConfigDict[str.upper(portName)]['Signal'] == 'GPIO_Analog':
                index = portName.find('-')
                if index != -1:
                    GPIO_Conf[portName[0: index]] = GPIO_Analog_Pars(str.upper(portName), rawConfigDict)
                else:
                    GPIO_Conf[portName] = GPIO_Analog_Pars(str.upper(portName), rawConfigDict)

    return GPIO_Conf