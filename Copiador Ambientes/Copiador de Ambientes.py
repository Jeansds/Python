from selenium import webdriver
from selenium.webdriver import Edge
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import re
from tkinter import *
import os

Caminho = "C:/Downloads/"
Base = ""
Empresa = ""
dados = []
valores = []
Botoes = []
Dados = []
KPIS = []
Relatorios = []
Relatorios_Moveis = []
Servidores = []
Servidores_Moveis = []
Hidden_Dados = []
Hidden_Relatorios = []
ids_values = ["value-format-select", "currency-select", "value-select", "goal-select", "status-select",
  "status-set-select", "trendset-select", "drillthough-type-select",
  "kpi-label-input", "kpi-description-input", "trendset-set-input"]

def Get_Xpath(X):
	a= driver.execute_script("""gPt=function(c){
                                 if(c.id!==''){
                                     return'id("'+c.id+'")'
                                 } 
                                 if(c===document.body){
                                     return c.tagName
                                 }
                                 var a=0;
                                 var e=c.parentNode.childNodes;
                                 for(var b=0;b<e.length;b++){
                                     var d=e[b];
                                     if(d===c){
                                         return gPt(c.parentNode)+'/'+c.tagName+'['+(a+1)+']'
                                     }
                                     if(d.nodeType===1&&d.tagName===c.tagName){
                                         a++
                                     }
                                 }
                             };
                             return gPt(arguments[0]).toLowerCase();""", X)
	return str(a)

def Carregar_xpath(X):
	link = False
	while(link == False):
		try:
			retorno = driver.find_element_by_xpath(X)
			link = True
		except(NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, WebDriverException):
			time.sleep(1)
	time.sleep(0.3)
	return retorno

def Carregar_id(X):
	link = False
	while(link == False):
		try:
			retorno = driver.find_element_by_id(X)
			link = True
		except(NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, WebDriverException):
			time.sleep(1)
	time.sleep(0.3)
	return retorno

def Carregar_class(X):
	link = False
	while(link == False):
		try:
			retorno = driver.find_element_by_class_name(X)
			link = True
		except(NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, WebDriverException):
			time.sleep(1)
	time.sleep(0.3)
	return retorno

def Carregar_name(X):
	link = False
	while(link == False):
		try:
			retorno = driver.find_element_by_name(X)
			link = True
		except(NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, WebDriverException):
			time.sleep(1)
	time.sleep(0.3)
	return retorno

def Carregar_nameS(X):
	link = False
	while(link == False):
		try:
			retorno = driver.find_elements_by_name(X)
			link = True
		except(NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, WebDriverException):
			time.sleep(1)
	time.sleep(0.3)
	return retorno

def Reset():
	Carregar_xpath("//a[contains(text(),'Página Inicial')]").click()
	Carregar_xpath("//span[contains(text(),'" + Empresa + "')]").click()

def Copiar_Empresa():
	Carregar_xpath("//span[contains(text(),'" + Base + "')]").click()
	b = Carregar_class("datasets hidden-xs ng-scope")
	a = driver.find_elements_by_xpath(Get_Xpath(b) + "//li")
	c = b.find_elements_by_class_name("context")
	b = b.find_elements_by_class_name("multiline-ellipsis ng-binding")
	for i in b:
		Dados.append(i.text)
	for i in a:
		if i.get_attribute("class") == "ng-scope hidden":
			Hidden_Dados.append(True)
		else:
			Hidden_Dados.append(False)
	for i in c:
		i.click()
		time.sleep(1)
		a = Carregar_class("actions-group hidden-xs ng-scope")
		driver.find_element_by_xpath(Get_Xpath(a) + "/span/a").click()
		time.sleep(0.5)
	b = Carregar_class("reports ng-scope")
	a = driver.find_elements_by_xpath(Get_Xpath(b) + "//li")
	c = b.find_elements_by_class_name("context")
	b = b.find_elements_by_class_name("multiline-ellipsis ng-binding")
	for i in b:
		Relatorios.append(i.text)
	for i in a:
		if i.get_attribute("class") == "ng-scope hidden":
			Hidden_Relatorios.append(True)
		else:
			Hidden_Relatorios.append(False)
	for i in c:
		i.click()
		time.sleep(1)
		a = Carregar_class("metadata ng-scope")
		driver.find_element_by_xpath(Get_Xpath(a) + "/footer/div[4]/span/a").click()
		time.sleep(0.5)
	b = Carregar_class("kpis ng-scope")
	b = b.find_elements_by_class_name("name ng-binding")
	for i in b:
		KPIS.append(re.sub(" ", "%20", i.text))
	b = Carregar_class("mobile-reports ng-scope")
	c = b.find_elements_by_class_name("context")
	b = b.find_elements_by_class_name("name ng-binding")
	for i in c:
		i.click()
		time.sleep(1)
		a = Carregar_class("actions-group hidden-xs ng-scope")
		driver.find_element_by_xpath(Get_Xpath(a) + "/span/a").click()
		time.sleep(0.5)
	for i in b:
		Relatorios_Moveis.append(i.text)
