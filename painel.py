#Comando para ativar a venv .\tf_env2\Scripts\activate

import customtkinter as ctk 
import customtkinter
from tkinter import filedialog
from main import main
import sys, os
from PIL import Image, ImageTk
import threading
from time import sleep
from tkinter import messagebox
import random

caminho_arquivo = None
#Função resource_path
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
#Função para coletar o arquivo da imagem
def selecionar_arquivo():
    # Abre a janela para seleção de arquivo
    global caminho_arquivo
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=(("Arquivos jpg", "*.jpg"), ("Todos os arquivos", "*.*"))
    )
    
    # Verifica se um arquivo foi selecionado
    if caminho_arquivo:
        print(caminho_arquivo)
        nova_imagem = Image.open(caminho_arquivo)
        nova_imagem = nova_imagem.resize((312, 280), Image.LANCZOS)
        imagem_tk = ImageTk.PhotoImage(nova_imagem)
        label_image_frame.configure(image=imagem_tk)
    else:
        messagebox.showerror("Selecione o Arquivo", "Você não selecionou o arquivo!")
    
#Função de imagens
stop_event = False

def randow_image():
    global stop_event
    while stop_event == False:
        numero = random.randint(1, 153)
        label_imagem.configure(image=None)
        label_imagem.image = None
        nova_imagem = Image.open(f"Imagens/healthy ({numero}).jpg")
        nova_imagem = nova_imagem.resize((312, 280), Image.LANCZOS)
        imagem_tk = ImageTk.PhotoImage(nova_imagem)
        label_imagem.configure(image=imagem_tk)
        label_imagem.image = imagem_tk
        
            
#O comando abaixo server para compilar o arquivo em um executavel
#python -m PyInstaller --clean --noconfirm main.spec
#Função de scanear imagem
def scan_image():
    button_scan.configure(state="disabled")
    global stop_event
    label_doente.configure(text="")
    label_healtly.configure(text="")
    print(caminho_arquivo)
    #Criando a animação das imagens
    if stop_event == False:
        thread = threading.Thread(target=randow_image)
        thread.start()
    else:
        stop_event = False
        thread = threading.Thread(target=randow_image)
        thread.start()
    #Iniciando scaneamento
    result = None
    label_result.configure(text="Verificando padrões visuais...")
    def ai_scan():
        global result
        global stop_event
        result = main(image_path=caminho_arquivo)
        print(result)  
        if str(result).startswith("0"):
            label_result.configure(text="")
            label_doente.configure(text="Planta Doente!")

        elif str(result).startswith("1"):
            label_result.configure(text="")
            label_healtly.configure(text="Planta saudável!")

        
        stop_event = True
        label_imagem.configure(image=None)
        label_imagem.image = None
        nova_imagem = Image.open(f"plant-logo-icon-design-free-vector.jpg")
        nova_imagem = nova_imagem.resize((312, 280), Image.LANCZOS)
        imagem_tk = ImageTk.PhotoImage(nova_imagem)
        label_imagem.configure(image=imagem_tk)
        label_imagem.image = imagem_tk
        button_scan.configure(state="normal")

        
    thread_scan = threading.Thread(target=ai_scan)
    thread_scan.start()
    


#Definindo janella
janella = ctk.CTk()
#Definindo o titulo da janella
janella.title("Painel da IA")
#Definindo tipos de fontes
fonte_arial_negrito_25 = customtkinter.CTkFont('Arial', 25, 'bold')
fonte_arial_negrito_18 = customtkinter.CTkFont('Arial', 18, 'bold')
fonte_arial_12 = customtkinter.CTkFont('Arial', 12)
fonte_arial_negrito_12 = customtkinter.CTkFont('Arial', 12, 'bold')
fonte_arial_negrito_15 = customtkinter.CTkFont('Arial', 15, 'bold')

#Definindo o icone da janella
#icon_path = resource_path("vector-soil-plant-icon (1).ico")
#janella.iconbitmap(icon_path)
#Definindo valores X e Y
valorY = 400
valorX = 700
janella.minsize(valorX, valorY)
janella.maxsize(valorX, valorY)
#Definindo o protocolo do onclosing
def on_closing():
    if messagebox.askokcancel("Sair", "Deseja realmente sair do programa?"):
        # Para o cronômetro se estiver rodando
        # Encerra todas as threads (se necessário)
        for thread in threading.enumerate():
            if thread != threading.main_thread():
                thread.join(timeout=0.1)
        
        # Fecha a janela principal
        janella.destroy()
        # Encerra o programa
        sys.exit(0)

janella.protocol("WM_DELETE_WINDOW", on_closing)
###################

#Definindo variaveis da tela AI
title_plant_scan = ctk.CTkLabel(janella, text="PlantScan", font=fonte_arial_negrito_18)
frame_left = ctk.CTkFrame(janella, height=300, width=335,corner_radius=10)
frame_right = ctk.CTkFrame(janella, height=300, width=335, corner_radius=10)
label_result = ctk.CTkLabel(janella, text=" ", font=fonte_arial_negrito_18)
label_healtly = ctk.CTkLabel(janella, text=" ", font= fonte_arial_negrito_18)
label_doente = ctk.CTkLabel(janella, text=" ", font=fonte_arial_negrito_18)

#Carregando imagem
nova_imagem = Image.open(f"plant-logo-icon-design-free-vector.jpg")
nova_imagem = nova_imagem.resize((312, 280), Image.LANCZOS)
imagem_tk = ImageTk.PhotoImage(nova_imagem)

#Definindo os elementos do frame primario da tela AI
label_imagem = ctk.CTkLabel(frame_left, image=imagem_tk, text="")

#Definindo os elementos do frame secundario da tela AI
label_arquivo = ctk.CTkLabel(frame_right, text='Selecione um aquivo:', font=fonte_arial_negrito_18)
button_Select = ctk.CTkButton(frame_right, text="Selecionar", font=fonte_arial_negrito_18, width=100, corner_radius=10, command=selecionar_arquivo)
frame_image = ctk.CTkFrame(frame_right, width=310, height=200, corner_radius=10)
button_scan = ctk.CTkButton(frame_right, text="Scanear", corner_radius=10, command=scan_image)

#Definindo os elementos do frame da image
label_image_frame = ctk.CTkLabel(frame_image, text="")
###################

#Posicionando elementos da tela AI
title_plant_scan.grid(row=0, column=0, padx=307, pady=10, sticky='w')
frame_left.grid(row=1, column=0,padx=10, pady=0, sticky="w")   
frame_right.grid(row=1, column=0,padx=355, pady=0, sticky="w")
label_result.grid(row=2, column=0, padx=200, pady=0, sticky="w")
label_healtly.grid(row=2, column=0, padx=285, pady=0, sticky="w")
label_doente.grid(row=2, column=0, padx=290, pady=0, sticky="w")
#Posicionando os elementos do frame primario
label_imagem.grid(row=0, column=0, padx=10,pady=10, sticky="w")

#Posicionando os elementos do frame secundario
label_arquivo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
button_Select.grid(row=0, column=0, padx=210, pady=10, sticky="w")
frame_image.grid(row=1, column=0, padx=10, pady=0, sticky="w")
button_scan.grid(row=2, column=0, padx=100, pady=10, sticky="w")

#Posicionando os elementos do frame da image
label_image_frame.grid(row=1, column=0, padx=0, pady=0, sticky="w")

#Bloqueando o grid
frame_left.grid_propagate(False)
frame_right.grid_propagate(False)
frame_image.grid_propagate(False)



#Iniciando o loop
janella.mainloop()
#main(image_path="healthy (1).png")

