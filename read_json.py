import os, json
import pandas as pd

def read_json(root, columns=['published', 'title', 'text']):
    articles = pd.DataFrame(columns=columns)

    json_files = (os.path.join(path, file)
                  for path, subdirs, files in os.walk(root)
                  for file in files
                  if file.endswith('.json'))

    for index, file in enumerate(json_files):
        with open(file, encoding='utf-8') as json_data:
            raw_data = json.load(json_data)
            data = {key: raw_data[key] for key in columns}
            df = pd.DataFrame(data, index=[index])
            articles = articles.append(df)

    articles.published = pd.to_datetime(articles.published)
    return articles.sort_values('published').reset_index(drop=True)