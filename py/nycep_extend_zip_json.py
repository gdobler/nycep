import os
import json
import pandas as pd

# -------- 
#  Extend the json file with additional attributes
#
#  2014/07/21 - Written by Greg Dobler (CUSP/NYU)
# -------- 

def nycep_extend_zip_json(key, value_dic, ofile='nyc-zip-code-extend.json', 
                          opath='../output', dfile='nyc-zip-code.json', 
                          dpath='../data'):

    # -- ensure unicode
    key = unicode(key)

    # -- get the original json data
    data = json.load(open(os.path.join(dpath,dfile)))


    # -- loop through zips and add the appropriate key and values
    nzip = len(data['features'])
    for ii in range(nzip):
        tzip = data['features'][ii]['properties']['ZIP']
        try:
            tvalue = value_dic[tzip]
            data['features'][ii]['properties'][key] = tvalue
        except:
            data['features'][ii]['properties'][key] = 0.0


    # -- write to json
    json.dump(data,open(os.path.join(opath,ofile),'w'))

    return


if __name__=='__main__':

    # -- read in csv file
    lines = [line for line in open('../output/zips_park_pcnt.csv')][1:]
    value_dic = {}
    for line in lines:
        tzip, value     = line.split(',')
        value_dic[tzip] = float(value)

    nycep_extend_zip_json('pctpark',value_dic)
