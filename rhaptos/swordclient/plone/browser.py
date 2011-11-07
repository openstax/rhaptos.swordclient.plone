from zope import interface, schema
from zope.formlib import form
from five.formlib import formbase

class IDeposit(interface.Interface):
    text = schema.TextLine(title=u'Deposit URL',
                           description=u'Deposit the current page to the URL',
                           required=False)

class Deposit(formbase.PageForm):
    """
    """

    form_fields = form.FormFields(IDeposit)

    @form.action("Submit")
    def handle_submit(self):
        pass

