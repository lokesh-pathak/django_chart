from django.core.management.base import BaseCommand
from application.models import SampleData


class Command(BaseCommand):

    def insertData(self):
        with open('adult_data') as file:
            user_data = []
            for line in file:
                data = line.strip().replace('?', '').lower().split(',')
                user_data.append(SampleData(age= data[0].strip(),
                                            workclass= data[1].strip(),
                                            fnlwgt= data[2].strip(),
                                            education= data[3].strip(),
                                            education_num= data[4].strip(),
                                            marital_status= data[5].strip(),
                                            occupation= data[6].strip(),
                                            relationship= data[7].strip(),
                                            race= data[8].strip(),
                                            sex= data[9].strip(),
                                            capital_gain= data[10].strip(),
                                            capital_loss= data[11].strip(),
                                            hours_per_week= data[12].strip(),
                                            native_country= data[13].strip()
                                        ))
        SampleData.objects.bulk_create(user_data)

    def handle(self):
        print ('Please wait Processing the data.....')
        self.insertData()
        print('Data Inserted Successfully.')