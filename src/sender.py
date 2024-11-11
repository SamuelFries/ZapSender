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
            print(f"Searching for contact '{contact}'...")

            # Pausa para dar tempo do resultado aparecer
            time.sleep(5)

            # Tenta localizar o contato exato na lista de resultados
            contact_found = False
            attempts = 5
            for _ in range(attempts):
                try:
                    contact_element = self.driver.find_element(By.XPATH, f'//span[@title="{contact}"]')
                    contact_element.click()
                    contact_found = True
                    print(f"Contact '{contact}' found and selected.")
                    break
                except Exception:
                    print(f"Contact '{contact}' not found, retrying...")
                    time.sleep(2)  # Espera antes de tentar novamente
            
            if not contact_found:
                print(f"Could not find contact '{contact}' after {attempts} attempts.")
                return

            # Aguarda a caixa de mensagem estar disponível e envia a mensagem
            message_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
            )
            
            # Envia a mensagem letra por letra para evitar problemas de interrupção
            for char in message:
                message_box.send_keys(char)
                time.sleep(0.1)  # Pequeno atraso entre cada caractere
            
            # Pressiona Enter para enviar a mensagem
            message_box.send_keys(Keys.RETURN)
            time.sleep(2)  # Pausa para garantir que a mensagem foi enviada
            
            print(f"Message sent to {contact}.")
        except TimeoutException:
            print("Could not find the elements needed to send the message.")
        except Exception as e:
            print(f"Could not send message. Error: {str(e)}")

    def close(self):
        # Fecha o navegador
        self.driver.quit()