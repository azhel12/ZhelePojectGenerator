import re

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

    return timerConf