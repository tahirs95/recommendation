import json
from flask import Flask, jsonify, request

app = Flask(__name__)

a = ["Tshirt", "Sweater", "Jacket", "Shirt"]
b = ["Trousers", "Shorts", "Skirts"]
c = ["Shoes", "Sneakers", "Sandals", "Boots"]


@app.route('/', methods=['POST'])
def hello_world():
    content = request.json
    inputs = content['inputs']
    # with open('abc.json') as json_file:
    #     inputs = json.load(json_file)

    final = []
    upper = []
    middle = []
    lower = []
    color_dict = {}

    for i in inputs:
        if i["category"][0] in a:
            upper.append(i)
        elif i["category"][0] in b:
            middle.append(i)
        elif i["category"][0] in c:
            lower.append(i)

    for u in upper:
        for u_color in u["colors"]:
            color_dict[u_color] = 0

    for color, value in color_dict.items():
        for m in middle:
            for m_color in m['colors']:
                if m_color == color:
                    color_dict[color] +=1
                    final.append(m)
        for l in lower:
            for l_color in l['colors']:
                if l_color == color:
                    color_dict[color] +=1
                    final.append(l)

    recommend_color = max(color_dict, key=color_dict.get)

    recommendations = []
    for f in final:
        for color in f["colors"]:
            if color == recommend_color:
                recommendations.append(f)

    for u in upper:
        for color in u["colors"]:
            if color == recommend_color:
                recommendations.append(u)

    if len(recommendations) >= 3:
        return jsonify(Recommendation=recommendations)
    else:
        return jsonify(Error="No recommendations.")



if __name__ == '__main__':
   app.run()