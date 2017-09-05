import unittest
import shoppinglister.views
from flask import url_for


class ViewsTests(unittest.TestCase):
    """ Contains tests for the views """

    def test_page_redirects_when_not_logged_in(self):
        """ Tests whether going to shopping_list without logging in
         redirects to the signin page """

        with shoppinglister.app.test_request_context():
            self.assertEqual(
                shoppinglister.views.shopping_list().status_code, 302)
            self.assertEqual(shoppinglister.views.shopping_list().location,
                             url_for('lister.login'))

    def test_logout(self):
        """ Tests whether the loguot loads and redirects to login """

        with shoppinglister.app.test_request_context():
            self.assertEqual(shoppinglister.views.logout().status_code, 302)
            self.assertEqual(shoppinglister.views.logout().location,
                             url_for('lister.signup'))


if __name__ == '__main__':
    unittest.main()
