import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class CadPass:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()        

    def login(self): 
        driver = self.driver
        driver.get("http://0.0.0.0/admin/login/")
        time.sleep(5)

        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        time.sleep(5)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        bot.cad()

    def cad(self):
        driver = self.driver
        driver.get("http://0.0.0.0/admin/core/passagem/add/")
        
        ref_arquivo = open("passagem.txt","r")    
        time.sleep(5)

        for linha in ref_arquivo:
            time.sleep(3)

            valores = linha.split()
            
            if(valores[0] == 'aqua'): #AQUA              
                select = Select(driver.find_element_by_id('id_antena'))
                select.select_by_visible_text('Cacheira Paulista/CP5')
                select = Select(driver.find_element_by_id('id_servidor'))
                select.select_by_visible_text('SOLARIA')
                datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                datai.click()
                datai.clear()
                datai.send_keys(valores[1])
                dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                dataf.click()
                dataf.clear()
                dataf.send_keys(valores[1])
                horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                horai.click()
                horai.clear()
                horai.send_keys(valores[2])
                horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                horaf.click()
                horaf.clear()
                horaf.send_keys(valores[3])
                select = Select(driver.find_element_by_id('id_sensor'))       
                select.select_by_visible_text('AQUA/MODIS')
                time.sleep(5)
                driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()

            elif(valores[0] == 'AMZ'): #AMAZONIA              
                select = Select(driver.find_element_by_id('id_antena'))
                select.select_by_visible_text('Cacheira Paulista/CP5')
                select = Select(driver.find_element_by_id('id_servidor'))
                select.select_by_visible_text('SOLARIA')
                datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                datai.click()
                datai.clear()
                datai.send_keys(valores[1])
                dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                dataf.click()
                dataf.clear()
                dataf.send_keys(valores[1])
                horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                horai.click()
                horai.clear()
                horai.send_keys(valores[2])
                horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                horaf.click()
                horaf.clear()
                horaf.send_keys(valores[3])
                select = Select(driver.find_element_by_id('id_sensor'))       
                select.select_by_visible_text('AMAZONIA 1/WFI')
                time.sleep(5)
                driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()
                
                select = Select(driver.find_element_by_id('id_antena'))
                select.select_by_visible_text('Cacheira Paulista/CP5')
                select = Select(driver.find_element_by_id('id_servidor'))
                select.select_by_visible_text('COROT')
                datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                datai.click()
                datai.clear()
                datai.send_keys(valores[1])
                dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                dataf.click()
                dataf.clear()
                dataf.send_keys(valores[1])
                horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                horai.click()
                horai.clear()
                horai.send_keys(valores[2])
                horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                horaf.click()
                horaf.clear()
                horaf.send_keys(valores[3])
                select = Select(driver.find_element_by_id('id_sensor'))       
                select.select_by_visible_text('AMAZONIA 1/WFI')
                time.sleep(5)
                driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()
            
            elif(valores[0] == 'CBERS04'): #CBERS04              
                select = Select(driver.find_element_by_id('id_antena'))
                select.select_by_visible_text('Cacheira Paulista/CP5')
                select = Select(driver.find_element_by_id('id_servidor'))
                select.select_by_visible_text('SOLARIA')
                datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                datai.click()
                datai.clear()
                datai.send_keys(valores[1])
                dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                dataf.click()
                dataf.clear()
                dataf.send_keys(valores[1])
                horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                horai.click()
                horai.clear()
                horai.send_keys(valores[2])
                horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                horaf.click()
                horaf.clear()
                horaf.send_keys(valores[3])
                select = Select(driver.find_element_by_id('id_sensor'))       
                select.select_by_visible_text('CBERS4/MUX')
                time.sleep(5)
                driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()
                
                select = Select(driver.find_element_by_id('id_antena'))
                select.select_by_visible_text('Cacheira Paulista/CP5')
                select = Select(driver.find_element_by_id('id_servidor'))
                select.select_by_visible_text('COROT')
                datai = driver.find_element_by_xpath("//input[@name='inicio_0']")
                datai.click()
                datai.clear()
                datai.send_keys(valores[1])
                dataf = driver.find_element_by_xpath("//input[@name='fim_0']")
                dataf.click()
                dataf.clear()
                dataf.send_keys(valores[1])
                horai = driver.find_element_by_xpath("//input[@name='inicio_1']")
                horai.click()
                horai.clear()
                horai.send_keys(valores[2])
                horaf = driver.find_element_by_xpath("//input[@name='fim_1']")
                horaf.click()
                horaf.clear()
                horaf.send_keys(valores[3])
                select = Select(driver.find_element_by_id('id_sensor'))       
                select.select_by_visible_text('CBERS4/AWFI')
                time.sleep(5)
                driver.find_element_by_xpath("//button[contains(text(), 'Salvar e adicionar outro(a)')]").click()
            
            else:
                print('teste')
            
                          
        ref_arquivo.close()      

        driver.close()

bot = CadPass('USUARIO', 'SENHA')

bot.login()