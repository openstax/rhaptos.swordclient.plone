from zope.formlib import form
from Products.Five import BrowserView

class Deposit(BrowserView):
    """
    """

    @ form.action("Submit")
    def handle_submit(self):
        pass

