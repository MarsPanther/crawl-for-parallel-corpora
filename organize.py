import errno
import shutil


ti = ["ማቴዎስ", "ማርቆስ", "ሉቃስ", "ዮሃንስ", "ግብሪ-ሃዋርያት", "ሮሜ", "1-ቈረንቶስ", "2-ቈረንቶስ", "ገላትያ", "ኤፌሶን", "ፊልጲ", "ቈሎሴ",
      "1-ተሰሎንቄ", "2-ተሰሎንቄ", "1-ጢሞቴዎስ", "2-ጢሞቴዎስ", "ቲቶስ", "ፊልሞን", "እብራውያን", "ያእቆብ", "1-ጴጥሮስ", "2-ጴጥሮስ",
      "1-ዮሃንስ", "2-ዮሃንስ", "3-ዮሃንስ", "ይሁዳ", "ራእይ"]
en = ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1-Corinthians", "2-Corinthians", "Galatians",
      "Ephesians", "Philippians", "Colossians", "1-Thessalonians", "2-Thessalonians", "1-Timothy", "2-Timothy",
      "Titus", "Philemon", "Hebrews", "James", "1-Peter", "2-Peter", "1-John", "2-John", "3-John", "Jude", "Revelation"]
am = ["ማቴዎስ", "ማርቆስ", "ሉቃስ", "ዮሐንስ", "የሐዋርያት-ሥራ", "ሮም", "1-ቆሮንቶስ", "2-ቆሮንቶስ", "ገላትያ", "ኤፌሶን", "ፊልጵስዩስ", "ቆላስይስ",
      "1-ተሰሎንቄ", "2-ተሰሎንቄ", "1-ጢሞቴዎስ", "2-ጢሞቴዎስ", "ቲቶ", "ፊልሞና", "ዕብራውያን", "ያዕቆብ", "1-ጴጥሮስ", "2-ጴጥሮስ",
      "1-ዮሐንስ", "2-ዮሐንስ", "3-ዮሐንስ", "ይሁዳ", "ራእይ"]
oromo = ["Maatewos", "Maarqos", "Luqaas", "Yohannis", "Hojii-Ergamootaa", "Roomaa", "1-Qorontos", "2-Qorontos",
         "Galaatiyaa", "Efesoon", "Filiphisiiyus", "Qolosaayis", "1-Tasalonqee", "2-Tasalonqee", "1-Ximotewos",
         "2-Ximotewos", "Tiitoos", "Fiilmoon", "Ibroota", "Yaaqoob", "1-Pheexiros", "2-Pheexiros", "1-Yohaannis",
         "2-Yohaannis", "3-Yohaannis", "Yihudaa", "Mul’ata"]
src = "amharic/ማቴዎስ"
dest = "DataSet2/amharic/ማቴዎስ"


def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)


for items in am:
    copy(src="DataSet1/amharic/"+items, dest="DataSet2/amharic/"+items)


for items in en:
    copy(src="DataSet1/english/"+items, dest="DataSet2/english/"+items)

for items in ti:
    copy(src="DataSet1/tigrigna/"+items, dest="DataSet2/tigrigna/"+items)

