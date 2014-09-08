import calculate_frequencies as cf
import add_ngrams_mongo as addng
import calculate_specific_ngrams as spn
import add_disease_group_fields as adg

#import time

#start_time = time.time()


#addng.update_all_tweets_in_database(4)
#cf.insert_all_relative_frequencies()

#f=cf.calculate_frequencies_whole_corpus(4)
#f=cf.calculate_all_frequencies(2,'group','Blood')
#print f

l=adg.create_list_of_diseases_and_groups('/Users/cato/programacion/HealthCare_Twitter_Analysis/Twitter Data/Jan to May')
print l



