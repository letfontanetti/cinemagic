from Modulos import *

#deixa q janela2 visivel
def open2 ():
    Janela.deiconify

def btnsessao():
    pass

Janela = CriarJanela("Filmes em Cartaz", "800x700", 2)
Janela.configure(fg_color='#f5f5f5')

#           FRAME 1 - HEADER
frame1 = CriarFrame(Janela,0,0,800,50)
frame1.grid(columnspan=13)
frame1.configure(fg_color="#A40000", corner_radius=0)

frase1 = CriarLabel(frame1, 'O melhor do cinema aguarda você!', 5,6)
frase1.configure(font=('inria sans', 13),text_color='white', )

frase2 = CriarLabel(Janela, 'Selecione uma poltrona para comprar seu ingresso', 1,4)
frase2.configure(font=('inria sans', 10),text_color='#4E5B60')

imagemfilme = CriarImagem(Janela,"image/image2.png",2,3,150,100)
imagemfilme.grid(sticky="E")

frame2 = CriarFrame(Janela,2,4,500,150)
frame2.grid(columnspan=13)
frame2.configure(fg_color="#A40000", corner_radius=0)

titulo = CriarLabel(frame2, 'Som da Liberdade                          ', 0,0)
titulo.configure(font=('inria sans', 12, 'bold'),text_color='white')

subtitulo = CriarLabel(frame2, '2D LEGENDADO - SALA 3                ', 1,0)
subtitulo.configure(font=('inria sans', 12),text_color='white')

subtitulo1 = CriarLabel(frame2, 'Cineflix Shopping Praça Nova Araçatuba', 10,0)
subtitulo1.configure(font=('inria sans', 12),text_color='white')

subtitulo2 = CriarLabel(frame2, 'Data: Hoje 27/10/2023 - 19:00               ', 11,0)
subtitulo2.configure(font=('inria sans', 12),text_color='white')

#           Seleção das cadeiras
selecao = CriarCaixaDeTexto(frame2,200, 30, 13, 3, 'Selecione...')
tituloS = CriarLabel(frame2,'Escolha seu lugar:',12,3)

trocarsessao = CriarBotão(frame2, "Trocar sessão", btnsessao, 12, 0, 30, 20, "#E9A802" )
trocarsessao.grid(sticky="W")

comprar = CriarBotão(frame2, "Comprar", btnsessao, 0, 12, 30, 20, "#E9A802" )

imagemcadeiras = CriarImagem(Janela,"image/imagemcadeiras.png",5,4,350,450)

Janela.mainloop()