text="""Mango banana apple. pear Banana, grapes strawberry Apple pear mango banana Kiwi apple mango strawberry"""
d = dict() 
text = text.lower().split(" ")

for word in text:
        word=word.replace(".","").replace(",","")
        if word in d: 
            d[word] = d[word] + 1
        else: 
            d[word] = 1
for key in list(d.keys()):   
    print(key, "(", d[key],")")