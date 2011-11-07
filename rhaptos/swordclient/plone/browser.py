import base64
import urllib2
from zope import interface, schema
from zope.formlib import form
from five.formlib import formbase
from xml.dom.minidom import parseString
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zipfile import ZipFile, ZIP_DEFLATED
from cStringIO import StringIO
from urlparse import urlparse
class IDeposit(interface.Interface):
    url = schema.TextLine(title=u'Repository URL',
                          description=u'Repository URL',
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
    def handle_submit(self, action, data):
	"""Assemble Sword submission, assumes content in AT Document"""
        encoding = self.context.getCharset()
        ptext = self.context.getRawText()
        dom = parseString("<body>%s</body>" % ptext)
        remoteImages = []
        localImages = []
        for node in dom.getElementsByTagName("img"):
            src = node.getAttribute("img")
            src = src.encode('UTF-8')
            if src.startswith("http://"):
                remoteImages.append(src)
            elif src:
                localImages.append(src)
            
        ztemp = StringIO()
        zfile = ZipFile(ztemp, "w", ZIP_DEFLATED)
        zfile.writestr("index.html", ptext)
        zfile.close()
        zsize = ztemp.tell()
        ztemp.seek(0)
        auth_string = base64.encodestring("%(username)s:%(password)s" % data)[:-1]
        headers = {
            'Content-Type': 'application/zip',
            'Content-Length': zsize,
            'Content-Disposition': 'attachment; filename=%s.zip' % self.context.id,
            'Authorization':"Basic %s" % auth_string 
                    }
        request = urllib2.Request(data['url'], ztemp.read(), headers)
        response = urllib2.urlopen(request)
        # XXX: Wrap response in template
        return response.read()
        
        # parts = urlparse(self.request.form['url'])
        # host = parts.netloc.split(':')[0]
        # conn = httplib.HTTPConnection(host, port)
        # conn.putheader('content-type', 'application/zip')
        # conn.putheader('content-length', str(zsize))
        # conn.putheader('content-disposition', 'attachment; filename=%s.zip % self.context.id')
        # conn.putheader('authorization', 'Basic %s %auth_string')

        """TODO get images to add to zip file for upload""" 		
