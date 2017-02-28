import pandas as pd
import sklearn
import numpy as np
from sklearn import datasets, linear_model

def mentalhealthPredictor():

    dataset= pd.read_csv('survey_deleted250.csv')



    dataset= dataset.rename(columns={'Timestamp':'timestamp',
                                'When something good happens to me, I have people who I like to share the good news with.	':'Q1',
                                'I finish whatever I begin.	':'Q2',
                               'When I do an	activity, I	enjoy it so much that I	lose track of time.	':'Q3',
                               'I get completely absorbed	in what I	am doing.	':'Q4',
                               'I am optimistic about my future	':'Q5',
                               'I keep at	my collegework until I	am	done with it.	':'Q6',
                               'When I have a problem, I have someone	who will be there for me.	':'Q7',
                               'In uncertain times, I expect the	best.	':'Q8',
                               'There are people in my life	who really care about me.	':'Q9',
                               'I think good things are going to	happen to me.	':'Q10',
                               'I have friends that I really care about.	':'Q11',
                               'Once I make a plan to	get something done, I stick to it.':'Q12',
                               'I believe	that	things will work out, no matter how difficult they seem.':'Q13',
                               'I work hard.	':'Q14',
                               'I have a lot of fun':'Q15',
                               'From the below categories which one do you identify with the most':'label'})


    dataset=dataset.drop('timestamp', axis=1)



    dataset.label[dataset.label=="Mentally distressed"] = 0
    dataset.label[dataset.label=="unaffected with life (neutral)"] = 1
    dataset.label[dataset.label=="Optimistic and happy with life"] = 2



    dataset[dataset=='Almost always'] = 2
    dataset[dataset=='Very Often'] = 1
    dataset[dataset=='Often'] = 0
    dataset[dataset=='Sometimes'] = -1
    dataset[dataset=='Almost never'] = -2


    dataset = dataset.astype(int)


    Y = np.array(dataset.label)
    X = np.array(dataset.drop('label',axis=1))


    from sklearn.model_selection import train_test_split
    train_x, validation_x, train_y, validation_y = train_test_split(X, Y, test_size=0.2, random_state= 0)



    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier(n_estimators = 200, oob_score = True, n_jobs = -1,random_state =50,max_features = "auto",min_samples_leaf = 2)
    rf.fit(train_x,train_y)
    output_rf = rf.predict(validation_x)
    return rf


