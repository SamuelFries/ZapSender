from sender import WhatsAppSender
from contacts_loader import load_contacts

def main():
    # Inicializa o WhatsAppSender
    sender = WhatsAppSender()

    # Carrega os contatos do arquivo CSV
    contacts = load_contacts("data/contacts.csv")
    
    # Carrega a mensagem do arquivo message.txt
    with open("data/messages/message.txt", "r") as file:
        message = file.read().strip()

    # Envia a mensagem para cada contato
    for contact in contacts:
        sender.send_message(contact, message)
    
    # Fecha o navegador após o envio das mensagens
    sender.close()

if __name__ == "__main__":
    main()