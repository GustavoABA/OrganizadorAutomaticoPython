import os
import time

# ________ ___  ___  ________   ________  ________      
#|\  _____\\  \|\  \|\   ___  \|\   ____\|\   ____\     
#\ \  \__/\ \  \\\  \ \  \\ \  \ \  \___|\ \  \___|_    
# \ \   __\\ \  \\\  \ \  \\ \  \ \  \    \ \_____  \   
#  \ \  \_| \ \  \\\  \ \  \\ \  \ \  \____\|____|\  \  
#   \ \__\   \ \_______\ \__\\ \__\ \_______\____\_\  \ 
#    \|__|    \|_______|\|__| \|__|\|_______|\_________\
#                                           \|_________|
def CriarPastas(PastaAtual,NomePasta):
    print("Chamando Funação Criar Pasta")
    DentroPastaAtual= os.path.join(PastaAtual,NomePasta) #criamos o caminho
    time.sleep(0.3)
    if not os.path.exists(DentroPastaAtual):
        print(DentroPastaAtual)
        os.mkdir(path=DentroPastaAtual)
# ________  ________  ________  ________  _______   ________   ________  ________     
#|\   __  \|\   __  \|\   __  \|\   ____\|\  ___ \ |\   ____\ |\   ____\|\   __  \    
#\ \  \|\  \ \  \|\  \ \  \|\  \ \  \___|\ \   __/|\ \  \___|_\ \  \___|\ \  \|\  \   
# \ \   ____\ \   _  _\ \  \\\  \ \  \    \ \  \_|/_\ \_____  \\ \_____  \ \  \\\  \  
#  \ \  \___|\ \  \\  \\ \  \\\  \ \  \____\ \  \_|\ \|____|\  \\|____|\  \ \  \\\  \ 
#   \ \__\    \ \__\\ _\\ \_______\ \_______\ \_______\____\_\  \ ____\_\  \ \_______\
#    \|__|     \|__|\|__|\|_______|\|_______|\|_______|\_________\\_________\|_______|
#                                                     \|_________\|_________|         
class Organizar:
    def __init__(self,PastaParaOrganizar):
        self.PastaParaOrganizar = PastaParaOrganizar
        
    def OrganizarPasta(self):
        print("Começando Processo de organização")
# ________  ________  ___  ________  ________     
#|\   ____\|\   __  \|\  \|\   __  \|\   __  \    
#\ \  \___|\ \  \|\  \ \  \ \  \|\  \ \  \|\  \   
# \ \  \    \ \   _  _\ \  \ \   __  \ \   _  _\  
#  \ \  \____\ \  \\  \\ \  \ \  \ \  \ \  \\  \| 
#   \ \_______\ \__\\ _\\ \__\ \__\ \__\ \__\\ _\ 
#    \|_______|\|__|\|__|\|__|\|__|\|__|\|__|\|__|
        PastaAtual = os.path.join(self.PastaParaOrganizar, "Organizar")
        time.sleep(0.3)    
        if not os.path.exists(PastaAtual):
            print("Criando Pasta para organizar")
            os.mkdir(path=PastaAtual)
            time.sleep(0.3)    
            #já dentro da pasta Organizar
            CriarPastas(PastaAtual,"Imagens")
            time.sleep(0.3)    
            CriarPastas(PastaAtual,"Videos")
            time.sleep(0.3)    
            CriarPastas(PastaAtual,"Verificar")
            time.sleep(0.3)    
            CriarPastas(PastaAtual,"Docs")
# _________  ________  _____ ______   ________  ________   ___  ___  ________     
#|\___   ___\\   __  \|\   _ \  _   \|\   __  \|\   ___  \|\  \|\  \|\   __  \    
#\|___ \  \_\ \  \|\  \ \  \\\__\ \  \ \  \|\  \ \  \\ \  \ \  \\\  \ \  \|\  \   
#     \ \  \ \ \   __  \ \  \\|__| \  \ \   __  \ \  \\ \  \ \   __  \ \  \\\  \  
#      \ \  \ \ \  \ \  \ \  \    \ \  \ \  \ \  \ \  \\ \  \ \  \ \  \ \  \\\  \ 
#       \ \__\ \ \__\ \__\ \__\    \ \__\ \__\ \__\ \__\\ \__\ \__\ \__\ \_______\
#        \|__|  \|__|\|__|\|__|     \|__|\|__|\|__|\|__| \|__|\|__|\|__|\|_______|
        ArquivosPasta = os.listdir(self.PastaParaOrganizar)
        print("Verificando Tamanhos")
        for ItemDaPasta in ArquivosPasta:
            nome , extencao = os.path.splitext(ItemDaPasta)
            origem = os.path.join(self.PastaParaOrganizar, ItemDaPasta)
            tamanho = os.path.getsize(origem)
            time.sleep(0.3)
            print(f"O tamanho é: {tamanho} Bytes")
            if tamanho > 1048576: # verificamos por gigabyte 1 GB = 1.024 × 1.024 × 1.024 = 1.048.576 KB
                print(f"Arquivo grande detectado {origem} necessario verificação de usuario")
                destino = os.path.join(self.PastaParaOrganizar,"Organizar" ,"Verificar", ItemDaPasta)
                try:
                    os.rename(origem, destino)
                    print(f"{ItemDaPasta} -> {destino}")
                except FileExistsError:
                    nomeAntigo, ext = os.path.splitext(ItemDaPasta)
                    NovoNome = "{nomeAntigo}_Copia{ext}"
                    os.rename(origem, NovoNome)
                    print(f"{ItemDaPasta} já existia. Renomeado para: {NovoNome}")
                except Exception as e:
                    print(f"Erro, seguindo para o proximo")
                    pass
