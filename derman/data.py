from sale.models import Factory, Drug
from datetime import datetime



factories = [{
    "title": "Mallinckrodt, Inc."
}, {
    "title": "Nelco Laboratories, Inc."
}, {
    "title": "American Sales Company"
}, {
    "title": "Guangdong Zhanjiang Jimin Pharmaceutical Co. Ltd"
}, {
    "title": "SHIONOGI INC."
}]

drugs = [{
    "title": "Alcohol",
    "factory": "Mallinckrodt, Inc.",
    "price": 45,
    "expirate": "2021-08-16",
    "recipe_needed": False
}, {
    "title": "Lanolin",
    "factory": "Mallinckrodt, Inc.",
    "price": 39,
    "expirate": "2022-01-27",
    "recipe_needed": False
}, {
    "title": "Divalproex Sodium",
    "factory": "Mallinckrodt, Inc.",
    "price": 27,
    "expirate": "2022-06-22",
    "recipe_needed": True
}, {
    "title": "cyclobenzaprine hydrochloride",
    "factory": "SHIONOGI INC.",
    "price": 26,
    "expirate": "2022-08-06",
    "recipe_needed": False
}, {
    "title": "TRICLOSAN",
    "factory": "SHIONOGI INC.",
    "price": 23,
    "expirate": "2022-01-17",
    "recipe_needed": False
}, {
    "title": "Fentanyl Citrate, Bupivacaine HCl",
    "factory": "Guangdong Zhanjiang Jimin Pharmaceutical Co. Ltd",
    "price": 22,
    "expirate": "2022-05-06",
    "recipe_needed": False
}, {
    "title": "Naproxen",
    "factory": "Guangdong Zhanjiang Jimin Pharmaceutical Co. Ltd",
    "price": 9,
    "expirate": "2022-03-08",
    "recipe_needed": True
}, {
    "title": "acetaminophen, dextromethorphan HBr, guaifenesin, phenylephrine HCl",
    "factory": "Guangdong Zhanjiang Jimin Pharmaceutical Co. Ltd",
    "price": 33,
    "expirate": "2021-12-09",
    "recipe_needed": False
}, {
    "title": "tacrolimus",
    "factory": "American Sales Company",
    "price": 9,
    "expirate": "2021-11-20",
    "recipe_needed": False
}, {
    "title": "Magnesium hydroxide",
    "factory": "American Sales Company",
    "price": 35,
    "expirate": "2021-09-10",
    "recipe_needed": True
}, {
    "title": "GLYCERIN",
    "factory": "American Sales Company",
    "price": 47,
    "expirate": "2021-09-10",
    "recipe_needed": False
}, {
    "title": "ALCOHOL",
    "factory": "Nelco Laboratories, Inc.",
    "price": 42,
    "expirate": "2022-08-14",
    "recipe_needed": True
}, {
    "title": "PEG-3350 and electrolytes",
    "factory": "Nelco Laboratories, Inc.",
    "price": 44,
    "expirate": "2021-11-03",
    "recipe_needed": False
}, {
    "title": "Fentanyl Citrate",
    "factory": "Nelco Laboratories, Inc.",
    "price": 16,
    "expirate": "2022-08-24",
    "recipe_needed": True
}, {
    "title": "Terazosin Hydrochloride",
    "factory": "Nelco Laboratories, Inc.",
    "price": 48,
    "expirate": "2022-08-24",
    "recipe_needed": False
}]


def createFactories():
    for f in factories:
        title_data = f.get('title')
        print(title_data)
        f_ins = Factory(title=title_data)
        f_ins.save()


def createDrugs():
    for d in drugs:
        f_ins = Factory.objects.get(title = d['factory'])
        d_ins = Drug.objects.create(
            title = d['title'],
            factory = f_ins,
            price = d['price'],
            expirate = d['expirate'],
            recipe_needed = d['recipe_needed']
        )

if __name__ == '__main__':
    createFactories()


