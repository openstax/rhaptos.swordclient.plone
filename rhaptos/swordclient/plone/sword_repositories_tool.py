from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import UniqueObject 
from OFS.SimpleItem import SimpleItem
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from zope.interface import Interface
from zope import schema

from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow

from Products.CMFPlone.PloneBaseTool import PloneBaseTool
from plone.z3cform import layout

from rhaptos.swordclient.plone import _

class ISwordRepository(Interface):
    repository_name = schema.TextLine(title=u"Repository Name")
    repository_url = schema.TextLine(title=u"Repository URL")

class ISwordRepositoriesSettings(Interface):
    """ Define schema for sword repositories tool"""
    """sword_repositories = schema.List(title=u"Sword Repositories",
        value_type=DictRow(title=u"Sword Repository", schema=ISwordRepository))"""
    sword_repositories = schema.TextLine(title=u"Sword Repositories")

class SwordRepositoriesEditForm(RegistryEditForm):
    label = _(u"Sword Repositories settings")
    description = _(u"Please enter details of available SWORD repositories")

    schema = ISwordRepositoriesSettings

class SwordRepositoriesTool(PloneBaseTool, SimpleItem):
    """The tool for managing connection details for sword repositories"""
    id = 'sword_repositories_tool'
    meta_type= 'Sword Repositories Tool'

    security = ClassSecurityInfo()

SwordRepositoriesEditFormView = layout.wrap_form(SwordRepositoriesEditForm, ControlPanelFormWrapper)
InitializeClass(SwordRepositoriesTool)