# ________  ________  ________  ________  ________   ___  ________  ________  ________     
#|\   __  \|\   __  \|\   ____\|\   __  \|\   ___  \|\  \|\_____  \|\   __  \|\   __  \    
#\ \  \|\  \ \  \|\  \ \  \___|\ \  \|\  \ \  \\ \  \ \  \\|___/  /\ \  \|\  \ \  \|\  \   
# \ \  \\\  \ \   _  _\ \  \  __\ \   __  \ \  \\ \  \ \  \   /  / /\ \   __  \ \   _  _\  
#  \ \  \\\  \ \  \\  \\ \  \|\  \ \  \ \  \ \  \\ \  \ \  \ /  /_/__\ \  \ \  \ \  \\  \| 
#   \ \_______\ \__\\ _\\ \_______\ \__\ \__\ \__\\ \__\ \__\\________\ \__\ \__\ \__\\ _\ 
#    \|_______|\|__|\|__|\|_______|\|__|\|__|\|__| \|__|\|__|\|_______|\|__|\|__|\|__|\|__|

        for ItemDaPasta in ArquivosPasta:
            origem = os.path.join(self.PastaParaOrganizar, ItemDaPasta)
            
            nome , extencao = os.path.splitext(ItemDaPasta)
            
            match extencao:


                case ".png" | ".jpg" | ".jpeg" | ".gif" | ".bmp" | ".webp" | ".tiff" | ".svg" | ".ico" | ".heic":
                    time.sleep(0.2)
                    destino = os.path.join(self.PastaParaOrganizar,"Organizar" ,"Imagens", ItemDaPasta)
                    try:
                        os.rename(origem, destino)
                        print(f"{ItemDaPasta} -> {destino}")
                    except FileExistsError:
                        nomeAntigo, ext = os.path.splitext(ItemDaPasta)
                        NovoNome = "{nomeAntigo}_Copia{ext}"
                        os.rename(origem, NovoNome)
                        print(f"{ItemDaPasta} já existia. Renomeado para: {NovoNome}")
                    except Exception as e:
                        print(f"Erro, seguindo para o proximo")
                        pass



                case ".mp4" | ".mkv" | ".avi" | ".mov" | ".wmv" | ".flv" | ".webm" | ".m4v" | ".mpeg" | ".mpg" | ".3gp":
                    time.sleep(0.2)
                    destino = os.path.join(self.PastaParaOrganizar,"Organizar" ,"Videos", ItemDaPasta)
                    try:
                        os.rename(origem, destino)
                        print(f"{ItemDaPasta} -> {destino}")
                    except FileExistsError:
                        nomeAntigo, ext = os.path.splitext(ItemDaPasta)
                        NovoNome = "{nomeAntigo}_Copia{ext}"
                        os.rename(origem, NovoNome)
                        print(f"{ItemDaPasta} já existia. Renomeado para: {NovoNome}")
                    except Exception as e:
                        print(f"Erro, seguindo para o proximo")
                        pass


                case _:
                    time.sleep(0.2)
                    destino = os.path.join(self.PastaParaOrganizar,"Organizar" ,"Docs", ItemDaPasta)
                    try:
                        os.rename(origem, destino)
                        print(f"{ItemDaPasta} -> {destino}")
                    except FileExistsError:
                        nomeAntigo, ext = os.path.splitext(ItemDaPasta)
                        NovoNome = "{nomeAntigo}_Copia{ext}"
                        os.rename(origem, NovoNome)
                        print(f"{ItemDaPasta} já existia. Renomeado para: {NovoNome}")
                    except Exception as e:
                        print(f"Erro, seguindo para o proximo")
                        pass