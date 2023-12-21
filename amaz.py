from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

edge_driver_path = 'C:/shelter-dom/msedgedriver.exe'

# Настройки Edge
options = Options()

# Инициализация службы EdgeDriver
service = Service(executable_path=edge_driver_path)

# Инициализация драйвера Edge
driver = webdriver.Edge(service=service, options=options)
# Открытие целевого веб-сайта (в данном случае Amazon)
driver.get("https://kru3en.github.io/shelter-dom/")

# Функция для проверки наличия новой категории
def check_new_category(category_name):
    try:
        # Найти новую категорию по ее названию на главной странице
        driver.find_element(By.LINK_TEXT, category_name)
        print(f"Категория '{category_name}' присутствует на главной странице.")
    except NoSuchElementException:
        print(f"Категория '{category_name}' НЕ присутствует на главной странице.")

# Тестирование для категории "Устройства для умногок дома"
check_new_category("Our pets")

# Закрытие браузера
driver.quit()
driver = webdriver.Edge(service=service, options=options)
driver.get("https://kru3en.github.io/shelter-dom/pets.html")
check_new_category("Cozy House")
driver.quit()

