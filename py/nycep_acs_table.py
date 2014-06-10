import numpy as np
from nycep_acs_read_table import *

class AcsTable():

    def __init__(cls,tlabel,year=2012,summary=5,dpath=None):

        # -- check path
        if dpath==None:
            print("Must set data path to ACS data!")
            return


        # -- initialize values
        cls.id   = tlabel
        cls.name = [i.split(',')[1][:-1] for i in 
                    open(os.path.join('../output/acs',str(year),
                                      str(summary),'table_names.csv'),
                         'r') if i.split(',')[0]==cls.id][0]


        # -- get the fields
        sfile  = os.path.join(dpath,str(year),str(summary),
                              'Sequence_Number_and_Table_Number_Lookup.txt')
        slines = [line for line in open(sfile,'r') if 
                  line.split(',')[1]==cls.id]

        cls.fields = []

        for line in slines:
            recs = line.split(',')
            if (len(recs[3])>0) and not recs[3].isspace():
                cls.fields.append(recs[7])


        # -- get the data from the table
        print("Reading ACS table")
        print("  {0}".format(cls.name))
        print("  id   : {0}".format(cls.id))
        print("  year : {0}".format(year))
        print("  avg  : {0}".format(summary))

        data = nycep_acs_read_table(cls.id,year=year,summary=summary,
                                    dpath=dpath)

        cls.fileid   = data['fileid']
        cls.filetype = data['filetype']
        cls.stusab   = data['stusab']
        cls.chariter = data['chariter']
        cls.sequence = data['sequence']
        cls.logrecno = np.array(data['logrecno'])
        cls.data     = np.array(data['vals']).astype(np.float)

        return
