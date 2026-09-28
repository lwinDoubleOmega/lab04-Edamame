import pytest
from bank import BankAccount

@pytest.fixture
def account():
    """Fixture that returns a BankAccount initialized with a balance of 100."""
    return BankAccount(100)

def test_withdraw_decreases_balance(account):
    """Test standard withdrawal reduces the balance correctly."""
    account.withdraw(40)
    assert account.balance == 60

def test_withdraw_overdraft_raises_error(account):
    """Test attempting to withdraw more than the available balance raises ValueError."""
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(150)