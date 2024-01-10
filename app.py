import streamlit as st
import pandas as pd
import numpy as np

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    PrecisionRecallDisplay,
)
from sklearn.metrics import precision_score, recall_score


def main():
    st.title("StreamLit Title: Binary Classification Web App")
    st.sidebar.title("StreamLit Title: Binary Classification Web App")


if __name__ == "__main__":
    main()
