from driver import Browser
from time import sleep

browser = Browser()

url = "https://seller.wildberries.ru/marketplace-orders-fbs/new-tasks"

browser.navigate_to(url)

browser.click('close_modal_btn')
browser.click('choose_all_orders_checkbox')
browser.click('create_new_delivery_btn')
browser.click('modal_accept_creating_delivery_btn')
browser.click('at_assembly_tab')
browser.click('delivery_row')
browser.click('print_stickers_btn')
browser.click('modal_accept_print_btn')
browser.print_opened_tab_qr_and_close()
browser.click('package_tab')
browser.click('create_package')
assert browser.check_element('package_list')
browser.click('print_package_qr_code_icon')
browser.print_opened_tab_qr_and_close()
browser.click('sent_to_delivery_btn')
browser.click('modal_accept_sending_btn')
browser.click('package_for_sending_row')
browser.click('print_dropdown_btn')
browser.click('package_qr_code_option')
browser.print_opened_tab_qr_and_close()

browser.quit()