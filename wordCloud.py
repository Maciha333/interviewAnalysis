from wordcloud import WordCloud
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

output_dir = "output"

for folderName in os.listdir(output_dir):
    folderPath = os.path.join(output_dir, folderName)
    if os.path.isdir(folderPath):
        issues_file_path = os.path.join(folderPath, "issues.txt")
        if os.path.exists(issues_file_path):
            with open(issues_file_path, "r") as file:
                issues_content = file.read()
                tokens = word_tokenize(issues_content.lower())

                stop_words = set(stopwords.words('english'))
                filtered_tokens = [word for word in tokens if word not in stop_words]

                lemmatizer = WordNetLemmatizer()
                lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

                processed_text = ' '.join(lemmatized_tokens)

                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(processed_text)

                image_path = os.path.join(folderPath, f"wordcloud_{folderName}.png")
                wordcloud.to_file(image_path)
