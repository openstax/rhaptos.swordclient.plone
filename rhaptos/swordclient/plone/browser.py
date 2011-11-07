from zope import interface, schema
from zope.formlib import form
from five.formlib import formbase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IDeposit(interface.Interface):
    text = schema.TextLine(title=u'Deposit URL',
                           description=u'Deposit the current page to the URL',
                           required=True)

    username = schema.TextLine(title=u'Username',
                           description=u'Username',
                           required=True)

    password = schema.TextLine(title=u'Password',
                           description=u'Password',
                           required=True)

class Deposit(formbase.PageForm):
    """
    """

    form_fields = form.FormFields(IDeposit)
    template = ViewPageTemplateFile('deposit.pt')

    @form.action("Submit")
    def handle_submit(self):
        pass

