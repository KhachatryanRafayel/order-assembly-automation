selectors = {
    # xpath
    'close_modal_btn': "//button[.//span[text()='Понятно']]",
    'at_assembly_tab': '//button[.//div[text()="На сборке"]]',
    'modal_accept_print_btn': "//button[.//span[text()='Распечатать']]",
    'package_tab':'//a[contains(@data-testid, "Supply-details-layout-tab") and text()="Упаковка для ПВЗ"]',
    'package_qr_code_option': '//button[text()="QR-код поставки"]',
    'package_for_sending_row': "//div[contains(@class, 'Table-row-view')][.//div[text()='Отгрузите поставку']]",
    # css
    'choose_all_orders_checkbox': '#checkbox-all',
    'create_new_delivery_btn': "button[data-testid='New-orders-action-button-new-supply-button-interface']",
    'modal_accept_creating_delivery_btn': "button[data-testid='Create-delivery-modal-create-delivery-button-primary']",
    'delivery_row': 'div[data-testid="Table-row-view"]',
    'print_stickers_btn': 'button[data-testid="On-assembly-tasks-page-filter-print-stickers-button-interface"]',
    'create_package':'[data-testid="Boxes-buttons-button-secondary"]',
    'print_package_qr_code_icon':'[data-testid="Box-item-print-sticker-button-interface"]',
    'sent_to_delivery_btn':"button[data-testid='Send-to-delivery-button-primary']",
    'modal_accept_sending_btn':'button[data-testid="Supply-to-delivery-confirm-view-submit-button-primary"]',
    'print_dropdown_btn':'[data-testid="Print-button-button-primary"]',
    # elements
    'package_list':"[data-testid='Packaging-boxes-list']"
}