from tkinter import Tk, IntVar, StringVar
from tkinter.ttk import Frame, Label, Entry, Button, Checkbutton


class Contato:
    def __init__(self, nome, telefone, email, preferencial):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.preferencial = preferencial

    def salvar(self) -> None:
        with open("contatos.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.write(
                f"{self.nome},{self.telefone},{self.email},{self.preferencial}"
            )

    def validar(self, alertar) -> bool:
        if len(self.nome) == 0 or self.nome.isspace():
            alertar("Nome inválido!")

            return False

        if not str(self.telefone).isdigit():
            alertar("Telefone inválido!")

            return False

        if "@" not in self.email or "." not in self.email:
            alertar("E-mail inválido!")

            return False

        return True


window = Tk()

window.title("Agenda")
window.geometry("450x450")
window.resizable(0, 0)

frame = Frame(window, padding=30)
frame.pack()

nome = StringVar()
telefone = StringVar()
email = StringVar()
preferencial = IntVar()

nome_label = Label(frame, text="Nome:")
telefone_label = Label(frame, text="Telefone:")
email_label = Label(frame, text="E-mail:")

nome_entry = Entry(frame, textvariable=nome)
telefone_entry = Entry(frame, textvariable=telefone)
email_entry = Entry(frame, textvariable=email)
preferencial_entry = Checkbutton(frame, text="Preferencial", variable=preferencial)


def alertar(mensagem: str):
    label = Label(frame, text=mensagem)
    label.grid(column=0, row=0, columnspan=3)

    label.after(2000, label.destroy)


def criar():
    contato = Contato(nome.get(), telefone.get(), email.get(), preferencial.get())

    if contato.validar(alertar):
        contato.salvar()

        alertar(f"Contato {nome.get()} salvo com sucesso.")

        nome.set("")
        telefone.set("")
        email.set("")
        preferencial.set(0)


botao = Button(frame, text="Criar", command=criar)

nome_label.grid(column=0, row=1, padx=5, pady=10, sticky="W")
telefone_label.grid(column=0, row=2, padx=5, pady=10, sticky="W")
email_label.grid(column=0, row=3, padx=5, pady=10, sticky="W")

nome_entry.grid(column=1, row=1, padx=20, pady=10)
telefone_entry.grid(column=1, row=2, padx=20, pady=10)
email_entry.grid(column=1, row=3, padx=20, pady=10)
preferencial_entry.grid(column=1, row=4, padx=20, pady=10)

botao.grid(column=1, row=5, padx=20, pady=10)

window.mainloop()
