#importing the pre_processing function form the pre_processing.py file
from pre_processing import pre_processing

#importing the required models from the sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
#assigning the values

#print(X_train, X_test, y_train, y_test)
#print(y_test.dtypes)
DC = DecisionTreeClassifier()
RF = RandomForestClassifier()
KNN = KNeighborsClassifier()
SVC = SVC()

def model_selection():
    X_train, X_test, y_train, y_test = pre_processing()
    acc = []
    for i in range(1):
        #print(i)
        DC.fit(X_train, y_train)
        #print("Accuracy obtained by Decision Tree Classifier model: " + str(DC.score(X_test, y_test)*100) + " %")
        dc = round(DC.score(X_test, y_test)*100)
        acc.append(dc)
        RF.fit(X_train, y_train)
        #print("Accuracy obtained by RandomForestClassifier model: " + str(RF.score(X_test, y_test)*100) + " %")
        rf = round(RF.score(X_test, y_test)*100)
        acc.append(rf)
        KNN.fit(X_train, y_train)
        #print("Accuracy obtained by RandomForestClassifier model: " + str(KNN.score(X_test, y_test)*100) + " %")
        knn = round(KNN.score(X_test, y_test)*100)
        acc.append(knn)
        SVC.fit(X_train, y_train)
        #print("Accuracy obtained by RandomForestClassifier model: " + str(SVC.score(X_test, y_test)*100) + " %")
        svc = round(SVC.score(X_test, y_test)*100)
        acc.append(svc)
    maximum = max(acc)
    if maximum == dc:
        a = dc
        b = "DC"
        #print("DC")
    elif maximum == rf:
        #print("RF")
        a = rf
        b = "RF"
    elif maximum == knn:
        #print("KNN")
        a = knn
        b = "KNN"
    else:
        #print(SVC)
        a = svc
        b = "SVC"

    #print(a,b)
    return(a,b) 
#model_selection()
