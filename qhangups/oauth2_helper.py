
def parseOAuth2Title(title):
    res = {};
    titleRes = title.split(' ')
    if len(titleRes) == 2:
        for kv in titleRes[1].split('&'):
            pair = kv.split('=')
            res[pair[0]] = pair[1]
    return [titleRes[0], res]
