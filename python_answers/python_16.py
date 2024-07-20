text="""Mango banana apple. pear Banana, grapes strawberry Apple pear mango banana Kiwi uwu apple mango strawberry"""
d = dict() 
vowels=['a','e','i','o','u']
text = text.lower()
for word in text:
        word=word.replace(".","").replace(",","").replace(" ","")
        if word in vowels:
            if word in d: 
                d[word] = d[word] + 1
            else: 
                d[word] = 1
for key in list(d.keys()):   
    print(key, "(", d[key],")")