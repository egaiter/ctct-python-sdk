import unittest

from constantcontact import Account_Info, Address

class Test_Account_Info(unittest.TestCase):
    def test_accinf_init_from_dict(self):
        account_info = Account_Info({'first_name': 'Bob', 'organization_name': 'League of super evil'})
        
        self.assertEqual(account_info.get_first_name(), 'Bob')
        self.assertEqual(account_info.get_organization_name(), 'League of super evil')

    def test_accinf_setter_getter(self):
        account_info = Account_Info()
        account_info.set_email('test@example.com')
        account_info.set_website('example.com')

        self.assertEqual(account_info.get_last_name(), None)
        self.assertEqual(account_info.get_email(), 'test@example.com')
        self.assertEqual(account_info.get_website(), 'example.com')

        account_info.delete_website()

        self.assertEqual(account_info.get_website(), None)

    def test_accinf_org_address(self):
        account_info = Account_Info()
        address = Address()
        address.set_line1('Mt. Doom')

        self.assertEqual(account_info.get_organization_address(), None)

        account_info.set_organization_address(address)

        self.assertEqual(account_info.get_organization_address(), address)

        account_info.clear_organization_address()

        self.assertEqual(account_info.get_organization_address(), None)


if __name__ == '__main__':
    unittest.main()
