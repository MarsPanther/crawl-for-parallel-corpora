import errno
import os
import requests
from bs4 import BeautifulSoup


def generate_language_address():
    language = ['en', 'am', 'om', 'ti']
    publications = ['publications', 'የሕትመት-ውጤቶች', 'wantoota-qophaʼan', 'እዋናዊ']
    book = ['bible', 'መጽሐፍ-ቅዱስ', 'kitaaba-qulqulluu', 'መጽሓፍ-ቅዱስ']
    nwt = ['nwt', 'nwt', 'bi12', 'nwt']
    name = ['books', 'መጻሕፍት', 'kitaabota', 'መጻሕፍቲ']
    i = 0
    sample_url = []
    while i <= 3:
        sample_url1 = "https://www.jw.org" + "/" + language[i] + "/" + publications[i] + "/" + book[i] + "/" + nwt[
            i] + "/" + name[i]
        sample_url.append(sample_url1)
        i += 1
    global_book_list = []
    for sample_url_item in sample_url:
        booklist = requests.get(sample_url_item)
        if booklist.status_code == 200:
            booklists = booklist.content
            soup = BeautifulSoup(booklists, 'html5lib')
            eachbook = soup.findAll("span", {"class": "fullName"})
            books_of_bible = []
            for each in eachbook:
                item = list(each.text.strip('\n'))
                if " " in item:
                    item[item.index(' ')] = '-'
                if " " in item:
                    item[item.index(' ')] = '-'
                s = ''.join(item)
                books_of_bible.append(s)
            global_book_list.append(books_of_bible)
    return global_book_list


def get_single_language_books( language ):
    all_books = generate_language_address()
    arry_to_lang = 0
    if language.lower() == 'English'.lower():
        arry_to_lang = 0
    elif language.lower() == 'Amharic'.lower():
        arry_to_lang = 1
    elif language.lower() == 'Oromifa'.lower():
        arry_to_lang = 2
    elif language.lower() == 'Tigrigna'.lower():
        arry_to_lang = 3
    else:
        arry_to_lang = 0    #set defult crawel to english
    return list(all_books[arry_to_lang])


def get_book_data(lang):
    language = lang
    try:
        os.makedirs(language)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    books = get_single_language_books(language)
    if language.lower() == 'English'.lower():
        arry_to_lang = 0
    elif language.lower() == 'Amharic'.lower():
        arry_to_lang = 1
    elif language.lower() == 'Oromifa'.lower():
        arry_to_lang = 2
    elif language.lower() == 'Tigrigna'.lower():
        arry_to_lang = 3
    else:
        arry_to_lang = 0
    print(books)
    url_languages = ['en', 'am', 'om', 'ti']
    ur_publications = ['publications', 'የሕትመት-ውጤቶች', 'wantoota-qophaʼan', 'እዋናዊ']
    url_books = ['bible', 'መጽሐፍ-ቅዱስ', 'kitaaba-qulqulluu', 'መጽሓፍ-ቅዱስ']
    url_nwt = ['nwt', 'nwt', 'bi12', 'nwt']
    url_holly_names = ['books', 'መጻሕፍት', 'kitaabota', 'መጻሕፍቲ']
    for i in books:
        os.makedirs(language+"/" + i)
        for number in range(1, 151):
            url = "http://www.jw.org" + "/" + url_languages[arry_to_lang] + "/" + ur_publications[arry_to_lang] + "/"\
                  + url_books[arry_to_lang] + "/" + url_nwt[arry_to_lang] + "/" + url_holly_names[arry_to_lang] + "/"\
                  + str(i) + "/" + str(number) + "/"
            print(url)
            crawl = requests.get(url)
            if crawl.status_code == 200:
                soup = BeautifulSoup(crawl.content, 'html5lib')
                for div in soup.find_all("a", {'class': 'footnoteLink'}):
                    div.decompose()
                for div in soup.find_all("a", {'class': 'xrefLink'}):
                    div.decompose()
                for div in soup.find_all("span", {'class': 'parabreak'}):
                    div.decompose()
                lines = soup.findAll("span", {"class": "verse"})
                file_book = open(language + "/" + i + "/" + str(number) + ".txt", "w+")
                for a in lines:
                    text = a.text
                    text = text.replace('\n', ' ')
                    file_book.write(text.strip()+"\n")
            else:
                break
        file_book.close()

if __name__ == '__main__':
    #print(get_book_data('english'))
    #print(get_book_data('amharic'))
    #print(get_book_data('english'))
    #print(get_book_data('tigrigna'))
    print(get_book_data('oromifa'))
