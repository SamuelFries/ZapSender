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
        
        # Pausa para permitir o login (ajuste o tempo conforme necessário)
        time.sleep(30)  # Aumente esse valor se precisar de mais tempo para o login

    def send_message(self, contact, message):
        try:
            # Aguarda a barra de pesquisa estar disponível e busca o contato
            search_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            search_box.clear()
            search_box.send_keys(contact)
            time.sleep(2)  # Pausa para garantir que o resultado da pesquisa aparece

            # Seleciona o contato correto na lista de resultados
            contact_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, f'//span[@title="{contact}"]'))
            )
            contact_element.click()
            time.sleep(2)  # Pausa para garantir que o chat com o contato foi aberto

            # Aguarda a caixa de mensagem estar disponível e envia a mensagem
            message_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )
            message_box.send_keys(message)
            message_box.send_keys(Keys.RETURN)
            time.sleep(2)  # Pausa para garantir que a mensagem foi enviada
            
            print(f"Message sent to {contact}.")
        except TimeoutException:
            print(f"Could not find the elements needed to send the message to {contact}.")
        except Exception as e:
            print(f"Could not send message to {contact}. Error: {str(e)}")

    def close(self):
        # Fecha o navegador
        self.driver.quit()