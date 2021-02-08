from selenium.webdriver.common.by import By


class RegisterPageLocators:
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD = (By.NAME, "registration-password1")
    REGISTER_BTN = (By.NAME, "registration_submit")
    REGISTER_PASSWORD_CONFIRM = (By.NAME, "registration-password2")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BTN = (By.NAME, "login_submit")

    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSWORD = (By.ID, "id_registration-password1")
    REG_REPEAT_PAS = (By.ID, "id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")


class ProductPageLocators:
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_STRONG_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_ADD_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasketPageLocators:
    BASKET_BTN = (By.CSS_SELECTOR, "span > a")
    BASKET_NO_ITEM = (By.ID, "content_inner")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".basket_formset")
