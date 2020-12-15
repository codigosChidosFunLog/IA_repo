import json

Tweets = []
ExclusionTweets = []
Streams = []
Words = {}
JsonProbabilidades = {}

##########################1-Carga el Json con los tweets y las palabras a descartar
with open("tweets.json", "r") as read_file:
    data = json.load(read_file)
    Tweets = data["Tweets"]
    ExclusionTweets = data["Exclusiones"]
    print(Tweets)
    print(ExclusionTweets)

##########################2.-Obtiene los tweets que son Stream
for data in Tweets:
    if data['Stream']:
        Streams.append(data["texto"])

print(Streams)
##########################3.-Filtro para descartar palabras que no son necesarias para la matriz de probabilidades
for data in Streams:
    for word in data.split():
        if word not in ExclusionTweets:
            if word in Words:
                Words[word] += 1
            else:
                Words[word] = 1

print(Words)

##########################4.-Calcula valor de la matriz de probabilidades y crea la estructura Json con esos valores
JsonProbabilidades["Probabilidades"] = []
for data in Words:
    p_word = Words[data]/len(Streams)
    JsonProbabilidades["Probabilidades"].append([data, p_word])

print(JsonProbabilidades)

##########################4.-Guarda la estructura de probabilidades en un archivo llamado data.json
with open("data.json", 'x') as file:
    json.dump(JsonProbabilidades, file)
