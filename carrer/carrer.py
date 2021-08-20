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
"https://jobs.yoomoney.ru/?tfc_storepartuid[224297426]=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
"https://opencollective.com/hiring",
"https://team.domclick.ru/vacancy",
"https://okko.tv/careers",
"https://us.wildberries.ru/services/jobs",
"https://jobs.citrix.com/wrike-careers",
"https://welcome.stepik.org/ru/careers#rec338120670",
"https://kontur.ru/career/vacancies/city-6240",
"https://yandex.ru/jobs/vacancies/?professions=frontend-developer&cities=saint-petersburg",
"https://blog.cardsmobile.ru/work#jobs",
"https://career.biocad.ru/vacancies/search?name=frontend&department=103&area=#scrollTo=#vacancies-search-toolbar-section"
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


