import webbrowser

links = ["https://my.sbertalents.ru/#/search?keywords=frontend", 
"https://job.alfabank.ru/vacancies?city=all&specialty=1008&specialty_sub=1114",
"https://www.tinkoff.ru/career/it/?specialtyUrl=front-end-razrabotka",
"https://team.mail.ru/vacancy/?specialty=&town=&tag=&search=frontend",
"https://vk.com/jobs?category=jobs_cat_frontend",
"https://job.ozon.ru/vacancy/?query=frontend",
"https://ramblergroup.com/career", # нет фронта лул
"https://www.avito.ru/company/job/departments/1",
"https://career.habr.com/companies/tm",
"https://career.habr.com/companies/2gis/vacancies"
"https://careers.kaspersky.ru/vacancy/search/?q=frontend",
"https://www.jetbrains.com/careers/jobs/",
"https://job.itmo.ru/ru/catalog?category=3"

 ]


second_links = [
    "https://material-ui.com/ru/company/careers/",
    "https://www.softwarecountry.com/company/careers/",
    "https://dbtc-career.ru/summerinternship/",
    "https://oktech.ru/vacancy/?#vacancies"

]

interns = [
]

for url in links:
    webbrowser.open(url)


