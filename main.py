import socket


class SERVER():
    pocket = ""
    client_now = ""

    out_str = ""
    caller = ""

    serv_data = ""
    def __init__():
        try:
            print("__Begin:  ")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            SERVER.serv_data = sock
            sock.bind(('127.0.0.1', 8889))
            sock.listen(1)
            sock.setblocking(False)
            while True:
                try:
                    SERVER.client_now, addr = sock.accept()
                except socket.error:
                    pass
                else:

                    SERVER.client_now.setblocking(True)
                    SERVER.pocket = SERVER.client_now.recv(102400).decode()
                    print("     pocket: ",SERVER.pocket)



                    SERVER.caller = str(SERVER.pocket[32:37])
                    print("     Caller:  ", SERVER.caller)

                    if SERVER.caller == "ADDAC": #создание нового аккаунта
                        SERVER.client_now.sendall(b"ok")
                        SERVER.CREATE_NEW_ACCOUNT()
                    if SERVER.caller == "PAROL": #сверка введ. польз. пароля с ранее созданными
                        SERVER.client_now.sendall(b"ok")
                        SERVER.PASSWORD_REQUEST()
                    if SERVER.caller == "GETFL": #Отправка всех существующих заказов к клиенту
                        SERVER.client_now.sendall(b"ok")
                        SERVER.SEND_PROJECTS()
                    if SERVER.caller == "NEWPJ": #Coздание нового проекта
                        SERVER.client_now.sendall(b"ok")
                        SERVER.CREATE_NEW_PROJECTS()

                    if SERVER.caller == "NaDIA": #ИНЖЕНЕР: вступить в диагностику
                        SERVER.client_now.sendall(b"ok")
                        SERVER.INJ.vstupit_v_diagnosticu()
                    if SERVER.caller == "ZaDIA":  # ИНЖЕНЕР: вступить в диагностику
                        SERVER.client_now.sendall(b"ok")
                        SERVER.INJ.zakrit_diagnosticu()

                    if SERVER.caller == "NaCEN":
                        SERVER.client_now.sendall(b"ok")
                        SERVER.MEZ.vstupit_v_uzn_cen()
                    if SERVER.caller == "ZaCEN":
                        SERVER.client_now.sendall(b"ok")
                        SERVER.MEZ.zakrit_uzn_cen()

                    sock.setblocking(False)
        except:
            print("The enD")

    def PASSWORD_REQUEST():
        login = ""
        parol = ""
        dol = ""

        counter = 38
        while True:
            if str(SERVER.pocket[counter]) != "_":
                login += str(SERVER.pocket[counter])
                counter += 1
            else:
                break
        print("login:", login)
        counter += 1
        while True:
            if str(SERVER.pocket[counter]) != "_":
                parol += str(SERVER.pocket[counter])
                counter += 1
            else:
                break
        print("parol:", parol)

        counter += 1
        while True:
            if str(SERVER.pocket[counter]) != "_":
                dol += str(SERVER.pocket[counter])
                counter += 1
            else:
                break
        print("Должность:", dol)
        # output_file.write(buf_file.readline()[count_string])
        nomes_str_acc = ""
        with open("..\SERVER_CHAY\DATABASE\occounts.txt") as acc:
            len_of_acc = 0
            # for i, l in enumerate(acc):
            #     len_of_acc += 1
            #     print("len_of_acc ",len_of_acc)
            # print('kkk')
            parol_real = ""
            login_real = ""
            FIO = ""

            i_FLAG = 0
            for index, line in enumerate(acc):
                print("string #", index, ": ", line)
                if login in line and dol in line:

                    counte = 0
                    while True:
                        if str(line[counte]) != " ":
                            login_real += str(line[counte])
                            counte += 1
                        else:
                            break
                    print("login_real: ", login_real)

                    counte += 1
                    while True:
                        if str(line[counte]) != " ":
                            parol_real += str(line[counte])

                            counte += 1
                        else:
                            break
                    print("parol_real: ", parol_real)

                    counte += 5
                    while True: #familiya
                        # print("familia line[counte]: ", line[counte])
                        if str(line[counte]) != " ":
                            FIO += str(line[counte])
                            counte += 1
                            # print("str(line[counte])",str(line[counte]))
                        else:
                            break

                    FIO += " "
                    counte += 1
                    while True:  # imya
                        # print("imya line[counte]: ", line[counte])
                        if str(line[counte]) != " ":
                            FIO += str(line[counte])
                            counte += 1
                        else:
                            break

                    FIO += " "
                    counte += 1
                    print(FIO)
                    print("LENNNNNNNNNNNNNNNN100 of .txt string:", len(line), ", counte: ",counte)
                    # try:
                    while True:  # otchestvo
                        o = len(line) -1
                        if counte >= o:
                            print("break-fuck")
                            break

                        # print("9line",line[counte])
                        if str(line[counte]) != " ":
                            # print("otchestvo line[counte]: ", line[counte])
                            FIO += str(line[counte])
                            counte += 1
                            # print("str(line[counte])otch",str(line[counte])," counte: ",counte)
                        else:
                            print("break2")
                            break
                    # except:
                    #     print("fuck555")

                    print("parol_real: ", parol_real)
                    print("login_real: ", login_real)
                    print("FIO: ", FIO)

                    if parol_real.strip() == parol.strip() and login_real.strip() == login.strip():
                        print("8333333333333333333333333333333333333333333333333")
                        SERVER.client_now.sendall(FIO.encode())
                        return

                    if parol_real != parol and login_real == login:
                        print("83333333333333333333333333333333333333333333333331")
                        i_FLAG += 1
            else:
                if i_FLAG != 0:
                    print("bad_parol")
                    SERVER.client_now.sendall(b"bad_parol")

                    return
                else:
                    print("acc_does_not")
                    SERVER.client_now.sendall(b"acc_does_not")
                    return

    def CREATE_NEW_ACCOUNT():
        time = SERVER.pocket[0:16]
        print("time of registration: ",time)
        dolg = SERVER.pocket[17:20]
        print("Class of staff: ", dolg)
        name_abiturienta = ""
        login = ""
        parol = ""

        counter = 38
        while True:
            if SERVER.pocket[counter] != "?":
                name_abiturienta += SERVER.pocket[counter]
            else:
                break
            counter += 1
        print("Name of abiturient: ",name_abiturienta)

        counter += 1
        while True:
            if SERVER.pocket[counter] != "?":
                login += SERVER.pocket[counter]
            else:
                break
            counter += 1
        print("login: ", login)

        counter += 1
        while True:
            if SERVER.pocket[counter] != "?":
                parol += SERVER.pocket[counter]
            else:
                break
            counter += 1
        print("parol: ", parol)

        #проверяем есть ли такой запрос или уже сущ. акк
        otvet = ""
        flag = 0
        with open("..\SERVER_CHAY\DATABASE\onew_accounts.txt", 'r') as zayavki:
            counter = 1
            # while True:

            for index, line in enumerate(zayavki):
                if login in line and dolg in line:
                    flag = 1
                # if name_abiturienta in line:
                #     flag = 1
        with open("..\SERVER_CHAY\DATABASE\occounts.txt", 'r') as created_acc:
            for index, line in enumerate(created_acc):
                if login in line and dolg in line:
                    flag = 1
                # if name_abiturienta in line:
                #     flag = 1

        if flag == 0:
            with open("..\SERVER_CHAY\DATABASE\onew_accounts.txt", 'a') as new_acc:
                new_acc.write(time+"?"+name_abiturienta+"?"+dolg+"?"+login+"?"+parol+"\n")
            print(time+"?"+name_abiturienta+"?"+dolg+"?"+login+"?"+parol+"\n")
            otvet = "VCE_OK"
            print("OK NAME")
            SERVER.client_now.sendall(otvet.encode())
        if flag == 1:
            flag = 0
            print("BAD NAME")
            otvet = "VCE_BAD"
            SERVER.client_now.sendall(otvet.encode())

    def SEND_PROJECTS():
        send_str_withall_projects = ""

        import os
        directory = '..\SERVER_CHAY\DATABASE\projects'
        files = os.listdir(directory)
        with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'w') as buf_file:
            buf_file.write("")
        for name in files:
            print("reading file:",name," ",name.find("#manual"))
            if name.find("#manual") <= 0 and name != "ofile_buf_for_send_all_files.txt":
                path = "..\SERVER_CHAY\DATABASE\projects\ "
                with open( path.strip()+ f'{name}', 'r') as continie_file:

                    with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'a') as buf_file:
                        for index, line in enumerate(continie_file):
                            g = line.strip("\n")
                            print("g ",g)
                            g += "\n"
                            buf_file.write(g)
        with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'r') as buf_file:
            for index, line in enumerate(buf_file):
                # g = line.strip("\n")
                # g += "?"
                send_str_withall_projects += line
        if send_str_withall_projects == "":
            send_str_withall_projects = "sboy"
        print("send_str_withall_projects",send_str_withall_projects)
        SERVER.client_now.sendall(send_str_withall_projects.encode())

    ##################INPUT DATA#####################
    nomer_proecta = ""
    data_sozdaniya_proecta = ""

    imya_menedgera = ""

    name_of_organisation = ""
    elect_pochta_of_contact_face = ""
    number_time_for_end = ""

    INN = ""
    KPP = ""
    number_of_contact_face = ""
    name_of_contact_face = ""

    adress_of_organisation = ""
    oborudovanie = ""
    seriyniy_nomer = ""
    kodovoye_nazvanie = ""
    kolichestvo = ""
    edinitsy = ""
    nomer_sticker_plomby = ""
    komplektatia = ""
    opisanie_neispravnosti_ot_zakazchika = ""
    input_meh_destroy = ""

    status_remonta = ""
    dogovor_podpisan = ""

    def CREATE_NEW_PROJECTS():
        SERVER.nomer_proecta = ""
        SERVER.data_sozdaniya_proecta = ""

        SERVER.imya_menedgera = ""

        SERVER.name_of_organisation = ""
        SERVER.elect_pochta_of_contact_face = ""
        SERVER.number_time_for_end = ""

        SERVER.INN = ""
        SERVER.KPP = ""
        SERVER.number_of_contact_face = ""
        SERVER.name_of_contact_face = ""

        SERVER.adress_of_organisation = ""
        SERVER.oborudovanie = ""
        SERVER.seriyniy_nomer = ""
        SERVER.kodovoye_nazvanie = ""
        SERVER.kolichestvo = ""
        SERVER.edinitsy = ""
        SERVER.nomer_sticker_plomby = ""
        SERVER.komplektatia = ""
        SERVER.opisanie_neispravnosti_ot_zakazchika = ""
        SERVER.input_meh_destroy = ""

        SERVER.status_remonta = ""
        SERVER.dogovor_podpisan = ""

        print("Creating new project...")
        new_text = SERVER.client_now.recv(102400).decode()
        print("new_text: ",new_text)

        SERVER.pocket = new_text
        try:
            print("nomer proecta: ", SERVER.nomer_proecta)
            if "divive pocket" == "divive pocket":
                counter = 0
                while True:
                    if new_text[counter] != "?":
                        SERVER.nomer_proecta += new_text[counter]
                    else:
                        break
                    counter += 1
                print("nomer proecta: ", SERVER.nomer_proecta)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.data_sozdaniya_proecta += new_text[counter]
                    else:
                        break
                    counter += 1
                print("data sozdaniya proecta: ", SERVER.data_sozdaniya_proecta)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.imya_menedgera += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of menedger: ", SERVER.imya_menedgera)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.name_of_organisation += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of org: ", SERVER.name_of_organisation)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.elect_pochta_of_contact_face += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of pocht: ", SERVER.elect_pochta_of_contact_face)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.number_time_for_end += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of time-end: ", SERVER.number_time_for_end)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.INN += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of org-INN: ", SERVER.INN)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.KPP += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of org-KPP: ", SERVER.KPP)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.number_of_contact_face += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Number of contact face: ", SERVER.number_of_contact_face)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.name_of_contact_face += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of cont.face: ", SERVER.name_of_contact_face)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.adress_of_organisation += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Adress: ", SERVER.adress_of_organisation)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.oborudovanie += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of oborudovanie: ", SERVER.oborudovanie)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.seriyniy_nomer += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of seriyniy nomer: ", SERVER.seriyniy_nomer)

                try:
                    counter += 1
                    while True:
                        if SERVER.pocket[counter] != "?":
                            SERVER.kodovoye_nazvanie += new_text[counter]
                        else:
                            break
                        counter += 1
                    print("Name of cod. nazvanie: ", SERVER.kodovoye_nazvanie)
                except:
                    print("Отсутствует кодовое название")

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.kolichestvo += new_text[counter]
                    else:
                        break
                    counter += 1
                print("kolichestvo: ", SERVER.kolichestvo)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.edinitsy += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of edinitsy: ", SERVER.edinitsy)

                try:
                    counter += 1
                    while True:
                        if SERVER.pocket[counter] != "?":
                            SERVER.nomer_sticker_plomby += new_text[counter]
                        else:
                            break
                        counter += 1
                    print("Nomer stik. plombi: ", SERVER.nomer_sticker_plomby)
                except:
                    print("Отсутствует стикер-пломба")

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.komplektatia += new_text[counter]
                    else:
                        break
                    counter += 1
                print("komplektatia: ", SERVER.komplektatia)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.opisanie_neispravnosti_ot_zakazchika += new_text[counter]
                    else:
                        break
                    counter += 1
                print("opisanie neispravnosti ot zakazchika: ", SERVER.opisanie_neispravnosti_ot_zakazchika)

                try:
                    counter += 1
                    while True:
                        if SERVER.pocket[counter] != "?":
                            SERVER.input_meh_destroy += new_text[counter]
                        else:
                            break
                        counter += 1
                    print("Input meh. destroy: ", SERVER.input_meh_destroy)
                except:
                    print("Отсутствует описание вх. мех. повреждения")

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.status_remonta += new_text[counter]
                    else:
                        break
                    counter += 1
                print("Name of status remonta: ", SERVER.status_remonta)

                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        SERVER.dogovor_podpisan += new_text[counter]
                    else:
                        break
                    counter += 1
                print("dogovor_podpisan?: ", SERVER.dogovor_podpisan)

                # counter += 1
                # while True:
                #     if SERVER.pocket[counter] != "?":
                #         SERVER.name_of_organisation += new_text[counter]
                #     else:
                #         break
                #     counter += 1
                # print("Name of org: ", SERVER.name_of_organisation)
        except:
            SERVER.client_now.sendall(b"non_full_pocket")
            print("Не полная посылка")
        else:
            SERVER.client_now.sendall(b"okok")
            print("Посылка удачно распакована")
        name = "#" + SERVER.nomer_proecta
        path = "..\SERVER_CHAY\DATABASE\projects\ "
        path.strip()
        path += name
        path += ".txt"

        with open(path, 'w') as new_prj:
            new_prj.write("")
        with open(path, 'a') as new_prj:
            new_prj.write("###")
            new_prj.write(SERVER.nomer_proecta + "\n")
            new_prj.write(SERVER.data_sozdaniya_proecta + "\n")
            new_prj.write(SERVER.imya_menedgera + "\n")
            new_prj.write(SERVER.name_of_organisation + "\n")
            new_prj.write(SERVER.elect_pochta_of_contact_face + "\n")
            new_prj.write(SERVER.number_time_for_end + "\n")
            new_prj.write(SERVER.INN + "\n")
            new_prj.write(SERVER.KPP + "\n")
            new_prj.write(SERVER.number_of_contact_face + "\n")
            new_prj.write(SERVER.name_of_contact_face + "\n")
            new_prj.write(SERVER.adress_of_organisation + "\n")
            new_prj.write(SERVER.oborudovanie + "\n")
            new_prj.write(SERVER.seriyniy_nomer + "\n")
            new_prj.write(SERVER.kodovoye_nazvanie + "\n")
            new_prj.write(SERVER.kolichestvo + "\n")
            new_prj.write(SERVER.edinitsy + "\n")
            new_prj.write(SERVER.nomer_sticker_plomby + "\n")
            new_prj.write(SERVER.komplektatia + "\n")
            new_prj.write(SERVER.opisanie_neispravnosti_ot_zakazchika + "\n")
            new_prj.write(SERVER.input_meh_destroy + "\n")
            new_prj.write(SERVER.status_remonta + "\n")
            new_prj.write(SERVER.dogovor_podpisan + "\n")

        name = "#" + SERVER.nomer_proecta + "#manual"
        path = "..\SERVER_CHAY\DATABASE\projects\ "
        path.strip()
        path += name
        path += ".txt"
        with open(path, 'w') as new_manual:
            new_manual.write("")
        with open(path, 'a') as new_manual:
            new_manual.write(SERVER.data_sozdaniya_proecta + "Создание проекта"+"\n")

    class INJ():
        def vstupit_v_diagnosticu():
            counter = 37
            l = ""
            p = ""
            dol = ""
            nomer_zakaza = ""

            try:
                while True:
                    if SERVER.pocket[counter] != "?":
                        l += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        p += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        dol += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        nomer_zakaza += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
            except:
                pass
            print("lp",l,p,dol,nomer_zakaza)

            name_of_accFILE = l + "_" + p + "_" + dol
            path = "../SERVER_CHAY/DATABASE/oaccounts/ "
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            print("path",path)
            with open(path, 'a') as new_accFILE:
                import datetime
                now = str(datetime.datetime.now())
                # 2021-08-06 22:45:02.522446
                year = now[0:4]
                mounth = now[5:7]
                day = now[8:10]
                hour = now[11:13]
                minut = now[14:16]
                times = day +"."+mounth+"."+year+" "+hour+":"+minut
                new_accFILE.write("123")
                strs = str(times)+" - Вступает в диагностику заказа №"+str(nomer_zakaza)+"\n"
                new_accFILE.write(strs)

            name_of_accFILE = " #" + str(nomer_zakaza).strip() + "#manual"
            path = "../SERVER_CHAY/DATABASE/projects/"
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            print("path", path)

            with open(path, 'a') as new_accFILE:
                import datetime
                now = str(datetime.datetime.now())
                # 2021-08-06 22:45:02.522446
                year = now[0:4]
                mounth = now[5:7]
                day = now[8:10]
                hour = now[11:13]
                minut = now[14:16]
                times = day + "." + mounth + "." + year + " " + hour + ":" + minut
                # strs = str(times) + " - за диагностику взялся" + " " + l+ " " +dol+ "\n"
                # new_accFILE.write(strs)

            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'w') as buf_file:
                buf_file.write("")

            #узнаем имя заполнявшего
            immya = ""
            with open("..\SERVER_CHAY\DATABASE\occounts.txt", 'r') as buf_file:

                for index,line in enumerate(buf_file):
                    if l in line and dol in line:

                        counter = 0
                        while True:
                            if line[counter] != " ":
                                pass
                            else:
                                break
                            counter+=1
                        counter += 1
                        while True:
                            if line[counter] != " ":
                                pass
                            else:
                                break
                            counter+=1
                        counter += 1
                        while True:
                            if line[counter] != " ":
                                pass
                            else:
                                break
                            counter+=1
                        counter += 1
                        while True:
                            if line[counter] != " ":
                                immya += line[counter]
                            else:
                                break
                            counter+=1
                        counter += 1
                        immya += " "
                        while True:
                            if line[counter] != " ":
                                immya += line[counter]
                            else:
                                break
                            counter+=1
                        counter += 1
                        immya += " "
                        try:
                            while True:
                                if line[counter] != " ":
                                    immya += line[counter]
                                else:
                                    break
                                counter+=1
                        except:
                            pass
                        break
            print("immya",immya)

            #меняем статус заказа
            print("per")
            name_of_accFILE = "#" + str(nomer_zakaza).strip()
            path = "../SERVER_CHAY/DATABASE/projects/"
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            try:
                with open(path, 'r') as proj_file:
                    pass
            except:
                name_of_accFILE = " #" + str(nomer_zakaza).strip()
                path = "../SERVER_CHAY/DATABASE/projects/"
                path.strip()
                path += name_of_accFILE
                path += ".txt"
            print("path", path)
            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'a') as buf_file:
                print("159")
                with open(path, 'r') as proj_file:
                    for index,line in enumerate(proj_file):
                        if index < 20:
                            buf_file.write(line)
                        if index == 20:
                            buf_file.write("Диагностика в процессе\n")
                        if index > 20:
                            buf_file.write(line)
                    j = immya
                    buf_file.write(j)
            #перезаписываем файл с учётом эвентов, и запихиваем результаты диагностики
            stri = ""
            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'r') as buf_file:
                with open(path, 'w') as proj_file:
                    proj_file.write("")

                with open(path, 'a') as proj_file:
                    for index, line in enumerate(buf_file):
                        proj_file.write(line)
            name_of_accFILE = "#" + str(nomer_zakaza).strip() + "#manual"
            path = "../SERVER_CHAY/DATABASE/projects/"
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            try:
                with open(path, 'r') as proj_file:
                    pass
            except:
                name_of_accFILE = " #" + str(nomer_zakaza).strip() + "#manual"
                path = "../SERVER_CHAY/DATABASE/projects/"
                path.strip()
                path += name_of_accFILE
                path += ".txt"
            with open(path, 'a') as proj_file:
                import datetime
                now = str(datetime.datetime.now())
                # 2021-08-06 22:45:02.522446
                year = now[0:4]
                mounth = now[5:7]
                day = now[8:10]
                hour = now[11:13]
                minut = now[14:16]
                times = day + "." + mounth + "." + year + " " + hour + ":" + minut
                stri = times + " - Диагностику заказа начинает " + immya
                proj_file.write(stri)

    #     def zakrit_diagnosticu():
    #         counter = 37
    #         l = ""
    #         p = ""
    #         dol = ""
    #         nomer_zakaza = ""
    #         pocket = ""
    #
    #         dia_LE = []
    #         dia_LE_buf = ""
    #
    #         dia_LE_ist = []
    #         dia_LE_ist_buf = ""
    #
    #         dia_SP = []
    #         dia_SP_buf = ""
    #         ######
    #         soput_LE = []
    #         soput_LE_ist = []
    #         soput_SP = []
    #         soput_LE_ed = []
    #         try:
    #             while True:
    #                 if SERVER.pocket[counter] != "?":
    #                     l += SERVER.pocket[counter]
    #                 else:
    #                     break
    #                 counter += 1
    #             counter += 1
    #             while True:
    #                 if SERVER.pocket[counter] != "?":
    #                     p += SERVER.pocket[counter]
    #                 else:
    #                     break
    #                 counter += 1
    #             counter += 1
    #             while True:
    #                 if SERVER.pocket[counter] != "?":
    #                     dol += SERVER.pocket[counter]
    #                 else:
    #                     break
    #                 counter += 1
    #             counter += 1
    #             while True:
    #                 if SERVER.pocket[counter] != "?":
    #                     nomer_zakaza += SERVER.pocket[counter]
    #                 else:
    #                     break
    #                 counter += 1
    #             counter += 4
    #             #достоем описание проделанных работ
    #             stroka_opisaniya = ""
    #             while True:
    #                 print("counter:", counter)
    #                 print("stroka_opisaniya ", stroka_opisaniya)
    #                 # print("STROKA",SERVER.pocket[counter],SERVER.pocket[counter+1],SERVER.pocket[counter+2])
    #                 if SERVER.pocket[counter] != "/" and SERVER.pocket[counter+1] != "?":
    #                     stroka_opisaniya += SERVER.pocket[counter]
    #                 else:
    #                     counter += 1
    #                     counter += 1
    #                     # counter += 1
    #                     # counter += 1
    #                     break
    #                 counter += 1
    #
    #             #достоем элементы диагностики
    #             flag_zapolneniya_lineEdit = 0
    #             dia_LE = []
    #             dia_LE_ist = []
    #             dia_SP = []
    #             ######
    #             soput_LE = []
    #             soput_LE_ist = []
    #             soput_SP = []
    #             soput_LE_ed = []
    #
    #
    #             No_mass = 0
    #             counter += 1
    #             print("154")
    #             FLAG_WHILE = 1
    #             slash = "\ "
    #             slash = slash.strip()
    #             while True:
    #                 if
    #             # while True:
    #             #     if (SERVER.pocket[counter] != slash and SERVER.pocket[counter + 1] != slash) or\
    #             #             (SERVER.pocket[counter] != "/" and SERVER.pocket[counter] != "?" and SERVER.pocket[counter] != "/"):
    #             #         while True:
    #             #             if (SERVER.pocket[counter] != slash and SERVER.pocket[counter + 1] != slash) and \
    #             #                     (SERVER.pocket[counter] != "/" and SERVER.pocket[counter] != "?" and SERVER.pocket[
    #             #                         counter] != "/"):
    #             #                 dia_LE_ist_buf += SERVER.pocket[counter]
    #             #                 counter += 1
    #             #             else:
    #             #                 soput_LE.append(dia_LE_ist_buf)
    #             #                 dia_LE_ist_buf = ""
    #             #                 break
    #             #         while True:
    #             #             if (SERVER.pocket[counter] != slash and SERVER.pocket[counter + 1] != slash) and \
    #             #                     (SERVER.pocket[counter] != "/" and SERVER.pocket[counter] != "?" and SERVER.pocket[
    #             #                         counter] != "/"):
    #             #                 dia_LE_ist_buf += SERVER.pocket[counter]
    #             #                 counter += 1
    #             #             else:
    #             #                 soput_LE_ist.append(dia_LE_ist_buf)
    #             #                 dia_LE_ist_buf = ""
    #             #                 break
    #             #         while True:
    #             #             if (SERVER.pocket[counter] != slash and SERVER.pocket[counter + 1] != slash) and \
    #             #                     (SERVER.pocket[counter] != "/" and SERVER.pocket[counter] != "?" and SERVER.pocket[
    #             #                         counter] != "/"):
    #             #                 dia_LE_ist_buf += SERVER.pocket[counter]
    #             #                 counter += 1
    #             #             else:
    #             #                 soput_SP.append(dia_LE_ist_buf)
    #             #                 dia_LE_ist_buf = ""
    #             #                 break
    #             #         while True:
    #             #             if (SERVER.pocket[counter] != slash and SERVER.pocket[counter + 1] != slash) and \
    #             #                     (SERVER.pocket[counter] != "/" and SERVER.pocket[counter] != "?" and SERVER.pocket[
    #             #                         counter] != "/"):
    #             #                 dia_LE_ist_buf += SERVER.pocket[counter]
    #             #                 counter += 1
    #             #             else:
    #             #                 soput_LE_ed.append(dia_LE_ist_buf)
    #             #                 dia_LE_ist_buf = ""
    #             #                 break
    #             #     if SERVER.pocket[counter] == "/" and SERVER.pocket[counter] != "?" and SERVER.pocket[counter] != "/":
    #             #         break
    #             print("")
    #             print("dia_LE", dia_LE)
    #             print("dia_LE_ist", dia_LE_ist)
    #             print("dia_SP", dia_SP)
    #             ######
    #             print("soput_LE", soput_LE)
    #             print("soput_LE_ist", soput_LE_ist)
    #             print("soput_SP", soput_SP)
    #             print("soput_LE_ed", soput_LE_ed)
    #
    #         except:
    #             print("osoznal")
    #             pass
    #
    #         print("     stroka_opisaniya", stroka_opisaniya)
    #         # print("     data элементы для диагностики: ",LE,LE_ist,SP)
    #         # print("     data cопутств. элементы: ", SP_soput,LE_ed_soput, LE_soput,LE_ist_soput)
    #         # print("     data элементы для ремонта: ", LE_rem, SP_rem)
    #         #
    #         # print("     Личные данные заполняющего",l,p,dol,nomer_zakaza)
    #
    #         name_of_accFILE = l + "_" + p + "_" + dol
    #         path = "../SERVER_CHAY/DATABASE/oaccounts/ "
    #         path.strip()
    #         path += name_of_accFILE
    #         path += ".txt"
    #         print("path1",path)
    #         with open(path, 'a') as new_accFILE:
    #             import datetime
    #             now = str(datetime.datetime.now())
    #             # 2021-08-06 22:45:02.522446
    #             year = now[0:4]
    #             mounth = now[5:7]
    #             day = now[8:10]
    #             hour = now[11:13]
    #             minut = now[14:16]
    #             times = day +"."+mounth+"."+year+" "+hour+":"+minut
    #             strs = str(times)+" - Закрывает диагностику заказа №"+str(nomer_zakaza)+"\n"
    #             new_accFILE.write(strs)
    #
    #
    # ######################
    #         name_of_accFILE = " #" + str(nomer_zakaza).strip()
    #         path = "../SERVER_CHAY/DATABASE/projects/"
    #         path.strip()
    #         path += name_of_accFILE
    #         path += ".txt"
    #         print("pathh", path)
    #         try:
    #             with open(path, 'r') as proj_file:
    #                 pass
    #         except:
    #             name_of_accFILE = "#" + str(nomer_zakaza).strip()
    #             path = "../SERVER_CHAY/DATABASE/projects/"
    #             path.strip()
    #             path += name_of_accFILE
    #             path += ".txt"
    #             print("pathh", path)
    #
    #         with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'w') as buf_file:
    #             buf_file.write("")
    #
    #         #меняем статус заказа
    #         print("per")
    #         with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'a') as buf_file:
    #             with open(path, 'r') as proj_file:
    #                 for index,line in enumerate(proj_file):
    #                     if index < 20:
    #                         buf_file.write(line)
    #                     if index == 20:
    #                         buf_file.write("Ожидание цен закупа\n")
    #                     if index > 20:
    #                         buf_file.write(line)
    #         print("per")
    #
    #         #перезаписываем файл с учётом эвентов, и запихиваем результаты диагностики
    #         stri = ""
    #         with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'r') as buf_file:
    #             with open(path, 'w') as proj_file:
    #                 proj_file.write("")
    #
    #             with open(path, 'a') as proj_file:
    #                 for index, line in enumerate(buf_file):
    #                     proj_file.write(line)
    #                 stri += stroka_opisaniya
    #                 stri += "\n"
    #                 for i in range(len(LE)):
    #                     stri += LE[i]
    #                     stri += "?"
    #                     stri += LE_ist[i]
    #                     stri += "?"
    #                     stri += SP[i]
    #                     stri += "?"
    #                 stri += "\n"
    #                 # SP_soput, LE_ed_soput, LE_soput
    #                 for i in range(len(LE_soput)):
    #                     stri += SP_soput[i]
    #                     stri += "?"
    #                     stri += LE_ed_soput[i]
    #                     stri += "?"
    #                     stri += LE_soput[i]
    #                     stri += "?"
    #                 stri += "\n"
    #                 for i in range(len(LE_rem)):
    #                     stri += LE_rem[i]
    #                     stri += "?"
    #                     stri += SP_rem[i]
    #                     stri += "?"
    #                 stri += "\n"
    #                 proj_file.write(stri)
    #
    #             name_of_accFILE = "#" + str(nomer_zakaza).strip() + "#manual"
    #             path = "../SERVER_CHAY/DATABASE/projects/"
    #             path.strip()
    #             path += name_of_accFILE
    #             path += ".txt"
    #             try:
    #                 with open(path, 'r') as proj_file:
    #                     pass
    #             except:
    #                 name_of_accFILE = " #" + str(nomer_zakaza).strip() + "#manual"
    #                 path = "../SERVER_CHAY/DATABASE/projects/"
    #                 path.strip()
    #                 path += name_of_accFILE
    #                 path += ".txt"
    #                 # узнаем имя заполнявшего
    #             immya = ""
    #             with open("..\SERVER_CHAY\DATABASE\occounts.txt", 'r') as buf_file:
    #
    #                 for index, line in enumerate(buf_file):
    #                     if l in line and dol in line:
    #
    #                         counter = 0
    #                         while True:
    #                             if line[counter] != " ":
    #                                 pass
    #                             else:
    #                                 break
    #                             counter += 1
    #                         counter += 1
    #                         while True:
    #                             if line[counter] != " ":
    #                                 pass
    #                             else:
    #                                 break
    #                             counter += 1
    #                         counter += 1
    #                         while True:
    #                             if line[counter] != " ":
    #                                 pass
    #                             else:
    #                                 break
    #                             counter += 1
    #                         counter += 1
    #                         while True:
    #                             if line[counter] != " ":
    #                                 immya += line[counter]
    #                             else:
    #                                 break
    #                             counter += 1
    #                         counter += 1
    #                         immya += " "
    #                         while True:
    #                             if line[counter] != " ":
    #                                 immya += line[counter]
    #                             else:
    #                                 break
    #                             counter += 1
    #                         counter += 1
    #                         immya += " "
    #                         try:
    #                             while True:
    #                                 if line[counter] != " ":
    #                                     immya += line[counter]
    #                                 else:
    #                                     break
    #                                 counter += 1
    #                         except:
    #                             pass
    #                         break
    #             print("immya", immya)
    #
    #             with open(path, 'a') as proj_file:
    #                 import datetime
    #                 now = str(datetime.datetime.now())
    #                 # 2021-08-06 22:45:02.522446
    #                 year = now[0:4]
    #                 mounth = now[5:7]
    #                 day = now[8:10]
    #                 hour = now[11:13]
    #                 minut = now[14:16]
    #                 times = day + "." + mounth + "." + year + " " + hour + ":" + minut
    #                 stri = times + " - Закрывает диагностику заказа " + str(immya)
    #                 proj_file.write(stri)
        def zakrit_diagnosticu():
            counter = 37
            l = ""
            p = ""
            dol = ""
            nomer_zakaza = ""
            pocket = ""


            while True:
                # print("COUNTER",SERVER.pocket[counter],counter)
                if SERVER.pocket[counter] != "?":
                    l += SERVER.pocket[counter]
                else:
                    break
                counter += 1
            counter += 1
            while True:
                # print("COUNTER", SERVER.pocket[counter], counter)
                if SERVER.pocket[counter] != "?":
                    p += SERVER.pocket[counter]
                else:
                    break
                counter += 1
            counter += 1
            while True:
                # print("COUNTER", SERVER.pocket[counter], counter)
                if SERVER.pocket[counter] != "?":
                    dol += SERVER.pocket[counter]
                else:
                    break
                counter += 1
            counter += 1
            while True:
                # print("COUNTER", SERVER.pocket[counter], counter)
                if SERVER.pocket[counter] != "?":
                    nomer_zakaza += SERVER.pocket[counter]
                else:
                    break
                counter += 1
            counter += 4
            #достоем описание проделанных работ
            stroka_opisaniya = ""
            while True:
                # print("counter:", counter)
                # print("stroka_opisaniya ", stroka_opisaniya)
                # print("STROKA",SERVER.pocket[counter],SERVER.pocket[counter+1],SERVER.pocket[counter+2])
                if SERVER.pocket[counter] != "/" and SERVER.pocket[counter+1] != "?":
                    stroka_opisaniya += SERVER.pocket[counter]
                else:
                    counter += 1
                    counter += 1
                    # counter += 1
                    # counter += 1
                    break
                counter += 1

            #достоем элементы диагностики
            flag_zapolneniya_lineEdit = 0
            LE = []
            LE_buf = ""
            LE_ist = []
            LE_ist_buf = ""
            SP = []
            SP_buf = ""
            No_el_mass = 0
            counter += 1
            FLAG_WHILE = 1
            print("00000000000000000000000000000000000000000000000000000000000000000000")
            while True:
                print("COUNTER", SERVER.pocket[counter], counter)
                if FLAG_WHILE == 1:
                    # print("SERVER.pocket[counter]",SERVER.pocket[counter],SERVER.pocket[counter+1],SERVER.pocket[counter+2])
                    k = "\ "
                    # if SERVER.pocket[counter] != k.strip():
                    #     counter += 1
                    if SERVER.pocket[counter] != k.strip() and SERVER.pocket[counter] != "/" and SERVER.pocket[counter+1] != "?" and SERVER.pocket[counter+2] != "/":
                        print("159 kod",flag_zapolneniya_lineEdit)
                        if flag_zapolneniya_lineEdit == 1:
                            LE_ist_buf += SERVER.pocket[counter]
                        if flag_zapolneniya_lineEdit == 0:
                            LE_buf += SERVER.pocket[counter]
                        if flag_zapolneniya_lineEdit == 2:
                            SP_buf += SERVER.pocket[counter]
                            print("SP_buf ++", SP_buf)
                        # counter += 1
                        # counter += 1
                        # break
                    else:
                        if SERVER.pocket[counter] == k.strip() and SERVER.pocket[counter + 1] != k.strip():
                            if flag_zapolneniya_lineEdit == 0:
                                LE.append(LE_buf)
                                LE_buf = ""
                                flag_zapolneniya_lineEdit = 1
                            else:
                                if flag_zapolneniya_lineEdit == 1:
                                    LE_ist.append(LE_ist_buf)
                                    LE_ist_buf = ""
                                    flag_zapolneniya_lineEdit = 2
                                else:
                                    if flag_zapolneniya_lineEdit == 2:
                                        SP.append(SP_buf)
                                        SP_buf = ""
                                        flag_zapolneniya_lineEdit = 0
                            # counter += 1
                        else:
                            if SERVER.pocket[counter] == k.strip() and SERVER.pocket[counter + 1] == k.strip():
                                if flag_zapolneniya_lineEdit == 0:
                                    LE.append(LE_buf)
                                    LE_buf = ""

                                    flag_zapolneniya_lineEdit = 1
                                else:
                                    if flag_zapolneniya_lineEdit == 1:
                                        LE_ist.append(LE_ist_buf)
                                        LE_ist_buf = ""
                                        flag_zapolneniya_lineEdit = 2
                                    else:
                                        if flag_zapolneniya_lineEdit == 2:#название элемента
                                            SP.append(SP_buf)
                                            SP_buf = ""
                                            flag_zapolneniya_lineEdit = 0
                                counter += 1
                                No_el_mass += 1
                            else:
                                if SERVER.pocket[counter] == "/" and SERVER.pocket[counter + 1] == "?" and SERVER.pocket[
                                    counter + 2] == "/":
                                    counter += 1
                                    counter += 1

                                    if flag_zapolneniya_lineEdit == 2:
                                        SP_buf += SERVER.pocket[counter]
                                    if flag_zapolneniya_lineEdit == 1:
                                        LE_ist_buf += SERVER.pocket[counter]
                                    if flag_zapolneniya_lineEdit == 0:
                                        LE_buf += SERVER.pocket[counter]
                                    FLAG_WHILE = 0
                                    break
                                    # lpo = []
                                    # if LE == lpo:
                                    # break
                                else:
                                    pass

                    counter += 1
                else:
                    break
            #"""
            # достоем элементы сопут.расходов
            flag_zapolneniya_lineEdit = 0
            LE_soput = [] #eдиницы
            LE_buf = ""

            LE_ed_soput = [] #количество
            LE_ed_soput_buf = ""

            LE_ist_soput = []
            LE_ist_soput_buf = ""

            SP_soput = []   #имя
            SP_buf = ""

            No_el_mass = 0
            counter += 1
            FLAG_WHILE = 1
            while True:
                if FLAG_WHILE == 1:
                    # print("SERVER.pocket[counter]",SERVER.pocket[counter],SERVER.pocket[counter+1],SERVER.pocket[counter+2])
                    k = "\ "
                    # if SERVER.pocket[counter] != k.strip():
                    #     counter += 1
                    if SERVER.pocket[counter] != k.strip() and SERVER.pocket[counter] != "/" and \
                            SERVER.pocket[counter + 1] != "?" and SERVER.pocket[counter + 2] != "/":
                        if flag_zapolneniya_lineEdit == 3:
                            LE_ed_soput_buf += SERVER.pocket[counter]
                        if flag_zapolneniya_lineEdit == 2:
                            SP_buf += SERVER.pocket[counter]
                        if flag_zapolneniya_lineEdit == 1:
                            LE_ist_soput_buf += SERVER.pocket[counter]
                        if flag_zapolneniya_lineEdit == 0:
                            LE_buf += SERVER.pocket[counter]

                        # counter += 1
                        # counter += 1
                        # break
                    else:
                        if SERVER.pocket[counter] == k.strip() and SERVER.pocket[counter + 1] != k.strip():
                            if flag_zapolneniya_lineEdit == 1:
                                LE_ist_soput.append(LE_ist_soput_buf)
                                LE_ist_soput_buf = ""
                                flag_zapolneniya_lineEdit = 2
                            else:
                                if flag_zapolneniya_lineEdit == 2:
                                    SP_soput.append(SP_buf)
                                    SP_buf = ""
                                    flag_zapolneniya_lineEdit = 3
                                else:
                                    if flag_zapolneniya_lineEdit == 3:
                                        LE_ed_soput.append(LE_ed_soput_buf)
                                        LE_ed_soput_buf = ""
                                        flag_zapolneniya_lineEdit = 0
                                    else:
                                        if flag_zapolneniya_lineEdit == 0:
                                            LE_buf += SERVER.pocket[counter - 1]
                                            LE_soput.append(LE_buf)
                                            LE_buf = ""
                                            flag_zapolneniya_lineEdit = 1
                            # counter += 1
                        else:
                            if SERVER.pocket[counter] == k.strip() and SERVER.pocket[
                                counter + 1] == k.strip():
                                print("DVE POLOSKI")
                                if flag_zapolneniya_lineEdit == 1:
                                    LE_ist.append(LE_buf)
                                    LE_ist_buf = ""
                                    flag_zapolneniya_lineEdit = 2
                                else:
                                    if flag_zapolneniya_lineEdit == 2:
                                        SP_soput.append(SP_buf)
                                        SP_buf = ""
                                        flag_zapolneniya_lineEdit = 3
                                    else:
                                        if flag_zapolneniya_lineEdit == 0:
                                            LE_soput.append(LE_buf)
                                            LE_buf = ""
                                            flag_zapolneniya_lineEdit = 1
                                        else:
                                            if flag_zapolneniya_lineEdit == 3:
                                                LE_ed_soput.append(LE_ed_soput_buf)
                                                LE_ed_soput_buf = ""
                                                flag_zapolneniya_lineEdit = 0
                                counter += 1
                                No_el_mass += 1
                            else:
                                if SERVER.pocket[counter] == "/" and SERVER.pocket[counter + 1] == "?" and \
                                        SERVER.pocket[
                                            counter + 2] == "/":
                                    counter += 1
                                    counter += 1

                                    # if flag_zapolneniya_lineEdit == 3:
                                    #     SP_buf += SERVER.pocket[counter]
                                    # if flag_zapolneniya_lineEdit == 2:
                                    #     LE_ed_soput_buf += SERVER.pocket[counter]
                                    # if flag_zapolneniya_lineEdit == 0:
                                    #     LE_buf += SERVER.pocket[counter]
                                    # if flag_zapolneniya_lineEdit == 1:
                                    #     LE_ist_buf += SERVER.pocket[counter]
                                    FLAG_WHILE = 0
                                    break
                                    # lpo = []
                                    # if LE == lpo:
                                    # break
                                else:
                                    pass

                    counter += 1
                else:
                    break

            #как не надо исправлять ошибки
            for i in range(len(LE_soput)):
                bbb = LE_soput[i]
                ddd = bbb[0:len(LE_soput[i])-1]
                LE_soput[i] = ddd

            # достоем элементы диагностики
            flag_zapolneniya_lineEdit = 1
            LE_rem = []
            LE_buf = ""
            LE_ist_rem = []
            LE_ist_buf = ""
            SP_rem = []
            SP_buf = ""
            No_el_mass = 0
            counter += 1
            FLAG_WHILE = 1
            while True:
                if FLAG_WHILE == 1:
                    # print("SERVER.pocket[counter]",SERVER.pocket[counter],SERVER.pocket[counter+1],SERVER.pocket[counter+2])
                    k = "\ "
                    # if SERVER.pocket[counter] != k.strip():
                    #     counter += 1
                    if SERVER.pocket[counter] != k.strip() and SERVER.pocket[counter] != "/" and \
                            SERVER.pocket[counter + 1] != "?" and SERVER.pocket[counter + 2] != "/":
                        if flag_zapolneniya_lineEdit == 0:
                            LE_buf += SERVER.pocket[counter]
                        if flag_zapolneniya_lineEdit == 1:
                            LE_ist_buf += SERVER.pocket[counter]
                        if flag_zapolneniya_lineEdit == 2:
                            SP_buf += SERVER.pocket[counter]
                        # counter += 1
                        # counter += 1
                        # break
                    else:
                        if SERVER.pocket[counter] == k.strip() and SERVER.pocket[counter + 1] != k.strip():
                            if flag_zapolneniya_lineEdit == 0:
                                LE_rem.append(LE_buf)
                                LE_buf = ""
                                flag_zapolneniya_lineEdit = 1
                            else:
                                if flag_zapolneniya_lineEdit == 2:
                                    SP_rem.append(SP_buf)
                                    SP_buf = ""
                                    flag_zapolneniya_lineEdit = 0
                                else:
                                    if flag_zapolneniya_lineEdit == 1:
                                        LE_ist_rem.append(LE_ist_buf)
                                        LE_ist_buf = ""
                                        flag_zapolneniya_lineEdit = 2
                            # counter += 1
                        else:
                            if SERVER.pocket[counter] == k.strip() and SERVER.pocket[
                                counter + 1] == k.strip():
                                if flag_zapolneniya_lineEdit == 0:
                                    LE_rem.append(LE_buf)
                                    LE_buf = ""
                                    flag_zapolneniya_lineEdit = 1
                                else:
                                    if flag_zapolneniya_lineEdit == 2:
                                        LE_rem.append(LE_buf)
                                        LE_buf = ""
                                        flag_zapolneniya_lineEdit = 0
                                    else:
                                        if flag_zapolneniya_lineEdit == 1:
                                            LE_ist_rem.append(LE_ist_buf)
                                            LE_ist_buf = ""
                                            flag_zapolneniya_lineEdit = 2
                                counter += 1
                                No_el_mass += 1
                            else:
                                if SERVER.pocket[counter] == "/" and SERVER.pocket[counter + 1] == "?" and \
                                        SERVER.pocket[
                                            counter + 2] == "/":
                                    counter += 1
                                    counter += 1

                                    if flag_zapolneniya_lineEdit == 1:
                                        LE_ist_buf += SERVER.pocket[counter]
                                    if flag_zapolneniya_lineEdit == 0:
                                        LE_buf += SERVER.pocket[counter]
                                    if flag_zapolneniya_lineEdit == 2:
                                        SP_buf += SERVER.pocket[counter]
                                    FLAG_WHILE = 0
                                    break
                                    # lpo = []
                                    # if LE == lpo:
                                    # break
                                else:
                                    pass

                    counter += 1
                else:
                    break



            print("     stroka_opisaniya", stroka_opisaniya)
            print("     data элементы для диагностики: ",LE,LE_ist,SP)
            print("     data cопутств. элементы: ", LE_soput,LE_ist_soput, SP_soput,LE_ed_soput)
            print("     data элементы для ремонта: ",LE_ist_rem, SP_rem, LE_rem)
            #
            # print("     Личные данные заполняющего",l,p,dol,nomer_zakaza)

            name_of_accFILE = l + "_" + p + "_" + dol
            path = "../SERVER_CHAY/DATABASE/oaccounts/ "
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            print("path1",path)
            with open(path, 'a') as new_accFILE:
                import datetime
                now = str(datetime.datetime.now())
                # 2021-08-06 22:45:02.522446
                year = now[0:4]
                mounth = now[5:7]
                day = now[8:10]
                hour = now[11:13]
                minut = now[14:16]
                times = day +"."+mounth+"."+year+" "+hour+":"+minut
                strs = str(times)+" - Закрывает диагностику заказа №"+str(nomer_zakaza)+"\n"
                new_accFILE.write(strs)


    ######################
            name_of_accFILE = " #" + str(nomer_zakaza).strip()
            path = "../SERVER_CHAY/DATABASE/projects/"
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            print("pathh", path)
            try:
                with open(path, 'r') as proj_file:
                    pass
            except:
                name_of_accFILE = "#" + str(nomer_zakaza).strip()
                path = "../SERVER_CHAY/DATABASE/projects/"
                path.strip()
                path += name_of_accFILE
                path += ".txt"
                print("pathh", path)

            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'w') as buf_file:
                buf_file.write("")

            #меняем статус заказа
            print("per")
            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'a') as buf_file:
                with open(path, 'r') as proj_file:
                    for index,line in enumerate(proj_file):
                        if index < 20:
                            buf_file.write(line)
                        if index == 20:
                            buf_file.write("Ожидание цен закупа\n")
                        if index > 20:
                            buf_file.write(line)
            print("per")

            #перезаписываем файл с учётом эвентов, и запихиваем результаты диагностики
            stri = ""
            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'r') as buf_file:
                with open(path, 'w') as proj_file:
                    proj_file.write("")

                with open(path, 'a') as proj_file:
                    for index, line in enumerate(buf_file):
                        proj_file.write(line)
                    stri += stroka_opisaniya
                    stri += "\n"
                    for i in range(len(LE)):
                        stri += LE[i]
                        stri += "?"
                        stri += LE_ist[i]
                        stri += "?"
                        stri += SP[i]
                        stri += "?"
                    stri += "\n"
                    # SP_soput, LE_ed_soput, LE_soput
                    for i in range(len(LE_soput)):
                        stri += LE_soput[i]
                        stri += "?"
                        stri += LE_ist_soput[i]
                        stri += "?"
                        stri += SP_soput[i]
                        stri += "?"
                        stri += LE_ed_soput[i]
                        stri += "?"
                    stri += "\n"
                    for i in range(len(LE_rem)):

                        stri += LE_ist_rem[i]
                        stri += "?"
                        stri += SP_rem[i]
                        stri += "?"
                        stri += LE_rem[i]
                        stri += "?"
                    stri += "\n"
                    proj_file.write(stri)

                name_of_accFILE = "#" + str(nomer_zakaza).strip() + "#manual"
                path = "../SERVER_CHAY/DATABASE/projects/"
                path.strip()
                path += name_of_accFILE
                path += ".txt"
                try:
                    with open(path, 'r') as proj_file:
                        pass
                except:
                    name_of_accFILE = " #" + str(nomer_zakaza).strip() + "#manual"
                    path = "../SERVER_CHAY/DATABASE/projects/"
                    path.strip()
                    path += name_of_accFILE
                    path += ".txt"
                    # узнаем имя заполнявшего
                immya = ""
                with open("..\SERVER_CHAY\DATABASE\occounts.txt", 'r') as buf_file:

                    for index, line in enumerate(buf_file):
                        if l in line and dol in line:

                            counter = 0
                            while True:
                                if line[counter] != " ":
                                    pass
                                else:
                                    break
                                counter += 1
                            counter += 1
                            while True:
                                if line[counter] != " ":
                                    pass
                                else:
                                    break
                                counter += 1
                            counter += 1
                            while True:
                                if line[counter] != " ":
                                    pass
                                else:
                                    break
                                counter += 1
                            counter += 1
                            while True:
                                if line[counter] != " ":
                                    immya += line[counter]
                                else:
                                    break
                                counter += 1
                            counter += 1
                            immya += " "
                            while True:
                                if line[counter] != " ":
                                    immya += line[counter]
                                else:
                                    break
                                counter += 1
                            counter += 1
                            immya += " "
                            try:
                                while True:
                                    if line[counter] != " ":
                                        immya += line[counter]
                                    else:
                                        break
                                    counter += 1
                            except:
                                pass
                            break
                print("immya", immya)

                with open(path, 'a') as proj_file:
                    import datetime
                    now = str(datetime.datetime.now())
                    # 2021-08-06 22:45:02.522446
                    year = now[0:4]
                    mounth = now[5:7]
                    day = now[8:10]
                    hour = now[11:13]
                    minut = now[14:16]
                    times = day + "." + mounth + "." + year + " " + hour + ":" + minut
                    stri = times + " - Закрывает диагностику заказа " + str(immya)
                    proj_file.write(stri)
    class MEZ():
        def vstupit_v_uzn_cen():
            print("oprst")
            counter = 37
            l = ""
            p = ""
            dol = ""
            nomer_zakaza = ""

            try:
                while True:
                    if SERVER.pocket[counter] != "?":
                        l += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        p += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        dol += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        nomer_zakaza += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
            except:
                pass
            print("lp",l,p,dol,nomer_zakaza)

            name_of_accFILE = l + "_" + p + "_" + dol
            path = "../SERVER_CHAY/DATABASE/oaccounts/ "
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            print("path",path)
            with open(path, 'a') as new_accFILE:
                import datetime
                now = str(datetime.datetime.now())
                # 2021-08-06 22:45:02.522446
                year = now[0:4]
                mounth = now[5:7]
                day = now[8:10]
                hour = now[11:13]
                minut = now[14:16]
                times = day +"."+mounth+"."+year+" "+hour+":"+minut
                strs = str(times)+" - Начал узнавать цены поставщиков деталей заказа №"+str(nomer_zakaza)+"\n"
                new_accFILE.write(strs)

            name_of_accFILE = " #" + str(nomer_zakaza).strip() + "#manual"
            path = "../SERVER_CHAY/DATABASE/projects/"
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            print("path", path)

            with open(path, 'a') as new_accFILE:
                import datetime
                now = str(datetime.datetime.now())
                # 2021-08-06 22:45:02.522446
                year = now[0:4]
                mounth = now[5:7]
                day = now[8:10]
                hour = now[11:13]
                minut = now[14:16]
                times = day + "." + mounth + "." + year + " " + hour + ":" + minut
                # strs = str(times) + " - Узнавать цены поставщиков деталей заказа начал" + " " + l+ " " +dol+ "\n"
                # new_accFILE.write(strs)

            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'w') as buf_file:
                buf_file.write("")

            #узнаем имя заполнявшего
            immya = ""
            with open("..\SERVER_CHAY\DATABASE\occounts.txt", 'r') as buf_file:

                for index,line in enumerate(buf_file):
                    if l in line and dol in line:

                        counter = 0
                        while True:
                            if line[counter] != " ":
                                pass
                            else:
                                break
                            counter+=1
                        counter += 1
                        while True:
                            if line[counter] != " ":
                                pass
                            else:
                                break
                            counter+=1
                        counter += 1
                        while True:
                            if line[counter] != " ":
                                pass
                            else:
                                break
                            counter+=1
                        counter += 1
                        while True:
                            if line[counter] != " ":
                                immya += line[counter]
                            else:
                                break
                            counter+=1
                        counter += 1
                        immya += " "
                        while True:
                            if line[counter] != " ":
                                immya += line[counter]
                            else:
                                break
                            counter+=1
                        counter += 1
                        immya += " "
                        try:
                            while True:
                                if line[counter] != " ":
                                    immya += line[counter]
                                else:
                                    break
                                counter+=1
                        except:
                            pass
                        break
            print("immya",immya)

            #меняем статус заказа
            print("per")
            name_of_accFILE = "#" + str(nomer_zakaza).strip()
            path = "../SERVER_CHAY/DATABASE/projects/"
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            try:
                with open(path, 'r') as proj_file:
                    pass
            except:
                name_of_accFILE = " #" + str(nomer_zakaza).strip()
                path = "../SERVER_CHAY/DATABASE/projects/"
                path.strip()
                path += name_of_accFILE
                path += ".txt"
            print("path", path)
            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'a') as buf_file:
                print("159")
                with open(path, 'r') as proj_file:
                    for index,line in enumerate(proj_file):
                        if index < 20:
                            buf_file.write(line)
                        if index == 20:
                            buf_file.write("Цены закупа в процессе\n")
                        if index > 20:
                            buf_file.write(line)
                    j = immya
                    buf_file.write(j)
            #перезаписываем файл с учётом эвентов, и запихиваем результаты диагностики
            stri = ""
            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'r') as buf_file:
                with open(path, 'w') as proj_file:
                    proj_file.write("")

                with open(path, 'a') as proj_file:
                    for index, line in enumerate(buf_file):
                        proj_file.write(line)
            name_of_accFILE = "#" + str(nomer_zakaza).strip() + "#manual"
            path = "../SERVER_CHAY/DATABASE/projects/"
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            try:
                with open(path, 'r') as proj_file:
                    pass
            except:
                name_of_accFILE = " #" + str(nomer_zakaza).strip() + "#manual"
                path = "../SERVER_CHAY/DATABASE/projects/"
                path.strip()
                path += name_of_accFILE
                path += ".txt"
            with open(path, 'a') as proj_file:
                import datetime
                now = str(datetime.datetime.now())
                # 2021-08-06 22:45:02.522446
                year = now[0:4]
                mounth = now[5:7]
                day = now[8:10]
                hour = now[11:13]
                minut = now[14:16]
                times = day + "." + mounth + "." + year + " " + hour + ":" + minut
                stri = times + " - Узнавать цены поставщиков деталей заказа начинает " + immya
                proj_file.write(stri)
        def zakrit_uzn_cen():
            counter = 37
            l = ""
            p = ""
            dol = ""
            nomer_zakaza = ""
            pocket = ""

            try:
                while True:
                    if SERVER.pocket[counter] != "?":
                        l += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        p += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        dol += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    if SERVER.pocket[counter] != "?":
                        nomer_zakaza += SERVER.pocket[counter]
                    else:
                        break
                    counter += 1
                counter += 1
                while True:
                    try:
                        pocket += SERVER.pocket[counter]
                        counter += 1
                    except:
                        break

                print("     Личные данные заполняющего:")
                print("         log:", l)
                print("         par:", p)
                print("         dol:", dol)
                print("         nom:", nomer_zakaza)
                print("     Данные о ценах:")
                print("         pocket:", pocket)
            except:
                pass
            name_of_accFILE = l + "_" + p + "_" + dol
            path = "../SERVER_CHAY/DATABASE/oaccounts/ "
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            print("path1",path)
            with open(path, 'a') as new_accFILE:
                    import datetime
                    now = str(datetime.datetime.now())
                    # 2021-08-06 22:45:02.522446
                    year = now[0:4]
                    mounth = now[5:7]
                    day = now[8:10]
                    hour = now[11:13]
                    minut = now[14:16]
                    times = day +"."+mounth+"."+year+" "+hour+":"+minut
                    strs = str(times)+" - Закрывает выяснение цен заказа №"+str(nomer_zakaza)+"\n"
                    new_accFILE.write(strs)


        ######################
            name_of_accFILE = " #" + str(nomer_zakaza).strip()
            path = "../SERVER_CHAY/DATABASE/projects/"
            path.strip()
            path += name_of_accFILE
            path += ".txt"
            print("pathh", path)
            try:
                with open(path, 'r') as proj_file:
                    pass
            except:
                name_of_accFILE = "#" + str(nomer_zakaza).strip()
                path = "../SERVER_CHAY/DATABASE/projects/"
                path.strip()
                path += name_of_accFILE
                path += ".txt"
                print("pathh", path)

            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'w') as buf_file:
                buf_file.write("")

            #меняем статус заказа
            print("per")
            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'a') as buf_file:
                with open(path, 'r') as proj_file:
                    for index,line in enumerate(proj_file):
                        print("lll",line)
                        if index < 20:
                            buf_file.write(line)
                        if index == 20:
                            buf_file.write("Ожидание согласования\n")
                        if index > 20:
                            buf_file.write(line)
            print("per")

            #перезаписываем файл с учётом эвентов, и запихиваем результаты диагностики
            stri = ""
            with open("..\SERVER_CHAY\DATABASE\projects\ofile_buf_for_send_all_files.txt", 'r') as buf_file:
                with open(path, 'w') as proj_file:
                    proj_file.write("")

                with open(path, 'a') as proj_file:
                    for index, line in enumerate(buf_file):
                        print("itss: ",line)
                        proj_file.write(line)
                    proj_file.write(pocket)

                name_of_accFILE = "#" + str(nomer_zakaza).strip() + "#manual"
                path = "../SERVER_CHAY/DATABASE/projects/"
                path.strip()
                path += name_of_accFILE
                path += ".txt"
                try:
                    with open(path, 'r') as proj_file:
                        pass
                except:
                    name_of_accFILE = " #" + str(nomer_zakaza).strip() + "#manual"
                    path = "../SERVER_CHAY/DATABASE/projects/"
                    path.strip()
                    path += name_of_accFILE
                    path += ".txt"
                    # узнаем имя заполнявшего
                immya = ""
                with open("..\SERVER_CHAY\DATABASE\occounts.txt", 'r') as buf_file:

                    for index, line in enumerate(buf_file):
                        if l in line and dol in line:

                            counter = 0
                            while True:
                                if line[counter] != " ":
                                    pass
                                else:
                                    break
                                counter += 1
                            counter += 1
                            while True:
                                if line[counter] != " ":
                                    pass
                                else:
                                    break
                                counter += 1
                            counter += 1
                            while True:
                                if line[counter] != " ":
                                    pass
                                else:
                                    break
                                counter += 1
                            counter += 1
                            while True:
                                if line[counter] != " ":
                                    immya += line[counter]
                                else:
                                    break
                                counter += 1
                            counter += 1
                            immya += " "
                            while True:
                                if line[counter] != " ":
                                    immya += line[counter]
                                else:
                                    break
                                counter += 1
                            counter += 1
                            immya += " "
                            try:
                                while True:
                                    if line[counter] != " ":
                                        immya += line[counter]
                                    else:
                                        break
                                    counter += 1
                            except:
                                pass
                            break
                print("immya", immya)
                with open(path, 'a') as proj_file:
                    import datetime
                    now = str(datetime.datetime.now())
                    # 2021-08-06 22:45:02.522446
                    year = now[0:4]
                    mounth = now[5:7]
                    day = now[8:10]
                    hour = now[11:13]
                    minut = now[14:16]
                    times = day + "." + mounth + "." + year + " " + hour + ":" + minut
                    stri = times + " - Узнавать цены поставщиков деталей заказа заканчивает " + immya
                    proj_file.write(stri)

