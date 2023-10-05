import xml.etree.cElementTree as et

tree = et.parse("sample.xml")

root = tree.getroot()

job_titles = []
company_names = []
categories = []
cities = []

for title in root.iter('job_title'):
    job_titles.append(title.text)

for company in root.iter('company_name'):
    company_names.append(company.text)

for category in root.iter('category'):
    categories.append(category.text)

for city in root .iter('city'):
    cities.append(city.text)

print(job_titles)
print(company_names)
print(categories)
print(cities)