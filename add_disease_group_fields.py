##########################################################
#
# Author: Juan Ignacio Gil
# email: juan.ignacio.gil.gomez@gmail.com
# date: September 2014
#
##########################################################

"""
    add_disease_group_fields.py
    
    Explore the database and add the group and disease fields for all tweets, based on 
    their hastags
"""


from pymongo import MongoClient
import os

######################################################################################

#List of group and diseases

def create_list_of_diseases_and_groups(path):
    
    list_of_diseases_and_groups=[]
    
    #Navigate directory structure
    for group in os.listdir(path):
        try:
            for f in os.listdir(path+'/'+group):
                disease=f[7:-4]
                list_of_diseases_and_groups.append([disease,group])
        
        except:
            continue

    return list_of_diseases_and_groups


###########################################################################################


def find_disease_group(tweet):
    
    client = MongoClient()
    db = client['tweets']
    col = db.geo
    
    hashtags=[h['text'].lower() for h in tweet['entities']['hashtags']]
    
    l1=[['BleedingDisorders', 'Blood'], ['BloodCancer', 'Blood'], ['Cryoglobulinemia', 'Blood'], ['CryoGroup', 'Blood'], ['Hemophilia', 'Blood'], ['Leukaemia', 'Blood'], ['MMSM', 'Blood'], ['Myeloma', 'Blood'], ['Sepsis', 'Blood'], ['adcsm', 'Cancer'], ['ancsm', 'Cancer'], ['Angiosarcoma', 'Cancer'], ['BCANS', 'Cancer'], ['BCmets', 'Cancer'], ['BCSM', 'Cancer'], ['BladderCancer', 'Cancer'], ['blcsm', 'Cancer'], ['BloodCancer', 'Cancer'], ['BowelCancer', 'Cancer'], ['BrainCancer', 'Cancer'], ['BRCA', 'Cancer'], ['BRCA1', 'Cancer'], ['BRCA2', 'Cancer'], ['Brustkrebs', 'Cancer'], ['CancerChat', 'Cancer'], ['CancerFreeMe', 'Cancer'], ['CancerSurvivors', 'Cancer'], ['CervicalCancer', 'Cancer'], ['Chemo', 'Cancer'], ['ChildhoodCancer', 'Cancer'], ['ColonCancer', 'Cancer'], ['ColonChat', 'Cancer'], ['CRCSM', 'Cancer'], ['esocsm', 'Cancer'], ['GynCSM', 'Cancer'], ['hncsm', 'Cancer'], ['hpbcsm', 'Cancer'], ['hsronc', 'Cancer'], ['LCSM', 'Cancer'], ['Leukaemia', 'Cancer'], ['leusm', 'Cancer'], ['LiverCancer', 'Cancer'], ['LungCancer', 'Cancer'], ['Lymphoma', 'Cancer'], ['lymsm', 'Cancer'], ['LynchSyndrome', 'Cancer'], ['Lyphoma', 'Cancer'], ['mBCSM', 'Cancer'], ['MCAM', 'Cancer'], ['Melanoma', 'Cancer'], ['Mesothelioma', 'Cancer'], ['MMSM', 'Cancer'], ['Myeloma', 'Cancer'], ['NotJustOneDisease', 'Cancer'], ['OralCancer', 'Cancer'], ['OvarianCancer', 'Cancer'], ['OVCA', 'Cancer'], ['PanCan', 'Cancer'], ['pancsm', 'Cancer'], ['PCSM', 'Cancer'], ['ProstateCancer', 'Cancer'], ['radonc', 'Cancer'], ['RectalCancer', 'Cancer'], ['Retinoblastoma', 'Cancer'], ['scmsm', 'Cancer'], ['SkinCancer', 'Cancer'], ['stcsm', 'Cancer'], ['TesticularCancer', 'Cancer'], ['thmcsm', 'Cancer'], ['ThroatCancer', 'Cancer'], ['thycsm', 'Cancer'], ['ThyroidCancer', 'Cancer'], ['tscsm', 'Cancer'], ['XMRV', 'Cancer'], ['AFib', 'Cardiovasucular'], ['AtrialFibrillation', 'Cardiovasucular'], ['BloodClot', 'Cardiovasucular'], ['Cardiomyopathy', 'Cardiovasucular'], ['CHD', 'Cardiovasucular'], ['CHF', 'Cardiovasucular'], ['Cholesterol', 'Cardiovasucular'], ['CongestiveHeartFailure', 'Cardiovasucular'], ['CoronaryArteryDisease', 'Cardiovasucular'], ['DeepVeinThrombosis', 'Cardiovasucular'], ['DVT', 'Cardiovasucular'], ['Eclampsia', 'Cardiovasucular'], ['FMD', 'Cardiovasucular'], ['FMDaware', 'Cardiovasucular'], ['HeartDisease', 'Cardiovasucular'], ['HeartHealth', 'Cardiovasucular'], ['HighBloodPressure', 'Cardiovasucular'], ['HighCholesterol', 'Cardiovasucular'], ['HoFH', 'Cardiovasucular'], ['Hypertension', 'Cardiovasucular'], ['Lymphoedema', 'Cardiovasucular'], ['Preeclampsia', 'Cardiovasucular'], ['SCADheart', 'Cardiovasucular'], ['Thrombosis', 'Cardiovasucular'], ['Varicose', 'Cardiovasucular'], ['CleftLip', 'Congenital Anomolies'], ['CleftPalate', 'Congenital Anomolies'], ['CowdensSyndrome', 'Congenital Anomolies'], ['EmanuelSyndrome', 'Congenital Anomolies'], ['LongQT', 'Congenital Anomolies'], ['Marfan', 'Congenital Anomolies'], ['BowelCancer', 'Digestive'], ['CeliacDisease', 'Digestive'], ['Celiaquia', 'Digestive'], ['Cholera', 'Digestive'], ['Cirrhosis', 'Digestive'], ['Colitis', 'Digestive'], ['ColonCancer', 'Digestive'], ['ColonChat', 'Digestive'], ['ColonIrritable', 'Digestive'], ['CRCSM', 'Digestive'], ['Crohns', 'Digestive'], ['CrohnsDisease', 'Digestive'], ['Diverticulitis', 'Digestive'], ['EColi', 'Digestive'], ['Gallbladder', 'Digestive'], ['GERD', 'Digestive'], ['Halitosis', 'Digestive'], ['HCCD', 'Digestive'], ['Heartburn', 'Digestive'], ['Hepatitis', 'Digestive'], ['HepB', 'Digestive'], ['HepC', 'Digestive'], ['HepPartners', 'Digestive'], ['Hernia', 'Digestive'], ['IBD', 'Digestive'], ['IBS', 'Digestive'], ['LiverCancer', 'Digestive'], ['LiverDisease', 'Digestive'], ['LynchSyndrome', 'Digestive'], ['PanCan', 'Digestive'], ['RectalCancer', 'Digestive'], ['Ulcers', 'Digestive'], ['ChildhoodObesity', 'Endocrine'], ['Cushings', 'Endocrine'], ['Diabesity', 'Endocrine'], ['DiabetesEmpowered', 'Endocrine'], ['DiabetesLA', 'Endocrine'], ['Diabetics', 'Endocrine'], ['Gestationaldiabetes', 'Endocrine'], ['Gout', 'Endocrine'], ['Hypothyroidism', 'Endocrine'], ['InsightSBS', 'Endocrine'], ['MultipleEndocrineNeoplasia', 'Endocrine'], ['Overweight', 'Endocrine'], ['T1D', 'Endocrine'], ['ThyroidAwareness', 'Endocrine'], ['ThyroidCancer', 'Endocrine'], ['Triglycerides', 'Endocrine'], ['Bedwetting', 'Excretory'], ['BladderCancer', 'Excretory'], ['blcsm', 'Excretory'], ['Dialysis', 'Excretory'], ['ESRD', 'Excretory'], ['Incontinence', 'Excretory'], ['KidneyCancer', 'Excretory'], ['KidneyDisease', 'Excretory'], ['KidneyStones', 'Excretory'], ['Renal', 'Excretory'], ['RenalFailure', 'Excretory'], ['UTI', 'Excretory'], ['Deafness', 'ill Defined'], ['HearingLoss', 'ill Defined'], ['Menieres', 'ill Defined'], ['Nocturia', 'ill Defined'], ['Progeria', 'ill Defined'], ['RareDisease', 'ill Defined'], ['SIDS', 'ill Defined'], ['XMRV', 'ill Defined'], ['AIDS', 'Immune'], ['Alergia', 'Immune'], ['Allergies', 'Immune'], ['Amyloidosis', 'Immune'], ['ArtritisReumatoide', 'Immune'], ['Autoimmune', 'Immune'], ['FoodAllergy', 'Immune'], ['Glint', 'Immune'], ['HIVBC', 'Immune'], ['HIVchat', 'Immune'], ['IBD', 'Immune'], ['Lupus', 'Immune'], ['Myeloma', 'Immune'], ['PeanutAllergy', 'Immune'], ['PsoriaticArthritis', 'Immune'], ['Rheum', 'Immune'], ['RheumatoidArthritis', 'Immune'], ['Rhinitis', 'Immune'], ['SLE', 'Immune'], ['Urticaria', 'Immune'], ['AIDS', 'Infectious Disease'], ['Bronchitis', 'Infectious Disease'], ['Candidiasis', 'Infectious Disease'], ['Cholera', 'Infectious Disease'], ['Congestionnasal', 'Infectious Disease'], ['Dengue', 'Infectious Disease'], ['Flu', 'Infectious Disease'], ['Gripe', 'Infectious Disease'], ['Grippe', 'Infectious Disease'], ['H7N9', 'Infectious Disease'], ['Hepatitis', 'Infectious Disease'], ['HepB', 'Infectious Disease'], ['HepC', 'Infectious Disease'], ['HepPartners', 'Infectious Disease'], ['HIVBC', 'Infectious Disease'], ['HPV', 'Infectious Disease'], ['Influenza', 'Infectious Disease'], ['Leprosy', 'Infectious Disease'], ['Malaria', 'Infectious Disease'], ['McrFluSafe', 'Infectious Disease'], ['MdrTB', 'Infectious Disease'], ['Meningitis', 'Infectious Disease'], ['MRSA', 'Infectious Disease'], ['Pneumonia', 'Infectious Disease'], ['Resfriado', 'Infectious Disease'], ['STD', 'Infectious Disease'], ['Tuberculosis', 'Infectious Disease'], ['UTI', 'Infectious Disease'], ['YellowFever', 'Infectious Disease'], ['Anaphylaxis', 'Injury'], ['BackPain', 'Injury'], ['BrainInjury', 'Injury'], ['Deafness', 'Injury'], ['HearingLoss', 'Injury'], ['HeatStroke', 'Injury'], ['TBI', 'Injury'], ['BCANS', 'Lymphatic'], ['BCmets', 'Lymphatic'], ['BCSM', 'Lymphatic'], ['BRCA', 'Lymphatic'], ['BRCA1', 'Lymphatic'], ['BRCA2', 'Lymphatic'], ['Brustkrebs', 'Lymphatic'], ['Lymphoma', 'Lymphatic'], ['Lyphoma', 'Lymphatic'], ['mBCSM', 'Lymphatic'], ['HunterSyndrome', 'Metabolic'], ['MPSII', 'Metabolic'], ['Anaphylaxis', 'Multiple'], ['Andropause', 'Multiple'], ['Angiosarcoma', 'Multiple'], ['CancerChat', 'Multiple'], ['CancerSurvivors', 'Multiple'], ['Chemo', 'Multiple'], ['ChildhoodCancer', 'Multiple'], ['ChronicPain', 'Multiple'], ['CysticFibrosis', 'Multiple'], ['Dysautonomia', 'Multiple'], ['EhlersDanlos', 'Multiple'], ['FacialDifference', 'Multiple'], ['FacialDisfigurement', 'Multiple'], ['fragileX', 'Multiple'], ['HeatStroke', 'Multiple'], ['hncsm', 'Multiple'], ['Hyperglycemia', 'Multiple'], ['Inflammation', 'Multiple'], ['Malaria', 'Multiple'], ['Marfan', 'Multiple'], ['Mesothelioma', 'Multiple'], ['MRSA', 'Multiple'], ['NCDs', 'Multiple'], ['PainSomnia', 'Multiple'], ['PediatricCancer', 'Multiple'], ['Sarcoidosis', 'Multiple'], ['STD', 'Multiple'], ['YellowFever', 'Multiple'], ['Arthritis', 'Musculoskeletal'], ['Artritis', 'Musculoskeletal'], ['BackPain', 'Musculoskeletal'], ['Bursitis', 'Musculoskeletal'], ['CarpalTunnelSyndrome', 'Musculoskeletal'], ['dupuytrens', 'Musculoskeletal'], ['Fibromyalgia', 'Musculoskeletal'], ['HipPain', 'Musculoskeletal'], ['Myositis', 'Musculoskeletal'], ['Osteoarthritis', 'Musculoskeletal'], ['Osteoporosis', 'Musculoskeletal'], ['Sciatica', 'Musculoskeletal'], ['Spondylitis', 'Musculoskeletal'], ['TeamSpondy', 'Musculoskeletal'], ['TennisElbow', 'Musculoskeletal'], ['ADD', 'Neurological'], ['ALS', 'Neurological'], ['Alzheimer', 'Neurological'], ['Alzheimers', 'Neurological'], ['Arachnoiditis', 'Neurological'], ['Aspergers', 'Neurological'], ['Ataxia', 'Neurological'], ['BattenDisease', 'Neurological'], ['BrainCancer', 'Neurological'], ['BrainInjury', 'Neurological'], ['BrainTumor', 'Neurological'], ['BTSM', 'Neurological'], ['CaudaEquina', 'Neurological'], ['Cerebral', 'Neurological'], ['Chiari', 'Neurological'], ['DementiaChallengers', 'Neurological'], ['DownSyndrome', 'Neurological'], ['Dysautonomia', 'Neurological'], ['Dystonia', 'Neurological'], ['Epilepsy', 'Neurological'], ['IIH', 'Neurological'], ['MemoryLoss', 'Neurological'], ['Meningitis', 'Neurological'], ['Migraine', 'Neurological'], ['MND', 'Neurological'], ['MoebiusSyndrome', 'Neurological'], ['MultScler', 'Neurological'], ['Narcolepsy', 'Neurological'], ['Neuropathy', 'Neurological'], ['Parkinsons', 'Neurological'], ['RettSyndrome', 'Neurological'], ['Seizures', 'Neurological'], ['Shingles', 'Neurological'], ['Stroke', 'Neurological'], ['Synesthesia', 'Neurological'], ['TBI', 'Neurological'], ['theARCchat', 'Neurological'], ['TrigeminalNeuralgia', 'Neurological'], ['ADHD', 'Other Files'], ['Alopecia', 'Other Files'], ['Anorexia', 'Other Files'], ['Autism', 'Other Files'], ['Breastcancer', 'Other Files'], ['Cancer', 'Other Files'], ['Celiac', 'Other Files'], ['ChronicPain', 'Other Files'], ['CysticFibrosis', 'Other Files'], ['Dementia', 'Other Files'], ['Depression', 'Other Files'], ['Diabetes', 'Other Files'], ['Diabetic', 'Other Files'], ['Dyslexia', 'Other Files'], ['EDS', 'Other Files'], ['Fibromyalgia', 'Other Files'], ['HIV', 'Other Files'], ['Leukemia', 'Other Files'], ['LungCancer', 'Other Files'], ['MERS', 'Other Files'], ['MultipleSclerosis', 'Other Files'], ['Obesity', 'Other Files'], ['PancreaticCancer', 'Other Files'], ['Polio', 'Other Files'], ['PTSD', 'Other Files'], ['AnorexiaNervosa', 'Psych'], ['Anxiety', 'Psych'], ['BDD', 'Psych'], ['bePNDaware', 'Psych'], ['Bipolar', 'Psych'], ['BipolarDisorder', 'Psych'], ['BPD', 'Psych'], ['Bulimia', 'Psych'], ['EatingDisorder', 'Psych'], ['EatingDisorders', 'Psych'], ['EndEd', 'Psych'], ['Hypochondria', 'Psych'], ['OCD', 'Psych'], ['PPD', 'Psych'], ['PPDchat', 'Psych'], ['Schizofrenie', 'Psych'], ['Schizophrenia', 'Psych'], ['Trichotillomania', 'Psych'], ['ALS', 'Rare Diseases'], ['Amyloidosis', 'Rare Diseases'], ['Ataxia', 'Rare Diseases'], ['BattenDisease', 'Rare Diseases'], ['CowdensSyndrome', 'Rare Diseases'], ['Cryoglobulinemia', 'Rare Diseases'], ['CryoGroup', 'Rare Diseases'], ['Cushings', 'Rare Diseases'], ['EmanuelSyndrome', 'Rare Diseases'], ['FMD', 'Rare Diseases'], ['FMDaware', 'Rare Diseases'], ['GPFAD2013', 'Rare Diseases'], ['HunterSyndrome', 'Rare Diseases'], ['Marfan', 'Rare Diseases'], ['Mastocytosis', 'Rare Diseases'], ['Mesothelioma', 'Rare Diseases'], ['MoebiusSyndrome', 'Rare Diseases'], ['MPSII', 'Rare Diseases'], ['MultipleEndocrineNeoplasia', 'Rare Diseases'], ['Myositis', 'Rare Diseases'], ['PulmonaryFibrosis', 'Rare Diseases'], ['RareDisease', 'Rare Diseases'], ['RareDiseaseDay', 'Rare Diseases'], ['RettSyndrome', 'Rare Diseases'], ['Sarcoidosis', 'Rare Diseases'], ['SCADheart', 'Rare Diseases'], ['TrigeminalNeuralgia', 'Rare Diseases'], ['Vasculitis', 'Rare Diseases'], ['CervicalCancer', 'Reproductive'], ['Endometriosis', 'Reproductive'], ['Fibroid', 'Reproductive'], ['Fibroids', 'Reproductive'], ['GynCSM', 'Reproductive'], ['HPV', 'Reproductive'], ['Infertility', 'Reproductive'], ['OvarianCancer', 'Reproductive'], ['OVCA', 'Reproductive'], ['PCOS', 'Reproductive'], ['PCSM', 'Reproductive'], ['Peyronies', 'Reproductive'], ['PeyroniesDisease', 'Reproductive'], ['Preeclampsia', 'Reproductive'], ['ProstateCancer', 'Reproductive'], ['SecondaryInfertility', 'Reproductive'], ['TesticularCancer', 'Reproductive'], ['Asthma', 'Respiratory'], ['Bronchitis', 'Respiratory'], ['Congestionnasal', 'Respiratory'], ['COPD', 'Respiratory'], ['Flu', 'Respiratory'], ['GPFAD2013', 'Respiratory'], ['Gripe', 'Respiratory'], ['Grippe', 'Respiratory'], ['Influenza', 'Respiratory'], ['LCSM', 'Respiratory'], ['McrFluSafe', 'Respiratory'], ['McrFluSafe13', 'Respiratory'], ['MdrTB', 'Respiratory'], ['Pneumonia', 'Respiratory'], ['PulmonaryFibrosis', 'Respiratory'], ['Resfriado', 'Respiratory'], ['Rhinitis', 'Respiratory'], ['SleepApnea', 'Respiratory'], ['SleepDisorder', 'Respiratory'], ['StockportFluFighting', 'Respiratory'], ['Tuberculosis', 'Respiratory'], ['Cholesteatoma', 'Sense Organs'], ['ACNE', 'Skin'], ['Angioedema', 'Skin'], ['Bald', 'Skin'], ['Baldness', 'Skin'], ['Eczema', 'Skin'], ['HairLoss', 'Skin'], ['Hives', 'Skin'], ['Leprosy', 'Skin'], ['Mastocytosis', 'Skin'], ['Melanoma', 'Skin'], ['Psoriasis', 'Skin'], ['Shingles', 'Skin'], ['SkinCancer', 'Skin'], ['Urticaria', 'Skin']]
    l2=[[d[0].lower(),d[1].lower()] for d in l1]
    
    #Search for disease in the hashtags and add it to the group
    dg=['None','None']
    for d in l2:
        if d[0] in hashtags:
            dg=d
            break
    
    return dg

###########################################################################################


def update_all_tweets_in_database():
    
    """
        Go through the tweets in the database
        """
    
    #Database
    client = MongoClient()
    db = client['tweets']
    col = db.geo
    
    docs=col.find().batch_size(50)
    #docs=col.find().batch_size(50)
    total=docs.count()
    print repr(total)+' documents to include group and disease'
    nt=0
    
    #Iterate over all elements in the collection without n-grams field
    for tweet in docs:
        dg=find_disease_group(tweet)
        col.update({'_id':tweet['_id']}, {'$set': {'group':dg[0],'disease':dg[1]}}, upsert=False)
        nt+=1
        
        #Just for let you know that it's working
        if nt%1000==0:
            print tweet['text']+' ... '+repr(nt*100/total)+'% done...'

