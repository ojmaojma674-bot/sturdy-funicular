import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression


class LinearRegressionPredictor:
    """Predict rental price from room size using a simple regression model."""

    def __init__(self):
        X = np.array(
            [
                [500.0],
                [700.0],
                [900.0],
                [1100.0],
                [1300.0],
                [1500.0],
                [1700.0],
                [1900.0],
            ],
            dtype=float,
        )
        y = np.array([1500.0, 1800.0, 2200.0, 2500.0, 2900.0, 3300.0, 3600.0, 4100.0], dtype=float)

        self.model = LinearRegression()
        self.model.fit(X, y)

    def predict(self, room_size: float) -> float:
        size = float(room_size)
        prediction = self.model.predict(np.array([[size]], dtype=float))[0]
        return float(prediction)


class LogisticRegressionPredictor:
    """Predict success probability using a binary logistic regression model."""

    def __init__(self):
        X = np.array(
            [
                [1.0, 55.0],
                [2.0, 60.0],
                [3.0, 62.0],
                [4.0, 68.0],
                [5.0, 72.0],
                [6.0, 75.0],
                [7.0, 80.0],
                [8.0, 88.0],
            ],
            dtype=float,
        )
        y = np.array([0, 0, 0, 1, 1, 1, 1, 1], dtype=int)

        self.model = LogisticRegression(random_state=42, max_iter=1000)
        self.model.fit(X, y)

    def predict(self, study_hours: float, attendance: float) -> dict:
        feature_vector = np.array([[float(study_hours), float(attendance)]], dtype=float)
        probability = float(self.model.predict_proba(feature_vector)[0][1])
        prediction = int(probability >= 0.5)

        return {
            "probability": probability,
            "prediction": prediction,
            "label": "pass" if prediction == 1 else "fail",
        }


__all__ = ["LinearRegressionPredictor", "LogisticRegressionPredictor"]
