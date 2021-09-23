import webbrowser
import argparse

links = [
    "https://my.sbertalents.ru/#/search?keywords=frontend", 
    "https://job.alfabank.ru/vacancies?city=all&specialty=1008&specialty_sub=1114",
    "https://www.tinkoff.ru/career/it/?specialtyUrl=front-end-razrabotka",
    "https://job.ozon.ru/vacancy/?query=frontend",
    "https://career.habr.com/companies/tm",
    "https://boards.greenhouse.io/gitlab",
    "https://careers.kaspersky.ru/vacancy/search/?q=frontend",
    "https://www.jetbrains.com/careers/jobs/",
    "https://job.itmo.ru/ru/catalog?category=3",
    "https://csssr.com/ru-ru/jobs",
    "https://jobs.yoomoney.ru/?tfc_storepartuid[224297426]=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3",
    "https://team.domclick.ru/vacancy",
    "https://okko.tv/careers",
    "https://selectel.ru/careers/all/?code=frontend&area=spb",
    "https://jobs.qiwi.com/vacancies/it",
    "https://us.wildberries.ru/services/jobs",
    "https://jobs.citrix.com/wrike-careers",
    "https://welcome.stepik.org/ru/careers#rec338120670",
    "https://kontur.ru/career/vacancies/city-6240",
    "https://blog.cardsmobile.ru/work#jobs",
    "https://www.epam.com/careers/job-listings?recruitingUrl=%2Fcontent%2Fepam%2Fen%2Fcareers%2Fjob-listings%2Fjob&query=frontend&country=Russia&city=Saint+Petersburg&sort=relevance&department=Software+Engineering%2FTechnology&searchType=placeOfWorkFilter",
    "https://www.softwarecountry.com/company/careers/", 
    "https://dbtc-career.ru/graduateprogramme/",
    "https://city-mobil.ru/career?filter=0",
    "https://career.biocad.ru/vacancies/search?name=frontend&department=103&area=#scrollTo=#vacancies-search-toolbar-section"
    "https://deutschetelekomitsolutions.ru/jobs/?arrFilter_pf%5BVKR_SPEC%5D%5B%5D=43&arrFilter_pf%5BVKR_CITY%5D%5B%5D=1&set_filter=&set_filter=Y",
]

hard_jobs = [
    "https://team.mail.ru/vacancy/?specialty=&town=&tag=&search=frontend",
    "https://vk.com/jobs?category=jobs_cat_frontend",
    "https://boards.greenhouse.io/gitlab",
    "https://spb.hh.ru/employer/2873",
    "https://yandex.ru/jobs/vacancies/?professions=frontend-developer&cities=saint-petersburg",
]


second_links = [
    "https://material-ui.com/ru/company/careers/", # вряд ли возьмут
    "https://oktech.ru/vacancy/?#vacancies", # дублирование вакансий на mail.ru
    "https://www.avito.ru/company/job/departments/1", # москва
    "https://ramblergroup.com/career", # москва
    "https://opencollective.com/hiring", # редко набирают
    "https://tochka.com/hr/", # редко набирают
]

interns = [
]


parser = argparse.ArgumentParser()
parser.add_argument('top', metavar='t')

args = parser.parse_args()

for url in links:
    webbrowser.open(url)

if (args.top):
    for url in hard_jobs:
        webbrowser.open(url)


