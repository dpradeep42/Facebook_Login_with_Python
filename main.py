from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def login(email, password):
    server = webdriver.Chrome(ChromeDriverManager().install())
    server.get('https://www.facebook.com/')

    username = server.find_element_by_id('email')
    username.send_keys(email)

    passwd = server.find_element_by_id('pass')
    passwd.send_keys(password)

    login = server.find_element_by_name('login')
    login.click()

    #server.quit()


if __name__ == '__main__':
    login(input("Enter email ID: "), input("Enter Password: "))
