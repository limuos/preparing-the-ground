import json

un_tagged = open("un_tagged.txt", "w", encoding="utf-8")
li_tagged = open("li_tagged.txt", "w", encoding="utf-8")
sentiment = open("sentiment.txt", "w", encoding="utf-8")

neu = open("neutral_tagged.txt", "w", encoding="utf-8")
pos = open("positive_tagged.txt", "w", encoding="utf-8")
neg = open("negative_tagged.txt", "w", encoding="utf-8")

with open("SAIL_BN-EN_train_codemixed.json") as data_file:
    data = json.load(data_file)

for index in range(2500):
    un_tagged.write(data["data"][index]["text"] + "\n")
    li_tagged.write(data["data"][index]["lang_tagged_text"] + "\n")
    sentiment.write(str(data["data"][index]["sentiment"]) + "\n")

for index in range(2500):
    polarity = str(data["data"][index]["sentiment"])
    if polarity == "0":
        neu.write(data["data"][index]["lang_tagged_text"] + "\n")
    if polarity == "1":
        pos.write(data["data"][index]["lang_tagged_text"] + "\n")
    if polarity == "-1":
        neg.write(data["data"][index]["lang_tagged_text"] + "\n")

un_tagged.close()
li_tagged.close()
sentiment.close()

neu.close()
pos.close()
neg.close()
