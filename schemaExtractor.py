from __future__ import with_statement
import json
import os
import sys


def main2():
    with open('schema.json','r') as jf:
        ss = jf.read()
        ob = json.loads(ss)

        for k, v in ob.items():
            print k
            for kk, vv in v.items():
                print kk
                for kkk, vvv in vv.items():
                    print kkk, vvv


def main():
    path = 'E:\\Work\\schema'  # sys.argv[0]
    files = get_all_files(path)
    strs = []
    par = []
    types = []

    schemas = {}

    for fn in files:
        with open(fn, 'r') as fio:
            if not str(fn).lower().split('.')[0].endswith('_all'):
                continue

            print fn
            ds = os.path.basename(fn).split('_')
            strs.append(ds[0])
            strs.append('')
            js = fio.read()
            obj = json.loads(js)

            schema = {}

            for k, v in obj.items():
                if k == 'schema':
                    for key, val in v.items():
                        if key == 'ACL':
                            continue

                        col = {}
                        strs.append('--' + key)
                        for kk, vv in val.items():

                            if kk == 'v' or kk == 'read_only' or kk == 'user_private' or kk == 'comment':
                                continue

                            ck = kk
                            cv = ''

                            if kk not in par:
                                par.append(kk)

                            if kk == 'type':
                                if vv not in types:
                                    types.append(vv)

                            try:
                                strs.append('\t--' + kk + ':' + str(vv))
                                cv = str(vv)
                            except Exception:
                                # print Exception.message
                                # print '::::', key, kk, vv

                                # strs.append('\t--' + kk)
                                s = ''

                                if type(vv) is bool:
                                    print 'bool found'
                                    s = str(vv)
                                else:
                                    # print type(vv)
                                    s = vv.encode('utf-8')
                                    # print type(s)
                                strs.append('\t--' + kk + ':' + s.decode('utf-8'))
                                cv = s
                            finally:
                                pass

                            col[ck] = cv
                        schema[key] = col

            schemas[ds[0]] = schema
        strs.append('')
        strs.append('')
    # print strs
    print schemas

    jstr = json.dumps(schemas)

    print jstr

    with open('schema.json','w') as jf:
        jf.write(jstr)

    with open('file.txt', 'w') as fo:
        for s in strs:
           fo.write(s.encode('utf-8'))
           fo.write('\r\n')

        for p in par:
            fo.write(p)
            fo.write('\r\n')
        fo.write('\r\n')
        fo.write('\r\n')

        for t in types:
            fo.write(t)
            fo.write('\r\n')


def get_all_files(path):
    files = os.listdir(path)
    allfiles = []
    for fn in files:
        longfile = os.path.join(path, fn)
        if not os.path.isdir(longfile):
            allfiles.append(longfile)
    return allfiles


if __name__ == '__main__':
    main2()
