
import os
import sys
import configparser
from tkinter import *
import tkinter.filedialog as filedialog


Table_x = 1
config = configparser.ConfigParser()
config.read('D:\CEAS v1.0\Config.ini')



# создание записи в конфиг файл
def CreateNewConfRecord (Name, Path):
    STRY = str(Table_x)
    config.add_section(STRY)
    config.set(STRY, 'Name', Name)
    config.set(STRY, 'Path', Path)
    config.set(STRY, 'ID', str(Table_x))
    config.write(open('Config.ini', 'w'))

# Функция отвечает за создание кнопки в первом окне
def create_button (Name, path, ID):
    def FPath(event):
        os.startfile(path)
    global Table_x
    Table_x += 1
    button = Button(root, text=Name+' ['+str(ID)+']', width=30, height=1, bg='Yellow', bd=4, font='Times 12', pady='2', padx='10')
    button.bind('<Button 1>', FPath)
    button.grid(row=Table_x, column=0)

# Задание параметров новой кнопки
def CreateNewFile(self):

    root2 = Tk()
    def DoneAndClose(self):
        Name = ObjName.get()
        Path = root2.filename
        create_button(Name, Path, str(Table_x+1))
        CreateNewConfRecord(Name, Path)
        root2.destroy()

    def _ChoiceNewFile (self):
        root2.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))

    root2.title('Создать новый файл')
    root2.geometry('400x130')
    EnterName = Label(root2, text='Введите наименование:', bg='grey', fg='yellow', width=20, height=2)
    ObjName = Entry(root2)
    FilePath = Label(root2, text='Укажите путь файла:', bg='grey', fg='yellow', width=20, height=2)
    FPath = Button(root2, text='Выбрать', bg='grey80', fg='black', width=20, height=1)

    EnterName.grid(row=0, column=0, sticky='w')
    ObjName.grid(row=0, column=1, sticky='w')
    FilePath.grid(row=1, column=0, sticky='w')
    FPath.grid(row=1, column=1, sticky='w')
    FPath.bind('<Button 1>', _ChoiceNewFile)

    DoneButton = Button(root2, text='Готово', bg='grey', fg='yellow', width=20, height=2)
    DoneButton.grid(row=3, column=0)
    DoneButton.bind('<Button 1>', DoneAndClose)

   
    root2.mainloop()

def DeleteFile(self):

    root3 = Tk()

    def DeleteAndClose(self):
        ID = _ObjID.get()
        config.remove_section(ID)
        config.write(open('Config.ini', 'w'))
        root3.destroy()

    root3.title('Удалить файл')
    root3.geometry('400x130')
    _EnterID = Label(root3, text='ID файла:', bg='grey', fg='yellow', width=20, height=2)
    _ObjID = Entry(root3)

    _EnterID.grid(row=0, column=0, sticky='w')
    _ObjID.grid(row=0, column=1, sticky='w')

    DoneButton = Button(root3, text='Удалить', bg='grey', fg='yellow', width=20, height=2)
    DoneButton.grid(row=3, column=0)
    DoneButton.bind('<Button 1>', DeleteAndClose)

    root3.mainloop()




root = Tk()
root.title('CEAS')
root.geometry('1000x400')
root['bg']='light grey'
Non_write_title = Label(root, text='ЮИТС.305646.097 Упаковка', width=30, height=1, bg='lavender', fg='black', font='times 14', bd='3')
Non_write_title.grid(row=0, column=0)

ButToCreateNew = Button(root, text='Создать новый файл', width=30, height=1, bg='Light yellow', fg='black', font='times 14')
ButToCreateNew.grid(row=0, column=2)
ButToCreateNew.bind('<Button 1>', CreateNewFile)

ButToDelete = Button(root, text='Удалить', width=30, height=1, bg='tomato', fg='black', font='times 14')
ButToDelete.grid(row=0, column=3)
ButToDelete.bind('<Button 1>', DeleteFile)


for i in range(1, 40):
    try:
        Name = config.get(str(i), 'Name')
        Path = config.get(str(i), 'Path')
        ID = config.get(str(i), 'ID')
        create_button(Name, Path, ID)


    except:
        configparser.NoSectionError('NO Section')
        continue
print(Table_x)

root.mainloop()



