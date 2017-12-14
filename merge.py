from glob import glob

en = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1-Samuel', '2-Samuel', '1-Kings', '2-Kings', '1-Chronicles', '2-Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Song-of-Solomon', 'Isaiah', 'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1-Corinthians', '2-Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1-Thessalonians', '2-Thessalonians', '1-Timothy', '2-Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1-Peter', '2-Peter', '1-John', '2-John', '3-John', 'Jude', 'Revelation']
am = ['ዘፍጥረት', 'ዘፀአት', 'ዘሌዋውያን', 'ዘኁልቁ', 'ዘዳግም', 'ኢያሱ', 'መሳፍንት', 'ሩት', '1-ሳሙኤል', '2-ሳሙኤል', '1-ነገሥት', '2-ነገሥት', '1-ዜና-መዋዕል', '2-ዜና-መዋዕል', 'ዕዝራ', 'ነህምያ', 'አስቴር', 'ኢዮብ', 'መዝሙር', 'ምሳሌ', 'መክብብ', 'መኃልየ-መኃልይ', 'ኢሳይያስ', 'ኤርምያስ', 'ሰቆቃወ-ኤርምያስ', 'ሕዝቅኤል', 'ዳንኤል', 'ሆሴዕ', 'ኢዩኤል', 'አሞጽ', 'አብድዩ', 'ዮናስ', 'ሚክያስ', 'ናሆም', 'ዕንባቆም', 'ሶፎንያስ', 'ሐጌ', 'ዘካርያስ', 'ሚልክያስ', 'ማቴዎስ', 'ማርቆስ', 'ሉቃስ', 'ዮሐንስ', 'የሐዋርያት-ሥራ', 'ሮም', '1-ቆሮንቶስ', '2-ቆሮንቶስ', 'ገላትያ', 'ኤፌሶን', 'ፊልጵስዩስ', 'ቆላስይስ', '1-ተሰሎንቄ', '2-ተሰሎንቄ', '1-ጢሞቴዎስ', '2-ጢሞቴዎስ', 'ቲቶ', 'ፊልሞና', 'ዕብራውያን', 'ያዕቆብ', '1-ጴጥሮስ', '2-ጴጥሮስ', '1-ዮሐንስ', '2-ዮሐንስ', '3-ዮሐንስ', 'ይሁዳ', 'ራእይ']
tg = ['ዘፍጥረት', 'ዘጸኣት', 'ዘሌዋውያን', 'ዘሁልቍ', 'ዘዳግም', 'እያሱ', 'መሳፍንቲ', 'ሩት', '1-ሳሙኤል', '2-ሳሙኤል', '1-ነገስት', '2-ነገስት', '1-ዜና-መዋእል', '2-ዜና-መዋእል', 'እዝራ', 'ነህምያ', 'ኣስቴር', 'እዮብ', 'መዝሙር', 'ምሳሌ', 'መክብብ', 'መሃልየ-መሃልይ', 'ኢሳይያስ', 'ኤርምያስ', 'ድጕዓ', 'ህዝቅኤል', 'ዳንኤል', 'ሆሴእ', 'ዮኤል', 'ኣሞጽ', 'ኦብድያ', 'ዮናስ', 'ሚክያስ', 'ናሆም', 'ኣንባቆም', 'ጸፎንያስ', 'ሃጌ', 'ዘካርያስ', 'ሚልክያስ', 'ማቴዎስ', 'ማርቆስ', 'ሉቃስ', 'ዮሃንስ', 'ግብሪ-ሃዋርያት', 'ሮሜ', '1-ቈረንቶስ', '2-ቈረንቶስ', 'ገላትያ', 'ኤፌሶን', 'ፊልጲ', 'ቈሎሴ', '1-ተሰሎንቄ', '2-ተሰሎንቄ', '1-ጢሞቴዎስ', '2-ጢሞቴዎስ', 'ቲቶስ', 'ፊልሞን', 'እብራውያን', 'ያእቆብ', '1-ጴጥሮስ', '2-ጴጥሮስ', '1-ዮሃንስ', '2-ዮሃንስ', '3-ዮሃንስ', 'ይሁዳ', 'ራእይ']

