import re

def SPI_pars(rawConfigDict):
    SPI_Config = dict()

    if 'SPI1' in rawConfigDict.keys():
        SPI_Config['SPI1'] = dict()
        if 'CLKPolarity' in rawConfigDict['SPI1'].keys():
            indexFirstDigit = re.search("SPI_POLARITY_", rawConfigDict['SPI1']['CLKPolarity'])
            SPI_Config['SPI1']['Polarity'] = rawConfigDict['SPI1']['CLKPolarity'][indexFirstDigit.end(): len(rawConfigDict['SPI1']['CLKPolarity'])]

        if 'DataSize' in rawConfigDict['SPI1'].keys():
            indexFirstDigit = re.search("\d", rawConfigDict['SPI1']['DataSize'])
            SPI_Config['SPI1']['DataSize'] = rawConfigDict['SPI1']['DataSize'][indexFirstDigit.start(): indexFirstDigit.end()]

        if 'FirstBit' in rawConfigDict['SPI1'].keys():
            indexFirstDigit = re.search("SPI_FIRSTBIT_", rawConfigDict['SPI1']['FirstBit'])
            SPI_Config['SPI1']['FirstBit'] = rawConfigDict['SPI1']['FirstBit'][indexFirstDigit.end(): len(rawConfigDict['SPI1']['FirstBit'])]

        if 'BaudRatePrescaler' in rawConfigDict['SPI1'].keys():
            indexFirstDigit = re.search("SPI_BAUDRATEPRESCALER_", rawConfigDict['SPI1']['BaudRatePrescaler'])
            SPI_Config['SPI1']['BaudRatePrescaler'] = rawConfigDict['SPI1']['BaudRatePrescaler'][indexFirstDigit.end(): len(rawConfigDict['SPI1']['BaudRatePrescaler'])]

        if 'CLKPhase' in rawConfigDict['SPI1'].keys():
            indexFirstDigit = re.search("\d", rawConfigDict['SPI1']['CLKPhase'])
            SPI_Config['SPI1']['Phase'] = rawConfigDict['SPI1']['CLKPhase'][indexFirstDigit.start(): indexFirstDigit.end()]

    if 'SPI2' in rawConfigDict.keys():
        SPI_Config['SPI2'] = dict()
        if 'CLKPolarity' in rawConfigDict['SPI2'].keys():
            indexFirstDigit = re.search("SPI_POLARITY_", rawConfigDict['SPI2']['CLKPolarity'])
            SPI_Config['SPI2']['Polarity'] = rawConfigDict['SPI2']['CLKPolarity'][indexFirstDigit.end(): len(rawConfigDict['SPI2']['CLKPolarity'])]

        if 'DataSize' in rawConfigDict['SPI2'].keys():
            indexFirstDigit = re.search("\d", rawConfigDict['SPI2']['DataSize'])
            SPI_Config['SPI2']['DataSize'] = rawConfigDict['SPI2']['DataSize'][indexFirstDigit.start(): indexFirstDigit.end()]

        if 'FirstBit' in rawConfigDict['SPI2'].keys():
            indexFirstDigit = re.search("SPI_FIRSTBIT_", rawConfigDict['SPI2']['FirstBit'])
            SPI_Config['SPI2']['FirstBit'] = rawConfigDict['SPI2']['FirstBit'][indexFirstDigit.end(): len(rawConfigDict['SPI2']['FirstBit'])]

        if 'BaudRatePrescaler' in rawConfigDict['SPI2'].keys():
            indexFirstDigit = re.search("SPI_BAUDRATEPRESCALER_", rawConfigDict['SPI2']['BaudRatePrescaler'])
            SPI_Config['SPI2']['BaudRatePrescaler'] = rawConfigDict['SPI2']['BaudRatePrescaler'][indexFirstDigit.end(): len(rawConfigDict['SPI2']['BaudRatePrescaler'])]

        if 'CLKPhase' in rawConfigDict['SPI2'].keys():
            indexFirstDigit = re.search("\d", rawConfigDict['SPI2']['CLKPhase'])
            SPI_Config['SPI2']['Phase'] = rawConfigDict['SPI2']['CLKPhase'][indexFirstDigit.start(): indexFirstDigit.end()]

    return SPI_Config