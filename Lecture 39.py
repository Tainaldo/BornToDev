grad = float(input("คะแนนที่ได้ : "))

if grad >= 80 :
    print("เกรด A")
elif grad >= 75 and grad <80 :
    print("เกรด B+")
elif grad >= 70 and grad <75 :
    print("เกรด B")
elif grad >= 65 and grad <70 :
    print("เกรด C+")
elif grad >= 60 and grad <65 :
    print("เกรด C")
elif grad >= 55 and grad <60 :
    print("เกรด D+")
elif grad >= 50 and grad <55 :
    print("เกรด D")
else:
    print("เกรด F")