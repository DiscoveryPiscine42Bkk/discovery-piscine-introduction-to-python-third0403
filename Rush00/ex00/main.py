import os, time

Tasks = []
timer = 1


def selectMain():

  select = '''
===== Smart Farm Task Organizer =====
1. เพิ่มงานในฟาร์ม
2. แสดงรายการงานทั้งหมด
3. ลบงาน
4  สรุปจํานวนงานในแต่ละประเภท
5  ออกจากโปรแกรม
'''
  print(select)


def addTask():

  task = input("ป้อนชื่องาน: ")
  date = input("ป้อนวันที่ (dd/mm/yyyy): ")
  types = input("ประเภทงาน (พืชผัก/ปศุสัตว์/อื่นๆ): ")

  Tasks.append({"task": task, "date": date, "types": types})

  print("เพิ่มงานสำเร็จ")
  refresh()

#-----------> แก้ไขเรียบร้อยแล้วค่ะ
def showTask():

  while True:
    if len(Tasks) > 0:
      print("รายการงานทั้งหมด")
      for i in range(len(Tasks)):
        jsonData = Tasks[i]
        print(
            f"{i+1}. {jsonData['date']} - {jsonData['task']} ({jsonData['types']})"
        )

    else:
      print("⚠ ยังไม่มีงานในรายการ")
      refresh()

    print("\nกด Enter เพื่อกลับสู่เมนูหลัก")
    x = input(">>")
    if x == "":
      refresh()


def deleteTask():
  showTask()
  index = int(input("ลําดับของงานที่ต้องการลบ: "))
  if index <= len(Tasks):
    removed = Tasks.pop(index - 1)
    print(f"ลบงาน : {removed['task']} แล้ว")
    refresh()

  else:
    print("⚠ ยังไม่มีงานในรายการ")
    refresh()


def sumTask():
  if len(Tasks) > 0:
    types = {}
    print("📊 สรุปจํานวนงานในแต่ละประเภท :")
    for i in range(len(Tasks)):
      jsonData = Tasks[i]
      if jsonData["types"] in types:
        types[jsonData["types"]] += 1
      else:
        types[jsonData["types"]] = 1

    for key, value in types.items():
      print(f"- {key} : {value} งาน")

  else:
    print("⚠ ยังไม่มีงานในรายการ")
    refresh()


def mainsys():
  selectMain()
  x = input("เลือกเมนู (1-5): ")

  if x == "1":
    addTask()
  elif x == "2":
    showTask()

  elif x == "3":
    deleteTask()
  elif x == "4":
    sumTask()

  elif x == "5":
    print("🤝 ขอบคุณที่ใช้โปรแกรม Smart Farm")
    exit()


def refresh():
  time.sleep(timer)
  os.system("clear")

  mainsys()


mainsys()
