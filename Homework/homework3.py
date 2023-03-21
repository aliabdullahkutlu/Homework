from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class Test_Homework:
    
    def test_task1(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        time.sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        time.sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        time.sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        errorMessage = "Epic sadface: Username is required."
        print(errorMessage)
        time.sleep(1000)


    def test_task2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        time.sleep(2)
        usernameInput.send_keys("abc")
        passwordInput.send_keys("")
        time.sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        time.sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        errorMessage = "Epic sadface: Password is required."
        print(errorMessage)
        time.sleep(1000)    
        
        
    def test_task3(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        time.sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        time.sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        time.sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        errorMessage = "Epic sadface: Sorry, this user has been locked out."
        print(errorMessage)
        time.sleep(1000)  
    
    
    def test_task4(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        time.sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        time.sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        time.sleep(2)
        loginBtn.click()
        time.sleep(2)
        loginBtn = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        loginBtn.click()
        time.sleep(10000)
        
        
    def test_task5(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        time.sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        time.sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        time.sleep(2)
        loginBtn.click()
        time.sleep(1000)
        
        
    def test_task6(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID , "password")
        time.sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        time.sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        time.sleep(2)
        loginBtn.click()
        listOfEntity = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Sauce Demo sitesinde şu anda {len(listOfEntity)} adet ürün var.")
        time.sleep(1000)

testClass = Test_Homework()

# testClass.test_task1()
# ==>  Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

# testClass.test_task2()
# ==>  Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

# testClass.test_task3()
# ==>  Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

# testClass.test_task4()
# ==>  Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır.

# testClass.test_task5()
# ==>  Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.

# testClass.test_task6()
# ==> Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! YORUM SATIRLARINI KALDIRARAK İSTENEN DURUMLARI TEST EDEBİLİRSİNİZ. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 