# เป็น PROJECT คำนวณราคาค่าอาหารทั้งหมด ที่ลูกค้าสั่ง และ สามารถเพิ่มเมนูอีกได้ครับ
# DC : ม.6 หนุน ธิติสรร กทม. Insprie IT65

print ("สวัสดีลูกค้าทุกท่าน")
krapowcount = 0
kowmankaicount = 0
pepsicount = 0

while True:
    print("ร้านตามสั่งป้าสมพร:")
    print("1. กระเพราหมูสับ = $45")
    print("2. ข้าวมันไก่ = $50")
    print("3. PEPSI = $15")
    print("4. เลือกเมนูสำเร็จ และ คิดเงิน")

    choice = int(input("เลือกเมนูอาหาร : "))

    if choice == 1:
        amount = int(input("ต้องการกระเพราหมูสับ กี่จานดีครับ?: "))
        krapowcount += amount
    elif choice == 2:
        amount = int(input("ข้าวมันไก่ กี่จานดีครับ?: "))
        kowmankaicount += amount
    elif choice == 3:
        amount = int(input("ต้องการ PEPSI กี่ขวดดีครับ?: "))
        pepsicount += amount
    elif choice == 4:
        sub = (krapowcount * 45) + (kowmankaicount * 50) + (pepsicount * 15)
        total = sub
        print('จำนวน กระเพราหมูสับ: {0}'.format(krapowcount))
        print('จำนวน ข้าวมันไก่: {0}'.format(kowmankaicount))
        print('จำนวน PEPSI : {0}'.format(pepsicount))
        print('รวมราคาทั้งหมด: {:0.2f}'.format(total))
        print ("ขอบคุณที่ไว้ใจป้าสมพรมาอุดหนุนใหม่นะครับ")
        break
    elif choice > 4:
        print ("ขออภัยไม่พบเมนูที่ท่านเลือก กรุณาลองใหม่อีกครั้ง") 
        break