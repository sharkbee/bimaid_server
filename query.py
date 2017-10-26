
relatsymbols = dict()

relatsymbols['$ne'] = '!='
relatsymbols['$lt'] = '<'
relatsymbols['$lte'] = '<='
relatsymbols['$gt'] = '>'
relatsymbols['$gte'] = '>='


def makequery(content):

    cname = content['class']

    includes = []

    for k, v in content['condition'].items():

        if k == 'where':
            makequerygroup(cname, 'and', v)
            pass
        elif k == 'limit':
            # limit
            pass
        elif k == 'order':
            rev = False
            if v.startswith('-'):
                rev = True

            pass
        elif k == 'keys':
            pass
        elif k == 'include':

            includes = v.split(',')
            pass
        elif k == 'skip':
            # offset

            pass


def makequerygroup(clsname, ret, content):

    if ret == 'and':
        pass
    else:
        pass

    for k, v in content.items():
        if k == '$and' or k == '$or':

            makequerygroup(clsname, k.replace('$', ''), v)
        else:
            makequerystate(k, v)
            pass


def makequerystate(clsname, colname, content):

    querylist = []

    if content is dict:
        for k, v in content.items():
            qstr = ''
            if k == '$inQuery':
                vars = pickids(runquery(makequery(v)))

                qstr = makeinstate(clsname, colname, vars)

                pass
            elif k == '$select':
                vars = pickcol(v['key'], runquery(makequery(v['query'])))

                qstr = makeinstate(clsname, colname, vars)

                pass
            elif k == '$dontSelect':
                vars = pickcol(v['key'], runquery(makequery(v['query'])))

                qstr = makeinstate(clsname, colname, vars, notin=True)

                pass
            elif k == '$in':
                # dont know if neccesary, if the json class represent this as list, then just use it
                vars = v.split(',')

                qstr = makeinstate(clsname, colname, vars)

                pass
            elif k == '$nin':
                # dont know if neccesary, if the json class represent this as list, then just use it
                vars = v.split(',')

                qstr = makeinstate(clsname, colname, vars, notin=True)

                pass
            elif k == '$exists':
                pstr = '.'.join(clsname, colname)
                if v:
                    qstr = pstr + '!=None'
                else:
                    qstr = pstr + '==None'

                pass
    else:
        # equal statement
        rhalf = makevalue(clsname, colname, content)
        qstr = '.'.join(clsname, colname) + '==' + rhalf
        querylist.append(qstr)

    if len(querylist) > 1:
        return 'and_(' + ','.join(querylist) + ')'
    else:
        next(iter(querylist), '')


def makeinstate(clsname, colname, vars, notin=False):
    vals = []
    for var in vars:
        vals.append(makevalue(clsname, colname, var))
    instr = 'in_([' + ','.join(vals) + ')]'

    pre = ''

    if notin:
        pre = '~'

    qstr = '.'.join([pre + clsname, colname, instr])

    return qstr


def makevalue(clsname, colname, content):
    # check col type if is text
    # add quote or not
    return ''


def runquery(query):
    return []
    pass


def pickids(result):
    return []
    pass


def pickcol(colname, result):
    return []
    pass