import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'test_score': [85.5, 92.0, 78.5, 65.0, 88.0, 95.5, 72.0, 81.0, 99.5, 68.0],
    'grade_level': ['Fresher', 'Top', 'Fresher', 'Junior', 'Top', 'Senior', 'Junior', 'Fresher', 'Senior', 'Top'],
    'zip_code': [90210, 90211, 90210, 90212, 90211, 90210, 90212, 90211, 90210, 90210],
    'feedback_comments': ['Excellent', 'Good', 'OK', 'Poor', 'Great', 'Amazing', 'Fair', 'Solid', 'Perfect', 'Average']
}
df = pd.DataFrame(data)

def detect_column_types_simple(dataframe):
    column_types = {}
    for column in dataframe.columns:
        dtype = dataframe[column].dtype
        unique_values = dataframe[column].nunique()

        if dtype == 'float64' or dtype == 'int64':
            if unique_values < 20:
                column_types[column] = 'Categorical'
            else:
                column_types[column] = 'Numerical'
        elif dtype == 'object':
            if (unique_values / len(dataframe[column])) > 0.8:
                 column_types[column] = 'Text'
            else:
                 column_types[column] = 'Categorical'
    return column_types

def visualize(dataframe):
    column_types = detect_column_types_simple(dataframe)

    for column, col_type in column_types.items():
        print(f"\n> Generating plot for '{column}' (Type: {col_type})")

        if col_type == 'Numerical':
            plt.figure()
            sns.histplot(dataframe[column])
            plt.title(f'Histogram for {column}')
            plt.show()

            plt.figure()
            sns.boxplot(x=dataframe[column])
            plt.title(f'Boxplot for {column}')
            plt.show()

        
        elif col_type == 'Categorical':
            plt.figure(figsize=(8, 5))
            sns.countplot(x=dataframe[column])
            plt.title(f'Count Plot for {column}')
            plt.xticks(rotation=45)
            plt.show()

        
        elif col_type == 'Text':
            
            all_words = dataframe[column].str.cat(sep=' ').lower().split()
            word_counts = pd.Series(all_words).value_counts().head(15)

            plt.figure(figsize=(10, 6))
            sns.barplot(x=word_counts.values, y=word_counts.index)
            plt.title(f'Top 15 Most Frequent Words in {column}')
            plt.xlabel('Frequency (Count)')
            plt.ylabel('Words')
            plt.show()

visualize(df)
