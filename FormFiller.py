from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")
option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path='c://chromedriver.exe', options=option)

browser.get("https://forms.gle/FoAoauz53Xy7A4n68")

inputtext = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
textarea = browser.find_elements_by_class_name("quantumWizTextinputPapertextareaInput")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
dropdown = browser.find_elements_by_class_name("quantumWizMenuPaperselectContent")
scaleradiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOnRadio") #horizontal radio buttons
gridradiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOnRadio") 

submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

textarea[0].send_keys("Random Name")

radiobuttons[2].click()

checkboxes[1].click()
checkboxes[3].click()

submitbutton[0].click()

#browser.close()