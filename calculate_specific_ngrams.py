##########################################################
#
# Author: Juan Ignacio Gil
# email: juan.ignacio.gil.gomez@gmail.com
# date: August 2014
#
##########################################################

"""
    calculate_specific_ngrams.py
    
    Explore the database and calculate (and include in the database) the ngrams which have frequencies 
    significantly higher for a particular disease than for the whole corpus
    
"""


from pymongo import MongoClient
import scipy.stats as st

###########################################################################################

#Calculate specific ngrams
def calculate_characteristic_ngrams(level,field,n):

    #Find the ngrams for this {level:field} ordered by frequency
    
    client = MongoClient()
    db = client['HealthCare_Twitter_Analysis']
    col = db.frequencies
    ngtemp=db.ngtemp()

    #Defining the pipeline
    pipeline=[\
              {'$match': {'_id.'+level:field}},\
              {'$match' : {'n' : n}},\
              {'$project':{'_id':0,'text':'$_id.text',\
              'frequency':1,\
              'lambda':{'$divide': [ 1,'$relative frequency'] }}},\
              { '$sort' : { 'lambda' : 1}},\
              {'$out':'ngtemp'}
          ]


    col.aggregate(pipeline, allowDiskUse=True)

    #For each n-gram, search for the total frequency, and if the difference is significative,
    #add it to the solution
    charngrams=[]

    for ngram in ngtemp.find():
        g=col.find({ '_id' : { 'text' : ngram['text'], 'all' : 'True' } })

        #Frequencies in the disease
        fd=[1,ngram['lambda']-1]
        N=fd[1]+1
        ft=[N*g[0]['relative frequency'],N*(1-g[0]['relative frequency'])]

        #Chi square test to decide if the difference is significative
        chi=st.chisquare(fd,ft)

        if chi[1]<0.05:
            charngrams.append({'text':ngram['text'],'frequency':ngram['frequency']})

        if len(charngrams)==100:
            break

    result={}
    result['ngrams']=charngrams
    result[level]=field
    result['n']=n
    ngtemp.drop()
    return result

######################################################################################

#Insert in the database all charasteristic ngrams for each group and disease

def insert_all_characteristic_ngrams():
    
    client = MongoClient()
    db = client['HealthCare_Twitter_Analysis']
    ctw = db.tweets
    cchar= db.charngrams
    cchar.drop()
    
    #List of groups
    groups=db.tweets.distinct('group')
    diseases=db.tweets.distinct('disease')
    
    for n in range(1,5):
        
        #Insert the relative frequencies for each group
        for g in groups:
            f=calculate_characteristic_ngrams('group',g,n)
            cchar.insert(f)
            print('Completed for the group '+repr(g)+' n='+repr(n))
        
        #Insert the relative frequencies for each disease
        for d in diseases:
            f=calculate_characteristic_ngrams('disease',d,n)
            cchar.insert(f)
            print('Completed for the disease '+repr(d)+' n='+repr(n))
