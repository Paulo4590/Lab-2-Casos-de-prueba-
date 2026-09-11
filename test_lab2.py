import ecommerce_form
import logging
import pytest

logging.basicConfig(
    level=logging.DEBUG,
    filemode='w',
    filename='test.log'
)

@pytest.fixture
def system():
    return ecommerce_form.OnlinePurchase()

@pytest.mark.parametrize("quantity, expected", [(5, True), (0, False), (-1, False), (.8, False)])

@pytest.mark.unit 
def test_validate_quantity_compontent(system, quantity, expected):
    result = system.validate_quantity(quantity)
    assert result == expected



@pytest.mark.parametrize("coupon, expected", [('DISCOUNT10', True), ('DISCOUNT30', False),('DISCOUNT20', True),('DISCOUNT40', False)])

@pytest.mark.unit
def test_validate_coupon(system, coupon, expected):
    result = system.validate_coupon(coupon)
    assert result == expected   



@pytest.mark.parametrize("address, expected", [('Av patria', True), ('tres', False),  ('123456', False)])

@pytest.mark.wip
def test_validate_address(system, address, expected):
    result = system.validate_address(address)
    assert result == expected   




@pytest.mark.system

def test_purchase_itemzero():
    logging.info('TEST CASE 1')
    system = ecommerce_form.OnlinePurchase()
    
    cart = {
        'laptop': 0,
        'mouse': 2
    }
    coupon = 'DISCOUNT10'
    address = 'av patria'
    result = system.process_purchase(cart, coupon, address)
    
    assert 'integer greater than 0' in result
    
    logging.info('TEST CASE finished')

@pytest.mark.system

def test_invalid_coupon():
    logging.info('TEST CASE 2')
    system = ecommerce_form.OnlinePurchase()
    
    cart = {
        'laptop': 1,
        'mouse': 2
    }
    coupon = 'DISCOUNT30'
    address = 'av patria'
    result = system.process_purchase(cart, coupon, address)
    
    assert 'coupon code is not valid' in result
    logging.info(f'Invalid coupon test result: {result}')
    
    logging.info('TEST CASE finished')


@pytest.mark.system
    
def test_valid_coupon():
    logging.info('TEST CASE 3')
    system = ecommerce_form.OnlinePurchase()
    
    cart = {
        'laptop': 1,
        'mouse': 2
    }
    coupon = 'DISCOUNT10'
    address = 'av patria'
    result = system.process_purchase(cart, coupon, address)
    
    assert 'Error' not in result
    assert '990'  in result

    logging.info(f'Valid coupon test result: {result}')
    
    logging.info('TEST CASE finished')




if __name__ == '__main__':
    test_purchase_itemzero()
    test_valid_coupon()