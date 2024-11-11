import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WhatsAppSender:
    def __init__(self):
        # Inicializa o driver do Firefox (GeckoDriver) para o Selenium
        self.driver = webdriver.Firefox()
        self.driver.get("https://web.whatsapp.com")
        print("Please scan the QR code to log in.")
        time.sleep(30)  # Tempo para o usuário fazer o login (ajuste conforme necessário)

    def send_message(self, contact, message):
        try:
            # Localiza a barra de pesquisa e insere o nome do contato
            search_box = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            search_box.clear()
            search_box.send_keys(contact)
            time.sleep(2)  # Pausa curta para exibir resultados de busca

            # Seleciona o contato e clica para abrir a conversa
            contact_element = self.driver.find_element(By.XPATH, f'//span[@title="{contact}"]')
            contact_element.click()

            # Localiza a caixa de mensagem
            message_box = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )
            
            # Envia a mensagem letra por letra
            for char in message:
                message_box.send_keys(char)
                time.sleep(0.05)  # Pequena pausa entre cada caractere para simular digitação humana
            
            # Pressiona Enter para enviar a mensagem
            message_box.send_keys(Keys.RETURN)
            print(f"Message sent to {contact}.")

        except TimeoutException:
            print(f"Could not find the contact '{contact}' or message box.")

    def close(self):
        # Fecha o navegador
        self.driver.quit()