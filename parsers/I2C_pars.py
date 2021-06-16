import re

def I2C_pars(rawConfigDict):
    I2C_Config = dict()

    if 'I2C1' in rawConfigDict.keys():
        I2C_Config['I2c1'] = dict()

        if 'Speed' in rawConfigDict['I2C1'].keys():
            indexFirstDigit = re.search("\d", rawConfigDict['I2C1']['Speed'])
            I2C_Config['I2c1']['ClockSpeed'] = rawConfigDict['I2C1']['Speed'][indexFirstDigit.start(): len(rawConfigDict['I2C1']['Speed'])]
        elif 'I2C_Speed_Mode' in rawConfigDict['I2C1'].keys():
            index = re.search("_", rawConfigDict['I2C1']['Speed'])
            CLKSpeed = rawConfigDict['I2C1']['Speed'][index.end(): len(rawConfigDict['I2C1']['Speed'])]
            if (CLKSpeed == 'Fast'):
                I2C_Config['I2c1']['ClockSpeed'] = 400
            elif (CLKSpeed == 'Fast_Plus'):
                I2C_Config['I2c1']['ClockSpeed'] = 1000

        for item in rawConfigDict.keys():
            if 'Signal' in rawConfigDict[item]:
                if rawConfigDict[item]['Signal'] == 'I2C1_SDA':
                    I2C_Config['I2c1']['SDA'] = str.capitalize(str.lower(item))
                if rawConfigDict[item]['Signal'] == 'I2C1_SCL':
                    I2C_Config['I2c1']['SCL'] = str.capitalize(str.lower(item))

    if 'I2C2' in rawConfigDict.keys():
        I2C_Config['I2c2'] = dict()

        if 'Speed' in rawConfigDict['I2C2'].keys():
            indexFirstDigit = re.search("\d", rawConfigDict['I2C2']['Speed'])
            I2C_Config['I2c2']['ClockSpeed'] = rawConfigDict['I2C2']['Speed'][indexFirstDigit.start(): len(rawConfigDict['I2C2']['Speed'])]
        elif 'I2C_Speed_Mode' in rawConfigDict['I2C2'].keys():
            index = re.search("_", rawConfigDict['I2C2']['Speed'])
            CLKSpeed = rawConfigDict['I2C2']['Speed'][index.end(): len(rawConfigDict['I2C2']['Speed'])]
            if (CLKSpeed == 'Fast'):
                I2C_Config['I2c2']['ClockSpeed'] = 400
            elif (CLKSpeed == 'Fast_Plus'):
                I2C_Config['I2c2']['ClockSpeed'] = 1000

        for item in rawConfigDict.keys():
            if 'Signal' in rawConfigDict[item]:
                if rawConfigDict[item]['Signal'] == 'I2C2_SDA':
                    I2C_Config['I2c2']['SDA'] = str.capitalize(str.lower(item))
                if rawConfigDict[item]['Signal'] == 'I2C2_SCL':
                    I2C_Config['I2c2']['SCL'] = str.capitalize(str.lower(item))

    if 'I2C3' in rawConfigDict.keys():
        I2C_Config['I2c3'] = dict()

        if 'Speed' in rawConfigDict['I2C3'].keys():
            indexFirstDigit = re.search("\d", rawConfigDict['I2C3']['Speed'])
            I2C_Config['I2c3']['ClockSpeed'] = rawConfigDict['I2C3']['Speed'][indexFirstDigit.start(): len(rawConfigDict['I2C3']['Speed'])]
        elif 'I2C_Speed_Mode' in rawConfigDict['I2C3'].keys():
            index = re.search("_", rawConfigDict['I2C3']['Speed'])
            CLKSpeed = rawConfigDict['I2C3']['Speed'][index.end(): len(rawConfigDict['I2C3']['Speed'])]
            if (CLKSpeed == 'Fast'):
                I2C_Config['I2c3']['ClockSpeed'] = 400
            elif (CLKSpeed == 'Fast_Plus'):
                I2C_Config['I2c3']['ClockSpeed'] = 1000

        for item in rawConfigDict.keys():
            if 'Signal' in rawConfigDict[item]:
                if rawConfigDict[item]['Signal'] == 'I2C3_SDA':
                    I2C_Config['I2c3']['SDA'] = str.capitalize(str.lower(item))
                if rawConfigDict[item]['Signal'] == 'I2C3_SCL':
                    I2C_Config['I2c3']['SCL'] = str.capitalize(str.lower(item))


    return I2C_Config