def Copiar_Servidores():
	for i in range(len(Dados)):
		driver.get("https://bi.hubcard.com.br/reports/manage/catalogitem/datasource/" + Base + "/" + Dados[i])
		a = Carregar_class("content")
		Servidores.append(a.find_element_by_class_name("ng-binding ng-scope").text)
	for i in range(len(Relatorios_Moveis)):
		Servidores_Moveis.append([])
		driver.get("https://bi.hubcard.com.br/reports/manage/catalogitem/datasets/" + Base + "/" +
			(re.sub(" ", "%20", Relatorios_Moveis[i])))
		a = driver.find_elements_by_xpath(
			(Get_Xpath(Carregar_class("ng-scope content editdatasets"))) + "/edit-data-sets-form/div/form/div/span")

		for j in a:
			Servidores_Moveis[i].append(j.text)

def Copiar_KPIS():
	for j in range(len(KPIS)):
		valores.append([])
		dados.append([])
		Botoes.append([])
		driver.get("https://bi.hubcard.com.br/reports/manage/catalogitem/properties/" + Base + "/" + KPIS[j])
		Carregar_class("ng-pristine ng-valid ng-valid-required ng-valid-pattern ng-valid-maxlength")
		time.sleep(0.5)
		for i in ids_values:
			try:
				a = driver.find_element_by_id(i)
				valores[j].append(a.get_attribute("value"))
			except NoSuchElementException:
				valores[j].append(None)
		a = Carregar_class("ng-scope selected")
		Botoes[j].append(a.get_attribute("title"))
		a = Carregar_class("col-xs-6 form-col-right")
		a.find_element_by_class_name("input-group-btn").click()
		Carregar_xpath("//th[@class='ng-scope selected']")
		a = Carregar_class("links")
		a = a.find_elements_by_class_name("ng-scope")
		for i in a:
			Temp = i.text
			Temp = Temp.split()
			if dados[j].count(Temp[0])==0:
				dados[j].append(Temp[0])
		a = Carregar_nameS("options")
		for i in a:
			if i.is_selected() == True:
				dados[j].append(i.get_attribute("value"))
		Carregar_xpath("//button[contains(text(),'Cancelar')]").click()
		time.sleep(1)
		Carregar_xpath("//button[contains(text(),'Cancelar')]").click()
	time.sleep(1)

def Verificar_Dados():
	Erro = []
	Falhas = []
	b = Carregar_class("datasets hidden-xs ng-scope")
	b = b.find_elements_by_class_name("multiline-ellipsis ng-binding")
	if len(b) != len(Dados):
		for i in range(len(b)):
			Falhas.append(b[i].text)
		for i in range(Dados):
			if Falhas.count(Dados[i]) == 0:
				Erro.append(Dados[i])
	for i in Erro:
		Carregar_id("upload-file").send_keys(Caminho + i + ".rsd")
		time.sleep(1)
		driver.get("https://bi.hubcard.com.br/reports/browse/" + Empresa)
	for i in Dados:
		os.remove(Caminho + i + ".rdl")
	Falhas.clear()
	Erro.clear()
	b = Carregar_class("reports ng-scope")
	b = b.find_elements_by_class_name("multiline-ellipsis ng-binding")
	if len(b) != len(Relatorios):
		for i in range(len(b)):
			Falhas.append(b[i].text)
		for i in range(Relatorios):
			if Falhas.count(Relatorios[i]) == 0:
				Erro.append(Relatorios[i])
	for i in Erro:
		Carregar_id("upload-file").send_keys(Caminho + i + ".rdl")
		time.sleep(1)
		driver.get("https://bi.hubcard.com.br/reports/browse/" + Empresa)
	for i in Relatorios:
		os.remove(Caminho + i + ".rdl")
	Falhas.clear()

def Verificar_Servidores():
	for i in range(len(Dados)):
		driver.get("https://bi.hubcard.com.br/reports/manage/catalogitem/datasource/" + Empresa + "/" + Dados[i])
		a = Carregar_class("content")
		if a.find_element_by_class_name("ng-binding ng-scope").text != Servidores[i]:
			Temp = Servidores[i].split("/")
			Temp.remove("")
			Temp[0] = Empresa
			for j in Temp:
				a = Carregar_class("modal-content")
				a.find_element_by_xpath("//span[contains(text(),'" + j + "')]").click()
			time.sleep(1)
			try:
				driver.find_element_by_xpath("//span[contains(text(),'Aplicar')]").click()
			except WebDriverException:
				time.sleep(1)
			time.sleep(1)
	for i in range(len(Relatorios_Moveis)):
		driver.get("https://bi.hubcard.com.br/reports/manage/catalogitem/datasets/" + Empresa + "/" +
			(re.sub(" ", "%20", Relatorios_Moveis[i])))
		a = driver.find_elements_by_xpath(
			(Get_Xpath(Carregar_class("ng-scope content editdatasets"))) + "/edit-data-sets-form/div/form/div/button")
		for j in range(len(Relatorios_Moveis[i])):
			Temp = Servidores_Moveis[i].split("/")
			Temp.remove("")
			Temp[0] = Empresa
			a[j].click()
			for k in Temp:
				a = Carregar_class("modal-content")
				a.find_element_by_xpath("//span[contains(text(),'" + k + "')]").click()
			time.sleep(1)
			try:
				driver.find_element_by_xpath("//span[contains(text(),'Salvar')]").click()
			except WebDriverException:
				time.sleep(1)
			time.sleep(1)

