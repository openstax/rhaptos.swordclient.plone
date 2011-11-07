from zope import interface, schema
from zope.formlib import form
from five.formlib import formbase
from xml.dom.minidom import parseString
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
    """Submit the contents of this page and its referenced images to a sword service
    """
    form_fields = form.FormFields(IDeposit)
 
    template = ViewPageTemplateFile('deposit.pt')

    @form.action("Submit")
    def handle_submit(self):
	"""Assemble Sword submission, assumes content in AT Document"""
        encoding = self.context.getCharset()
        ptext = self.context.getRawText()
	dom = parseString("<body>%s</body>% ptext)
        remoteImages = []
        localImages = []
	for node in dom.getElementsByTagName("img"):
	    src = node.getAttribute("img")
	    src = src.encode('UTF-8')
            if src.startsWith("http://"):
		remoteImages.append(src)
	    elseif src:
		localImages.append(src)
        
	
        """todo get images to create zip file for upload""" 		
