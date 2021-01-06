from openpyxl import load_workbook
import random
wb = load_workbook('addressbokk.xlsx')
sheet = wb.active
def EmailAndName():
    number = random.randint(2, 4)
    Email = []
    email = sheet[f'A{number}'].value
    Email.append(email)
    name = sheet[f"B{number}"].value
    Email.append(name)
    return  Email
def RandomImeg():
    image = [
        "https://cerberus-laboratories.com/images/blog/random_numbers.jpg",
        'https://kursphp.com/wp-content/uploads/2020/09/php-random-number-2.jpg',
        'https://magazyngitarzysta.pl/i/images/7/6/4/d2FjPTQ0OXgx_src_141764-dulli.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYiSpFcBpo1Nss-Two9ixSTEfz1iuIoVyhCA&usqp=CAU']
    choiceimge = random.choice(image)
    return choiceimge
