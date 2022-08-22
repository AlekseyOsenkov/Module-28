class Locators:

    # login page objects
    username_textbox_name = 'login'
    password_textbox_name = 'password'
    login_button_class_name = 'auth_button'
    invalidUsername_message_css_selector = '#content-box > div > div'
    invalidPassword_message_css_selector = '#content-box > div > div'
    invalidUsernameAndPassword_css_selector = '#content-box > div > div'

    # home page objects
    welcome_css_selector = '#content-box > div > h2'
    click_my_tabs_css_selector = '#content-box > h1'
    my_tabs_link_text = 'Мои закладки'
    my_orders_link_text = 'Мои заказы'
    my_profile_link_text = 'Мой профиль'
    contact_link_text = 'Контактная информация'
    delivery_info_link_text = 'Информация о доставке'
    other_info_link_text = 'Дополнительная информация'
    change_password_link_text = 'Сменить пароль'
    new_password_class_name = 'password'
    confirmation_new_password_class_name = 'is_password'
    old_password_class_name = 'old_password'
    exit_link_text = 'Выход'
    basket_id = 'basket'
    catalog_products_class_name = 'catalog-list-menu'
    new_products_xpath = '//*[@id="menu"]/div/span[5]/a'
    sale_xpath = '//*[@id="menu"]/div/span[6]/a'
    discounts_and_bonuses_xpath = '//*[@id="menu"]/div/span[7]/a'
    payment_and_delivery_xpath = '//*[@id="menu"]/div/span[8]/a'
    hurry_up_xpath = '//*[@id="menu"]/div/span[9]/a'
    contacts_xpath = '//*[@id="menu"]/div/span[10]/a'
    airsoft_guns_xpath = '//*[@id="menu"]/div/div/div/ul/li[1]/a'
    all_guns_xpath = '//*[@id="left_box"]/div[1]/div[2]/div[3]/a[4]'
    pyrotechnics_xpath = '//*[@id="menu"]/div/div/div/ul/li[4]/a'
    all_guns_xpath_2 = '//*[@id="left_box"]/div[1]/div[2]/div[3]/a[4]'
    link_vk_xpath = '//*[@id="content-left"]/div[2]/a[1]'
    link_facebook_xpath = '//*[@id="content-left"]/div[2]/a[2]'
    link_twitter_xpath = '//*[@id="content-left"]/div[2]/a[3]'
    link_instagram_xpath = '//*[@id="content-left"]/div[2]/a[4]'
    link_youtube_xpath = '//*[@id="content-left"]/div[2]/a[5]'
    link_telegram_bot_xpath = '//*[@id="content-left"]/div[2]/a[6]'
    email_us_css_selector = '#footer > div.center > div.office > div > div.call-back-footer > a'
    close_the_form_css_selector = 'body > div.fancybox-wrap.fancybox-desktop.fancybox-type-iframe.fancybox-opened > div > div.fancybox-item.fancybox-close'
    articles_xpath = '//*[@id="footer"]/div[1]/div[2]/ul/li[4]/a'
    top_logo_css_selector = '#logo > a'
    button_buy_vint1_xpath = '//*[@id="indicator_catalog"]/div[1]/div[1]/div/button[1]'