def Hidden_Objects():
	for i in range(len(Dados)):
		if Hidden_Dados[i] == True:
			driver.get("https://bi.hubcard.com.br/reports/manage/catalogitem/" + Empresa + "/" + Dados[i])
			if Carregar_id("checkbox_disable").is_selected() == False:
				Carregar_xpath("//span[contains(text(),'Ocultar este item')]").click()
				time.sleep(0.1)
				Carregar_xpath("//span[contains(text(),'Aplicar')]").click()
				time.sleep(1)
	for i in range(len(Relatorios)):
		if Hidden_Relatorios[i] == True:
			driver.get("https://bi.hubcard.com.br/reports/manage/catalogitem/properties/" + Empresa + "/" + Relatorios[i])
			if Carregar_id("checkbox_disable").is_selected() == False:
				Carregar_xpath("//span[contains(text(),'Ocultar este item')]").click()
				time.sleep(0.1)
				Carregar_xpath("//span[contains(text(),'Aplicar')]").click()
				time.sleep(1)

def Colar_KPIS():
	for j in range(len(KPIS)):
		Carregar_xpath("//span[contains(text(),'Novo')]").click()
		Carregar_xpath("//span[contains(text(),'KPI')]").click()
		Carregar_class("ng-pristine ng-valid ng-valid-required ng-valid-pattern ng-valid-maxlength")
		a = Select(Carregar_id("value-format-select"))
		a = a.select_by_value("DefaultCurrency")
		time.sleep(2)
		for i in range(len(ids_values)):
			if valores[j][i] != None:
				try:
					a = Select(driver.find_element_by_id(ids_values[i]))
					a.select_by_value(valores[j][i])
				except:
					try:
						Temp = driver.find_element_by_id(ids_values[i])
						Temp.click()
						Temp.clear()
						Temp.send_keys(valores[j][i])
					except:
						pass
		a = driver.find_elements_by_xpath("//ul[@class='visualizations']/li")
		for i in a:
			if i.get_attribute("title") == Botoes[j][0]:
				i.click()
				time.sleep(0.5)
				break
		a = Carregar_class("col-xs-6 form-col-right")
		a.find_element_by_class_name("input-group-btn").click()
		dados[j][0] = Empresa
		for i in range(len(dados[j])):
			link = False
			while(link == False):
				try:
					a = Carregar_class("modal-content")
					a.find_element_by_xpath("//span[contains(text(),'" + dados[j][i] + "')]").click()
					link = True
				except :
					time.sleep(1)
		time.sleep(0.5)
		Carregar_xpath("//button[contains(text(),'OK')]").click()
		time.sleep(0.5)
		while True:
			try:
				driver.find_element_by_xpath("//button[contains(text(),'Cancelar')]").click()
				break
			except WebDriverException:
				time.sleep(1)
		time.sleep(1)

def Carregar_Relatorios_Moveis():
	driver.get("https://bi.hubcard.com.br/reports/browse/")
	Carregar_xpath("//span[contains(text(),'" + Empresa + "')]").click()
	for i in Relatorios_Moveis:
		Carregar_id("upload-file").send_keys(Caminho + i + ".rsmobile")
		time.sleep(1)
		driver.get("https://bi.hubcard.com.br/reports/browse/"+Empresa)
		os.remove(Caminho + i + ".rsmobile")

def Iniciar():
	global driver
	driver = Edge(executable_path = 'C:/Users/U300398/Desktop/MicrosoftWebDriver.exe')
	
def Todos_os_Processos(l1):
	driver.get("https://bi.hubcard.com.br/reports/browse/")
	Copiar_Empresa()
	Copiar_KPIS()
	Copiar_Servidores()
	Reset()
	Verificar_Dados()
	Carregar_Relatorios_Moveis()
	Verificar_Servidores()
	Reset()
	Hidden_Objects()
	Reset()
	Colar_KPIS()
	l1.destroy()
	l1 = Label(window, text = "Finalizado", font = (None, 15))
	l1.grid(row = 2, columnspan = 2)

window = Tk()
l1 = Label(window, text = "Esperando", font = (None, 15))
l1.grid(row = 2, columnspan = 2)
b1 = Button(window, text = "Todos os processos", command = lambda:Todos_os_Processos(l1), height = 2, width = 15)
b1.grid(row = 1, column = 0)
b2 = Button(window, text = "Iniciar Programa", command = lambda:Iniciar(), height = 2, width = 15)
b2.grid(row = 0, column = 0)
b3 = Button(window, text = "Fechar Navegador", command = lambda:driver.quit(), height = 2, width = 15)
b3.grid(row = 0, column = 1)
b4 = Button(window, text = "Finalizar", command = quit, height = 2, width = 15)
b4.grid(row = 1, column = 1)
window.mainloop()