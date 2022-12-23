from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib
# from webdriver_manager.firefox import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import dadosPlanilha

import random





s = Service('C:/Users/.../chromedriver.exe')
driver = webdriver.Chrome(service=s)

# driver = webdriver.Firefox()



def enviar_midia(midia):
  driver.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
  attach = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
  attach.send_keys(midia)
  time.sleep(3)
  send = driver.find_element(By.CSS_SELECTOR,"span[data-icon='send']")
  print(send)
  send.click()

  # while (len(driver.find_elements(By.CSS_SELECTOR,"spanaria-label=' Entregue '"))<1 or len(driver.find_elements(By.CSS_SELECTOR,"span[aria-label=' Lida ']"))<1):
  #   print(driver.find_elements(By.CSS_SELECTOR,"spanaria-label=' Entregue '"))
  #   print(driver.find_elements(By.CSS_SELECTOR,"span[aria-label=' Lida ']"))

  #   time.sleep(1)



  time.sleep(3)


texto1 = "Olá, pode me ajudar?"

midia = "/home/lucas/Área de Trabalho/teste/logo.webp"

# textoCode = urllib.parse.quote(texto1)

# driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

# driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/div/div[2]/a').click()

while len(driver.find_elements(By.ID, "side"))<1:
  time.sleep(1)

contatos = dadosPlanilha.getContatos()

for i, mensagem in enumerate(contatos['nome']):
  nome = contatos.loc[i,"nome"]
  telefone = contatos.loc[i,"telefone"]

  # print(nome,telefone)

  driver.find_elements(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')[0].send_keys("lucas soares")
  # print("lucas soares")

  driver.find_elements(By.XPATH,'//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')[0].send_keys(Keys.ENTER)


  # while len(driver.find_elements(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div/div/div[2]'))<1:
  #   print("lucas")
  #   time.sleep(1)

  # driver.find_elements(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div/div/div[2]')[0].click()
  # print("click")

  while len(driver.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div'))<1:
    # print("botao mensagem")
    time.sleep(1)

  # print("input mensagem")

  fone = 5535999843637

  mensagem= f"Ol%C3%A1,%20{nome}%0A%0ATudo%20bem?%0A%0AGostar%C3%ADamos%20de%20te%20apresentar%20a%20Ritualiza!"

  link = f"https://api.whatsapp.com/send?phone={telefone}&text={mensagem}"



  # link = f"https://api.whatsapp.com/send?phone={fone}&text={textoCode}"
  # link = "https://api.whatsapp.com/send?phone=5537999843760&text=Ol%C3%A1,%20pode%20me%20ajudar"

  for letter in link:
    driver.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')[0].send_keys(letter)


  driver.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')[0].send_keys(Keys.ENTER)


  driver.find_elements(By.LINK_TEXT,link[:len(link)-1])[0].click()

  time.sleep(5)

  driver.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')[0].send_keys("!")

  enviar_midia(midia)

  # driver.find_elements(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')[0].send_keys(Keys.ENTER)

  tempo =random.uniform(0,2)

  print(tempo)

  time.sleep(tempo)





# print(textoCode)




# time.sleep(1)
# driver.get(link)



# while len(driver.find_elements(By.ID, "action-button"))<1:
#   print(driver.find_elements(By.ID, "action-button"))
#   time.sleep(1)

# driver.find_element(By.ID,"action-button").click()


# while len(driver.find_elements(By.XPATH, '//*[@id="fallback_block"]/div/div/h4[2]/a'))<1:
#   time.sleep(1)

# driver.find_element(By.XPATH,'//*[@id="fallback_block"]/div/div/h4[2]/a').click()



# driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")