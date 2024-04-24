from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import matplotlib.pyplot as plt
import seaborn as sns


output_dir = "output"

all_key_issues = []
for folder_name in os.listdir(output_dir):
    folder_path = os.path.join(output_dir, folder_name)
    if os.path.isdir(folder_path):
        issues_file_path = os.path.join(folder_path, "issues.txt")
        if os.path.exists(issues_file_path):
            with open(issues_file_path, "r") as file:
                key_issues = file.read()
                all_key_issues.append(key_issues)

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(all_key_issues)

cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

print(cosine_similarities)

plt.figure(figsize=(8, 6))
sns.heatmap(cosine_similarities, annot=True, cmap="YlGnBu", xticklabels=["interview 1","interview 2","interview 3","interview 4","interview 5","interview 6","interview 7","interview 8"], yticklabels=["interview 1","interview 2","interview 3","interview 4","interview 5","interview 6","interview 7","interview 8"])
plt.title("Cosine Similarity between issues extracted from interviews")
plt.xlabel("Interviews")
plt.ylabel("Interviews")
plt.xticks(rotation=35, ha="right")
plt.yticks(rotation=35)
plt.tight_layout()
plt.show()
