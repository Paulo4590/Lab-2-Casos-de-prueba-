import ecommerce_form
import logging

logging .basicConfig(
    level= logging.DEBUG,
    filemode='w',
    filename='test.log'
)

def test_purchase_itemzero():
    logging.info('TEST CASE 1')
    system = ecommerce_form.OnlinePurchase()

    cart ={
        'Laptop': 0,
        'Mouse': 2
    }

    coupon = 'DISCOUNT10'
    address = 'Av Patria'
    result = system.process_purchase(cart,coupon,address)

    assert 'integer greater than 0' in result, f"Expected error message for invalid quantity, but got: {result}"

    logging.info(f'TEST CASE FINISHED')

def test_purchase_invalid_coupon():
    logging.info('TEST CASE 3')
    system = ecommerce_form.OnlinePurchase()

    cart ={
        'Laptop': 1,
        'Mouse': 2
    }

    coupon = 'INVALID'
    address = 'Av Patria'
    result = system.process_purchase(cart,coupon,address)

    assert 'code is not valid' in result, f"Expected error message for invalid coupon, but got: {result}"

    logging.info(f'The purchase result is: {result}')
    logging.info(f'TEST CASE 3 FINISHED')

def test_purchase_valid_coupon():
    logging.info('TEST CASE 9')
    system = ecommerce_form.OnlinePurchase()

    cart ={
        'Laptop': 1,
        'Mouse': 2
    }

    coupon = 'DISCOUNT10'
    address = 'Av Patria'
    result = system.process_purchase(cart,coupon,address)

    assert 'DISCOUNT10' in result
    assert '935' in result

    logging.info(f'The purchase result is: {result}')
    logging.info(f'TEST CASE 9 FINISHED')