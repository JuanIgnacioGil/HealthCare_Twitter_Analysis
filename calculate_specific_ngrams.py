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
def calculate_frequency(level,field,n):

    #Find the ngrams for this {level:field} ordered by frequency
    
    client = MongoClient()
    db = client['HealthCare_Twitter_Analysis']
    col = db.frequencies

    #Defining the pipeline
    pipeline=[\
              {'$match': {'_id.'+level:field}},\
              {'$match' : {'n' : n}},\
              {'$project':{'_id':0,'text':'$_id.text',\
              'frequency':1,\
              'lambda':{'$divide': [ 1,'$relative frequency'] }}},\
              { '$sort' : { 'lambda' : 1} }
          ]


    f=col.aggregate(pipeline, allowDiskUse=True)

    #For each n-gram, search for the total frequency, and if the difference is significative,
    #add it to the solution
    charngrams=[]

    for ngram in f['result']:
        g=col.find({ '_id' : { 'text' : ngram['text'], 'all' : 'True' } })

        #Frequencies in the disease
        fd=[1,ngram['lambda']-1]
        N=fd[1]+1
        ft=[N*g[0]['relative frequency'],N*(1-g[0]['relative frequency'])]

        #Chi square test to decide if the difference is significative
        chi=st.chisquare(fd,ft)

        if chi[1]<0.05:
            t=' '.join(ngram['text'])
            charngrams.append({'text':t,'frequency':ngram['frequency']})

        if len(charngrams)==100:
            break

    return charngrams
