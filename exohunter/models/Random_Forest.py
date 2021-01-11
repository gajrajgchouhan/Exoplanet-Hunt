import sklearn.metrics as m
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from exohunter import reader

__all__ = ['Random_Forest']

class Random_Forest:
    def __init__(self, loc, test_size=0.3, random_state=42):
        labels, fluxes = reader(loc)
        X_train, X_test, y_train, y_test = train_test_split(
            fluxes, labels, test_size=test_size, random_state=random_state)
        self.y_test = y_test
        classifier = RandomForestClassifier(max_features = 'sqrt')
        classifier.fit(X_train, y_train)
        self.y_pred = classifier.predict(X_test)
        self.confusion_matrix = m.confusion_matrix(self.y_pred, y_test)
        self.accuracy = m.accuracy_score(y_test, self.y_pred)
        self.recall = m.recall_score(y_test, self.y_pred)
        self.precision = m.precision_score(y_test, self.y_pred)

    def print_scores(self):
        print('Accuracy:', self.accuracy)
        print('Precision:', self.precision)
        print('Recall:', self.recall)

    def classification_report(self):
        return m.classification_report(self.y_pred, self.y_test)
