A Python package providing utilities for data science tasks, including automatic data visualization, text cleaning, and column type detection.

Features
Auto Visualizer: Automatically generate visualizations for numerical, categorical, and text columns in pandas DataFrames. Text Cleaner: Clean and preprocess text data by removing punctuation, stopwords, filler words, and applying lemmatization. Column Detector: Automatically detect column types (numerical, categorical, text) in pandas DataFrames.

Installation
Install the package using pip:

pip install ds-helper
Usagehttps://github.com/nirmala272006-arch/DS_helper/edit/main/README.md
Auto Visualizer
import pandas as pd
from ds_helper.auto_visualizer import plot_numerical, plot_categorical, plot_text, plot_pairplot

 Load your data
df = pd.read_csv('your_data.csv')

 Visualize numerical columns
plot_numerical(df)

 Visualize categorical columns
plot_categorical(df)

Visualize text columns
plot_text(df)

Create pairplot for numerical columns
plot_pairplot(df)
Text Cleaner
from ds_helper.text_cleaner import TextCleaner

 Initialize the cleaner
cleaner = TextCleaner(filler_words=['uh', 'um'], use_lemmatization=True)

#Clean text
clean_text = cleaner.clean("This is a sample text with some filler words like uh and um.")
print(clean_text)
Column Detector
from ds_helper.column_detector import detect_column_types

#Detect column types
types = detect_column_types(df, threshold=20)
print(types)
Dependencies
pandas
matplotlib
seaborn
wordcloud
nltk (optional, for text cleaning with stopwords and lemmatization)




Author
Nirmala Rathod
(https://github.com/nirmala272006-arch/DS_helper.git)
