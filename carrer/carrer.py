import webbrowser

links = ["https://my.sbertalents.ru/#/search?keywords=frontend", 
"https://job.alfabank.ru/vacancies?city=all&specialty=1008&specialty_sub=1114",
"https://www.tinkoff.ru/career/it/?specialtyUrl=front-end-razrabotka",
"https://team.mail.ru/vacancy/?specialty=&town=&tag=&search=frontend",
"https://vk.com/jobs?category=jobs_cat_frontend",
"https://job.ozon.ru/vacancy/?query=frontend",
"https://career.habr.com/companies/tm",
"https://career.habr.com/companies/2gis/vacancies"
"https://careers.kaspersky.ru/vacancy/search/?q=frontend",
"https://www.jetbrains.com/careers/jobs/",
"https://volgograd.hh.ru/employer/1795976",
"https://csssr.com/ru-ru/jobs",
]


second_links = [
    "https://material-ui.com/ru/company/careers/", # вряд ли возьмут
    "https://www.softwarecountry.com/company/careers/", # редко размещают вакансии для джунов
    "https://dbtc-career.ru/summerinternship/",
    "https://oktech.ru/vacancy/?#vacancies", # дублирование вакансий на mail.ru
    "https://www.avito.ru/company/job/departments/1", # москва
    "https://ramblergroup.com/career", # москва
]

interns = [
]

for url in links:
    webbrowser.open(url)


