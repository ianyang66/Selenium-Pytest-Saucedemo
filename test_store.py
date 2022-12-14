import pytest, time
from login_page_var import *
from web_fixtures import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
@pytest.mark.shop
class Test_Shop(Store_Test):
    def test_add_item(self):
        self.login(good_user, all_passwords)
        self.add_backpack()
        time.sleep(3)
        cart_amount = self.driver.find_element(By.CLASS_NAME,'shopping_cart_badge')
        assert cart_amount.text == '1'
        self.remove_backpack()

    def test_add_3_items(self):
        self.login(good_user, all_passwords)
        self.add_bike_light()
        self.add_jacket()
        self.add_bolt_shirt()
        time.sleep(3)
        cart_amount = self.driver.find_element(By.CLASS_NAME,'shopping_cart_badge')
        assert cart_amount.text == '3'
        self.remove_bike_light()
        assert cart_amount.text == '2'
        self.remove_jacket()
        assert cart_amount.text == '1'
        self.remove_bolt_shirt()

    def test_add_all_items(self):
        self.login(good_user, all_passwords)
        self.add_backpack()
        self.add_bike_light()
        self.add_bolt_shirt()
        self.add_jacket()
        self.add_onsie()
        self.add_t_shirt()
        time.sleep(3)
        cart_amount = self.driver.find_element(By.CLASS_NAME,'shopping_cart_badge')
        assert cart_amount.text == '6'
        self.remove_backpack()
        assert cart_amount.text == '5'
        self.remove_bolt_shirt()
        assert cart_amount.text == '4'
        self.remove_jacket()
        assert cart_amount.text == '3'
        self.remove_onsie()
        assert cart_amount.text == '2'
        self.remove_bike_light()
        assert cart_amount.text == '1'
        self.remove_t_shirt()

    @pytest.mark.sorting
    def test_sort_low_to_high(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Price (low to high)')
        prices = []
        i = 0 
        time.sleep(3)
        for item in self.driver.find_elements(By.CLASS_NAME,'inventory_item_price'):
            number = float(item.text[1:])
            prices.append(number)
        while i < len(prices) - 1:
            assert prices[i] <= prices[i + 1]
            i += 1


    @pytest.mark.sorting
    def test_sort_high_to_low(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Price (high to low)')
        prices = []
        i = 0 
        time.sleep(3)
        for item in self.driver.find_elements(By.CLASS_NAME,'inventory_item_price'):
            number = float(item.text[1:])
            prices.append(number)
        while i < len(prices) - 1:
            assert prices[i] >= prices[i + 1]
            i += 1

    @pytest.mark.sorting
    def test_sort_a_to_z(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        names = []
        time.sleep(3)
        for name in self.driver.find_elements(By.CLASS_NAME,'inventory_item_name'):
            names.append(name.text)
        sorts = sorted(names)
        assert names == sorts

    @pytest.mark.sorting
    def test_sort_z_to_a(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (Z to A)')
        names = []
        time.sleep(3)
        for name in self.driver.find_elements(By.CLASS_NAME,'inventory_item_name'):
            names.append(name.text)
        reverse = sorted(names, reverse=True)
        assert names == reverse

    @pytest.mark.product
    def test_click_backpack(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.CLASS_NAME,'inventory_item_name')
        items[0].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4'

    @pytest.mark.product
    def test_click_bike(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.CLASS_NAME,'inventory_item_name')
        items[1].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0'

    @pytest.mark.product
    def test_click_bolt_shirt(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.CLASS_NAME,'inventory_item_name')
        items[2].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=1'

    @pytest.mark.product
    def test_click_fleece(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.CLASS_NAME,'inventory_item_name')
        items[3].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=5'

    @pytest.mark.product
    def test_click_onsie(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.CLASS_NAME,'inventory_item_name')
        items[4].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=2'

    @pytest.mark.product
    def test_click_testing_shirt(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.CLASS_NAME,'inventory_item_name')
        items[5].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=3'

    @pytest.mark.product_pic
    def test_click_backpack_pic(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_img']")
        items[0].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4'

    @pytest.mark.product_pic
    def test_click_bike_pic(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_img']")
        items[1].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0'


    @pytest.mark.product_pic
    def test_click_bolt_pic(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_img']")
        items[2].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=1'


    @pytest.mark.product_pic
    def test_click_fleece_pic(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_img']")
        items[3].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=5'


    @pytest.mark.product_pic
    def test_click_onsie_pic(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_img']")
        items[4].click()
        time.sleep(1)        
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=2'


    @pytest.mark.product_pic
    def test_click_testing_shirt_pic(self):
        self.login(good_user, all_passwords)
        options = Select(self.driver.find_element(By.CLASS_NAME,'product_sort_container'))
        options.select_by_visible_text('Name (A to Z)')
        items = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_img']")
        items[5].click()
        time.sleep(1)
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=3'




        