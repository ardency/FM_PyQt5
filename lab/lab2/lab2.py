import re
import copy
from pprint import pprint
import numpy as np

class student():
    def __init__(self,name):
        self.name=name
        self.score_info = {}
        self.rank_info = {}
        self.total_score = 0
    def set_score(self,subject,score):
        self.score_info[subject] = score
    def count_total(self):
        for s in self.score_info.keys():
            self.total_score += self.score_info[s]
    def set_rank(self,subject,rank):
        self.rank_info[subject] = ra

class subject():
    def __init__(self,name):
        self.name=name
        self.score={}
        self.rank = []
        self.avg = 0
        self.std = 0
    def load_score(self,data):
        for k in data:
            self.score[k] = float(data[k])
        #self.score = copy.deepcopy(data)
    def rank_student(self):
        self.rank = sorted(self.score.items(), key=lambda x:x[1],reverse=True)
        #print(self.rank)
        idx = 1
        print("Subject: %s" % self.name)
        for st,s in self.rank:
            print("\t Rank : %2d : Student: %10s [%.2f] " % ( idx, st, s))
            idx += 1
    def stat_score(self):
        #pprint(self.score.values())
        self.avg = np.mean(list(self.score.values()))
        self.std  = np.std(list(self.score.values()))
        print("Subject: %s : Avg score : %.2f ; std-mean: %f" % (self.name,self.avg,self.std))

class Class():
    def __init__(self,name='Class#2'):
        self.name=name
        self.score_data={}
        self.subjects = []
        self.sObjs = []
    def load_score(self,data_file,verbose=False):
        titles = []
        with open(data_file,'r') as fh:
            for l in fh.readlines():
                if re.match('Name',l):
                    titles=l.split(',')
                    #print(titles)
                    for i in titles:
                        if re.match('Name',i): continue
                        self.subjects.append(i.strip())
                        self.score_data[i.strip()] = {}
                    self.score_data['total'] = {}
                    #self.subjects.append('total')
                else:
                    sinfo=l.split(',')
                    sdict = {}
                    for i in range(0,len(titles)):
                        sdict[titles[i].strip()] = sinfo[i].strip()
                    for s in self.subjects:
                        self.score_data[s][sdict['Name']] = sdict[s]
                    #self.score_data[sdict['Name']] = copy.deepcopy(sdict)
                    st = 0
                    for s in sdict.keys():
                        if s == 'Name': continue
                        st += float(sdict[s])
                    self.score_data['total'][sdict['Name']] = st
        if verbose:
            pprint(self.score_data)
        #pprint(self.score_data)
        self.subjects.append('total')
        for s in self.subjects:
            SbjObj = subject(name=s)
            SbjObj.load_score(data=self.score_data[s])
            self.sObjs.append(SbjObj)

    def rank_student(self):
        for sObj in self.sObjs:
            sObj.rank_student()
    def stat_score(self):
        for sObj in self.sObjs:
            sObj.stat_score()


#def load_score():

if __name__=='__main__':
    data_file = './data.csv'
    MyClass = Class()
    MyClass.load_score(data_file)
    MyClass.rank_student()
    MyClass.stat_score()
    #score_data = load_score(data_file)
    #sort1(score_data)
    #sort2(score_data)
    #caculate_data(score_data)