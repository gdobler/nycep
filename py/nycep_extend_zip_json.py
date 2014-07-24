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

    # -- add in pcnt parks
    lines = [line for line in open('../output/zips_park_pcnt.csv')][1:]
    value_dic = {}
    for line in lines:
        tzip, value     = line.split(',')
        value_dic[tzip] = float(value)

    nycep_extend_zip_json('pctpark',value_dic)


    # -- add the ZBP and ACS data
    lines = [line for line in open('../data/featuresForMap.csv')][1:]
    inc_dic = {}
    emp_dic = {}
    pay_dic = {}
    est_dic = {}
    sal_dic = {}
    for line in lines:
        tzip, inc, emp, pay, est = line.split(',')

        inc = float(inc) if len(inc)>0 else 0.0
        emp = float(emp) if len(emp)>0 else 0.0
        pay = float(pay) if len(pay)>0 else 0.0
        est = float(est) if len(est)>0 else 0.0

        inc_dic[tzip] = inc
        emp_dic[tzip] = emp
        pay_dic[tzip] = pay
        est_dic[tzip] = est
        sal_dic[tzip] = pay/(emp+(emp==0))

    nycep_extend_zip_json('median_hh_income', inc_dic, 
                          ofile='nyc-zip-code-extend.json', opath='../output', 
                          dfile='nyc-zip-code-extend.json', dpath='../output')

    nycep_extend_zip_json('num_employees', emp_dic, 
                          ofile='nyc-zip-code-extend.json', opath='../output', 
                          dfile='nyc-zip-code-extend.json', dpath='../output')

    nycep_extend_zip_json('payroll', pay_dic, 
                          ofile='nyc-zip-code-extend.json', opath='../output', 
                          dfile='nyc-zip-code-extend.json', dpath='../output')

    nycep_extend_zip_json('num_establishments', est_dic, 
                          ofile='nyc-zip-code-extend.json', opath='../output', 
                          dfile='nyc-zip-code-extend.json', dpath='../output')

    nycep_extend_zip_json('salary', sal_dic, 
                          ofile='nyc-zip-code-extend.json', opath='../output', 
                          dfile='nyc-zip-code-extend.json', dpath='../output')
