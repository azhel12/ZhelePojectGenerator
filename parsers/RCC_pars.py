import re

def RCC_Pars(rawConfigDict):
    rccConfigDict = dict()

    if 'AHBCLKDivider' in rawConfigDict['RCC'].keys():
        indexFirstDigit = re.search("\d", rawConfigDict['RCC']['AHBCLKDivider'])
        rccConfigDict['AHBPrescaler'] = rawConfigDict['RCC']['AHBCLKDivider'][indexFirstDigit.start(): len(rawConfigDict['RCC']['AHBCLKDivider'])]

    if 'APB1CLKDivider' in rawConfigDict['RCC'].keys():
       indexFirstDigit = re.search("\d", rawConfigDict['RCC']['APB1CLKDivider'])
       rccConfigDict['APB1Prescaler'] = rawConfigDict['RCC']['APB1CLKDivider'][indexFirstDigit.start(): len(rawConfigDict['RCC']['APB1CLKDivider'])]

    if 'APB2CLKDivider' in rawConfigDict['RCC'].keys():
        indexFirstDigit = re.search("\d", rawConfigDict['RCC']['APB2CLKDivider'])
        rccConfigDict['APB2Prescaler'] = rawConfigDict['RCC']['APB2CLKDivider'][indexFirstDigit.start(): len(rawConfigDict['RCC']['APB2CLKDivider'])]

    if 'HSEDivPLL' in rawConfigDict['RCC'].keys():
       indexFirstDigit = re.search("\d", rawConfigDict['RCC']['HSEDivPLL'])
       rccConfigDict['HSEDivider'] = rawConfigDict['RCC']['HSEDivPLL'][indexFirstDigit.start(): len(rawConfigDict['RCC']['HSEDivPLL'])]

    if 'AHBCLKDivider' in rawConfigDict['RCC'].keys():
        indexFirstDigit = re.search("\d", rawConfigDict['RCC']['AHBCLKDivider'])
        rccConfigDict['AHBPrescaler'] = rawConfigDict['RCC']['AHBCLKDivider'][indexFirstDigit.start(): len(rawConfigDict['RCC']['AHBCLKDivider'])]

    if 'PLLSourceVirtual' in rawConfigDict['RCC'].keys():
        if rawConfigDict['RCC']['PLLSourceVirtual'][-3:] == 'HSE':
            rccConfigDict['clockSource'] = 'External'
        else:
            rccConfigDict['clockSource'] = 'Internal'

    if 'PLLMUL' in rawConfigDict['RCC'].keys():
        indexFirstDigit = re.search("\d", rawConfigDict['RCC']['PLLMUL'])
        rccConfigDict['Multiplier'] = rawConfigDict['RCC']['PLLMUL'][indexFirstDigit.start(): len(rawConfigDict['RCC']['PLLMUL'])]

    if 'TimSys_Div' in rawConfigDict['RCC'].keys():
        indexFirstDigit = re.search("\d", rawConfigDict['RCC']['TimSys_Div'])
        rccConfigDict['SystemTimer'] = rawConfigDict['RCC']['TimSys_Div'][indexFirstDigit.start(): len(rawConfigDict['RCC']['TimSys_Div'])]

    if 'SYSCLKSource' in rawConfigDict['RCC'].keys():
        indexFirstDigit = re.search('RCC_SYSCLKSOURCE_', rawConfigDict['RCC']['SYSCLKSource'])
        rccConfigDict['SystemClock'] = rawConfigDict['RCC']['SYSCLKSource'][indexFirstDigit.end(): len(rawConfigDict['RCC']['SYSCLKSource'])]

    if 'PLLDivider' in rawConfigDict['RCC'].keys():
        indexFirstDigit = re.search("\d", rawConfigDict['RCC']['PLLDivider'])
        rccConfigDict['PLLDivider'] = rawConfigDict['RCC']['PLLDivider'][indexFirstDigit.start(): len(rawConfigDict['RCC']['PLLDivider'])]

    if 'PLLM' in rawConfigDict['RCC'].keys():
        rccConfigDict['PLLM'] = rawConfigDict['RCC']['PLLM']

    if 'PLLN' in rawConfigDict['RCC'].keys():
        rccConfigDict['PLLN'] = rawConfigDict['RCC']['PLLN']

    return rccConfigDict