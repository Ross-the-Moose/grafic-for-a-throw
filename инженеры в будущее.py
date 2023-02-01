from math import *
from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox as mb

g = 9.8066

iz_vibory = True
iz_viboryvn = True

vo_dano = False
vk_dano = False
ho_dano = False
H_dano = False
T_dano = False
tmh_dano = False
L_dano = False
alfa_dano = False

x1 = 50
x2 = 50
t = 0
y2 = 50


def is_digit(st):
    num = "1234567890.,"
    if st.count(".") + st.count(",") != 0 and st.count(".") + st.count(",") != 1:
        # print("-" + str(i) + "-")
        return False
    for i in st:
        if i not in num:
            # print(i)
            return False
    return True


def vibory():
    root = Tk()
    root.geometry('300x520')

    text = Label(text="Выберите тип броска: \n только один!", font=("Verdana", 17))
    text.place(x=0, y=0)

    def d_ugol_ho():
        if iz_vibory:
            root.destroy()

        rootangle_ho = Tk()
        rootangle_ho.title("Под углом к горизонту(с ho)")
        rootangle_ho.geometry('900x650')
        title = Label(
            text="Выберите известные величины:(все величины - числа не меньше нуля)\n "
                 "- начальная скорость[м/с],    - угол между направлением Vo и горизонтом[рад],\n    - начальная "
                 "высота[м],    - максимальная высота подъема[м],   - дальность полета[м],\n                          "
                 "             - общее время полета[с]",
            font=("Verdana", 14))

        title.place(x=0, y=0)
        vot = Label(text="Vo", font=("Verdana", 13, BOLD))
        vot.place(x=15, y=25)
        alfat = Label(text="α", font=("Verdana", 13, BOLD))
        alfat.place(x=325, y=25)
        tt = Label(text="T", font=("Verdana", 13, BOLD))
        tt.place(x=440, y=71)
        lt = Label(text="L", font=("Verdana", 13, BOLD))
        lt.place(x=650, y=48)
        Ht = Label(text="ho", font=("Verdana", 13, BOLD))
        Ht.place(x=0, y=48)
        hot = Label(text="H", font=("Verdana", 13, BOLD))
        hot.place(x=266, y=48)

        instruck1 = Label(text="1.Введите в соответствующих полях ЧИСЛОВЫЕ\nзначения ТРЁХ величин, "
                               "по которым будет построен\nваш график.", font=("Verdana", 14), justify=LEFT)

        instruck2 = Label(text="2.Нажмите на кнопки, соответствующие введенным\n"
                               "величинам в любом порядке", font=("Verdana", 14), justify=LEFT)

        instruck3 = Label(text="3.Нажмите кнопку 'Рассчитай'", font=("Verdana", 14), justify=LEFT)

        instruck1.place(x=350, y=200)
        instruck2.place(x=350, y=300)
        instruck3.place(x=350, y=400)

        warning = Label(text="Невозможная комбинация: H и T", font=("Verdana", 15))
        warning['fg'] = '#ff4d00'
        warning.place(x=20, y=80)

        def truvo():
            global vo_dano
            vo_dano = True
            # print(voe.get())

        def trualfa():
            global alfa_dano
            alfa_dano = True
            # print(alfae.get())

        def trut():
            global T_dano
            T_dano = True
            # print(Te.get())

        def trul():
            global L_dano
            L_dano = True
            # print(Le.get())

        def truh():
            global H_dano
            H_dano = True
            # print(He.get())

        def truho():
            global ho_dano
            ho_dano = True
            # print(hoe.get())

        def nazad():
            rootangle_ho.destroy()
            vibory()

        back = Button(text="BACK", font=("Verdana", 15))
        back.config(command=nazad)
        back.place(x=750, y=95)

        how_to_back = Label(text="Для возвращения на главный экран нажмите кнопку 'BACK' ^", font=("verdana", 12))
        how_to_back.place(x=350, y=150)
        palka = Label(text="|\n|", font=("VERDANA", 12))
        palka.place(x=864, y=114)
        strelka = Label(text="<—", font=("verdana", 12))
        strelka.place(x=830, y=105)

        voe = Entry(width=15)
        voe.place(x=200, y=158)
        alfae = Entry(width=15)
        alfae.place(x=200, y=208)
        He = Entry(width=15)
        He.place(x=200, y=258)
        hoe = Entry(width=15)
        hoe.place(x=200, y=308)
        Le = Entry(width=15)
        Le.place(x=200, y=358)
        Te = Entry(width=15)
        Te.place(x=200, y=408)

        vob = Button(rootangle_ho, text="Vo =", font=("Verdana", 13))
        alfab = Button(rootangle_ho, text="α =", font=("Verdana", 13))
        tb = Button(rootangle_ho, text="T =", font=("Verdana", 13))
        Lb = Button(rootangle_ho, text="L =", font=("Verdana", 13))
        Hb = Button(rootangle_ho, text="H =", font=("Verdana", 13))
        hob = Button(rootangle_ho, text="ho =", font=("Verdana", 13))

        vob.place(x=100, y=150, width=80)
        vob.config(command=truvo)
        #
        alfab.place(x=100, y=200, width=80)
        alfab.config(command=trualfa)
        #
        Hb.place(x=100, y=250, width=80)
        Hb.config(command=truh)
        #
        hob.place(x=100, y=300, width=80)
        hob.config(command=truho)
        #
        Lb.place(x=100, y=350, width=80)
        Lb.config(command=trul)
        #
        tb.place(x=100, y=400, width=80)
        tb.config(command=trut)

        def teory():
            print(
                "Координата y по оси OY шарика изменяется по закону y(t) = ho + Vo * t - g*t²/2\n координата x по оси OX шарика изменяется по закону x(t) = Vo * cos")

        teory = Button(rootangle_ho, text="Теория", font=("Verdana", 15))
        teory.config(command=print_teory)

        def draw(vo, H, alfa, T, L, ho, tmh, vk):
            global x1
            x1 = 50
            global x2
            x2 = 50
            c = Canvas(rootangle_ho, bg='white', width=900, height=650)
            c.pack()
            c.create_line(0, 600, 800, 600, width=2, arrow=LAST)
            c.create_line(50, 650, 50, 0, width=2, arrow=LAST)
            if L > H:
                if L > 600:
                    g_x = 600
                    g_y = 600 - H * g_x / L
                    yho = 600 - ho * g_x / L
                else:
                    yho = 600 - ho
                    g_x = L
                    g_y = 600 - H
            else:
                if H > 590:
                    g_y = 10
                    g_x = L * 590 / H
                    yho = 600 - ho * 590 / H
                else:
                    g_x = L
                    yho = 600 - ho
                    g_y = 600 - H
            c.create_text(35, 10, text="y, м", font=("Verdana", 10))
            c.create_text(800, 590, text="x, м", font=("Verdana", 10))
            c.create_line(45, yho, 55, yho, width=2)
            c.create_text(70, yho, text="ho", font=("Verdana", 10))
            c.create_text(30, g_y, text="H", font=("Verdana", 10))
            c.create_text(45, 614, text="0")
            c.create_line(45, g_y, 55, g_y, width=2)
            c.create_line(g_x, 605, g_x, 595, width=2)
            c.create_text(g_x, 605, text="L", font=("Verdana", 10))
            root_text = Tk()
            root_text.geometry('750x250')
            root_text.title("Данные")
            txt = "Начальная скорость Vo = " + str(round(vo, 2)) + "м/с\nКонечая скорость Vк" + str(vk) + \
                  "м/с\nУгол между направлением Vo и горизонтом α =" + str(alfa) + "рад\nНачальная высота ho = 0 м" + \
                  "\nМаксимальная высота подъема H = " + str(H) + "м\nДальность полета L = " + str(L) + \
                  "м\nОбщее время полета T = " + str(T) + "с\nВремя подъема на максимальную высоту tmaxh = " \
                  + str(tmh) + "с"
            dannye = Label(root_text, text=txt, font=("Verdana", 15), justify=LEFT)
            dannye.place(x=0, y=0)

            def delete_d():
                global iz_vibory
                iz_vibory = False
                rootangle_ho.destroy()
                root_text.destroy()
                d_ugol_ho()

            delete_b = Button(c, text="Спасибо! Назад!", font=("Verdana", 20))
            delete_b.config(command=delete_d)
            delete_b.place(x=600, y=100)
            c.create_line(45, g_y, 55, g_y, width=2)
            c.create_line(g_x + 50, 605, g_x + 50, 595, width=2)
            voo = (g * g_x / sin(2 * alfa)) ** 0.5

            def func():
                global x1, x2
                x1 = x2
                x2 += g_x / 2000
                y1 = yho + tan(alfa) * (x1 - 50) - g * (x1 - 50) ** 2 / (2 * voo ** 2 * cos(alfa) ** 2)
                y2 = yho + tan(alfa) * (x2 - 50) - g * (x2 - 50) ** 2 / (2 * voo ** 2 * cos(alfa) ** 2)
                c.create_line(x1, 600 - y1, x2, 600 - y2, width=3, fill="#007d34")
                if y2 > 0:
                    rootangle_ho.after(1, func)
                    # print(y1, y2)
                else:
                    pass

            func()

            mb.showerror("Предупреждение!",
                         "Если вы не видите график, то:\n1. Его построение занимает некоторое время\n2. "
                         "График маленький из-за выбранных величин\n(это можно понять из расположения"
                         " рисок на оси)\n\nдля продолжения нажмите ок/закройте это окно")

        # def d_error(war):
        # global canv
        # canv = Canvas(rootangle_ho, bg='white', width=900, height=650)
        # canv.pack()
        # canv.create_line(0, 600, 800, 600, width=1, arrow=LAST)
        # canv.create_line(50, 650, 50, 0, width=1, arrow=LAST)
        # txt = "Мне кажется, что вы ошиблись при вводе значений " + str(war) + "\nПерепроверьте их, пожалуйста!"
        # canv.create_text(450, 300, text=txt, font=("Verdana", 15))

        #  def delete_d():
        #      global iz_vibory
        #      iz_vibory = False
        #      global canv
        #      сanv.destroy()
        #      d_ugol_ho()

        #  delete_b = Button(canv, text="Спасибо! Назад!", font=("Verdana", 20))
        #  delete_b.config(command=delete_d)
        #  delete_b.place(x=600, y=100)

        def GO():
            global vo_dano
            global H_dano
            global alfa_dano
            global T_dano
            global L_dano
            global ho_dano
            if vo_dano and alfa_dano and ho_dano and is_digit(voe.get()) and is_digit(alfae.get()) and is_digit(
                    hoe.get()):
                vo = round(float(voe.get()), 2)  # 1
                alfa = round(float(alfae.get()), 2)
                ho = round(float(hoe.get()), 2)
                H = round(ho + vo ** 2 * sin(alfa) ** 2 / 2 / g, 2)
                tmh = round(vo * sin(alfa) / g, 2)
                T = round(tmh + (2 * H / g) ** 0.5, 2)
                L = round(vo * cos(alfa) * T, 2)
                vk = round((2 * g * H + vo * cos(alfa)) ** 0.5, 2)
                draw(vo, H, alfa, T, L, ho, tmh, vk)
            elif vo_dano and alfa_dano and H_dano and is_digit(voe.get()) and is_digit(alfae.get()) and is_digit(
                    He.get()):
                vo = round(float(voe.get()), 2)  # 2
                alfa = round(float(alfae.get()), 2)
                H = round(float(He.get()), 2)
                ho = round(H - vo ** 2 * sin(alfa) ** 2 / 2 / g, 2)
                tmh = round(vo * sin(alfa) / g, 2)
                T = round(tmh + (2 * H / g) ** 0.5, 2)
                L = round(vo * cos(alfa) * T, 2)
                vk = round((2 * g * H + vo * cos(alfa)) ** 0.5, 2)
                draw(vo, H, alfa, T, L, ho, tmh, vk)
            elif vo_dano and alfa_dano and T_dano and is_digit(voe.get()) and is_digit(alfae.get()) and is_digit(
                    Te.get()):
                vo = round(float(voe.get()), 2)  # 3
                alfa = round(float(alfae.get()), 2)
                T = round(float(Te.get()), 2)
                H = round((g * T ** 2 + vo ** 2 * sin(alfa) ** 2 - 2 * T * vo * sin(alfa)) / 2, 2)
                ho = round(H - vo ** 2 * sin(alfa) ** 2 / 2 / g, 2)
                tmh = round(vo * sin(alfa) / g, 2)
                L = round(vo * cos(alfa) * T, 2)
                vk = round((2 * g * H + vo * cos(alfa)) ** 0.5, 2)
                draw(vo, H, alfa, T, L, ho, tmh, vk)
            elif vo_dano and alfa_dano and L_dano and is_digit(voe.get()) and is_digit(alfae.get()) and is_digit(
                    Le.get()):
                vo = round(float(voe.get()), 2)  # 4(5)
                alfa = round(float(alfae.get()), 2)
                L = round(float(Le.get()), 2)
                T = round(L / (vo * cos(alfa)), 2)
                H = round((g * T ** 2 + vo ** 2 * sin(alfa) ** 2 - 2 * T * vo * sin(alfa)) / 2, 2)
                ho = round(H - vo ** 2 * sin(alfa) ** 2 / 2 / g, 2)
                tmh = round(vo * sin(alfa) / g, 2)
                vk = round((2 * g * H + vo * cos(alfa)) ** 0.5, 2)
                draw(vo, H, alfa, T, L, ho, tmh, vk)
            elif vo_dano and ho_dano and H_dano and is_digit(voe.get()) and is_digit(hoe.get()) and is_digit(
                    He.get()):
                ho = round(float(hoe.get()), 2)  # 5(6)
                vo = round(float(voe.get()), 2)
                H = round(float(He.get()), 2)
                alfa = round(asin((2 * g * (H - ho)) ** 0.5 / vo), 2)
                tmh = round(vo * sin(alfa) / g, 2)
                vk = round((2 * g * H) ** 0.5, 2)
                T = round(tmh + (2 * g * H) ** 0.5 / g, 2)
                L = round(vo * cos(alfa) * T, 2)
                draw(vo, H, alfa, T, L, ho, tmh, vk)
            else:
                mb.showerror("Ошибка в вводе величин!",
                             "Неверные входные данные!\nПерепроверьте ввод и/или перечитайте инструкцию!\n А ЕЩЕ ПЕРЕЧИТАЙТЕ ИНСТРУКЦИЮ. ВОЗМОЖНО ЭТО ВАМ ПОМОЖЕТ")
                # print(is_digit(alfae.get()))
            vo_dano = False
            alfa_dano = False
            H_dano = False
            T_dano = False
            L_dano = False

        go = Button(rootangle_ho, text="Рассчитай!", font=("Verdana", 15))
        go.place(x=100, y=510)
        go.config(command=GO)

    def d_ugol():
        if iz_vibory:
            root.destroy()

        rootangle = Tk()
        rootangle.title("Под углом к горизонту(с земли)")
        rootangle.geometry('900x650')
        title = Label(
            text="Выберите известные величины:(все величины - числа не меньше нуля)\n"
                 "- начальная скорость[м/с],    - угол между направлением Vo и горизонтом[рад],\n   - максимальная "
                 "высота подъема[м],   - дальность полета[м],   - общее время полета[с]",
            font=("Verdana", 14))

        title.place(x=0, y=0)
        vot = Label(text="Vo", font=("Verdana", 13, BOLD))
        vot.place(x=8, y=25)
        alfat = Label(text="α", font=("Verdana", 13, BOLD))
        alfat.place(x=318, y=25)
        tt = Label(text="T", font=("Verdana", 13, BOLD))
        tt.place(x=630, y=48)
        lt = Label(text="L", font=("Verdana", 13, BOLD))
        lt.place(x=383, y=48)
        Ht = Label(text="H", font=("Verdana", 13, BOLD))
        Ht.place(x=0, y=48)

        instruck1 = Label(text="1.Введите в соответствующих полях ЧИСЛОВЫЕ\nзначения ДВУХ величин, "
                               "по которым будет построен\nваш график.", font=("Verdana", 14), justify=LEFT)

        instruck2 = Label(text="2.Нажмите на кнопки, соответствующие введенным\n"
                               "величинам в любом порядке", font=("Verdana", 14), justify=LEFT)

        instruck3 = Label(text="3.Нажмите кнопку 'Рассчитай'", font=("Verdana", 14), justify=LEFT)

        instruck1.place(x=350, y=200)
        instruck2.place(x=350, y=300)
        instruck3.place(x=350, y=400)

        warning = Label(text="Невозможная комбинация: H и T", font=("Verdana", 15))
        warning['fg'] = '#ff4d00'
        warning.place(x=20, y=80)

        def truvo():
            global vo_dano
            vo_dano = True

        def trualfa():
            global alfa_dano
            alfa_dano = True

        def trut():
            global T_dano
            T_dano = True

        def trul():
            global L_dano
            L_dano = True

        def truh():
            global H_dano
            H_dano = True

        def nazad():
            rootangle.destroy()
            vibory()

        back = Button(text="BACK", font=("Verdana", 15))
        back.config(command=nazad)
        back.place(x=750, y=95)

        how_to_back = Label(text="Для возвращения на главный экран нажмите кнопку 'BACK' ^", font=("verdana", 12))
        how_to_back.place(x=350, y=150)
        palka = Label(text="|\n|", font=("VERDANA", 12))
        palka.place(x=864, y=114)
        strelka = Label(text="<—", font=("verdana", 12))
        strelka.place(x=830, y=105)

        voe = Entry(width=15)
        voe.place(x=200, y=158)
        Te = Entry(width=15)
        Te.place(x=200, y=218)
        alfae = Entry(width=15)
        alfae.place(x=200, y=278)
        Le = Entry(width=15)
        Le.place(x=200, y=338)
        He = Entry(width=15)
        He.place(x=200, y=398)

        vob = Button(rootangle, text="Vo =", font=("Verdana", 13))
        alfab = Button(rootangle, text="α =", font=("Verdana", 13))
        tb = Button(rootangle, text="T =", font=("Verdana", 13))
        Lb = Button(rootangle, text="L =", font=("Verdana", 13))
        Hb = Button(rootangle, text="H =", font=("Verdana", 13))

        vob.place(x=100, y=150, width=80)
        vob.config(command=truvo)
        #
        alfab.place(x=100, y=270, width=80)
        alfab.config(command=trualfa)
        #
        Lb.place(x=100, y=330, width=80)
        Lb.config(command=trul)
        #
        tb.place(x=100, y=210, width=80)
        tb.config(command=trut)
        #
        Hb.place(x=100, y=390, width=80)
        Hb.config(command=truh)

        def draw(vo, H, alfa, T, L):
            global x1
            x1 = 50
            global x2
            x2 = 50
            c = Canvas(rootangle, bg='white', width=1000, height=900)
            c.pack()
            c.create_line(0, 600, 800, 600, width=2, arrow=LAST)
            c.create_line(50, 650, 50, 0, width=2, arrow=LAST)
            if L > H:
                if L > 600:
                    g_x = 600
                    g_y = 600 - H * g_x / L
                else:
                    g_x = L
                    g_y = 600 - H
            else:
                if H > 590:
                    g_y = 10
                    g_x = L * 590 / H
                else:
                    g_x = L
                    g_y = 600 - H

            c.create_text(35, 10, text="y, м", font=("Verdana", 10))
            c.create_text(800, 590, text="x, м", font=("Verdana", 10))
            c.create_line(45, g_y, 55, g_y, width=2)
            c.create_text(70, g_y, text="ho", font=("Verdana", 10))
            c.create_text(30, g_y, text="H", font=("Verdana", 10))
            c.create_text(45, 614, text="0")
            c.create_line(45, g_y, 55, g_y, width=2)
            c.create_line(g_x, 605, g_x, 595, width=2)
            c.create_text(g_x, 605, text="L", font=("Verdana", 10))
            root_text = Tk()
            root_text.geometry('750x250')
            root_text.title("Данные")
            txt = "Начальная скорость Vo = " + str(round(vo, 2)) + "м/с\nКонечая скорость Vк = Vo = " + str(vo) + \
                  "м/с\nУгол между направлением Vo и горизонтом α =" + str(alfa) + "рад\nНачальная высота ho = 0 м" + \
                  "\nМаксимальная высота подъема = " + str(H) + "м\nДальность полета L = " + str(L) + \
                  "м\nОбщее время полета T = " + str(T) + "с\nВремя подъема на максимальную высоту tmaxh = T/2 = " \
                  + str(T / 2) + "с "
            dannye = Label(root_text, text=txt, font=("Verdana", 15), justify=LEFT)
            dannye.place(x=0, y=0)

            def delete_d():
                global iz_vibory
                iz_vibory = False
                rootangle.destroy()
                root_text.destroy()
                d_ugol()

            delete_b = Button(c, text="Спасибо! Назад!", font=("Verdana", 20))
            delete_b.config(command=delete_d)
            delete_b.place(x=600, y=100)
            c.create_line(45, g_y, 55, g_y, width=2)
            c.create_line(g_x + 50, 605, g_x + 50, 595, width=2)
            voo = (g * g_x / sin(2 * alfa)) ** 0.5

            def func():
                global x1, x2
                x1 = x2
                x2 += g_x / 5000
                y1 = tan(alfa) * (x1 - 50) - g * (x1 - 50) ** 2 / (2 * voo ** 2 * cos(alfa) ** 2)
                y2 = tan(alfa) * (x2 - 50) - g * (x2 - 50) ** 2 / (2 * voo ** 2 * cos(alfa) ** 2)
                c.create_line(x1, 600 - y1, x2, 600 - y2, width=3, fill="#007d34")
                if y2 > 0:
                    rootangle.after(1, func)
                    # print(y1, y2)
                else:
                    pass

            func()
            mb.showerror("Предупреждение!",
                         "Если вы не видите график, то:\n1. Его построение занимает некоторое время\n2. "
                         "График маленький из-за выбранных величин\n(это можно понять из расположения"
                         " рисок на оси)\n\nдля продолжения нажмите ок/закройте это окно")

        def d_error(war):
            c = Canvas(rootangle, bg='white', width=900, height=650)
            c.pack()
            c.create_line(0, 600, 800, 600, width=1, arrow=LAST)
            c.create_line(50, 650, 50, 0, width=1, arrow=LAST)
            txt = "Мне кажется, что вы ошиблись при вводе значений " + str(war) + "\nПерепроверьте их, пожалуйста!"
            c.create_text(450, 300, text=txt, font=("Verdana", 15))

            def delete_d():
                global iz_vibory
                iz_vibory = False
                rootangle.destroy()
                root_text.destroy()
                d_ugol()

            delete_b = Button(c, text="Спасибо! Назад!", font=("Verdana", 20))
            delete_b.config(command=delete_d)
            delete_b.place(x=600, y=100)

        def GO():
            global vo_dano
            global H_dano
            global alfa_dano
            global T_dano
            global L_dano
            if vo_dano and alfa_dano and is_digit(voe.get()) and is_digit(alfae.get()):
                vo = round(float(voe.get()), 2)  # 1
                alfa = round(float(alfae.get()), 2)
                t = round(2 * vo * sin(alfa) / g, 2)
                L = round(vo * cos(alfa) * t, 2)
                H = round(vo ** 2 * sin(alfa) ** 2 / 2 / g, 2)
                draw(vo, H, alfa, t, L)
            elif vo_dano and L_dano and is_digit(voe.get()) and is_digit(Le.get()):
                vo = round(float(voe.get()), 2)
                L = round(float(Le.get()), 2)
                alfa = round(asin(g * L / vo / vo) / 2, 2)
                h = round(vo ** 2 * sin(alfa) ** 2 / 2 / g, 2)
                T = round(vo * sin(alfa) * 2 / g, 2)
                draw(vo, h, alfa, T, L)  # 2
            elif vo_dano and H_dano and is_digit(voe.get()) and is_digit(He.get()):
                vo = round(float(voe.get()), 2)
                H = round(float(He.get()), 2)
                alfa = round(asin((2 * g * H / vo / vo) ** 0.5), 2)
                T = round(2 * vo * sin(alfa) / g, 2)
                L = round(vo * cos(alfa) * T, 2)
                draw(vo, H, alfa, T, L)
            elif vo_dano and T_dano and is_digit(voe.get()) and is_digit(Te.get()):
                vo = round(float(voe.get()), 2)
                t = round(float(Te.get()), 2)
                alfa = round(asin(g * t / 2 / vo), 2)
                h = round(vo ** 2 * sin(alfa) ** 2 / 2 / g, 2)
                L = round(vo * cos(alfa) * t, 2)
                draw(vo, h, alfa, t, L)  # 4
            elif alfa_dano and L_dano and is_digit(alfae.get()) and is_digit(Le.get()):
                L = round(float(Le.get()), 2)
                a = round(float(alfae.get()), 2)
                vo = round((g * L / sin(2 * a)) ** 0.5, 2)
                t = round(L / vo / cos(a), 2)
                H = round(vo ** 2 * sin(a) ** 2 / 2 / g, 2)
                draw(vo, H, a, t, L)  # 5
            elif L_dano and T_dano and is_digit(Le.get()) and is_digit(Te.get()):
                L = round(float(Le.get()), 2)
                t = round(float(Te.get()), 2)
                a = round(atan(g * t * t / 2 / L), 2)
                vo = round(L / cos(a) / t, 2)
                h = round(vo ** 2 * sin(a) ** 2 / 2 / g, 2)
                draw(vo, h, a, t, L)  # 6
            elif alfa_dano and T_dano and is_digit(alfae.get()) and is_digit(Te.get()):  # 7
                T = round(float(Te.get()), 2)
                alfa = round(float(alfae.get()), 2)
                L = round(g * T ** 2 / 2 * cos(alfa) / sin(alfa), 2)
                vo = round(L / cos(alfa) / T, 2)
                H = round(vo ** 2 * sin(alfa) ** 2 / 2 / g, 2)
                draw(vo, H, alfa, T, L)
            elif alfa_dano and H_dano and is_digit(alfae.get()) and is_digit(He.get()):
                alfa = round(float(alfae.get()), 2)
                H = round(float(He.get()), 2)
                vo = round((2 * g * H) ** 0.5 / sin(alfa), 2)
                T = round(2 * vo * sin(alfa) / g, 2)
                L = round(vo * cos(alfa) * T, 2)
                draw(vo, H, alfa, T, L)  # 8
            elif H_dano and L_dano and is_digit(He.get()) and is_digit(Le.get()):
                H = round(float(He.get()), 2)
                L = round(float(Le.get()), 2)
                alfa = round(atan(4 * H / L), 2)
                vo = round((L * g / sin(2 * alfa)) ** 0.5, 2)
                T = round(2 * vo * sin(alfa) / g, 2)
                draw(vo, H, alfa, T, L)  # 9
            else:
                mb.showerror("Ошибка в вводе величин!",
                             "Неверные входные данные!\nПерепроверьте ввод и/или перечитайте инструкцию!\n А ЕЩЕ ПЕРЕЧИТАЙТЕ ИНСТРУКЦИЮ. ВОЗМОЖНО ЭТО ВАМ ПОМОЖЕТ")
            vo_dano = False
            alfa_dano = False
            H_dano = False
            T_dano = False
            L_dano = False

        go = Button(rootangle, text="Рассчитай!", font=("Verdana", 15))
        go.place(x=100, y=510)
        go.config(command=GO)

    def d_horizon():
        if iz_vibory:
            root.destroy()

        roothor = Tk()
        roothor.title("Горизонтальный бросок")
        roothor.geometry('900x650')
        title = Label(
            text="Выберите известные величины:(все величины - числа не меньше нуля)\n"
                 " - начальная скорость[м/с],      - конечная скорость[м/с],\n    - начальная высота[м],   "
                 "- время полета[с],   - дальность полета[м]",
            font=("Verdana", 14))

        title.place(x=90, y=0)
        vot = Label(text="Vo", font=("Verdana", 13, BOLD))
        vot.place(x=133, y=25)
        vkt = Label(text="Vк", font=("Verdana", 13, BOLD))
        vkt.place(x=445, y=25)
        ht = Label(text="h", font=("Verdana", 13, BOLD))
        ht.place(x=100, y=48)
        tt = Label(text="T", font=("Verdana", 13, BOLD))
        tt.place(x=357, y=48)
        lt = Label(text="L", font=("Verdana", 13, BOLD))
        lt.place(x=563, y=48)

        instruck1 = Label(text="1.Введите в соответствующих полях ЧИСЛОВЫЕ\nзначения ДВУХ величин, "
                               "по которым будет построен\nваш график.", font=("Verdana", 14), justify=LEFT)

        instruck2 = Label(text="2.Нажмите на кнопки, соответствующие введенным\n"
                               "величинам в любом порядке", font=("Verdana", 14), justify=LEFT)

        instruck3 = Label(text="3.Нажмите кнопку 'Рассчитай'", font=("Verdana", 14), justify=LEFT)

        instruck1.place(x=350, y=200)
        instruck2.place(x=350, y=300)
        instruck3.place(x=350, y=400)

        warning = Label(text="Невозможная комбинация: h и T", font=("Verdana", 15))
        warning['fg'] = '#ff4d00'
        warning.place(x=20, y=80)

        def truvo():
            global vo_dano
            vo_dano = True

        def truvk():
            global vk_dano
            vk_dano = True

        def truh():
            global ho_dano
            ho_dano = True

        def trut():
            global T_dano
            T_dano = True

        def trul():
            global L_dano
            L_dano = True

        def nazad():
            roothor.destroy()
            vibory()

        back = Button(text="BACK", font=("Verdana", 15))
        back.config(command=nazad)
        back.place(x=750, y=95)

        how_to_back = Label(text="Для возвращения на главный экран нажмите кнопку 'BACK' ^", font=("verdana", 12))
        how_to_back.place(x=350, y=150)
        palka = Label(text="|\n|", font=("VERDANA", 12))
        palka.place(x=864, y=114)
        strelka = Label(text="<—", font=("verdana", 12))
        strelka.place(x=830, y=105)

        voe = Entry(width=15)
        voe.place(x=200, y=158)
        vke = Entry(width=15)
        vke.place(x=200, y=218)
        hoe = Entry(width=15)
        hoe.place(x=200, y=278)
        Le = Entry(width=15)
        Le.place(x=200, y=338)
        Te = Entry(width=15)
        Te.place(x=200, y=398)

        vob = Button(roothor, text="Vo =", font=("Verdana", 13))
        vkb = Button(roothor, text="Vк =", font=("Verdana", 13))
        hob = Button(roothor, text="h =", font=("Verdana", 13))
        tb = Button(roothor, text="T =", font=("Verdana", 13))
        Lb = Button(roothor, text="L =", font=("Verdana", 13))

        vob.place(x=100, y=150, width=80)
        vob.config(command=truvo)
        #
        vkb.place(x=100, y=210, width=80)
        vkb.config(command=truvk)
        #
        hob.place(x=100, y=270, width=80)
        hob.config(command=truh)
        #
        Lb.place(x=100, y=330, width=80)
        Lb.config(command=trul)
        #
        tb.place(x=100, y=390, width=80)
        tb.config(command=trut)

        def draw(vo, vk, h, T, L):
            global x1
            x1 = 50
            global x2
            x2 = 50
            c = Canvas(roothor, bg='white', width=900, height=650)
            c.pack()
            c.create_line(0, 600, 800, 600, width=2, arrow=LAST)
            c.create_line(50, 650, 50, 0, width=2, arrow=LAST)

            if L > h:
                if L > 600:
                    g_x = 600
                    g_y = 600 - h * g_x / L
                else:
                    g_x = L
                    g_y = 600 - h
            else:
                if h > 590:
                    g_y = 10
                    g_x = L * 590 / h
                else:
                    g_x = L
                    g_y = 600 - h

            root_text = Tk()
            root_text.geometry('700x150')
            root_text.title("Данные")
            txt = "Начальная скорость Vo = " + str(round(vo, 2)) + "м/с\nКонечая скорость Vк = " + str(
                vk) + "м/с\nНачальная высота ho = " + str(h) + "м\nДальность полета L = " + str(
                L) + "м\nОбщее время полета T = " + str(T) + "с"
            dannye = Label(root_text, text=txt, font=("Verdana", 15), justify=LEFT)
            dannye.place(x=0, y=0)

            def delete_d():
                global iz_vibory
                iz_vibory = False
                roothor.destroy()
                root_text.destroy()
                d_horizon()

            delete_b = Button(c, text="Спасибо! Назад!", font=("Verdana", 20))
            delete_b.config(command=delete_d)
            delete_b.place(x=600, y=100)
            c.create_line(45, g_y, 55, g_y, width=2)
            c.create_line(g_x + 50, 605, g_x + 50, 595, width=2)

            def func():
                global x1, x2
                vo1 = g_x / (2 * (600 - g_y) / g) ** 0.5
                x1 = x2
                x2 += g_x / 3000
                y1 = 600 - ((600 - g_y) - (g * (x1 - 50) ** 2) / (2 * vo1 ** 2))
                y2 = 600 - ((600 - g_y) - (g * (x2 - 50) ** 2) / (2 * vo1 ** 2))
                c.create_line(x1, y1, x2, y2, width=3, fill="#007d34")
                if y2 < 600:
                    roothor.after(1, func)
                else:
                    pass

            func()
            mb.showerror("Предупреждение!",
                         "Если вы не видите график, то:\n1. Его построение занимает некоторое время\n2. "
                         "График маленький из-за выбранных величин\n(это можно понять из расположения"
                         " рисок на оси)\n\nдля продолжения нажмите ок/закройте это окно")

        def d_error(war):
            c = Canvas(roothor, bg='white', width=900, height=650)
            c.pack()
            c.create_line(0, 600, 800, 600, width=1, arrow=LAST)
            c.create_line(50, 650, 50, 0, width=1, arrow=LAST)
            txt = "Мне кажется, что вы ошиблись при вводе значений " + str(war) + "\nПерепроверьте их, пожалуйста!"
            c.create_text(450, 300, text=txt, font=("Verdana", 15))

            def delete_d():
                global iz_vibory
                iz_vibory = False
                roothor.destroy()
                d_vniz()

            delete_b = Button(c, text="Спасибо! Назад!", font=("Verdana", 20))
            delete_b.config(command=delete_d)
            delete_b.place(x=600, y=100)

        def GO():
            global vo_dano
            global vk_dano
            global ho_dano
            global T_dano
            global L_dano
            if vo_dano and ho_dano and is_digit(voe.get()) and is_digit(hoe.get()):
                vo = round(float(voe.get()), 2)  # 1
                h = round(float(hoe.get()), 2)
                t = round((2 * h / g) ** 0.5, 2)
                L = round(vo * t, 2)
                vk = round((vo ** 2 + (g * t) ** 2) ** 0.5, 2)
                draw(vo, vk, h, t, L)
            elif vo_dano and L_dano and is_digit(voe.get()) and is_digit(Le.get()):
                vo = round(float(voe.get()), 2)
                L = round(float(Le.get()), 2)
                t = round(L / vo, 2)
                h = round(g * t * t / 2, 2)
                vk = round((vo ** 2 + (g * t) ** 2) ** 0.5, 2)
                draw(vo, vk, h, t, L)  # 2
            elif vo_dano and vk_dano and is_digit(voe.get()) and is_digit(vke.get()):
                vo = round(float(voe.get()), 2)
                vk = round(float(vke.get()), 2)
                if (vk ** 2 - vo ** 2) / g ** 2 >= 0:
                    t = round(((vk ** 2 - vo ** 2) / g ** 2) ** 0.5, 2)
                    L = round(vo * t, 2)
                    h = round(g * t ** 2 / 2, 2)
                    draw(vo, vk, h, t, L)  # 3
                else:
                    d_error("Vo и Vк")
            elif vo_dano and T_dano and is_digit(voe.get()) and is_digit(Te.get()):
                vo = round(float(voe.get()), 2)
                t = round(float(Te.get()), 2)
                L = round(vo * t, 2)
                h = round(g * t ** 2 / 2, 2)
                vk = round((vo ** 2 + (g * t) ** 2) ** 0.5, 2)
                draw(vo, vk, h, t, L)  # 4
            elif ho_dano and L_dano and is_digit(hoe.get()) and is_digit(Le.get()):
                L = round(float(Le.get()), 2)
                h = round(float(hoe.get()), 2)
                t = round((2 * h / g) ** 0.5, 2)
                vo = round(L / t, 2)
                vk = round((vo ** 2 + (g * t) ** 2) ** 0.5, 2)
                draw(vo, vk, h, t, L)  # 5
            elif L_dano and T_dano and is_digit(Le.get()) and is_digit(Te.get()):
                l = round(float(Le.get()), 2)
                t = round(float(Te.get()), 2)
                vo = round(l / t, 2)
                h = round(g * t ** 2 / 2, 2)
                vk = round((vo ** 2 + (g * t) ** 2) ** 0.5, 2)
                draw(vo, vk, h, t, l)  # 6
            elif ho_dano and vk_dano and is_digit(hoe.get()) and is_digit(vke.get()):  # 7
                vk = round(float(vke.get()), 2)
                h = round(float(hoe.get()), 2)
                t = round((2 * h / g) ** 0.5, 2)
                if vk ** 2 - (g * t) ** 2 >= 0:
                    vo = round((vk ** 2 - (g * t) ** 2) ** 0.5, 2)
                    L = round(vo * t, 2)
                    draw(vo, vk, h, t, L)
                else:
                    d_error("h и Vк")
            elif T_dano and vk_dano and is_digit(Te.get()) and is_digit(vke.get()):
                t = round(float(Te.get()), 2)
                vk = round(float(vke.get()), 2)
                h = round(g * t ** 2 / 2, 2)
                if vk ** 2 - (g * t) ** 2:
                    vo = round((vk ** 2 - (g * t) ** 2) ** 0.5, 2)
                    L = round(vo * t, 2)
                    h = round(g * t ** 2 / 2, 2)
                    draw(vo, vk, h, t, L)  # 8
                else:
                    d_error("T и Vк")
            elif vk_dano and L_dano and is_digit(vke.get()) and is_digit(Le.get()):
                vk = round(float(vke.get()), 2)
                L = round(float(Le.get()), 2)
                if vk ** 4 - 4 * g ** 2 * L ** 2 >= 0:
                    t = round(((vk ** 2 + (vk ** 4 - 4 * g ** 2 * L ** 2) ** 0.5) / 2 * g ** 2) ** 0.5, 2)
                    vo = round(L / t, 2)
                    h = round(g * t ** 2 / 2, 2)
                    draw(vo, vk, h, t, L)  # 9
                else:
                    d_error("Vк и L")
            else:
                # print(vo_dano, ho_dano, is_digit(voe.get()), is_digit(alfae.get()))
                mb.showerror("Ошибка в вводе величин!",
                             "Неверные входные данные!\nПерепроверьте ввод и/или перечитайте инструкцию!\n А ЕЩЕ "
                             "ПЕРЕЧИТАЙТЕ ИНСТРУКЦИЮ. ВОЗМОЖНО ЭТО ВАМ ПОМОЖЕТ")
            vo_dano = False
            vk_dano = False
            ho_dano = False
            T_dano = False
            L_dano = False

        go = Button(roothor, text="Рассчитай!", font=("Verdana", 15))
        go.place(x=100, y=510)
        go.config(command=GO)

    # вертикально вниз
    def d_vniz():
        if iz_vibory:
            root.destroy()

        rootvn = Tk()
        rootvn.title("Бросок вертикально вниз")
        rootvn.geometry('900x650')
        title = Label(
            text="Выберите известные величины:(все величины - числа не меньше нуля)\n"
                 " - начальная скорость[м/с],      - конечная скорость[м/с],\n    - начальная высота[м],   "
                 "- время полета[с]",
            font=("Verdana", 14))

        title.place(x=90, y=0)
        vot = Label(text="Vo", font=("Verdana", 13, BOLD))
        vot.place(x=133, y=25)
        vkt = Label(text="Vк", font=("Verdana", 13, BOLD))
        vkt.place(x=445, y=25)
        hot = Label(text="ho", font=("Verdana", 13, BOLD))
        hot.place(x=216, y=48)
        tt = Label(text="T", font=("Verdana", 13, BOLD))
        tt.place(x=483, y=48)

        instruck1 = Label(text="1.Введите в соответствующих полях ЧИСЛОВЫЕ\nзначения ДВУХ величин, "
                               "по которым будет построен\nваш график.", font=("Verdana", 14), justify=LEFT)

        instruck2 = Label(text="2.Нажмите на кнопки, соответствующие введенным\n"
                               "величинам в любом порядке", font=("Verdana", 14), justify=LEFT)

        instruck3 = Label(text="3.Нажмите кнопку 'Рассчитай'", font=("Verdana", 14), justify=LEFT)

        instruck1.place(x=350, y=200)
        instruck2.place(x=350, y=300)
        instruck3.place(x=350, y=400)

        warning = Label(text="Невозможная комбинация: Vк и T", font=("Verdana", 15))
        warning['fg'] = '#ff4d00'
        warning.place(x=50, y=80)

        def nazad():
            rootvn.destroy()
            vibory()

        back = Button(text="BACK", font=("Verdana", 15))
        back.config(command=nazad)
        back.place(x=750, y=95)

        how_to_back = Label(text="Для возвращения на главный экран нажмите кнопку 'BACK' ^", font=("verdana", 12))
        how_to_back.place(x=350, y=150)
        palka = Label(text="|\n|", font=("VERDANA", 12))
        palka.place(x=864, y=114)
        strelka = Label(text="<—", font=("verdana", 12))
        strelka.place(x=830, y=105)

        def truvo():
            global vo_dano
            vo_dano = True

        def truvk():
            global vk_dano
            vk_dano = True

        def truho():
            global ho_dano
            ho_dano = True

        def trut():
            global T_dano
            T_dano = True

        voe = Entry(width=15)
        voe.place(x=200, y=158)
        vke = Entry(width=15)
        vke.place(x=200, y=238)
        hoe = Entry(width=15)
        hoe.place(x=200, y=318)
        Te = Entry(width=15)
        Te.place(x=200, y=398)

        vob = Button(rootvn, text="Vo =", font=("Verdana", 13))
        vkb = Button(rootvn, text="Vк =", font=("Verdana", 13))
        hob = Button(rootvn, text="ho =", font=("Verdana", 13))
        tb = Button(rootvn, text="T =", font=("Verdana", 13))

        vob.place(x=100, y=150, width=80)
        vob.config(command=truvo)
        #
        vkb.place(x=100, y=230, width=80)
        vkb.config(command=truvk)
        #
        hob.place(x=100, y=310, width=80)
        hob.config(command=truho)
        #
        tb.place(x=100, y=390, width=80)
        tb.config(command=trut)

        def draw(vo, ho, vk, T):
            c = Canvas(rootvn, bg='white', width=900, height=650)
            c.pack()
            c.create_line(0, 600, 800, 600, width=1, arrow=LAST)
            c.create_line(50, 650, 50, 0, width=1, arrow=LAST)
            if ho > 600:
                yho = 50
            else:
                yho = 600 - ho

            c.create_text(32, 10, text="y, м", font=("Verdana", 10))
            c.create_text(800, 590, text="x, м", font=("Verdana", 10))
            c.create_line(45, yho, 55, yho, width=2)
            c.create_text(70, yho, text="ho", font=("Verdana", 10))
            c.create_text(45, 614, text="0")

            txt = "Начальная скорость Vo = " + str(round(vo, 2)) + "м/с\nКонечая скорость Vк = " + str(
                vk) + "м/с\nНачальная высота ho = " + str(ho) + "м\nОбщее время полета T = " + str(T) + "с"
            c.create_text(450, 300, text=txt, font=("Verdana", 15))

            def delete_d():
                global iz_vibory
                iz_vibory = False
                rootvn.destroy()
                d_vniz()

            delete_b = Button(c, text="Спасибо! Назад!", font=("Verdana", 20))
            delete_b.config(command=delete_d)
            delete_b.place(x=600, y=100)

            global y2, t
            y2 = yho
            t = 0
            voo = vo * yho / ho

            def func():
                global t, y2
                t += T / 1000
                y1 = y2
                y2 = yho + voo * t + g * t ** 2 / 2
                if y2 < 600:
                    c.create_line(50, y1, 50, y2, width=3, fill="#007d34")
                    rootvn.after(1, func)
                else:
                    c.create_line(50, y2, 50, 600, width=3, fill="#007d34")
                    pass
                # print(y1, y2, yho)

            if T == 0:
                c.create_line(50, yho, 50, 600, width=3, fill="#007d34")
            else:
                func()
            mb.showerror("Предупреждение!",
                         "Если вы не видите график, то:\n1. Его построение занимает некоторое время\n2. "
                         "График маленький из-за выбранных величин\n(это можно понять из расположения"
                         " рисок на оси)\n\nдля продолжения нажмите ок/закройте это окно")

        def d_error(war):
            c = Canvas(rootvn, bg='white', width=900, height=650)
            c.pack()
            c.create_line(0, 600, 800, 600, width=1, arrow=LAST)
            c.create_line(50, 650, 50, 0, width=1, arrow=LAST)
            txt = "Мне кажется, что вы ошиблись при вводе значений " + str(war) + "\nПерепроверьте их, пожалуйста!"
            c.create_text(450, 300, text=txt, font=("Verdana", 15))

        def vnvoho():
            vo = round(float(voe.get()), 2)
            ho = round(float(hoe.get()), 2)
            vk = round((2 * g * ho + vo ** 2) ** 0.5, 2)
            T = round((vk - vo) / g, 2)
            draw(vo, ho, vk, T)

        def vnhoT():
            T = round(float(Te.get()), 2)
            ho = round(float(hoe.get()), 2)
            vo = round((2 * ho - g * T * T) / (2 * T), 2)
            vk = round(vo + g * T, 2)
            if vo >= 0:
                draw(vo, ho, vk, T)
            else:
                d_error("ho и T")

        def vnvovk():
            vo = round(float(voe.get()), 2)
            vk = round(float(vke.get()), 2)
            ho = round((vk ** 2 - vo ** 2) / 2 / g, 2)
            T = round((vk - vo) / g, 2)
            if ho >= 0 and T >= 0:
                draw(vo, ho, vk, T)
            else:
                d_error("Vo и Vк")

        def vnvot():
            vo = round(float(voe.get()), 2)
            T = round(float(Te.get()), 2)
            vk = round(vo + g * T, 2)
            ho = round((vk ** 2 - vo ** 2) / 2 / g, 2)

            if ho >= 0 and T >= 0:
                draw(vo, ho, vk, T)
            else:
                d_error("Vo и T")

        def vnvkho():
            ho = round(float(hoe.get()), 2)
            vk = round(float(vke.get()), 2)
            vo2 = round((vk ** 2 - 2 * g * ho), 2)
            if vo2 >= 0:
                vo = round(vo2 ** 0.5, 2)
                T = round((vk - vo) / g, 2)
                draw(vo, ho, vk, T)
            else:
                d_error("Vк и ho")

        def GO():
            global vo_dano
            global vk_dano
            global ho_dano
            global T_dano
            if vo_dano and ho_dano and is_digit(voe.get()) and is_digit(hoe.get()):
                vnvoho()  # 1
            elif ho_dano and T_dano and is_digit(hoe.get()) and is_digit(Te.get()):
                vnhoT()  # 2
            elif vo_dano and vk_dano and is_digit(voe.get()) and is_digit(vke.get()):
                vnvovk()  # 3
            elif ho_dano and vk_dano and is_digit(hoe.get()) and is_digit(vke.get()):
                vnvkho()  # 4
            elif vo_dano and T_dano and is_digit(voe.get()) and is_digit(Te.get()):
                vnvot()  # 5
            else:
                mb.showerror("Ошибка в вводе величин!",
                             "Неверные входные данные!\nПерепроверьте ввод и/или перечитайте инструкцию!\n А ЕЩЕ "
                             "ПЕРЕЧИТАЙТЕ ИНСТРУКЦИЮ. ВОЗМОЖНО ЭТО ВАМ ПОМОЖЕТ")

            vo_dano = False
            vk_dano = False
            ho_dano = False
            T_dano = False

        go = Button(rootvn, text="Рассчитай!", font=("Verdana", 15))
        go.place(x=100, y=510)
        go.config(command=GO)

    # вертикально вверх
    def d_vverh():
        if iz_vibory:
            root.destroy()
        rootvv = Tk()
        rootvv.title("Бросок вертикально вверх")
        rootvv.geometry('900x650')
        title = Label(
            text="Выберите известные величины:(все величины - числа не меньше нуля)\n"
                 "  - начальная скорость[м/с],     - конечная скорость[м/с],     - начальная высота[м],\n"
                 "   - максимальная высота подъема[м],   - время полета[с],          - время подъема на H[с]",
            font=("Verdana", 14))

        def saving():
            f = open('last_actions.txt', 'a')
            f.write('\n')
            f.write("Vo = " + str(vo) + "м/с\nVк = " + str(vk) + "м/с\nho = " + str(ho) + "м\nH = " + str(
                H) + "м\n T = " + str(T) + "c\n tmh = " + str(tmh) + "c")

        if_file = Button(rootvv, text="из файла!", font=("Verdana", 15))
        if_file.place(x=650, y=500)
        if_file.config(command=saving)

        vot = Label(text="Vo", font=("Verdana", 13, BOLD))
        vot.place(x=5, y=25)
        vkt = Label(text="Vк", font=("Verdana", 13, BOLD))
        vkt.place(x=315, y=25)
        hot = Label(text="ho", font=("Verdana", 13, BOLD))
        hot.place(x=610, y=25)
        ht = Label(text="H", font=("Verdana", 13, BOLD))
        ht.place(x=1, y=49)
        tt = Label(text="T", font=("Verdana", 13, BOLD))
        tt.place(x=380, y=49)
        tmht = Label(text="tmaxh", font=("Verdana", 13, BOLD))
        tmht.place(x=585, y=49)
        title.place(x=0, y=0)
        #
        # вводы для кнопок
        #
        voe = Entry(width=15)
        voe.place(x=200, y=158)
        vke = Entry(width=15)
        vke.place(x=200, y=208)
        hoe = Entry(width=15)
        hoe.place(x=200, y=278)
        He = Entry(width=15)
        He.place(x=200, y=328)
        Te = Entry(width=15)
        Te.place(x=200, y=398)
        tmhe = Entry(width=15)
        tmhe.place(x=200, y=448)
        # предупреждение об ошибке
        warning = Label(text="Невозможные комбинации: Vo и tmaxh, Vк и H, ho и T", font=("Verdana", 15))
        warning['fg'] = '#ff4d00'
        warning.place(x=20, y=80)

        # ф-и для изменения используемых переменных
        def truvo():
            global vo_dano
            vo_dano = True

        def truvk():
            global vk_dano
            vk_dano = True

        def truho():
            global ho_dano
            ho_dano = True

        def truh():
            global H_dano
            H_dano = True

        def trut():
            global T_dano
            T_dano = True

        def trutmh():
            global tmh_dano
            tmh_dano = True

        # кнопки для ввода величин

        vob = Button(rootvv, text="Vo =", font=("Verdana", 13))
        vkb = Button(rootvv, text="Vк =", font=("Verdana", 13))
        hob = Button(rootvv, text="ho =", font=("Verdana", 13))
        hb = Button(rootvv, text="H =", font=("Verdana", 13))
        tb = Button(rootvv, text="T =", font=("Verdana", 13))
        tmhb = Button(rootvv, text="tmaxh =", font=("Verdana", 13))

        instruck1 = Label(text="1.Введите в соответствующих полях ЧИСЛОВЫЕ\nзначения ДВУХ величин, "
                               "по которым будет построен\nваш график.", font=("Verdana", 14), justify=LEFT)

        instruck2 = Label(text="2.Нажмите на кнопки, соответствующие введенным\n"
                               "величинам в любом порядке", font=("Verdana", 14), justify=LEFT)

        instruck3 = Label(text="3.Нажмите кнопку 'Рассчитай'", font=("Verdana", 14), justify=LEFT)

        # razmernost = Label(text = "Скорость вводите в метрах в секунду (м/с)\nвысоту в метрах (м)\nвремя в секундах (с)", font = ("Verdana", 14), justify = "right")
        # razmernost.place(x = 350, y = 200)

        instruck1.place(x=350, y=200)
        instruck2.place(x=350, y=300)
        instruck3.place(x=350, y=400)

        def nazad():
            rootvv.destroy()
            vibory()

        back = Button(text="BACK", font=("Verdana", 15))
        back.config(command=nazad)
        back.place(x=750, y=95)
        #
        vob.place(x=100, y=150, width=80)
        vob.config(command=truvo)
        #
        vkb.place(x=100, y=200, width=80)
        vkb.config(command=truvk)
        #
        hob.place(x=100, y=270, width=80)
        hob.config(command=truho)
        #
        hb.place(x=100, y=320, width=80)
        hb.config(command=truh)
        #
        tb.place(x=100, y=390, width=80)
        tb.config(command=trut)
        #
        tmhb.place(x=100, y=440, width=80)
        tmhb.config(command=trutmh)

        #
        # функции рисования графиков и рассчета результатов
        #
        def draw(vo, ho, vk, T, H, tmh):
            c = Canvas(rootvv, bg='white', width=900, height=650)
            c.pack()
            c.create_line(0, 600, 800, 600, width=1, arrow=LAST)
            c.create_line(50, 650, 50, 0, width=1, arrow=LAST)
            if H > 580:
                yH = 20
                yho = 600 - 580 / H * ho
            else:
                yH = 600 - H
                yho = 600 - ho

            c.create_text(35, 10, text="y, м", font=("Verdana", 10))
            c.create_text(800, 590, text="x, м", font=("Verdana", 10))
            c.create_line(45, yho, 55, yho, width=2)
            c.create_text(70, yho, text="ho", font=("Verdana", 10))
            c.create_text(30, yH, text="H", font=("Verdana", 10))
            c.create_text(45, 614, text="0")
            c.create_line(45, yH, 55, yH, width=2)

            txt = "Начальная скорость Vo = " + str(round(vo, 2)) + "м/с\nКонечная скорость Vк = " + str(
                vk) + "м/с\nНачальная высота ho = " + str(ho) + "м\nМаксимальная высота H = " + str(
                H) + "м\nОбщее время полета T = " + str(T) + "с\nВремя подъема до максимальной высоты tmaxh = " + str(
                tmh) + "с"

            def delete_d():
                global iz_vibory
                iz_vibory = False
                rootvv.destroy()
                d_vverh()

            delete_b = Button(c, text="Спасибо! Назад!", font=("Verdana", 20))
            delete_b.config(command=delete_d)
            delete_b.place(x=600, y=100)

            def saving():
                f = open('last_actions.txt', 'a')
                f.write('\n')
                f.write("Vo = " + str(vo) + "м/с\nVк = " + str(vk) + "м/с\nho = " + str(ho) + "м\nH = " + str(
                    H) + "м\n T = " + str(T) + "c\n tmh = " + str(tmh) + "c")

            if_file = Button(rootvv, text="из файла!", font=("Verdana", 15))
            if_file.place(x=650, y=500)
            if_file.config(command=saving)

            global y2, t
            y2 = yH
            t = 0
            global k
            k = (600 - yH) / H

            def funcvverh():
                global t, y2, k
                if t < vo / g:
                    color = "#0bda51"
                else:
                    color = "#007d34"

                y1 = ho + vo * t - g * t ** 2 / 2
                t += T / 3000
                y2 = ho + vo * t - g * t ** 2 / 2
                t -= T / 3000
                if t < T:
                    t += T / 3000
                    c.create_line(50, 600 - k * y1, 50, 600 - k * y2, width=3, fill=color)
                    rootvv.after(1, funcvverh)
                else:
                    pass

            if T == 0:
                c.create_line(50, yho, 50, 600, width=3, fill=color)
            else:
                funcvverh()
            c.create_text(450, 270, text=txt, font=("Verdana", 15))
            mb.showerror("Предупреждение!",
                         "Если вы не видите график,10 то:\n1. Его построение занимает некоторое время\n2. "
                         "График маленький из-за выбранных величин\n(это можно понять из расположения"
                         " рисок на оси)\n\nдля продолжения нажмите ок/закройте это окно")

        def d_error(war):
            c = Canvas(rootvv, bg='white', width=900, height=650)
            c.pack()
            c.create_line(0, 600, 800, 600, width=1, arrow=LAST)
            c.create_line(50, 650, 50, 0, width=1, arrow=LAST)
            txt = "Мне кажется, что вы ошиблись при вводе значений " + str(war) + "\nПерепроверьте их, пожалуйста!"
            c.create_text(450, 300, text=txt, font=("Verdana", 15))

            def delete_d():
                global iz_vibory
                iz_vibory = False
                rootvv.destroy()
                d_vverh()

            delete_b = Button(c, text="Спасибо! Назад!", font=("Verdana", 20))
            delete_b.config(command=delete_d)
            delete_b.place(x=600, y=100)

        def vvvoho():
            vo = round(float(voe.get()), 2)
            ho = round(float(hoe.get()), 2)
            H = ho + vo ** 2 / (2 * g)
            H = round(H, 2)
            vk = round((2 * g * H) ** 0.5, 2)
            tmh = round(vo / g, 2)
            T = round(tmh + vk / g, 2)

            draw(vo, ho, vk, T, H, tmh)

        def vvvoh():
            vo = round(float(voe.get()), 2)
            H = round(float(He.get()), 2)
            ho = round(H - vo ** 2 / (2 * g), 2)
            vk = round((2 * g * H) ** 0.5, 2)
            tmh = round(vo / g, 2)
            T = round(tmh + vk / g, 2)
            if tmh > 0 and ho > 0 and H > 0 and T > 0 and vo > 0 and vk > 0:
                draw(vo, ho, vk, T, H, tmh)
            else:
                d_error("H и Vo")

        def vvvovk():
            vo = round(float(voe.get()), 2)
            vk = round(float(vke.get()), 2)
            H = round(vk ** 2 / (2 * g), 2)
            ho = round(H - vo ** 2 / (2 * g), 2)
            tmh = round(vo / g, 2)
            T = round(tmh + vk / g, 2)
            if tmh > 0 and ho > 0 and H > 0 and T > 0 and vo > 0 and vk > 0:
                draw(vo, ho, vk, T, H, tmh)
            else:
                d_error("Vo и Vк")

        def vvvot():
            vo = round(float(voe.get()), 2)
            T = round(float(Te.get()), 2)
            tmh = round(vo / g, 2)
            t2 = T - tmh
            vk = round(g * t2, 2)
            H = round(vk ** 2 / (2 * g), 2)
            ho = round(H - vo ** 2 / (2 * g), 2)
            if tmh > 0 and ho > 0 and H > 0 and T > 0 and vo > 0 and vk > 0:
                draw(vo, ho, vk, T, H, tmh)
            else:
                d_error("Vo и T")

        def vvvkho():
            vk = round(float(vke.get()), 2)
            ho = round(float(hoe.get()), 2)
            H = round(vk ** 2 / (2 * g), 2)
            vo2 = vk ** 2 - 2 * g * ho
            t2 = round(vk / g, 2)
            if ho > 0 and H > 0 and vo2 > 0 and vk > 0:
                vo = round(vo2 ** 0.5, 2)
                tmh = round(vo / g, 2)
                T = t2 + tmh
                draw(vo, ho, vk, T, H, tmh)
            else:
                d_error("Vк и ho")

        def vvhoH():
            ho = round(float(hoe.get()), 2)
            H = round(float(He.get()), 2)
            vo2 = 2 * g * (H - ho)
            vk = round((2 * g * H) ** 0.5, 2)
            if vo2 > 0 and ho > 0 and H > 0 and vk > 0:
                vo = round(vo2 ** 0.5, 2)
                tmh = round(vo / g, 2)
                T = round(tmh + vk / g, 2)
                draw(vo, ho, vk, T, H, tmh)
            else:
                d_error("ho и H")

        def vvhotmh():
            ho = round(float(hoe.get()), 2)
            tmh = round(float(tmhe.get()), 2)
            vo = round(g * tmh, 2)
            H = round(ho + vo ** 2 / (2 * g), 2)
            vk = round((2 * g * H) ** 0.5, 2)
            T = round(tmh + vk / g, 2)
            draw(vo, ho, vk, T, H, tmh)

        def vvvkT():
            vk = round(float(vke.get()), 2)
            T = round(float(Te.get()), 2)
            H = round(vk ** 2 / (2 * g), 2)
            tmh = round(T - vk / g, 2)
            vo = round(tmh * g, 2)
            ho = round(H - vo ** 2 / (2 * g), 2)
            if tmh > 0 and ho > 0 and H > 0 and T > 0 and vo > 0 and vk > 0:
                draw(vo, ho, vk, T, H, tmh)
            else:
                d_error("Vк и T")

        def vvHT():
            H = round(float(He.get()), 2)
            T = round(float(Te.get()), 2)
            vk = round((2 * g * H) ** 0.5, 2)
            tmh = round(T - vk / g, 2)
            vo = round(tmh * g, 2)
            ho = round(H - vo ** 2 / (2 * g), 2)
            if tmh > 0 and ho > 0 and H > 0 and T > 0 and vo > 0 and vk > 0:
                draw(vo, ho, vk, T, H, tmh)
            else:
                d_error("H и T")

        def vvHtmh():
            H = round(float(He.get()), 2)
            tmh = round(float(tmhe.get()), 2)
            vk = round((2 * g * H) ** 0.5, 2)
            t2 = vk / g
            T = round(tmh + t2, 2)
            vo = round(tmh * g, 2)
            ho = round(H - vo ** 2 / (2 * g), 2)
            if tmh > 0 and ho > 0 and H > 0 and T > 0 and vo > 0 and vk > 0:
                draw(vo, ho, vk, T, H, tmh)
            else:
                d_error("H и tmaxh")

        def vvTtmh():
            tmh = round(float(tmhe.get()), 2)
            T = round(float(Te.get()), 2)
            vk = round((T - tmh) * g, 2)
            vo = round(tmh * g, 2)
            H = round(vk ** 2 / (2 * g), 2)
            ho = round(H - vo ** 2 / (2 * g), 2)
            if tmh > 0 and ho > 0 and H > 0 and T > 0 and vo > 0 and vk > 0:
                draw(vo, ho, vk, T, H, tmh)
            else:
                d_error("T и tmaxh")

        def vvvktmh():
            vk = round(float(vke.get()), 2)
            tmh = round(float(tmhe.get()), 2)
            t2 = vk / g
            T = round(t2 + tmh, 2)
            H = round(vk ** 2 / (2 * g), 2)
            vo = round(tmh * g, 2)
            ho = round(H - vo ** 2 / (2 * g), 2)
            if tmh > 0 and ho > 0 and H > 0 and T > 0 and vo > 0 and vk > 0:
                draw(vo, ho, vk, T, H, tmh)
            else:
                d_error("Vк и tmaxh")

        #
        # обработка данных
        #
        def GO():
            global vo_dano
            global vk_dano
            global ho_dano
            global H_dano
            global T_dano
            global tmh_dano

            if vo_dano and ho_dano and voe.get() != "" and hoe.get() != "" and is_digit(voe.get()) and is_digit(
                    hoe.get()):
                vvvoho()  # 1
            elif vo_dano and H_dano and voe.get() != "" and He.get() != "" and is_digit(voe.get()) and is_digit(
                    He.get()):
                vvvoh()  # 2
            elif vo_dano and vk_dano and voe.get() != "" and vke.get() != "" and is_digit(voe.get()) and is_digit(
                    vke.get()):
                vvvovk()  # 3
            elif vo_dano and T_dano and voe.get() != "" and Te.get() != "" and is_digit(voe.get()) and is_digit(
                    Te.get()):
                vvvot()  # 4
            elif vk_dano and ho_dano and vke.get() != "" and hoe.get() != "" and is_digit(vke.get()) and is_digit(
                    hoe.get()):
                vvvkho()  # 5
            elif ho_dano and H_dano and hoe.get() != "" and He.get() != "" and is_digit(He.get()) and is_digit(
                    hoe.get()):
                vvhoH()  # 6
            elif ho_dano and tmh_dano and hoe.get() != "" and tmhe.get() != "" and is_digit(tmhe.get()) and is_digit(
                    hoe.get()):
                vvhotmh()  # 7
            elif vk_dano and T_dano and vke.get() != "" and Te.get() != "" and is_digit(vke.get()) and is_digit(
                    Te.get()):
                vvvkT()  # 8
            elif H_dano and T_dano and He.get() != "" and Te.get() != "" and is_digit(He.get()) and is_digit(Te.get()):
                vvHT()  # 9
            elif H_dano and tmh_dano and tmhe.get() != "" and He.get() != "" and is_digit(He.get()) and is_digit(
                    tmhe.get()):
                vvHtmh()  # 10
            elif T_dano and tmh_dano and tmhe.get() != "" and Te.get() != "" and is_digit(Te.get()) and is_digit(
                    tmhe.get()):
                vvTtmh()  # 11c
            elif vk_dano and tmh_dano and vke.get() != "" and tmhe.get() != "" and is_digit(vke.get()) and is_digit(
                    tmhe.get()):
                vvvktmh()  # 12
            else:
                mb.showerror("Ошибка в вводе величин!",
                             "Неверные входные данные!\nПерепроверьте ввод и/или перечитайте инструкцию!\n А ЕЩЕ ПЕРЕЧИТАЙТЕ ИНСТРУКЦИЮ. ВОЗМОЖНО ЭТО ВАМ ПОМОЖЕТ")

            vo_dano = False
            vk_dano = False
            ho_dano = False
            H_dano = False
            T_dano = False
            tmh_dano = False

        #
        go = Button(rootvv, text="Рассчитай!", font=("Verdana", 15))
        go.place(x=100, y=510)
        go.config(command=GO)

        how_to_back = Label(text="Для возвращения на главный экран нажмите кнопку 'BACK' ^", font=("verdana", 12))
        how_to_back.place(x=350, y=150)
        palka = Label(text="|\n|", font=("VERDANA", 12))
        palka.place(x=864, y=114)
        strelka = Label(text="<—", font=("verdana", 12))
        strelka.place(x=830, y=105)

    global iz_vibory
    iz_vibory = True

    vverh = Button(root, text="Вертикально вверх", font=("Verdana", 15))
    vverh.config(command=d_vverh)
    vverh.place(x=0, y=70, width=300, height=90)

    ugol = Button(root, text="Под углом к горизонту\nс земли (0 < угол < π/2)", font=("Verdana", 15))
    ugol.config(command=d_ugol)
    ugol.place(x=0, y=160, width=300, height=90)

    ugol_ho = Button(root, text="Под углом к горизонту\nс ho (0 < угол < π/2)", font=("Verdana", 15))
    ugol_ho.config(command=d_ugol_ho)
    ugol_ho.place(x=0, y=250, width=300, height=90)

    vniz = Button(root, text="Вертикально вниз", font=("Verdana", 15))
    vniz.config(command=d_vniz)
    vniz.place(x=0, y=430, width=300, height=90)

    gorizontalno = Button(root, text="Горизонтальный бросок", font=("Verdana", 15))
    gorizontalno.config(command=d_horizon)
    gorizontalno.place(x=0, y=340, width=300, height=90)

    root.mainloop()


vibory()
