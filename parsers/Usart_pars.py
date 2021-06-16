import re

def Usart_Pars(rawConfigDict):
    number = 0
    portsName = []
    while ('Pin' + str(number) in rawConfigDict['Mcu']):
        index = rawConfigDict['Mcu']['Pin' + str(number)].find('-')
        portsName.append(str.capitalize(str.lower(rawConfigDict['Mcu']['Pin' + str(number)])))
        number = number + 1

    usartConfigDict = dict()

    for portName in portsName:
        if str.upper(portName) in rawConfigDict.keys():
            if 'Signal' in rawConfigDict[str.upper(portName)].keys():
                if rawConfigDict[str.upper(portName)]['Signal'] == 'USART1_RX':
                    usartConfigDict['USART1'] = dict()
                    index = portName.find('-')
                    if index != -1:
                        usartConfigDict['USART1']['RX'] = portName[0: index]
                    else:
                        usartConfigDict['USART1']['RX'] = portName
                if rawConfigDict[str.upper(portName)]['Signal'] == 'USART1_TX':
                    index = portName.find('-')
                    if index != -1:
                        usartConfigDict['USART1']['TX'] = portName[0: index]
                    else:
                        usartConfigDict['USART1']['TX'] = portName
                if rawConfigDict[str.upper(portName)]['Signal'] == 'USART2_RX':
                    usartConfigDict['USART3'] = dict()
                    index = portName.find('-')
                    if index != -1:
                        usartConfigDict['USART2']['RX'] = portName[0: index]
                    else:
                        usartConfigDict['USART2']['RX'] = portName
                if rawConfigDict[str.upper(portName)]['Signal'] == 'USART2_TX':
                    index = portName.find('-')
                    if index != -1:
                        usartConfigDict['USART2']['TX'] = portName[0: index]
                    else:
                        usartConfigDict['USART2']['TX'] = portName
                if rawConfigDict[str.upper(portName)]['Signal'] == 'USART3_RX':
                    usartConfigDict['USART3'] = dict()
                    index = portName.find('-')
                    if index != -1:
                        usartConfigDict['USART3']['RX'] = portName[0: index]
                    else:
                        usartConfigDict['USART3']['RX'] = portName
                if rawConfigDict[str.upper(portName)]['Signal'] == 'USART3_TX':
                    index = portName.find('-')
                    if index != -1:
                        usartConfigDict['USART3']['TX'] = portName[0: index]
                    else:
                        usartConfigDict['USART3']['TX'] = portName
                if rawConfigDict[str.upper(portName)]['Signal'] == 'USART4_RX':
                    usartConfigDict['USART4'] = dict()
                    index = portName.find('-')
                    if index != -1:
                        usartConfigDict['USART4']['RX'] = portName[0: index]
                    else:
                        usartConfigDict['USART4']['RX'] = portName
                if rawConfigDict[str.upper(portName)]['Signal'] == 'USART4_TX':
                    index = portName.find('-')
                    if index != -1:
                        usartConfigDict['USART4']['TX'] = portName[0: index]
                    else:
                        usartConfigDict['USART4']['TX'] = portName

    if 'USART2' in rawConfigDict.keys():
        usartConfigDict['USART2'] = dict()
        if 'IPParameters' in rawConfigDict['USART2'].keys():
            indexFirstDigit = re.search("-", rawConfigDict['USART2']['IPParameters'])
            usartConfigDict['USART2']['IPParameters'] = rawConfigDict['USART2']['IPParameters'][indexFirstDigit.start(): len(rawConfigDict['USART2']['IPParameters'])]
        if 'VirtualMode-Asynchronous' in rawConfigDict['USART2'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART2']['VirtualMode-Asynchronous'])
            usartConfigDict['USART2']['VirtualMode-Asynchronous'] = rawConfigDict['USART2']['VirtualMode-Asynchronous'][indexFirstDigit.start(): len(rawConfigDict['USART2']['VirtualMode-Asynchronous'])]
        if 'VirtualMode-Synchronous' in rawConfigDict['USART2'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART2']['VirtualMode-Synchronous'])
            usartConfigDict['USART2']['VirtualMode-Synchronous'] = rawConfigDict['USART2']['VirtualMode-Synchronous'][indexFirstDigit.start(): len(rawConfigDict['USART2']['VirtualMode-Synchronous'])]
        if 'VirtualMode-Multiprocessor_communication' in rawConfigDict['USART1'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART2']['VirtualMode-Multiprocessor_communication'])
            usartConfigDict['USART2']['VirtualMode-Multiprocessor_communication'] = rawConfigDict['USART2']['VirtualMode-Multiprocessor_communication'][indexFirstDigit.start(): len(rawConfigDict['USART2']['VirtualMode-Multiprocessor_communication'])]
        if 'VirtualMode-Half_duplex(single_wire_mode)' in rawConfigDict['USART2'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART2']['VirtualMode-Half_duplex(single_wire_mode)'])
            usartConfigDict['USART2']['VirtualMode-Half_duplex(single_wire_mode)'] = rawConfigDict['USART2']['VirtualMode-Half_duplex(single_wire_mode)'][indexFirstDigit.start(): len(rawConfigDict['USART2']['VirtualMode-Half_duplex(single_wire_mode)'])]

    if 'USART3' in rawConfigDict.keys():
        usartConfigDict['USART3'] = dict()
        if 'IPParameters' in rawConfigDict['USART3'].keys():
            indexFirstDigit = re.search("-", rawConfigDict['USART3']['IPParameters'])
            usartConfigDict['USART3']['IPParameters'] = rawConfigDict['USART3']['IPParameters'][indexFirstDigit.start(): len(rawConfigDict['USART3']['IPParameters'])]
        if 'VirtualMode-Asynchronous' in rawConfigDict['USART3'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART3']['VirtualMode-Asynchronous'])
            usartConfigDict['USART3']['VirtualMode-Asynchronous'] = rawConfigDict['USART3']['VirtualMode-Asynchronous'][indexFirstDigit.start(): len(rawConfigDict['USART3']['VirtualMode-Asynchronous'])]
        if 'VirtualMode-Synchronous' in rawConfigDict['USART3'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART3']['VirtualMode-Synchronous'])
            usartConfigDict['USART3']['VirtualMode-Synchronous'] = rawConfigDict['USART3']['VirtualMode-Synchronous'][indexFirstDigit.start(): len(rawConfigDict['USART3']['VirtualMode-Synchronous'])]
        if 'VirtualMode-Multiprocessor_communication' in rawConfigDict['USART3'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART3']['VirtualMode-Multiprocessor_communication'])
            usartConfigDict['USART3']['VirtualMode-Multiprocessor_communication'] = rawConfigDict['USART3']['VirtualMode-Multiprocessor_communication'][indexFirstDigit.start(): len(rawConfigDict['USART3']['VirtualMode-Multiprocessor_communication'])]
        if 'VirtualMode-Half_duplex(single_wire_mode)' in rawConfigDict['USART3'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART3']['VirtualMode-Half_duplex(single_wire_mode)'])
            usartConfigDict['USART3']['VirtualMode-Half_duplex(single_wire_mode)'] = rawConfigDict['USART3']['VirtualMode-Half_duplex(single_wire_mode)'][indexFirstDigit.start(): len(rawConfigDict['USART3']['VirtualMode-Half_duplex(single_wire_mode)'])]

    if 'USART4' in rawConfigDict.keys():
        usartConfigDict['USART4'] = dict()
        if 'IPParameters' in rawConfigDict['USART4'].keys():
            indexFirstDigit = re.search("-", rawConfigDict['USART4']['IPParameters'])
            usartConfigDict['USART4']['IPParameters'] = rawConfigDict['USART4']['IPParameters'][indexFirstDigit.start(): len(rawConfigDict['USART4']['IPParameters'])]
        if 'VirtualMode-Asynchronous' in rawConfigDict['USART4'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART1']['VirtualMode-Asynchronous'])
            usartConfigDict['USART4']['VirtualMode-Asynchronous'] = rawConfigDict['USART4']['VirtualMode-Asynchronous'][indexFirstDigit.start(): len(rawConfigDict['USART4']['VirtualMode-Asynchronous'])]
        if 'VirtualMode-Synchronous' in rawConfigDict['USART4'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART4']['VirtualMode-Synchronous'])
            usartConfigDict['USART4']['VirtualMode-Synchronous'] = rawConfigDict['USART4']['VirtualMode-Synchronous'][indexFirstDigit.start(): len(rawConfigDict['USART4']['VirtualMode-Synchronous'])]
        if 'VirtualMode-Multiprocessor_communication' in rawConfigDict['USART4'].keys():
            indexFirstDigit = re.search("_",rawConfigDict['USART4']['VirtualMode-Multiprocessor_communication'])
            usartConfigDict['USART4']['VirtualMode-Multiprocessor_communication'] = rawConfigDict['USART4']['VirtualMode-Multiprocessor_communication'][indexFirstDigit.start(): len(rawConfigDict['USART4']['VirtualMode-Multiprocessor_communication'])]
        if 'VirtualMode-Half_duplex(single_wire_mode)' in rawConfigDict['USART4'].keys():
            indexFirstDigit = re.search("_",rawConfigDict['USART4']['VirtualMode-Half_duplex(single_wire_mode)'])
            usartConfigDict['USART4']['VirtualMode-Half_duplex(single_wire_mode)'] = rawConfigDict['USART4']['VirtualMode-Half_duplex(single_wire_mode)'][indexFirstDigit.start(): len(rawConfigDict['USART4']['VirtualMode-Half_duplex(single_wire_mode)'])]

    if 'USART1' in rawConfigDict.keys():
        usartConfigDict['USART1'] = dict()
        if 'IPParameters' in rawConfigDict['USART1'].keys():
            indexFirstDigit = re.search("-", rawConfigDict['USART1']['IPParameters'])
            usartConfigDict['USART1']['IPParameters'] = rawConfigDict['USART1']['IPParameters'][indexFirstDigit.start(): len(rawConfigDict['USART1']['IPParameters'])]
        if 'VirtualMode-Asynchronous' in rawConfigDict['USART1'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART1']['VirtualMode-Asynchronous'])
            usartConfigDict['USART1']['VirtualMode-Asynchronous'] = rawConfigDict['USART1']['VirtualMode-Asynchronous'][indexFirstDigit.start(): len(rawConfigDict['USART1']['VirtualMode-Asynchronous'])]
        if 'VirtualMode-Synchronous' in rawConfigDict['USART1'].keys():
            indexFirstDigit = re.search("_", rawConfigDict['USART1']['VirtualMode-Synchronous'])
            usartConfigDict['USART1']['VirtualMode-Synchronous'] = rawConfigDict['USART1']['VirtualMode-Synchronous'][indexFirstDigit.start(): len(rawConfigDict['USART1']['VirtualMode-Synchronous'])]
        if 'VirtualMode-Multiprocessor_communication' in rawConfigDict['USART1'].keys():
            indexFirstDigit = re.search("_",rawConfigDict['USART1']['VirtualMode-Multiprocessor_communication'])
            usartConfigDict['USART1']['VirtualMode-Multiprocessor_communication'] = rawConfigDict['USART1']['VirtualMode-Multiprocessor_communication'][indexFirstDigit.start(): len(rawConfigDict['USART1']['VirtualMode-Multiprocessor_communication'])]
        if 'VirtualMode-Half_duplex(single_wire_mode)' in rawConfigDict['USART1'].keys():
            indexFirstDigit = re.search("_",rawConfigDict['USART1']['VirtualMode-Half_duplex(single_wire_mode)'])
            usartConfigDict['USART1']['VirtualMode-Half_duplex(single_wire_mode)'] = rawConfigDict['USART1']['VirtualMode-Half_duplex(single_wire_mode)'][indexFirstDigit.start(): len(rawConfigDict['USART1']['VirtualMode-Half_duplex(single_wire_mode)'])]

    return usartConfigDict