tg2 = ['ማቴዎስ', 'ማርቆስ', 'ሉቃስ', 'ዮሃንስ', 'ግብሪ-ሃዋርያት', 'ሮሜ', '1-ቈረንቶስ', '2-ቈረንቶስ', 'ገላትያ', 'ኤፌሶን', 'ፊልጲ', 'ቈሎሴ', '1-ተሰሎንቄ', '2-ተሰሎንቄ', '1-ጢሞቴዎስ', '2-ጢሞቴዎስ', 'ቲቶስ', 'ፊልሞን', 'እብራውያን', 'ያእቆብ', '1-ጴጥሮስ', '2-ጴጥሮስ', '1-ዮሃንስ', '2-ዮሃንስ', '3-ዮሃንስ', 'ይሁዳ', 'ራእይ']
en2 = ['Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1-Corinthians', '2-Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1-Thessalonians', '2-Thessalonians', '1-Timothy', '2-Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1-Peter', '2-Peter', '1-John', '2-John', '3-John', 'Jude', 'Revelation']
am2 = ['ማቴዎስ', 'ማርቆስ', 'ሉቃስ', 'ዮሐንስ', 'የሐዋርያት-ሥራ', 'ሮም', '1-ቆሮንቶስ', '2-ቆሮንቶስ', 'ገላትያ', 'ኤፌሶን', 'ፊልጵስዩስ', 'ቆላስይስ', '1-ተሰሎንቄ', '2-ተሰሎንቄ', '1-ጢሞቴዎስ', '2-ጢሞቴዎስ', 'ቲቶ', 'ፊልሞና', 'ዕብራውያን', 'ያዕቆብ', '1-ጴጥሮስ', '2-ጴጥሮስ', '1-ዮሐንስ', '2-ዮሐንስ', '3-ዮሐንስ', 'ይሁዳ', 'ራእይ']
oromifa2 = ['Maatewos', 'Maarqos', 'Luqaas', 'Yohannis', 'Hojii-Ergamootaa', 'Roomaa', '1-Qorontos', '2-Qorontos',
            'Galaatiyaa', 'Efesoon', 'Filiphisiiyus', 'Qolosaayis', '1-Tasalonqee', '2-Tasaloniiqee', '1-Ximotewos', '2-Ximotewos', 'Tiitoos', 'Fiilmoon', 'Ibroota', 'Yaaqoob', '1-Pheexiros', '2-Phexros', '1-Yohaannis', '2-Yohannis', '3-Yohannis', 'Yihudaa', 'Mul’ata']

read_files_am_1 = []
for i in am:
    read_files_am_1.append((glob("DataSet1/amharic/" + i + "/*.txt")))

read_files_en_1 = []
for j in en:
    read_files_en_1.append((glob("DataSet1/english/" + j + "/*.txt")))

read_files_tg_1 = []
for k in tg:
    read_files_tg_1.append((glob("DataSet1/tigrigna/" + k + "/*.txt")))

read_files_am_2 = []
for i in am2:
    read_files_am_2.append((glob("DataSet2/amharic/" + i + "/*.txt")))

read_files_tg_2 = []
for i in tg2:
    read_files_tg_2.append((glob("DataSet2/tigrigna/" + i + "/*.txt")))

read_files_en_2 = []
for i in en2:
    read_files_en_2.append((glob("DataSet2/english/" + i + "/*.txt")))

read_files_or_2 = []
for i in oromifa2:
    read_files_or_2.append((glob("DataSet2/oromifa/" + i + "/*.txt")))

with open("DataSet3/old_amharic.txt", "wb") as outfile:
    for am in read_files_am_1:
        for z in am:
            with open(z, "rb") as infile:
                outfile.write(infile.read())


with open("DataSet3/old_english.txt", "wb") as outfile:
    for en in read_files_en_1:
        for y in en:
            with open(y, "rb") as infile:
                outfile.write(infile.read())

with open("DataSet3/old_tigrigna.txt", "wb") as outfile:
    for tg in read_files_tg_1:
        for x in tg:
            with open(x, "rb") as infile:
                outfile.write(infile.read())


with open("DataSet3/new_amharic.txt", "wb") as outfile:
    for am2 in read_files_am_2:
        for m in am2:
            with open(m, "rb") as infile:
                outfile.write(infile.read())

with open("DataSet3/new_tigrigna.txt", "wb") as outfile:
    for tg2 in read_files_tg_2:
        for n in tg2:
            with open(n, "rb") as infile:
                outfile.write(infile.read())

with open("DataSet3/new_english.txt", "wb") as outfile:
    for en2 in read_files_en_2:
        for l in en2:
            with open(l, "rb") as infile:
                outfile.write(infile.read())

with open("DataSet3/new_oromifa.txt", "wb") as outfile:
    for or2 in read_files_or_2:
        for o in or2:
            with open(o, "rb") as infile:
                outfile.write(infile.read())

