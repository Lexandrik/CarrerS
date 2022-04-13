import pandas as pd
import requests
import openpyxl
######check
# делаем запрос на API careerspace
response = requests.get('https://careerspace.app/api/v1/jobs/filter/?sortBy=new-desc&remote=false&take=50000')
# преобразуем ответ в JSON формат для обработки
data = response.json()
# заносим JSON в DataFrame
df_jobs = pd.DataFrame(data['jobs'])
# преобразуем столбец job_locations
df_jobs['good_job_locations'] = df_jobs['job_locations'].apply(lambda x: x[0]['job_location_name'] if len(x)!=0 else 'no_location')
df_jobs['company_name'] = df_jobs['company'].apply(lambda x: x['company_name'])
# указываем столбцы для вывода в итоговый DataFrame df_jobs1
df_jobs1 = df_jobs[['job_name',
                    'job_salary_from',
                    'job_salary_to',
                    'job_salary_currency',
                    'company_name',
                    'good_job_locations'
                   ]]
# запись в .xlsx полученного df_jobs1
#df_jobs1.to_excel('df_jobs1.xlsx', index = False)