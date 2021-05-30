def global_Pars(fileName):
    f = open(fileName)
    rawConfigDict = dict()
    flag = 0

    for line in f:

        if flag == 0:
            flag = 1
            continue

        var = line[0:line.index('=')]
        val = line[line.index('=') + 1:len(line)]
        if '.' in var:
            key = var[0:line.index('.')]
            subKey = var[line.index('.') + 1: len(line)]
        else:
            key = var
            subKey = val
        if key in rawConfigDict:
            rawConfigDict[key][subKey] = val[: -1]
        else:
            rawConfigDict[key] = {subKey: val[: -1]}

    return rawConfigDict