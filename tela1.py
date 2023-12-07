import customtkinter as Tk
from Modulos import *

one = False
two = False

Janela = CriarJanela("Filmes em Cartaz", "700x600", 1)
Janela.configure(fg_color='Black')

#         FRAME 1 - HEADER
frame1 = CriarFrame(Janela,0,0,700,100)
frame1.grid(columnspan=13)
frame1.configure(fg_color='#A40000', corner_radius=0)
logo = CriarImagem(frame1,"image/imgofc.png",0,0,100,100)

frame2 = CriarFrameScrool(Janela, 1, 6, 700, 600)
frame2.configure(corner_radius=0)


#          FRAME 2 - FILMES
filmes = CriarLabel(frame2, 'Filmes - Cinemagic', 1,2)
filmes.configure(font=('arial', 20, 'bold'),text_color='#DAA520')

cartaz = CriarLabel(frame2,'Em Cartaz', 2,1)
cartaz.configure(font=('arial', 15, 'bold'), text_color='#A40000')

breve = CriarLabel(frame2,'Em Breve', 2,2)
breve.configure(font=('arial', 15, 'bold'),text_color='white')

#           FRAME 3 - FILME1(RESISTÊNCIA)
imagem = CriarImagem(frame2,"image/image3.png",3,1,200,150)
tfilme1 = CriarLabel(frame2,'Resistência',3,2)
tfilme1.configure(font=('arial', 18, 'bold'))

inform1 = CriarLabel(frame2,'Ficção',3,3)
inform1.configure(font=('arial', 16))

inform2 = CriarLabel(frame2,'2h13',3,4)
inform2.configure(font=('arial', 16))


#            SESSÕES/SOBRE O FILME1
inform3 = CriarLabel(frame2, 'Sessões',4,1)
inform3.configure(font=('arial', 16))

inform4 = CriarLabel(frame2, 'Sobre o filme',4,2)
inform4.configure(font=('arial', 16), text_color='#DAA520')

#             FRAME 4 - RESUMO DO FILME1
frame4 = CriarFrame(frame2,5,0,600,100)
frame4.grid(columnspan=13)
frame4.configure(fg_color="#363636", corner_radius=10)

resumof = CriarLabel(frame4, 'Em meio a uma futura guerra entre a raça humana e as forças da inteligência artificial,\n Joshua, um endurecido ex-agente das forças especiais que lamenta o desaparecimento\n de sua esposa, é recrutado para caçar e matar o Criador, o indescritível arquiteto da\nIA avançada que desenvolveu uma arma misteriosa com o poder de\nacabar com a guerra - e a própria humanidade.', 5,0)
resumof.configure(font=('arial', 15), corner_radius=10)

#             FRAME 5 - FILME2(SOM DA LIBERDADE)
espaco = CriarLabel(frame2,'',6,1)
imagem1 = CriarImagem(frame2,"image/image2.png",7,1,200,150)

tfilme2 = CriarLabel(frame2,'Som da liberdade',7,2)
tfilme2.configure(font=('arial', 18, 'bold'))

inform5 = CriarLabel(frame2,'Ação, Drama',7,3)
inform5.configure(font=('arial', 16))

inform6 = CriarLabel(frame2,'2h11',7,4)
inform6.configure(font=('arial', 16))

inform7 = CriarLabel(frame2, 'Sessões',8,1)
inform7.configure(font=('arial', 16), text_color='#DAA520')

inform8 = CriarLabel(frame2, 'Sobre o filme',8,2)
inform8.configure(font=('arial', 16))

#               FRAME 6 - SESSÕES FILME2

#váriaveis 'one' e 'two' para declarar se os dois botões foram selecionados
#se forem selecionados são definidos como verdadeiro
def clique(num = 1):
    #one e two são globais(podem ser acessadas e modificadas em qualquer parte do programa)
    global one
    global two
    if num == 1:
        one = True
    if num == 2:
        two = True
    print(one)
    print(two)
#deixa a janela1 invisivel e a 2 visivel
    if one and two:
        one = False
        two = False
        from tela2 import open2
        Janela.withdraw()
        open2()
#se ambos os botões foram clicados, a função esconde a janela atual e chama a função open2 do módulo tela2.

sessao1 = Tk.CTkButton(frame2, text='Sexta-feira - 27/10', command=clique,width=100,height=40,fg_color='#A40000',hover_color='#DAA520',text_color='White')
sessao1.grid(row=9,column=1)

sessao2 = Tk.CTkButton(frame2, text='Sabádo - 28/10', command=clique,width=100,height=40,fg_color='#A40000',hover_color='#DAA520',text_color='White')
sessao2.grid(row=9,column=2)

sessao3 = Tk.CTkButton(frame2, text='Domingo - 29/10', command=clique,width=100,height=40,fg_color='#A40000',hover_color='#DAA520',text_color='White')
sessao3.grid(row=9,column=3)

espaco1 = CriarLabel(frame2,'',10,1)

#lambda é uma função anonima que permite passar um parametro em um botão
horario1 = Tk.CTkButton(frame2, text='1º horário: 16h15', command=lambda :clique(2),width=100,height=40,fg_color='#DAA520',hover_color='#A40000',text_color='White')
horario1.grid(row=11,column=1)

horario2 = Tk.CTkButton(frame2, text='2º horário: 19h00', command=lambda :clique(2),width=100,height=40,fg_color='#DAA520',hover_color='#A40000',text_color='White')
horario2.grid(row=11,column=2)

Janela.mainloop()