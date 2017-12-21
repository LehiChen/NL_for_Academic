import re,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = "https://music.163.com/playlist?id=453316317"
#driver = webdriver.PhantomJS(executable_path="phantomjs-2.1.1-windows//bin//phantomjs")
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(url)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe"))
trs = driver.find_elements_by_css_selector('span a[href]')
trs_bad = driver.find_elements_by_css_selector('a[hidefocus="true"]')
for i in range(1,600):
	try:
		print(i)
		if trs[i] not in trs_bad:
			trs[i].click()
		else:
			continue
		temp_url = driver.current_url[:22] + driver.current_url[24:]
		driver.get(temp_url)
		driver.switch_to.frame(driver.find_element_by_xpath("//iframe"))
		lyric_content = driver.find_element_by_css_selector('div[id="lyric-content"]').text[:-2].strip()
		flag_ctrl = driver.find_element_by_css_selector('a[id="flag_ctrl"]')
		flag_ctrl.click()
		flag_more = driver.find_element_by_css_selector('div[id="flag_more"]').text
		print(lyric_content)
		print(flag_more)
		with open("lyrics//%s.txt"%i,'w',encoding="UTF-8") as f:
			f.write(lyric_content+flag_more)
	except:
		continue
	finally:
		driver.get(url)
		driver.switch_to.frame(driver.find_element_by_xpath("//iframe"))
		trs = driver.find_elements_by_css_selector('span a[href]')
		trs_bad = driver.find_elements_by_css_selector('a[hidefocus="true"]')
		times = i/25*300
		driver.execute_script("window.scrollBy(0,%s)"%times)
print("FINISH!!!!!!!")