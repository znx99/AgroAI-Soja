def randow_image():
    numero = 1
    for i in range(896):
        try:
            sleep(0.5)
            label_imagem.configure(image=None)
            label_imagem.image = None
            sleep(0.5)
            
            # Verifique se o caminho está correto ou ajuste conforme necessário
            image_path = os.path.join("Planta Saudavel-20250612T104253Z-1-001", f"healthy ({numero}).jpg")
            
            if not os.path.exists(image_path):
                print(f"Arquivo não encontrado: {image_path}")
                break
                
            nova_imagem = Image.open(image_path)
            nova_imagem = nova_imagem.resize((300, 200), Image.LANCZOS)
            imagem_tk = ImageTk.PhotoImage(nova_imagem)
            label_imagem.configure(image=imagem_tk)
            label_imagem.image = imagem_tk
            numero += 1
            
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            break