#class of menegment behind new-reg accouts
class CREATE_NEW_ACCOUNT():
    input_str = ""
    def moder_NOT():
        with open("..\SERVER_CHAY\DATABASE\onew_accounts.txt", 'r') as new_acc:
            for index, line in enumerate(new_acc):
                if line.strip() == CREATE_NEW_ACCOUNT.input_str:
                    print("flag")
                else:
                    print("ooo")
                    with open("..\SERVER_CHAY\DATABASE\onew_acc_buf.txt", 'a') as new_acc_buff:
                        new_acc_buff.write(line)
        with open("..\SERVER_CHAY\DATABASE\onew_accounts.txt", 'w') as new_acc:
            new_acc.write("")

        with open("..\SERVER_CHAY\DATABASE\onew_accounts.txt", 'a') as new_acc:
            with open("..\SERVER_CHAY\DATABASE\onew_acc_buf.txt", 'r') as new_acc_buff:
                for index, line in enumerate(new_acc_buff):
                    new_acc.write(line)
        with open("..\SERVER_CHAY\DATABASE\onew_acc_buf.txt", 'w') as new_acc:
            new_acc.write("")
    def moder_OK():
        with open("..\SERVER_CHAY\DATABASE\onew_accounts.txt", 'r') as new_acc:
            for index, line in enumerate(new_acc):
                if line.strip() == CREATE_NEW_ACCOUNT.input_str:
                    flag = 1
                    with open("..\SERVER_CHAY\DATABASE\occounts.txt", 'r') as acc:
                        for index1, line1 in enumerate(acc):
                            if line1.strip() == CREATE_NEW_ACCOUNT.input_str:
                                flag = 0
                                break
                    if flag == 1:
                        with open("..\SERVER_CHAY\DATABASE\occounts.txt", 'a') as acc:
                            input_str_norm_format = ""
                            login = ""
                            parol = ""
                            dolg = ""
                            FIO = ""

                            counter = 0
                            # day,mounth,year
                            while True:
                                if CREATE_NEW_ACCOUNT.input_str[counter] != " ":
                                    pass
                                else:
                                    break
                                counter += 1
                            counter += 1
                            #hour and minutes
                            while True:
                                if CREATE_NEW_ACCOUNT.input_str[counter] != "?":
                                    pass
                                else:
                                    break
                                counter += 1

                            if "name" == "name":
                                counter += 1
                                # familiya
                                while True:
                                    if CREATE_NEW_ACCOUNT.input_str[counter] != " ":
                                        FIO += CREATE_NEW_ACCOUNT.input_str[counter]
                                        # print("fam:  ", CREATE_NEW_ACCOUNT.input_str[counter])
                                    else:
                                        break
                                    counter += 1

                                counter += 1
                                FIO += " "
                                # imya
                                while True:
                                    if CREATE_NEW_ACCOUNT.input_str[counter] != " ":
                                        FIO += CREATE_NEW_ACCOUNT.input_str[counter]
                                        # print("imi:  ", CREATE_NEW_ACCOUNT.input_str[counter])
                                    else:
                                        break
                                    counter += 1
                                counter += 1
                                FIO += " "
                                # otch
                                while True:
                                    if CREATE_NEW_ACCOUNT.input_str[counter] != "?":
                                        FIO += CREATE_NEW_ACCOUNT.input_str[counter]
                                        # print("otch:  ", CREATE_NEW_ACCOUNT.input_str[counter])
                                    else:
                                        break
                                    counter += 1
                            print("fio: ", FIO)

                            counter += 1
                            while True:
                                if CREATE_NEW_ACCOUNT.input_str[counter] != "?":
                                    dolg += CREATE_NEW_ACCOUNT.input_str[counter]
                                    # print("otch:  ", CREATE_NEW_ACCOUNT.input_str[counter])
                                else:
                                    break
                                counter += 1
                            print("dolg: ", dolg)

                            counter += 1
                            while True:
                                if CREATE_NEW_ACCOUNT.input_str[counter] != "?":
                                    login += CREATE_NEW_ACCOUNT.input_str[counter]
                                    # print("otch:  ", CREATE_NEW_ACCOUNT.input_str[counter])
                                else:
                                    break
                                counter += 1
                            print("login: ", login)

                            try:
                                counter += 1
                                while True:
                                    if CREATE_NEW_ACCOUNT.input_str[counter] != "\n":
                                        parol += CREATE_NEW_ACCOUNT.input_str[counter]
                                        # print("otch:  ", CREATE_NEW_ACCOUNT.input_str[counter])
                                    else:
                                        break
                                    counter += 1

                            except:
                                print("parol: ", parol)
                                pass

                            name_of_accFILE = login + "_" +parol+ "_"+dolg
                            path = "..\SERVER_CHAY\DATABASE\oaccounts\ "
                            path += name_of_accFILE
                            path += ".txt"
                            with open(path, 'w') as new_accFILE:
                                new_accFILE.write("")

                            input_str_norm_format = login + " " + parol + " " + dolg + " " + FIO + "\n"
                            acc.write(input_str_norm_format)
        CREATE_NEW_ACCOUNT.moder_NOT()
#class of menegment behind new-name projects
class CREATE_NEW_PROJECTS():
    ##################INPUT DATA#####################
    input_name_of_file = ""
    def non_rename():
        import os
        directory = '..\SERVER_CHAY\DATABASE\projects'
        files = os.listdir(directory)
        flag = 1
        for file in files:
            if file == CREATE_NEW_PROJECTS.input_name_of_file:
                SERVER.client_now.sendall(b"bad_name_pls_rename")
                return
        SERVER.client_now.sendall(b"ok_name")

if __name__ == "__main__":
    # SERVER.SEND_PROJECTS()
    # CREATE_NEW_ACCOUNT.moder_OK()
    SERVER.__init__()





